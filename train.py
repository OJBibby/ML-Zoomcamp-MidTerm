import numpy as np
import pandas as pd
import xgboost as xgb
import bentoml
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

df = pd.read_csv('insurance.csv')
df = df[(df['charges'] < df['charges'].mean() + 3*df['charges'].std())].copy()
df = df[(df['bmi'] < df['bmi'].mean() + 3*df['bmi'].std())].copy()
X = df.drop(columns=['charges'])
y = df['charges'].values
dicts = X.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)
X_full_train, X_test, y_full_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_full_train, y_full_train, test_size=0.25, random_state=42)
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=dv.get_feature_names())
dval = xgb.DMatrix(X_val, label=y_val, feature_names=dv.get_feature_names())
xgb_params = {
    'eta': 0.25,
    'max_depth': 2,
    'min_child_weight': 1,

    'objective': 'reg:squarederror',
    'nthread': 8,
    'eval_metric': 'rmse',
    'seed': 42,
    'verbosity': 1,
}
model = xgb.train(xgb_params, dtrain, num_boost_round=100)
print(bentoml.xgboost.save_model("medical_cost_model", model, custom_objects={"dictVectorizer": dv}))