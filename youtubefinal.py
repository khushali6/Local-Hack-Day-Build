
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# %matplotlib inline
import warnings
warnings.filterwarnings("ignore")
from google.colab import files
data_to_load = files.upload()
import io
df = pd.read_csv(io.BytesIO(data_to_load['test_comments.csv']))
#import os
#print(os.listdir("../input"))

pd.set_option('display.max_columns',500)
from IPython.display import display
with pd.option_context('display.max_rows', 100, 'display.max_columns', 10):
    display(df) #need display to show the dataframe when using with in jupyter
    #some pandas stuff
#pd.set_option('display.max_columns',500)

US_comments = pd.read_csv('test_comments.csv', error_bad_lines=False)

#pd.set_option('display.max_columns',500)
from IPython.display import display
with pd.option_context('display.max_rows', 219, 'display.max_columns', 10):
    display(df)
US_comments.head()

US_comments.shape

US_comments.isnull().sum()

US_comments.dropna(inplace=True)

US_comments.isnull().sum()

US_comments.shape

US_comments.nunique()

US_comments.info()

#pd.set_option('display.max_columns',500)
#from IPython.display import display
#with pd.option_context('display.max_rows', 218, 'display.max_columns', 10):
#    display(df)
US_comments.head()
from IPython.display import display
with pd.option_context('display.max_rows', 218, 'display.max_columns', 10):
    display(df)

#from IPython.display import display
#with pd.option_context('display.max_rows', 100, 'display.max_columns', 10):
    #display(df) #need display to show the dataframe when using with in jupyter
    #some pandas stuff
tokenized_tweet = US_comments['Comment'].apply(lambda x: x.split())
tokenized_tweet.head()
from IPython.display import display
with pd.option_context('display.max_rows', 100, 'display.max_columns', 10):
    display(df)

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

wnl = WordNetLemmatizer()

import nltk
nltk.download('stopwords')
import nltk
nltk.download('wordnet')
tokenized_tweet.apply(lambda x: [wnl.lemmatize(i) for i in x if i not in set(stopwords.words('english'))]) 
tokenized_tweet.head()
from IPython.display import display
with pd.option_context('display.max_rows', 218, 'display.max_columns', 10):
    display(df)

for i in range(len(tokenized_tweet)):
    tokenized_tweet[i] = ' '.join(tokenized_tweet[i])

US_comments['Comment'] = tokenized_tweet

import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

US_comments['Sentiment Score'] = US_comments['Comment'].apply(lambda x:sia.polarity_scores(x)['compound'])
from IPython.display import display
with pd.option_context('display.max_rows', 218, 'display.max_columns', 10):
    display(df)

US_comments.head()
from IPython.display import display
with pd.option_context('display.max_rows', 218, 'display.max_columns', 10):
    display(df)

US_comments['Sentiment'] = US_comments['Sentiment Score'].apply(lambda s : 'Positive' if s > 0 else ('Neutral' if s == 0 else 'Negative'))
from IPython.display import display
with pd.option_context('display.max_rows', 218, 'display.max_columns', 10):
    display(df)

US_comments.head()
from IPython.display import display
with pd.option_context('display.max_rows', 218, 'display.max_columns', 10):
    display(df)

US_comments.Sentiment.value_counts()

all_words = ' '.join([text for text in US_comments['Comment']])
from wordcloud import WordCloud
wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)

plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()