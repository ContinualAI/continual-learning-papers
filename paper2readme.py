#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright (c) 2020 ContinualAI                                               #
# Copyrights licensed under the MIT License.                                   #
# See the accompanying LICENSE file for terms.                                 #
#                                                                              #
# Date: 16-06-2021                                                             #
# Author(s): Andrea Cossu                                                      #
# E-mail: contact@continualai.org                                              #
# Website: www.continualai.org                                                 #
################################################################################


# Python 2-3 compatible
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import bibtexparser
import random
from bibtexparser.customization import convert_to_unicode
from bibtexparser.bparser import BibTexParser
import copy
import os

random.seed(1)


def build_tags_string(tag2c):
    output = ""
    for tagname, color in tag2c.items():
        output += create_tag(tagname)
        output += "  "

    return output


def create_tag(tagname):
    output = "[{}] ".format(tagname)
    return output


def count_current_papers(bibtex_path, main_bib_path):
    with open(os.path.join(bibtex_path, main_bib_path), 'r') as f:
        papers = bibtexparser.load(f)
    return len(papers.entries)


def remove_mendeley_notice_from_files(filename):
    with open(filename, 'r') as fin:
        data = fin.read().splitlines(True)

    if data[0].startswith("Automatically generated"):
        with open(filename, 'w') as fout:
            fout.writelines(data[5:])


def extract_bibtex(bib_database, id):

    # print("bib_database.entries: ", bib_database.entries)
    pos = None
    for i, entry in enumerate(bib_database.entries):
        if entry['ID'] == id:
            pos = i
            # print(entry['ID'])

    bib_db = copy.deepcopy(bib_database)
    # print(id)
    # print("pos:", pos)
    del bib_db.entries[pos+1:]
    del bib_db.entries[:pos]
    str = bibtexparser.dumps(bib_db)
    return str


def bibtex_string2html(str, remove_abstract=True):

    lines = str.split("\n")
    final_str = ""
    # print(lines)
    for i, line in enumerate(lines):

        if remove_abstract and line.strip().startswith("abstract"):
            continue

        if line == "":
            continue
        if i == 0:
            final_line = line + "<br>"
        else:
            final_line = line + "<br>"

        final_str += final_line

    # print(final_str)
    return final_str


def journal_or_booktitle(item):

    if "journal" in item.keys():
        return "*" + item["journal"] + "*"
    elif "booktitle" in item.keys():
        return "*" + item["booktitle"] + "*"
    elif item["ENTRYTYPE"] == "book":
        return "*" + item["publisher"] + "*"
    else:
        print("WARNING: venue missing in '" + str(item["title"]) + "'!!!")
        return ""


def pages_or_void(item):

    if "pages" in item.keys():
        return ", " + item["pages"]
    else:
        return ""


def get_author(item):

    authors_list = item['author'].split(" and ")
    str = ""
    for i, aut in enumerate(authors_list):
        # print(aut)
        try:
            surname, name = aut.split(", ")
        except ValueError:
            surname, name = aut.split(" ")

        authors_list[i] = name + " " + surname
        if i == len(authors_list) - 1:
            str += " and " + name + " " + surname
        elif i == 0:
            str += name + " " + surname
        else:
            str += ', ' + name + " " + surname

    return str


def get_title(item):

    title = item['title'].replace("{", "").replace("}", "")

    if "url" in item.keys():
        return "[" + title + "](" + item["url"] + ")"
    else:
        return title


# settings ---------------------------------------------------------------------
bibtex_path = "bibtex"
full_bib_db = "Continual Learning Papers.bib"
full_bib_db_path = full_bib_db
template_file_path = "README_template.md"
tag2fill = "<TAG>"
papercount2fill = "<PAPER_COUNT>"
output_filename = "README.md"
# this respect also the order of the sections
bib_files = [
    "Continual Learning Papers-Applications.bib",
    "Continual Learning Papers-Architectural Methods.bib",
    "Continual Learning Papers-Benchmarks.bib",
    "Continual Learning Papers-Bioinspired Methods.bib",
    "Continual Learning Papers-Catastrophic Forgetting Studies.bib",
    "Continual Learning Papers-Classics.bib",
    "Continual Learning Papers-Continual Few Shot Learning.bib",
    "Continual Learning Papers-Continual Meta Learning.bib",
    "Continual Learning Papers-Continual Reinforcement Learning.bib",
    "Continual Learning Papers-Continual Sequential Learning.bib",
    "Continual Learning Papers-Dissertation and Theses.bib",
    "Continual Learning Papers-Generative Replay Methods.bib",
    "Continual Learning Papers-Hybrid Methods.bib",
    "Continual Learning Papers-Meta Continual Learning.bib",
    "Continual Learning Papers-Metrics and Evaluations.bib",
    "Continual Learning Papers-Neuroscience.bib",
    "Continual Learning Papers-Others.bib",
    "Continual Learning Papers-Regularization Methods.bib",
    "Continual Learning Papers-Rehearsal Methods.bib",
    "Continual Learning Papers-Review Papers and Books.bib",
    "Continual Learning Papers-Robotics.bib"

]
sec_descriptions = [
    "In this section we maintain a list of all applicative papers "
    "produced on continual learning and related topics.",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some architectural methods.",
    "In this section we list all the papers related to new benchmarks "
    "proposals for continual learning and related topics. ",
    "In this section we list all the papers related to bioinspired continual "
    "learning approaches.",
    "In this section we list all the major contributions trying to understand "
    "catastrophic forgetting and its implication in machines that learn "
    "continually.",
    "In this section you'll find pioneering and classic continual learning "
    "papers. We recommend to read all the papers in this section for a "
    "good background on current continual deep learning developments.",
    "Here we list the papers related to Few-Shot continual and incremental learning.",
    "In this section we list all the papers related to the continual "
    "meta-learning.",
    "In this section we list all the papers related to the continual "
    "Reinforcement Learning.",
    "Here we maintain a list of all the papers related to the continual "
    "learning at the intersection with sequential learning.",
    "In this section we maintain a list of all the dissertation and thesis "
    "produced on continual learning and related topics.",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some generative replay methods.",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some hybrid methods, mixing different strategies.",
    "In this section we list all the papers related to the meta-continual "
    "learning.",
    "In this section we list all the papers related to the continual learning "
    "evalution protocols and metrics.",
    "In this section we maintain a list of all Neuroscience papers "
    "that can be related (and useful) for continual machine learning.",
    "In this section we list all the other papers not appearing in at least "
    "one of the above sections.",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some regularization methods.",
    "In this section we collect all the papers introducing a continual "
    "learning strategy employing some rehearsal methods.",
    "In this section we collect all the main review papers and books on "
    "continual learning and related subjects. These may constitute a solid "
    "starting point for continual learning newcomers.",
    "In this section we maintain a list of all Robotics papers "
    "that can be related to continual learning."
]


with open('tags.csv', 'r') as f:
    tags_list = [line.split(',')[0].strip() for line in f][1:]  # get all tags
    n_tags = len(tags_list)
    print("Read " + str(n_tags) + " tags.")

# ------------------------------------------------------------------------------

remove_mendeley_notice_from_files(os.path.join(bibtex_path, full_bib_db))

papers_count = {}
for bib_f in bib_files:
    papers_count[bib_f] = str(count_current_papers(bibtex_path, bib_f))


with open(os.path.join(bibtex_path, full_bib_db)) as bibtex_file:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    full_bib_db = bibtexparser.load(bibtex_file, parser=parser)

str2inject = ""
for i, bibfile in enumerate(bib_files):

    sec_title = bibfile.split("-")[1][:-4]
    with open(os.path.join(bibtex_path, bibfile)) as bibtex_file:
        parser = BibTexParser()
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    with open(template_file_path) as rf:
        template_str = rf.read()

    str2inject += "### " + sec_title + "\n\n**" + \
        papers_count[bibfile] + " papers**" + "\n\n" + \
        sec_descriptions[i] + "\n\n"

    for item in sorted(
            bib_database.entries, key=lambda j: j['year'], reverse=True):
        # print(item)

        str2inject_tags = ""
        if "keywords" in item.keys():
            # print(item["mendeley-tags"])
            str_tags = item["keywords"].replace(";", "").replace("[", "")
            str_tags = str_tags.replace(",", "")
            cur_tags = str_tags.replace(" ", "").split("]")
            del cur_tags[-1]
            # print(cur_tags)

            for tag in cur_tags:
                assert tag in tags_list
                str2inject_tags += create_tag(tag)

        str2inject += "- " + get_title(item) + \
                      " by " + get_author(item) + \
                      ". " + journal_or_booktitle(item) + \
                      pages_or_void(item) + \
                      ", " + item['year'] + ". " + \
                      str2inject_tags + "\n"

    if i != len(os.listdir(bibtex_path)) - 1:
        str2inject += "\n"
    else:
        str2inject = str2inject[:-1]


template_str = template_str.replace(papercount2fill,
                                    "**Search among " +
                                    str(count_current_papers(bibtex_path,
                                                             full_bib_db_path)) + " papers!**"
                                    )

template_str = template_str.replace(tag2fill, str2inject) #+ rst_end_str


with open(output_filename, "w") as wf:
    wf.write(template_str)
