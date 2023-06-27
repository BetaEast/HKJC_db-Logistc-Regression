import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import sklearn.metrics as metrics
import pandas as pd
from pathlib import Path
import os
import glob
import statsmodels.api as sm
import pickle



theRootPath = str(Path(os.path.dirname(__file__)))
thePara = theRootPath + "/z_Setting/para.txt"
savedModel = theRootPath + "/z_Setting/logistic_model.sav"
 
theData = ""
theTest = ""
for f in os.listdir(theRootPath + "/z_Setting/predict_set base raw"):
    theData = theRootPath + "/z_Setting/predict_set base raw/" + f

for f in os.listdir(theRootPath + "/z_Setting/predict_set test"):
    theTest = theRootPath + "/z_Setting/predict_set test/" + f


dataFrame = pd.read_csv(theData, sep = '|', encoding='utf8')
test_set = pd.read_csv(theTest, sep = '|', encoding='utf8')






lines1 = []
with open(thePara,'r', encoding='utf8') as f:
    lines1 = f.readlines()

startIndex1 = []
count1 = 0
for line in lines1:
    count1 = count1 + 1
    x = line.find("=") + 1
    startIndex1.append(x)

targetCol = lines1[0][startIndex1[0]:].strip()
drop_Arr_data_temp = lines1[1][startIndex1[1]:].strip()
drop_Arr_test_temp = lines1[2][startIndex1[2]:].strip()
theModule = int(lines1[3][startIndex1[3]:].strip())
testSize = float(lines1[4][startIndex1[4]:].strip())
randomState = int(lines1[5][startIndex1[5]:].strip())
testAccur = int(lines1[6][startIndex1[6]:].strip())
resultLimit = int(lines1[7][startIndex1[7]:].strip())

#sub into the result limit for the model:
dataFrame["result"] = np.where(dataFrame["result"] <= resultLimit, 1, 0)


temp_Arr1 = drop_Arr_data_temp.split(',')
temp_Arr2 = drop_Arr_test_temp.split(',')

drop_Arr_data = []
for theName in temp_Arr1:
    drop_Arr_data.append(theName)

drop_Arr_test = []   
for theName in temp_Arr2:
    drop_Arr_test.append(theName)



def run_logistic_regression():
    if testAccur == 0:
        
        X_train = dataFrame.drop(drop_Arr_data,axis=1)
        y_train = dataFrame[targetCol]
        log_reg = sm.Logit(y_train, X_train).fit()

        print(log_reg.summary())
        print("\n")

        logmodel = LogisticRegression()
        result = logmodel.fit(X_train, y_train)

    elif testAccur == 1:
        X_train, X_test, y_train, y_test = train_test_split(
        dataFrame.drop(drop_Arr_data,axis=1), 
        dataFrame[targetCol], 
        test_size=testSize, random_state=randomState)     
        
        #use the statsmodels to gen the statistics
        log_reg = sm.Logit(y_train, X_train).fit()
        print(log_reg.summary())
        print("\n")
        
        #train the raw data 
        logmodel = LogisticRegression()
        result = logmodel.fit(X_train, y_train)


        Predictions = result.predict(X_test)
        print(metrics.confusion_matrix(y_test, Predictions))
        print(metrics.classification_report(y_test,Predictions))
        print ("Accuracy : ", accuracy_score(y_test, Predictions))


    pickle.dump(result, open(savedModel, 'wb'))
    print("the logistic Model has been saved....")
    print("\n")

def run_predictSet_data():    
    df = pd.DataFrame(test_set)
    df1 = df.drop(drop_Arr_test,axis=1)

    # load the model from disk
    loaded_model = pickle.load(open(savedModel, 'rb'))
    
    df['Prob'] = loaded_model.predict_proba(df1)[:, 1] #sliced the array, taking all rows (:) but keeping the second column (1)
    df['Result'] = loaded_model.predict(df1)    

    df.to_csv(theRootPath + '/z_Setting/predict_set result/predict_result.csv', index=False, encoding='utf_8_sig')
    print('predicted result.csv is exported....')



if __name__ == "__main__": 
    try:
        if theModule == 0:
            run_logistic_regression()
        elif theModule == 1:        
            run_predictSet_data()
        elif theModule == 2:
            run_logistic_regression()
            run_predictSet_data()
        input("Press enter to exit...")
    except Exception as e:        
        print(str({e}))  
        print("failed to proceed...pls find the error above...")
        input("Press enter to exit...")




   

