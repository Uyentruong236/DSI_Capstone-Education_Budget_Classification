import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV, train_test_split, StratifiedShuffleSplit
from sklearn.preprocessing import Imputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import log_loss,roc_auc_score, roc_curve, accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


targets = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type',
       'Position_Type', 'Object_Type', 'Pre_K', 'Operating_Status']

word_predictors = ['Object_Description','Text_2','SubFund_Description','Job_Title_Description','Text_3','Text_4',      'Sub_Object_Description','Location_Description','Function_Description','Facility_or_Department','Position_Extra','Program_Description','Fund_Description','Text_1']

num_predictors = ['FTE', 'Total']

predictors = ['Object_Description','Text_2','SubFund_Description','Job_Title_Description','Text_3','Text_4',      'Sub_Object_Description','Location_Description','Function_Description','Facility_or_Department','Position_Extra','Program_Description','Fund_Description','Text_1', 'FTE', 'Total']