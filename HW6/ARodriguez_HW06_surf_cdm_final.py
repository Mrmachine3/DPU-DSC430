#!/usr/bin/python3
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: Anthony M. Rodriguez
# Date: 02/22/2024
# Usage: /usr/bin/python3 ARodriguez_HW06_surf_cdm.py
# Alternate Python Usage: /usr/bin/python3 -m ARodriguez_HW06_surf_cdm
# Alternate CLI Usage: ./ARodriguez_HW06_surf_cdm.py
# Git Repo URL: https://github.com/Mrmachine3/DPU-DSC430.git
# Video Explanation URL:
#
# Description:


# LIBRARIES
from urllib.request import urlopen, Request, urljoin
from html.parser import HTMLParser
import string
import re

# CLASSES
class TextParser(HTMLParser):
    """Word parser that evaluates words and prints the top 25

    Args:
        HTMLParser (class): Find tags and calls handler functions
    """

    def __init__(self):
            super().__init__()
            self.url = url
            self.in_text_tag = False
            self.words = []
    
    def handle_starttag(self, tag, attrs):
        for tag in ['p','h1','h2']:
            self.in_text_tag = True

    def handle_endtag(self, tag):
        for tag in ['p','h1','h2']:
            self.in_text_tag = False

    def handle_data(self, data):
        pattern = [r'[a-zA=Z]+']
        if self.in_text_tag:
            text = data.split()
            for string in text:
                words = match_regex(string,pattern)
                for word in words:
                    if '-' not in word:
                        self.words.append(remove_punctuation(word))
                    else:
                        continue
    
    def get_words(self):
        return self.words

class LinkParser(TextParser):
    """Link parser that extracts URLs from webpages

    Args:
        HTMLParser (class): Find tags and calls handler functions
    """

    def __init__(self):
            super().__init__()
            self.url = url
            self.in_text_tag = False
            self.links = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url,attr[1])
                    if absolute[:4] == 'http' or absolute[:5] == 'https':
                        self.links.append(absolute)
    def get_links(self):
        return self.links

# FUNCTIONS
def remove_punctuation(text):
    regex = re.compile('[%s]' % re.escape(string.punctuation))

    return regex.sub('',text)

def match_regex(data, patterns):
    """Returns list of matching strings from list of applicable regex patterns

    Args:
        data (list): literal strings of data what will be evaluated by applicable regex patterns
        patterns (list): raw string (denoted by r'') containing valid regex pattern applicable for data type

    Returns:
        list: list of strings matching the regex pattern(s)

    """
    matches = []

    for pattern in patterns:
        match = re.match(pattern,data)
        if match:
            matches.append(match[0])
    return list(dict.fromkeys(matches))

def find_url(url):
    try:
        print(f"Visiting the following:\n  {url}")
        req = Request(url,headers={'User-Agent': 'Mr.Machine'})
        content = urlopen(req).read().decode('utf-8')
        linkcollector = LinkParser()
        linkcollector.feed(content)
        urls = linkcollector.get_links()

        return urls
    except:
        pass

def get_html(url):
    try:
        print(f"\nRetrieving html content from the following:\n  {url}")
        req = Request(url,headers={'User-Agent': 'Mr.Machine'})
        content = urlopen(req).read().decode('utf-8')
        wordcollector = TextParser()
        wordcollector.feed(content)
        words = wordcollector.get_words()

        return words
    except:
        pass

def evaluate_frequency(words):
    # Initialize empty word dictionary
    word_frequency = {}

    for word in words:
        if len(word) > 0:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    return word_frequency
    
# MAIN PROGRAM FUNCTION
def main(url):

    urls = find_url(url)

    all_words = []

    for url in urls:
        if 'cdm.depaul.edu' in url:
            words = get_html(url)
            if words:
                for word in  words:
                    all_words.append(word)

    # Evaluate frequency of words from HTML text body
    freq = evaluate_frequency(all_words)

    # Sort dictionary on values in descending order
    converted_dict = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))

    # Prepare frequency table heading and data output
    heading = "Top"+str(' '*10)+"Word"+str(' '*10)+"Count"
    print(f"\n{heading}\n{('-'*len(heading))}")

    count = 0
    for idx, (k, v) in enumerate(converted_dict.items(), 1):
        print(f"{idx:<5} {k:10}\t{v}")
        count += 1
        if count == 25:
            break

# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    user_input = input(f"Enter target URL: ")

    if not user_input or user_input == '':
        default_url = 'https://www.cdm.depaul.edu'
        print(f"No input entered. Using default URL: '{default_url}'")
        url = default_url
    else:
        url = user_input

    main(url)