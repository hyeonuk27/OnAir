import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

labelencoder_dict = {}
onehotencoder_dict = {}
df = pd.read_csv('./ml_data.csv', index_col = 0)
df_X = df.drop(['state', 'delayed_time', 'weather', 'passengers'], axis=1)
X = None
for i in range(0, df_X.shape[1]):
    label_encoder = LabelEncoder()
    labelencoder_dict[i] = label_encoder
    feature = label_encoder.fit_transform(df_X.iloc[:,i].astype(str))
    feature = feature.reshape(df_X.shape[0], 1)
    onehot_encoder = OneHotEncoder(drop='first', sparse=False)
    feature = onehot_encoder.fit_transform(feature)
    onehotencoder_dict[i] = onehot_encoder
    if X is None:
        X = feature
    else:
        X = np.concatenate((X, feature), axis=1)

min_max_scaler = MinMaxScaler()
X_passengers = df['passengers'].to_frame()
min_max_scaler.fit(X_passengers)
X_scaled = min_max_scaler.transform(X_passengers)
X_scaled = pd.DataFrame(X_scaled, columns=X_passengers.columns)
X = np.concatenate((X, X_scaled), axis=1)
Y = df[df.columns[4]].to_numpy()
np.set_printoptions(precision=6, suppress=True)

train_input, test_input, train_target, test_target = train_test_split(X, Y, random_state=42)
lr = LogisticRegression()
lr.fit(train_input, train_target)
print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))

joblib.dump(lr, './delay_rate_passengers_predict.pkl')
joblib.dump(min_max_scaler, './passengers_min_max_scaler.pkl')