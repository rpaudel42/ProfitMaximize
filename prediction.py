# ******************************************************************************
# prediction.py
#
# Date      Name       Description
# ========  =========  ========================================================
# 6/17/19   Paudel     Initial version,
# ******************************************************************************
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

class Prediction():

    def __init__(self):
        pass

    def predict_linear_regression(self, X_train, X_test, y_train):
        '''
        Model for liner regression (to predict income)
        :param X_train:
        :param X_test:
        :param y_train:
        :return: Prediction val for train and test set
        '''
        lm = LinearRegression()
        lm.fit(X_train, y_train)
        y_pred_train = lm.predict(X_train)
        y_pred_test = lm.predict(X_test)
        return y_pred_train, y_pred_test

    def predict_rf_regression(self, X_train, X_test, y_train):
        '''
        Model for Random Forest regression (to predict income)
        :param X_train:
        :param X_test:
        :param y_train:
        :return: Prediction val for train and test set
        '''
        rf = RandomForestRegressor()
        rf.fit(X_train, y_train)
        y_pred_train = rf.predict(X_train)
        y_pred_test = rf.predict(X_test)
        return y_pred_train, y_pred_test

    def predict_revenue(self, taxi_summary):
        X = taxi_summary[
            ['hour', 'trip_distance', 'trip_duration', 'passenger_count', 'PULocationID',
             'DOLocationID']]
        y = taxi_summary['trip_revenue']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

        y_pred_train, y_pred_test = self.predict_linear_regression(X_train, X_test, y_train)
        print(" \n\n ----- Prediction using Linear Regression -----")
        ltest = np.sqrt(metrics.mean_squared_error(y_pred_test, y_test))
        print("Mean Square Error : ", ltest)

        y_pred_train, y_pred_test = self.predict_rf_regression(X_train, X_test, y_train)
        print(" \n\n ----- Prediction using Random Forest Regression -----")
        ltest = np.sqrt(metrics.mean_squared_error(y_pred_test, y_test))
        print("Mean Square Error : ", ltest)

        plt.scatter(y_test,y_pred_test)
        plt.show()

    def MDP_Dynamic_Program(self, L, A, T, p_pick, p_tran, r, t_drive, t_wait):
        '''
        Main Algorithm for implementation
        :param L:
        :param A:
        :param T:
        :param p_pick:
        :param p_tran:
        :param r:
        :param t_drive:
        :param t_wait:
        :return:
        '''
        print("\n\n Train the Algorithm for Optimum Policy")
        print("Due to time constraint I couldn't finish the code for this. \n Sorry for the inconvenience")
