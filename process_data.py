import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
def get_train_test_data(df,feature):
    y=df["label"]
    x=df.drop(columns=["label"])
    (x_train,x_test,y_train,y_test)=train_test_split(x,y,test_size=0.25)
    train_path="./train_data/"+feature+"_train.csv"
    train_label=pd.DataFrame(y_train)
    train_label=train_label.rename(columns={0:'label'})
    train_data=pd.concat([x_train,train_label],axis=1)
    test_path="./test_data/"+feature+"_test.csv"
    test_label=pd.DataFrame(y_test)
    test_label=test_label.rename(columns={0:'label'})
    test_data=pd.concat([x_test,test_label],axis=1)
    train_data.to_csv(train_path,sep=',',index=False,header=True)
    test_data.to_csv(test_path,sep=',',index=False,header=True)


df_postag=pd.read_csv("./feature_vector/postag.csv")
df_liwc=pd.read_csv("./feature_vector/liwc.csv")
df_similar=pd.read_csv("./feature_vector/similar.csv")
df_keyword=pd.read_csv("./feature_vector/keyword.csv")
df_postag_liwc=pd.concat([df_postag.drop(columns=["label"]),df_liwc],axis=1)
df_all_feature=pd.concat([df_similar.drop(columns=["label"]),df_keyword.drop(columns=["label"]),df_postag_liwc],axis=1)

get_train_test_data(df_postag, "postag")
get_train_test_data(df_liwc, "liwc")
get_train_test_data(df_similar, "similar")
get_train_test_data(df_keyword, "keyword")
get_train_test_data(df_postag_liwc, "postag_liwc")
get_train_test_data(df_all_feature, "all_feature")