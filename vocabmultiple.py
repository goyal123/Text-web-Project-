import glob
import errno
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def func(f):
    file = f.read()
    word = nltk.word_tokenize(file)
    NoWord = [',','(',')',':',';','.','%','\x96','{','}','[',']','!','?',"''","``"]
    word2 = [i for i in word if i not in NoWord]

    clean_tokens = word2[:]
    for token in word2:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

    print (len(set(clean_tokens)))
    print('\n')
    

path = 'C:/Users/akhil/Downloads/Aspire/enwiki-latest-pages-articles1.xml-p10p30302 (1)/removed.txt'
files = glob.glob(path)
for name in files:
    try:
        with open(name,encoding="ISO-8859-1") as f:
            func(f)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
        
