import glob
import errno
import enchant
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


def func(f):
    file = f.read()
    d = enchant.Dict("en_US") # ### Spell-Checking the tokenized words
    #print(my_article.text)
    print("MIS-SPELLED WORDS")
    print(list(set([word.encode('ascii', 'ignore') for word in word_tokenize(file) if d.check(word) is False and re.match('^[a-zA-Z ]*$',word)] )))  
    print('\n')
    

#path = 'C:/Users/ADITI/Desktop/twa project files/articles1/articles1/*.txt'
path = 'C:/Users/akhil/Downloads/Aspire/enwiki-latest-pages-articles1.xml-p10p30302 (1)/removed.txt'
files = glob.glob(path)
for name in files:
    try:
        with open(name,encoding="ISO-8859-1") as f:
            func(f)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise

 
