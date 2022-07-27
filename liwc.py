import numpy as np
import pandas as pd
df=pd.read_csv("./data/LIWC-22 Results - deceptive-opinion - LIWC Analysis (1).csv")
result=df[df.columns[6:123]].copy(deep=True)
result["label"]=1
for i in range(len(df)):
    if df["deceptive"][i]=="deceptive":
        result["label"][i]=0
result.to_csv("./feature_vector/liwc.csv",sep=',',index=False,header=True)
