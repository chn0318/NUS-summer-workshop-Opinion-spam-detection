import numpy as np
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
def remove_punctuation(text):
    text=" ".join(text.split())
    if(type(text)==float):
        return text
    ans=""  
    for i in text:     
        if i not in string.punctuation:
            ans+=i    
    return ans 

df=pd.read_csv("./data/deceptive-opinion.csv")
df['text']= df['text'].apply(lambda x:remove_punctuation(x))
keyword_list = ['very', 'VERY','!', 'really','REALLY', 'pretty', 'fairly', 'quite','greatly','highly','much', 'awfully', 'deeply', 'perfectly', 'absolutely','amazingly','completely','drastically', 'entirely','excessively','exceedingly','extremely','fully','largely','incredibly','wow','Wow', 'so','super','SO','SUPER']
result=pd.DataFrame(columns=["keyword","label"])
for i in range(0,len(df)):
    if df["deceptive"][i]=="truthful":
        sum_keyword=0
        for key in keyword_list:
            sum_keyword+=df["text"][i].count(key)
        result=result.append(pd.Series({"keyword":sum_keyword,"label":1}),ignore_index=True)
    else:
        sum_keyword=0
        for key in keyword_list:
            sum_keyword+=df["text"][i].count(key)
        result=result.append(pd.Series({"keyword":sum_keyword,"label":0}),ignore_index=True)
result.to_csv("./feature_vector/keyword.csv",sep=',',index=False,header=True)
