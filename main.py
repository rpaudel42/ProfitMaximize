# ******************************************************************************
# main.py
#
# Date      Name       Description
# ========  =========  ========================================================
# 6/15/19   Paudel     Initial version,
# ******************************************************************************

from preprocess import Preprocess
from model import Model

data_file = 'yellow_tripdata_2017-06.csv'
nrows = 10000
def main():
    preprocess = Preprocess(data_file, nrows)

    taxi_dataset = preprocess.preprocess_data()

    print(taxi_dataset.head())

if __name__ == '__main__':
    main()