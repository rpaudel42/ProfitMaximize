# ******************************************************************************
# preprocess.py
#
# Date      Name       Description
# ========  =========  ========================================================
# 6/19/19   Paudel     Initial version,
# ******************************************************************************
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Preprocess():

    def __init__(self, file_name, nrows):
        print("\n\nReading Data File Started . . .")
        self.taxi_df = pd.read_csv(file_name, nrows=nrows)
        print("Total Rows: ", len(self.taxi_df))

    def clean_data(self):
        '''
        Remove null and outliers
        :param taxi_df:
        :return:
        '''
        print("\n\nCleaning Data . . .")
        self.taxi_df = self.taxi_df.dropna(how='any', axis='rows')
        self.taxi_df = self.taxi_df[self.taxi_df.fare_amount >= 0]
        self.taxi_df = self.taxi_df[self.taxi_df.extra >= 0]
        self.taxi_df = self.taxi_df[self.taxi_df.passenger_count <= 6]


    def get_pickup_prob(self, pickup, dropoff):
        '''
        Calculate pickup probability for each location and time (hour of the day)
        :param pickup:
        :param dropoff:
        :return: dict of pickup probability based on location and time
        '''
        pickup_count = {}
        dropoff_count = {}
        p_pick = {}
        for index, row in dropoff.iterrows():
            key = str(row['DOLocationID'])+ ' '+ str(row['hour'])
            if key in dropoff_count:
                dropoff_count[key] += row['n_dropoff']
            else:
                dropoff_count[key] = row['n_dropoff']
        for index, row in pickup.iterrows():
            key = str(row['PULocationID'])+ ' '+ str(row['hour'])
            if key in pickup_count:
                pickup_count[key] += row['n_pickup']
            else:
                pickup_count[key] = row['n_pickup']

        for key in pickup_count:
            if key in dropoff_count:
                p_pick[key] = (pickup_count[key]/(pickup_count[key]+dropoff_count[key]))

        return p_pick

    def get_tranist_prob(self,taxi_transit):
        p_tran = {}
        trip_count = {}
        total = {}
        for index, row in taxi_transit.iterrows():
            if str(row['hour']) in total:
                total[str(row['hour'])] += row['n_trip']
            else:
                total[str(row['hour'])] = row['n_trip']

            key = str(row['PULocationID']) + ' ' + str(row['DOLocationID']) + ' ' +  str(row['hour'])

            if key in trip_count:
                trip_count[key] += row['n_trip']
            else:
                trip_count[key] = row['n_trip']

        for key in trip_count:
            hour = key.split(' ')[2]
            p_tran[key] = trip_count[key]/total[hour]
        return p_tran

    def get_location_list(self, file_name):
        '''
        Get list of all the pickup/dropoff location
        :param file_name:
        :return: Location array
        '''
        location = pd.read_csv(file_name)
        return np.array(location['LocationID'])

    def generate_feature(self):
        '''
        generate summary statistics related to the fare information by grouping based on day, hour, pickup location, and dropoff location.
        :return:
        '''

        self.taxi_df['tpep_pickup_datetime'] = pd.to_datetime(self.taxi_df.tpep_pickup_datetime)
        self.taxi_df['tpep_dropoff_datetime'] = pd.to_datetime(self.taxi_df.tpep_dropoff_datetime)

        self.taxi_df['hour'] = self.taxi_df['tpep_pickup_datetime'].apply(lambda x: x.hour)
        self.taxi_df['trip_duration'] = (self.taxi_df['tpep_dropoff_datetime'] - self.taxi_df['tpep_pickup_datetime']).astype(
            'timedelta64[m]')

        #find wait time between trip in same location
        self.taxi_df['prev_drop_time'] = self.taxi_df['tpep_dropoff_datetime'].shift(1)[
            (self.taxi_df['VendorID'] == self.taxi_df['VendorID'].shift(1))]# & (self.taxi_df['PULocationID'] == self.taxi_df['DOLocationID'].shift(1))]

        self.taxi_df = self.taxi_df.dropna(how='any', axis='rows')  # .reset_index()

        self.taxi_df['wait_time'] = (self.taxi_df['tpep_pickup_datetime'] - self.taxi_df['prev_drop_time']).astype('timedelta64[m]')

        taxi_summary = self.taxi_df.groupby(['hour', 'PULocationID', 'DOLocationID']).agg(
            { 'passenger_count': ['sum'], 'trip_distance': ['mean'],
             'trip_duration': ['mean'], 'wait_time':['mean'], 'PULocationID':['count'],  'total_amount': ['mean']}).reset_index()
        taxi_summary.columns = ['hour', 'PULocationID', 'DOLocationID', 'passenger_count',
                                'trip_distance', 'trip_duration', 'wait_time', 'n_trip', 'trip_revenue']
        taxi_summary.reset_index()

        taxi_pickup = taxi_summary.groupby(['hour', 'PULocationID']).agg({'n_trip':['sum']}).reset_index()
        taxi_pickup.columns=['hour', 'PULocationID', 'n_pickup']
        taxi_dropup = taxi_summary.groupby(['hour', 'DOLocationID']).agg({'n_trip': ['sum']}).reset_index()
        taxi_dropup.columns = ['hour', 'DOLocationID', 'n_dropoff']

        p_pick = self.get_pickup_prob(taxi_pickup, taxi_dropup)

        taxi_transit = taxi_summary.groupby(['hour', 'PULocationID', 'DOLocationID']).agg({'n_trip':['sum']}).reset_index()
        taxi_transit.columns = ['hour', 'PULocationID', 'DOLocationID', 'n_trip']
        p_tran = self.get_tranist_prob(taxi_transit)

        L = self.get_location_list('taxi+_zone_lookup.csv')
        T = [x for x in range(24)]
        t_drive = np.array(taxi_summary[['PULocationID', 'DOLocationID','hour','trip_duration']])
        t_wait = np.array(taxi_summary[['PULocationID', 'DOLocationID', 'hour', 'trip_duration']])
        r = np.array(taxi_summary[['PULocationID', 'DOLocationID','hour', 'trip_revenue']])
        A = np.array(taxi_summary[['PULocationID', 'DOLocationID', 'hour']])

        return taxi_summary, L, A, T, p_pick, p_tran, r, t_drive, t_wait

    def preprocess_data(self):
        '''
        clean and return final summary data set
        :return:
        '''
        self.clean_data()
        print("\n\nCleaning Completed")

        print("\n\nGenerating Features .....")
        return self.generate_feature()
