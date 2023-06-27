# HKJC_db-Logistic-Regression
HKJC database Logistic Regression Forecast

-Download the Latest ver. from the Release

How to use?
1.Go to the folder z_Setting
There are 1 file and 3 Folder included.

File - para.txt

1.targetCol - the column that represents the result of the particular horse in a single race

2.dropArr_rawData - Delete the columns not to be included in base raw data by placing the name

3.dropArr_predictionData - Delete the columns not to be included in test data by placing the name 

4.module_run - 

set to 0 = run Logistic Regression only

set to 1 = run prediction only(must have the previous model result first i.e. logistic_model.sav)

set to 2 = run both Logistic Regression and Prediction

5.testSize_sample - the ratio of training dataset and testing dataset from the raw dataset, default is 0.25 of test sample size, 0.75 traning dataset

6.randomState_sample - default is 0

7.testAccuracy_sample? - default is 0

8.setResult_limit - forecast the result of the horse limit to what level i.e set to 2 = below or equal to 2, set to 4 = below or equal to 4


Folder - predict_set base raw:
put the raw dataset from HKJC db in csv format with separator ("|")

Folder - predict_set test:
This is the dataset to be created for the prediction in txt format with separator ("|")

Folder - predict_set result:
It is the outcome of the Logistic Regression run by giving the result in csv format and the predicted percentage is given between 0 and 1

*Once the setting and the dataset is ready, click the logisticRegression_skl.exe to run the result
