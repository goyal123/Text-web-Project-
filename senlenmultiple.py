import glob
import errno
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def func(f):
    file = f.read()
    #no of sentences
    sent_tok = nltk.sent_tokenize(file)
    print(sent_tok)
##    ns = len(sent_tok)
##    print ("no of sentences-",ns)
##
##    #no of words
##    word_tok = nltk.word_tokenize(file) #need to take out commas plus other stuff
##    NoWord = [',','(',')',':',';','.','%','\x96','{','}','[',']','!','?',"''","``"]
##    word_tok2 = [i for i in word_tok if i not in NoWord]
##    nw = len(word_tok2)
##    print ("no of words-",nw)
##
##    #Average Sentence length are words divided by sentences
##    print("avg. sentence length",(nw/ns))
##    print('\n')

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

