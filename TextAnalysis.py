import string
#read PDF & Extract text
import PyPDF2
import re
# pdfFileObj = open('Tech Mahindra.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# PageNos=pdfReader.numPages
# print(PageNos)
#
# String='Management Discussion and Analysis'
# String1='Overview'
# for i in range(0,PageNos):
#     PageObj = pdfReader.getPage(i)
#     #print("this is page " + str(i))
#     Text = PageObj.extractText()
#     # print(Text)
#     ResSearch = re.search(String, Text)
#     ResSearch1 = re.search(String1, Text)
#     if ResSearch is not None and ResSearch1 is not None:
#         print(str(i+1))

# for i in range(74,88):
#     PageObj = pdfReader.getPage(i)
#     text = PageObj.extractText()
    # text3=''
    # text=''
    # text=text3+text
    # pageObj = pdfReader.getPage(PageNos)
    # text3 = pageObj.extractText()
    # text=text3+text
    # print(text)
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
print('The Flesch-Kincaid Readability score / readibility ease index is:',RE)

