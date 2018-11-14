
# coding: utf-8

# In[17]:


import glob
import nltk
from nltk.corpus import stopwords
import string
import pandas as pd


# In[18]:


def func(f):
    file = f.read()
    file = [ i for i in file if i not in string.punctuation ]
    file = ''.join(file)
    file = nltk.word_tokenize(file)
    file = [ word for word in file if word not in stopwords.words('english')]
    return len(set(file)) 


# In[21]:


files = glob.glob(r'E:\Project\text and web\articles1\*.txt')
data = {}
for name in files:
    filename = name.split('\\')[-1].split('.')[0]
    with open(name,encoding="utf8") as f:
        value = func(f)
        print(filename, value)
        data[filename]= value
print(data)  


# In[22]:


df = pd.read_csv('record.csv', encoding='iso-8859-1')


# In[23]:


lengths = [] 
for title in df['Title']:
    title = [ i for i in title if i not in string.punctuation+' ']
    title = ''.join(title)
    lengths.append(data[title])

df['Clean Tokens'] = lengths


# In[24]:


df.head()


# In[25]:


df.to_csv('#2 new_records.csv', index=False)

