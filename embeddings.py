import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
from bibtex2md import (bibtex_path, bib_files, template_file_path, 
	str2inject, papers_count, sec_descriptions)
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.manifold import TSNE
import numpy as np
import json
import plotly
import os


def get_2d_coordinates(vectorized_text):
	out = TSNE( 
		n_components=2, 
		random_state=42
		).fit_transform(vectorized_text)
	return out


def vectorize_text(text):
	vect_text = TfidfVectorizer(
		lowercase=True, 
		ngram_range=(1,3), 
		stop_words='english', 
		max_df=7, 
		min_df=2
	).fit_transform(text).toarray()
	return vect_text

papers = list()

for i, bibfile in enumerate(bib_files):
	sec_title = bibfile.split("-")[1][:-4]
	with open(os.path.join(bibtex_path, bibfile)) as bibtex_file:
		parser = BibTexParser()
		parser.customization = convert_to_unicode
		bib_database = bibtexparser.load(bibtex_file, parser=parser)

	with open(template_file_path) as rf:
		template_str = rf.read()

	str2inject += sec_title + \
		"\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n" + \
		"**" + papers_count[bibfile] + " papers" + "**\n\n" + \
		sec_descriptions[i] + "\n\n"

	for item in sorted(bib_database.entries, key=lambda j: j['year'], reverse=True):
		if 'abstract' in item.keys():
			abstract, title, author, url = item['abstract'], item['title'], item['author'], item['url']

			papers.append((abstract, title, author, url, i))
		else:
			continue

papers = np.array(papers)
vectorized_abstracts = vectorize_text(papers[:, 0])
out = get_2d_coordinates(vectorized_abstracts)

db = {}
db['annotation_text'] = list()
db['sec_title'] = list()
db['pos_x'] = list()
db['pos_y'] = list()
for i in range(len(papers)):
	annotation_text = f"<a href=\"{papers[i][3]}\">{papers[i][1]} ({papers[i][2]})</a>"
	db['annotation_text'].append(annotation_text)
	db['sec_title'].append(papers[i][4])
	db['pos_x'].append(out[i].tolist()[0])
	db['pos_y'].append(out[i].tolist()[1])

with open('embedding.json', 'w') as output:
	json.dump(db, output)


trace = plotly.graph_objs.Scatter(
    x=db['pos_x'], 
    y=db['pos_y'], 
    mode='markers',
    marker=dict(
            color='LightSkyBlue',
            size=15,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
    textfont=dict(
    	color='black',
    	size=10,
    	),
    marker_color=list(map(int, db['sec_title'])),
    text = db['annotation_text'],
    textposition="top center",
    hoverinfo="text",
)
plotly.offline.plot([trace], filename='embedding-plot.html', auto_open=False)
