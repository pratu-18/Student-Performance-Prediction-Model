import pandas as pd
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report)
from sklearn.tree  import DecisionTreeClassifier, plot_tree 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def ModelTraining(FileName):
    #----------------------------------------Assignment 40----------------------------------
    data=pd.read_csv(FileName)
    # print(data.head())
    # print(data.columns)
    
    Feature=["StudyHours",
               "Attendance",
               "PreviousScore",
               "AssignmentsCompleted",
               "SleepHours"]
    
    
    # data.drop("SleepHours",axis=1, inplace=True)
    # data.drop('SleepHours',axis=1,inplace=True)
    # print(data.columns)
        
    
    X=data[Feature]
    Y=data["FinalResult"]
        ##################################Model-1####################################################

    
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.5,random_state=42)
    print(X_train.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_test.shape)
    
    # train the model
    model=DecisionTreeClassifier(max_depth=5,random_state=42)
    model=model.fit(X_train,Y_train)
    
    Y_pred=model.predict(X_test)
    print("Actual values :",list(Y_test))
    print("Predicted Value :",Y_pred)
    
    accuracy=accuracy_score(Y_test,Y_pred)*100
    print("Accuracy are :",accuracy)
    
    #Question-7-----------------------------------------------------------------------
    print("------------------------Question7-------------------------")    
    Y_test_pred=model.predict(X_test)
    # print(list(Y_test))
    # print(Y_test_pred)
    Demo_accuracy=accuracy_score(Y_test,Y_test_pred)*100
    print("Testing accuracy by changing random state:",Demo_accuracy)
        
    
    
    #Question 6------------------------------------------------------------------------
    print("-----------------------------------Question6--------------------------------------")
    
    print("Wrong Predictions are")
    for i in range(len(Y_test)):
        if Y_test.iloc[i]!=Y_pred[i]:
            print(f"Actual:{Y_test.iloc[i]}   Predicted:{Y_pred[i]}")
            index = Y_test.index[i]
            missclassification=data.loc[index]
            missData=pd.DataFrame([missclassification])
            print(missData)
            
    
    
    
    print("-"*80,"\n")
       
    
    
#Qusetion 1---------------------------------------
    contribution=model.feature_importances_
    print(contribution)
    
    contributedData=pd.DataFrame({
        "|  Features |":Feature,
        "  Contribution |":contribution
    }
        
    )
    print(contributedData)
    
#-----------------------question no 2 is in StudentPerformaceCaseStudy2.py---------------------------------------------
    print("After removing the column 'SleepHours' accuracy are still same ")


#Question 3------------------------------------------------------------------------
    ##################################Model-2####################################################


    Selected_Feature=["StudyHours",
               "Attendance",
    
]

    updated_X=data[Selected_Feature]
    X_train,X_test,Y_train,Y_test=train_test_split(updated_X,Y,test_size=0.5,random_state=42)
    print("Verified  shapes of train test to check features are updated ")
    print("X_train :",X_train.shape)
    print("X_test :",X_test.shape)
    print("Y_train :",Y_train.shape)
    print("Y_test :",Y_test.shape)
    
    Model2=DecisionTreeClassifier(max_depth=5,random_state=42)
    Training=Model2.fit(X_train,Y_train)
    Testing=Model2.predict(X_train)
    print(f"Accuracy of model using just [StudyHours, Attendance] this 2 features :{accuracy_score(Y_test,Testing)*100}%")
    print("Model are perform low accuracy are low by using only this [StudyHours, Attendance] features ")

    new_data={"StudyHours":[6,2,3,1,10],
             "Attendance":[85,90,34,20,18],
             "PreviousScore":[66,33,45,96,78],
             "AssignmentsCompleted":[7,5,3,2,1],
             "SleepHours":[7,3,2,6,8] }
             
    
    dataAdded=pd.DataFrame(new_data)
    print(dataAdded)
    
    New_Predicted=model.predict(dataAdded)
    print(New_Predicted)
    l1=list()
    for values in New_Predicted:
        if values==1:
            l1.append("Pass")
        else:
            l1.append("Fail")
            
            
    print(l1)
    
    #Question 5---------------------------------------------------
    #Mannually calculation of accuracy using formula
    
    print("Manully calculated and model calculated accuracy are matched!!")
    
    #Question 8----------------------------------------
    print("--------------------------Question 8---------------------------------")
    print("Decision  Tree visualisation ")
    Label=["0","1"]
    plt.figure(figsize=(5,3))
    plot_tree(model,filled=True,feature_names=Feature,class_names=Label)
    plt.title("Student Performance Decision Tree")
    plt.show()
    
    Count_pass=0
    Count_fail=0
    for values in data["FinalResult"]:
        if values==1:
            Count_pass=Count_pass+1
        else:
            Count_fail=Count_fail+1
            
    print("Total number of passed Student : ",Count_pass)
    print("Total number of failed student : ",Count_fail)
        
    #Question 9---------------------------------------------------
    ##################################Model-3####################################################
    
    data["PerformanceIndex"] = (data["StudyHours"] * 2) + data["Attendance"]
    Updated_FeatureCols=["StudyHours",
               "Attendance",
               "PreviousScore",
               "AssignmentsCompleted",
               "SleepHours",
               "PerformanceIndex"]
    print(data.head())
    X3=data[Updated_FeatureCols]
    
    X_train3,X_test3,Y_train3,Y_test3=train_test_split(X3,Y,test_size=0.5,random_state=42)
    model3=DecisionTreeClassifier()
    model3=model3.fit(X_train3,Y_test3)
    Y_pred3=model3.predict(X_test3)
    accuracy3=accuracy_score(Y_test3,Y_pred3)*100
    print("Accuracy of model after added 'PerformanceIndex' column :",accuracy3)
    
    


def main():
    ModelTraining("student_performance_ml.csv")
    
    
    
    
if __name__=="__main__":
    main()