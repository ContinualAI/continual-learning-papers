from nltk.corpus import stopwords
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
from bibtex2md import (bibtex_path, bib_files, template_file_path,
                       str2inject, papers_count, sec_descriptions)
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import numpy as np
import json
import plotly
import os
import re
import nltk
nltk.download('stopwords')

model = SentenceTransformer('BogdanKuloren/continual-learning-paper-embeddings-model')
model.max_seq_length = 512

def remove_stopwords(word_list: str) -> str:
    processed_word_list = []
    for word in word_list.split(' '):
        word = word.lower()  # in case they arenet all lower cased
        if word not in stopwords.words("english"):
            processed_word_list.append(word)
    return ' '.join(processed_word_list)


def clean_brackets(text: str) -> str:
    ''' Remove brackets from text '''
    text = re.sub("[\\(\\[].*?[\\)\\]]", "", text)
    return text


def preprocess_inputs(papers: np.ndarray, index: int = 6) -> np.ndarray:
    ''' Select input samples for embedding model '''
    samples = papers[:, index]  # selecting concatenation samples
    return samples


def get_2d_coordinates(
        vectorized_text: np.ndarray,
        algorithm: str = 'pca') -> np.ndarray:
    ''' reduce embedding dimensions '''
    if algorithm == 'tsne':
        out = TSNE(
            n_components=2,
            random_state=42
        ).fit_transform(vectorized_text)
    elif algorithm == 'pca':
        out = PCA(
            n_components=2,
            random_state=42
        ).fit_transform(vectorized_text)
    else:
        raise NotImplementedError
    return out


def vectorize_text(text: list, vectorizer: str = 'transformer') -> np.ndarray:
    ''' Convert input text to vector representations '''
    if vectorizer == 'tfidf':
        vect_text = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 3),
            stop_words='english',
            max_df=7,
            min_df=2
        ).fit_transform(text).toarray()
    elif vectorizer == 'transformer':
        vect_text = model.encode(text)
    else:
        raise NotImplementedError
    return vect_text


def construct_dataset() -> np.ndarray:
    global str2inject
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

        for item in sorted(
                bib_database.entries,
                key=lambda j: j['year'],
                reverse=True):
            if 'abstract' in item.keys():
                abstract = clean_brackets(item['abstract'])
                title = item['title']
                author = item['author']
                url = item['url']
                keywords = clean_brackets(
                    item['keywords']) if 'keywords' in item.keys() else ' '
                concat = f'{str(abstract)} {set(title)} {str(keywords)}'

                papers.append(
                    (abstract, title, author, url, i, keywords, concat))
            else:
                continue

    papers = np.array(papers)
    return papers


def plot_dataset(papers: np.ndarray, embed: np.ndarray) -> dict:
    db = {}
    db['annotation_text'] = list()
    db['sec_title'] = list()
    db['pos_x'] = list()
    db['pos_y'] = list()
    for i in range(len(papers)):
        annotation_text = f"<a href=\"{papers[i][3]}\">{papers[i][1]} ({papers[i][2]})</a>"
        db['annotation_text'].append(annotation_text)
        db['sec_title'].append(papers[i][4])
        db['pos_x'].append(embed[i].tolist()[0])
        db['pos_y'].append(embed[i].tolist()[1])

    with open('embedding.json', 'w') as output:
        json.dump(db, output)
    return db


def save_html_visualization(db: dict):
    trace = plotly.graph_objs.Scatter(
        x=db['pos_x'],
        y=db['pos_y'],
        mode='markers',
        marker=dict(
            color='navy',
            size=15,
            line=dict(
                color='navy',
                width=2
            )
        ),
        textfont=dict(
            color='black',
            size=10,
        ),
        marker_color=list(map(int, db['sec_title'])),
        text=db['annotation_text'],
        textposition="top center",
        hoverinfo="text",
    )
    plotly.offline.plot(
        [trace],
        filename='embedding-plot.html',
        auto_open=False)


def main():
    papers = construct_dataset()
    preprocessed_inputs = preprocess_inputs(papers, index=6)
    vectorized_abstracts = vectorize_text(preprocessed_inputs)
    out = get_2d_coordinates(vectorized_abstracts)
    db = plot_dataset(papers, out)
    save_html_visualization(db)


if __name__ == '__main__':
    main()
