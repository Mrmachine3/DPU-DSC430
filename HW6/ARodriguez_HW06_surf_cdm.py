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
# Video Explanation URL: https://youtu.be/13TJNnLLOTg
#
# Description:
# This program recursively scrapes the html content from an initial webpage and all embedded URLS
# to calculate the frequency of words used in the HTML content. The program lists the top 25 words
# and their frequencies in a tabular format.

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

    # Initialize variables including words
    def __init__(self):
            super().__init__()
            self.url = url
            self.in_text_tag = False
            self.words = []
    
    # HTML start tag handler
    def handle_starttag(self, tag, attrs):
        for tag in ['p','h1','h2']:
            self.in_text_tag = True

    # HTML end tag handler
    def handle_endtag(self, tag):
        for tag in ['p','h1','h2']:
            self.in_text_tag = False

    # HTML data handler within HTML tags
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
    
    # Function to return list of words
    def get_words(self):
        return self.words

class LinkParser(TextParser):
    """Link parser that extracts URLs from webpages

    Args:
        HTMLParser (class): Find tags and calls handler functions
    """

    # Initialize variables including links
    def __init__(self):
            super().__init__()
            self.url = url
            self.in_text_tag = False
            self.links = []
    
    # HTML start tag handler
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url,attr[1])
                    if absolute[:4] == 'http' or absolute[:5] == 'https':
                        self.links.append(absolute)

    # Function to return list of urls
    def get_links(self):
        return self.links

# FUNCTIONS
def remove_punctuation(text):
    """Function to use regex to substitute all residual punctuation from strings

    Args:
        text (str): the string that may contain punctuation

    Returns:
        str: the string containing no punctuation
    """
    # Invoking regex methods to escape punctuation characters
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
    # Initialize empty list for regex matches
    matches = []

    # Parameterized regex pattern to use for matching text
    for pattern in patterns:
        match = re.match(pattern,data)
        if match:
            matches.append(match[0])
    return list(dict.fromkeys(matches))

def find_url(url):
    """A function to scrape all URLs from the initial webpage

    Args:
        url (str): a string representation of a URL

    Returns:
        list: a list of found links
    """
    try:
        # Initialize the LinkParser class to scrape URLs from webpages and return a list of all URLs
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
        # Initialize the TextParser class to scrape text from webpages and return a list of all words
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
    """A function to analyze all words found through webscraping process

    Args:
        words (list): a list of all words found by scraping webpage content

    Returns:
        dict: A dictionary listing the word as a key and the frequency of the word as the value
    """
    # Initialize empty word dictionary
    word_frequency = {}

    # Iterate through all words in the list of parameterized words passed into the function
    for word in words:
        # Checking for words greater than 0 characters
        if len(word) > 0:
            # checking if word already exists in the dictionary and incremeting the count; else setting value to 1
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    return word_frequency
    
# MAIN PROGRAM FUNCTION
def main(url):

    # Invokes function to scrape initial webpage for all URLs
    urls = find_url(url)

    # Initializes an empty list to temporarily store all words found on webpages
    all_words = []

    # Iterating through all collected URLs from initial URL
    for url in urls:
        # Limits recursive scraping to URLs containing the predefined subdomain of 'cdm.depaul.edu'
        if 'cdm.depaul.edu' in url:
            # Invoking function to scrape all words from each subsequent webpage
            words = get_html(url)
            if words:
                for word in  words:
                    all_words.append(word)

    # Evaluate frequency of words stored in 'all_words' list derived from all words scroped from all URLs
    freq = evaluate_frequency(all_words)

    # Sort dictionary on values in descending order
    converted_dict = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))

    # Prepare frequency table heading and data output
    heading = "Top"+str(' '*10)+"Word"+str(' '*10)+"Count"
    print(f"\n{heading}\n{('-'*len(heading))}")

    # Print top 25 words and their frequncies in a tabular format
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