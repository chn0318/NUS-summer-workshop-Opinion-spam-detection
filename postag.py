import nltk
from nltk import *
from nltk.tag.stanford import StanfordPOSTagger
from nltk.tokenize import word_tokenize
import numpy as np 
import pandas as pd 
java_path = "D:/JDK/bin/java.exe"
os.environ["JAVAHOME"] = java_path
jar = "D:/stanford-postagger-2018-10-16/stanford-postagger-2018-10-16/stanford-postagger.jar"
model = "D:/stanford-postagger-2018-10-16/stanford-postagger-2018-10-16/models/english-bidirectional-distsim.tagger"
pos_tagger = StanfordPOSTagger(model, jar, encoding = "utf-8")
df=pd.read_csv("./data/deceptive-opinion.csv")  
feature_vector_list=[]
for i in range(0,len(df)):
    print(i)
    tagger_dict={',':0, 'JJS':0, '#':0, 'VB':0, 'RBR':0, 'PRP$':0, 'LS':0, 'NN':0, 'VBP':0, 'MD':0, 'VBG':0, 'EX':0, 'VBZ':0, 'RBS':0, 'JJ':0, '.':0, 'JJR':0, 'NNPS':0, 'VBD':0, 'NNS':0, '$':0, 'RP':0, '``':0, 'IN':0, 'DT':0, 'TO':0, "''":0, ':':0, 'CC':0, 'VBN':0, 'PRP':0, 'WP':0, 'WDT':0, 'FW':0, 'NNP':0, 'UH':0, 'WRB':0, 'CD':0, 'PDT':0, 'SYM':0, 'POS':0, 'RB':0,'label':-1}
    if df["deceptive"][i]=="truthful":
        tagger_dict["label"]=1
    else:
        tagger_dict["label"]=0
    text=df["text"][i]
    words = nltk.word_tokenize(text)
    tagged_words = pos_tagger.tag(words)
    for j in range(len(tagged_words)):
        tagger_dict[tagged_words[j][1]]+=1
    feature_vector_list.append(tagger_dict)
feature_vector= pd.DataFrame(feature_vector_list)
feature_vector.to_csv("./feature_vector/postag.csv",sep=',',index=False,header=True)
