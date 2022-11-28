from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder
import pickle


df=pd.read_csv("data.csv")
df=df.drop(["etest_p","mba_p","sl_no"],axis=1)




object_cols=['gender','workex','specialisation','status']
Q1 = df['hsc_p'].quantile(0.25)
Q3 = df['hsc_p'].quantile(0.75)
IQR = Q3 - Q1 
filter = (df['hsc_p'] >= Q1 - 1.5 * IQR) & (df['hsc_p'] <= Q3 + 1.5 *IQR)
placement_filtered=df.loc[filter]

label_encoder = LabelEncoder()
for col in object_cols:
    placement_filtered[col] = label_encoder.fit_transform(placement_filtered[col])




dummy_hsc_b=pd.get_dummies(placement_filtered['hsc_b'], prefix='dummy')
dummy_ssc_b=pd.get_dummies(placement_filtered['ssc_b'], prefix='dummy')
dummy_hsc_s=pd.get_dummies(placement_filtered['hsc_s'], prefix='dummy')
dummy_degree_t=pd.get_dummies(placement_filtered['degree_t'], prefix='dummy')
placement_coded = pd.concat([placement_filtered,dummy_hsc_s,dummy_degree_t,dummy_hsc_b,dummy_ssc_b],axis=1)
placement_coded.drop(['hsc_b','degree_t','salary','ssc_b','hsc_s'],axis=1, inplace=True)


X=placement_coded.drop(['status'],axis=1)
y=placement_coded['status']
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8,random_state=1)

model=RandomForestClassifier(n_estimators=100,random_state=1)
model.fit(X_train,y_train)
# y_pred=model.predict(X_test)
# model_exp=pickle.dumps(model)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
