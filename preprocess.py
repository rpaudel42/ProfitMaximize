# ******************************************************************************
# preprocess.py
#
# Date      Name       Description
# ========  =========  ========================================================
# 6/16/19   Paudel     Initial version,
# ******************************************************************************
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#set seaborn style to matplotlib
plt.style.use('seaborn-whitegrid')


class Preprocess():

    def __init__(self, file_name, nrows):
        self.taxi_df = pd.read_csv(file_name, nrows=nrows)


    def clean_data(self):
        '''
        Remove null and outliers
        :param taxi_df:
        :return:
        '''
        self.taxi_df = self.taxi_df.dropna(how='any', axis='rows')
        self.taxi_df = self.taxi_df[self.taxi_df.fare_amount >= 0]
        self.taxi_df = self.taxi_df[self.taxi_df.extra >= 0]
        self.taxi_df = self.taxi_df[self.taxi_df.passenger_count <= 6]

    def generate_feature(self):
        '''
        generate summary statistics related to the fare information by grouping based on day, hour, pickup location, and dropoff location.
        :return:
        '''
        self.taxi_df['tpep_pickup_datetime'] = pd.to_datetime(self.taxi_df.tpep_pickup_datetime)
        self.taxi_df['tpep_dropoff_datetime'] = pd.to_datetime(self.taxi_df.tpep_dropoff_datetime)

        self.taxi_df['hour'] = self.taxi_df['tpep_pickup_datetime'].apply(lambda x: x.hour)
        self.taxi_df['day'] = self.taxi_df['tpep_pickup_datetime'].apply(lambda x: x.day)
        self.taxi_df['trip_duration'] = (self.taxi_df['tpep_dropoff_datetime'] - self.taxi_df['tpep_pickup_datetime']).astype(
            'timedelta64[m]')

        taxi_summary = self.taxi_df.groupby(['day', 'hour', 'PULocationID', 'DOLocationID']).agg(
            {'VendorID': ['count'], 'passenger_count': ['sum'], 'trip_distance': ['mean'], 'total_amount': ['mean'],
             'trip_duration': ['mean']}).reset_index()
        taxi_summary.columns = ['day', 'hour', 'PULocationID', 'DOLocationID', 'trip_count', 'passenger_count',
                                'trip_distance', 'trip_amount', 'trip_duration']
        return taxi_summary

    def preprocess_data(self):
        '''
        clean and return final summary data set
        :return:
        '''
        self.clean_data()
        return self.generate_feature()
