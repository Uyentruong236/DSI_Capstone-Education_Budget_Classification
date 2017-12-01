import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from spacy.en import English
from nltk.stem.porter import PorterStemmer
import nltk
from nltk.corpus import stopwords
from spacy.en import STOP_WORDS
nlp = English()


targets = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type',
       'Position_Type', 'Object_Type', 'Pre_K', 'Operating_Status']

word_predictors = ['Object_Description','Text_2','SubFund_Description','Job_Title_Description','Text_3','Text_4',      'Sub_Object_Description','Location_Description','Function_Description','Facility_or_Department','Position_Extra','Program_Description','Fund_Description','Text_1']

num_predictors = ['FTE', 'Total']
