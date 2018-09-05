#
# lobster.py - lobster
#
# (c) gdifiore 2018 <difioregabe@gmail.com>
#

import json

def readJSON(file):
    with open(file, 'r') as f:
        lobster_data = json.load(f) 
    return lobster_data

def getTitle(lobster_data):
    title = lobster_data["title"]
    return title

def getHeader(lobster_data):
    header = lobster_data["header"]
    return header

def getContent(lobster_data):
    content = lobster_data["content"]
    return content

def getAuthor(lobster_data):
    content = lobster_data["author"]
    return content

def getDate(lobster_data):
    content = lobster_data["date"]
    return content