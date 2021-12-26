import pandas as pd
import numpy as np

data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Data Cleaning
data['TotalCharges'] = data['TotalCharges'].str.replace(' ','0')
data['TotalCharges'] = data['TotalCharges'].astype(float)

# Remove some columns
data.drop(['customerID'],axis=1,inplace=True)
data.replace('No internet service','No',inplace=True)
data.replace('No phone service','No',inplace=True)

# Encoding the data
X = data.iloc[:,:-1]
X = pd.get_dummies(X,drop_first=True)
Y = data['Churn']
y = Y.apply(lambda x: 0 if x=='No' else 1)

# Splitting the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=98,stratify=y)

# Data Scaling
from sklearn.preprocessing import MinMaxScaler
# fit scaler to training data
norm = MinMaxScaler().fit(X_train)

# transform training data
X_train_norm = norm.transform(X_train)

# transforming testing dataset
X_test_norm = norm.transform(X_test)

# Balancing the imbalance data using SMOTE
from imblearn.over_sampling import SMOTE
sm = SMOTE()
X_train_sm, y_train_sm = sm.fit_resample(X_train_norm,y_train)

# Model training using RandomForest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

max_depth = np.arange(5,15)
forest_param = [{'n_estimators':[20,50,100,150,300,500],
                 'criterion':['gini','entropy'],'max_depth':max_depth,
                'max_features':['sqrt','log2']}]

from sklearn.model_selection import RandomizedSearchCV
model_rf = RandomizedSearchCV(rf,forest_param,cv=10,verbose=2,n_jobs=-1)

model_rf.fit(X_train_sm,y_train_sm)

#print(X_train_sm.shape)
#print(X_train.shape)

import pickle

filename = 'telecom.pkl'
pickle.dump(model_rf,open(filename,'wb'))