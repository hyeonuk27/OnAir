import pandas as pd
import numpy as np
import joblib

def getEncoded(data,labelencoder_dict,onehotencoder_dict):
    # except passengers
    data_exc = data.iloc[:, :-1]
    encoded_x = None
    for i in range(0,data_exc.shape[1]):
        label_encoder =  labelencoder_dict[i]
        feature = label_encoder.transform(data_exc.iloc[:,i])
        feature = feature.reshape(data_exc.shape[0], 1)
        onehot_encoder = onehotencoder_dict[i]
        feature = onehot_encoder.transform(feature)
        if encoded_x is None:
            encoded_x = feature
        else:
            encoded_x = np.concatenate((encoded_x, feature), axis=1)

    encoded_x = np.concatenate((encoded_x, data.iloc[:, -1].to_numpy().reshape(-1, 1)), axis=1)

    return encoded_x


model = joblib.load('./delay_rate_predict.pkl')
labelencoder = joblib.load('./labelencoder_dict.pkl')
onehotencoder = joblib.load('./onehotencoder_dict.pkl')
data = pd.DataFrame([['제주항공', 'TAO(청도)', 'Mist', 178981]], columns = ['airline', 'arrival', 'weather', 'passengers'])
input_data = getEncoded(data, labelencoder, onehotencoder)
print(model.predict_proba(input_data))