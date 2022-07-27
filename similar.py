import numpy as np
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
# 测量jaccard距离
def jaccard_sim(a, b):
    unions = len(set(a).union(set(b)))
    intersections = len(set(a).intersection(set(b)))
    return intersections / unions
# 去除标点func
def remove_punctuation(text):
    text=" ".join(text.split())
    if(type(text)==float):
        return text
    ans=""  
    for i in text:     
        if i not in string.punctuation:
            ans+=i    
    return ans
# 生成n-gram
def generate_N_grams(text,ngram=1):
    words=[word for word in text.split(" ") if word not in set(stopwords.words('english'))]  # Sentence after removing stopwords
    temp=zip(*[words[i:] for i in range(0,ngram)]) # decompression
    ans=[' '.join(ngram) for ngram in temp]
    return ans

df=pd.read_csv("./data/deceptive-opinion.csv")
df['text']= df['text'].apply(lambda x:remove_punctuation(x))
N_grams_list=[]
for i in range(len(df)):
    N_grams_list.append(generate_N_grams(df["text"][i],2))
similar_vector=[]  
for i in range(len(df)):
    similar=0
    for j in range(0,len(df)):
        if i!=j:
            tmp=jaccard_sim(N_grams_list[i],N_grams_list[j])
            if similar<tmp:
                similar=tmp
    similar_vector.append(similar)
result=pd.DataFrame(columns=["similarity","label"])
result["similarity"]=similar_vector
for i in range(len(result)):
    if df["deceptive"][i]=="truthful":
        result["label"][i]=1
    else:
        result["label"][i]=0
result.to_csv("./feature_vector/similar.csv",sep=',',index=False,header=True)