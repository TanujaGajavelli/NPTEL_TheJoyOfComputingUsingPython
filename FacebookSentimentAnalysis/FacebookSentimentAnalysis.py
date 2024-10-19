import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file='posts.xlsx'
xl=pd.ExcelFile(file)  #Read from excel file
dfs=xl.parse(xl.sheet_names[0])  #Parsing excel sheet to data frame
dfs=list(dfs['TimeLine']) #Removes the blank rows from data frames
print(dfs)
sid=SentimentIntensityAnalyzer()
str1='pm'
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])