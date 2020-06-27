#Some studies have analysed the relation between financial performance disclosed and the textual complexity in the annual report of a company 
#As a frist step, this program calculates the Flesch Readibility Index of the Chairman's letter in the annual report
#This program deploys web scraping and natural language toolkit


import string

import re

import requests

url = 'https://www.moneycontrol.com/annual-report/hindustanunilever/chairmans-speech/HU#HU'
res = requests.get(url)
html_page = res.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find(id='mar-2019')
text1 = text.get_text()
text2 = text1.strip()
# print(text2)
#make translator object to remove punctuation

translator=str.maketrans('','',string.punctuation)
text3=text2.translate(translator)

#word & sentence tokenization
from nltk.tokenize import sent_tokenize
SentToken=sent_tokenize(text2)
print(SentToken)
SentNos=len(SentToken)
print(SentNos)

from nltk.tokenize import word_tokenize
WordToken=word_tokenize(text3)
print(WordToken)
WordNos=len(WordToken)
print(WordNos)

#count syllables in a word
def syllable_count(word):
    word=word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
            if word.endswith("e") and not word.endswith("le"):
                count -= 1
    if count == 0:
        count += 1
    return count

#count syllables in all the words
from nltk.tokenize import word_tokenize
SyllableNos=0
for words in WordToken:
    a=syllable_count(words)
    SyllableNos = a + SyllableNos
print(SyllableNos)

#calculate Flesch-Kincaid Readability score:
ASL=WordNos/SentNos
ASW=SyllableNos/WordNos
RE=206.835-(1.015*ASL)-(84.6*ASW)

#result meaning
if RE>0 and RE<29:
    print('The text is very confusing to read')
elif RE>=30 and RE<49:
    print('The text is difficult to read')
elif RE>=50 and RE<59:
    print('The text is fairly difficult to read')
elif RE>=60 and RE<69:
    print('The text is standard')
elif RE>=70 and RE<79:
    print('The text is fairly easy to read')
elif RE>=80 and RE<89:
    print('The text is easy to read')
elif RE>90:
    print('The text is very easy to read')
#print results
print('Number of sentences:',SentNos)
print('Number of words:',WordNos)
print('The Flesch Readability score / readibility ease index is:',RE)

