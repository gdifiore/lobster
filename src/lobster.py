#!/usr/bin/env python
#
# lobster.py - lobster
#
# (c) gdifiore 2018 <difioregabe@gmail.com>
#

import os
import sys
import json
from lobster_json import *
from bs4 import BeautifulSoup

type = sys.argv[1]
file = sys.argv[2]
theme = sys.argv[3]

if type == "simple":
    def writeToHTML(title, header, content):
        html_file = theme + ".html"
        path = "themes\\" + html_file
        soup = BeautifulSoup(open(path), "html.parser")
        for i in soup.find_all('title'):
            i.string = title
        for i in soup.find_all(class_='header'):
            i.string = header
        for i in soup.find_all(class_='content'):
            i.string = content
        #print(soup)

        finished = theme + "_finished.html"
        with open(finished, "w") as text_file:
            text_file.write(str(soup))

    lobster_data = readJSON(file)
    title = getTitle(lobster_data)
    header = getHeader(lobster_data)
    content= getContent(lobster_data)
    writeToHTML(title, header, content)

if type == "blog":
    def writeToHTMLBlog(title, header, content, author, date):
        html_file = theme + ".html"
        path = "themes\\" + html_file
        soup = BeautifulSoup(open(path), "html.parser")
        for i in soup.find_all('title'):
            i.string = title
        for i in soup.find_all(class_='header'):
            i.string = header
        for i in soup.find_all(class_='content'):
            i.string = content
        for i in soup.find_all(class_='author'):
            i.string = author
        for i in soup.find_all(class_='date'):
            i.string = date
        #print(soup)

        finished = theme + "_finished.html"
        with open(finished, "w") as text_file:
            text_file.write(str(soup))


    lobster_data = readJSON(file)
    title = getTitle(lobster_data)
    header = getHeader(lobster_data)
    content= getContent(lobster_data)
    author = getAuthor(lobster_data)
    date = getDate(lobster_data)
    writeToHTMLBlog(title, header, content, author, date)

else:
    print(sys.argv[1])
    print("failure")