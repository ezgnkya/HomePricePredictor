import pandas as pd
import joblib

class RealEstateModel:
    def __init__(self, model_file):
        self.model = joblib.load(model_file)
        self.feature_names = self.model.feature_names_in_

    def predict(self, new_data):
        new_data_df = pd.DataFrame([new_data])
        new_data_encoded = pd.get_dummies(new_data_df)
        new_data_encoded_reformatted = new_data_encoded.reindex(columns=self.feature_names, fill_value=0)
        predicted_price = self.model.predict(new_data_encoded_reformatted)
        return predicted_price

def predict_process(build_age, gross_square, room_count, town_name):
    model_file_path = "real_estate_model_v03.pkl"
    model = RealEstateModel(model_file_path)
    new_data_point = {
        'build_age': build_age,
        'gross_square': gross_square,
        'room_count': room_count,
        'town_name': town_name
    }
    predicted_price = model.predict(new_data_point)
    return int(predicted_price[0])


