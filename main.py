# ******************************************************************************
# main.py
#
# Date      Name       Description
# ========  =========  ========================================================
# 6/19/19   Paudel     Initial version,
# ******************************************************************************

from preprocess import Preprocess
from prediction import Prediction

data_file = 'yellow_tripdata_2017-06.csv'
nrows = 2000000

def main():

    preprocess = Preprocess(data_file, nrows)
    taxi_summary, L, A, T, p_pick, p_tran, r, t_drive, t_wait = preprocess.preprocess_data()

    print("\n\nFeature Generation Completed .....")
    print("\n\n ---- Top 10 rows ---- \n\n", taxi_summary.head())

    prediction = Prediction()

    prediction.MDP_Dynamic_Program(L, A, T, p_pick, p_tran, r, t_drive, t_wait)

    print("\n\nStarting Revenue Prediction .....")
    prediction.predict_revenue(taxi_summary)

if __name__ == '__main__':
    main()