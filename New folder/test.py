# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:11:05 2021

@author: YXG0RZH
"""

def fetch_words():
    '''fffff
    Args: rrr'''
    import urllib
    import requests
    story = urllib.request.urlopen("http://sixty-north.com/c/t.txt")
    story_words= []
    for line in story:
        line_words = line.decode("utf8").split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)
        
def main():
    words = fetch_words()
    print_words(words)
        
        
if __name__ == "__main__" :
    main()
