# HKJC_db-Logistc-Regression
HKJC database Logistic Regression Forecast

-Download the Latest ver. from the Release

How to use?
1.Go to the folder z_Setting
There are 1 file and 3 Folder included.

File - para.txt
1.targetCol - the column that represents the result of the particular horse in a single race
2.drpoArr_rawData - Add or Delete the columns to be included in base raw data
3.dropArr_predictionData - Add or Delete the columns to be included in test data
4.module_run - 
set 0 = run Logistic Regression only
set 1 = run prediction only(must have the previous model result first)
set 2 = run both option of 0 and 1
5.testSize_sample - the ratio of training data set from the raw dataset, default is 0.25
6.randomState_sample - default is 0
7.testAccuracy_sample? - default is 0
8.setResult_limit - means the horse result in what level inculsive i.e set 1 = only wins, set 4 = below or equal to 4


Folder - predict_set base raw:
put the raw dataset from HKJC db in csv format

Folder - predict_set test:
This is the dataset to generate the prediction in txt format with separator ("|")

Folder - predict_set result:
It is the outcome of the Logistic Regression run in csv format

