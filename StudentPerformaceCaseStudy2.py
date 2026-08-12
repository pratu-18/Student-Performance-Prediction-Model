from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
    #----------------Assignment 39------------
   #decide X and Y
   
   
   CSV=pd.read_csv("student_performance_ml.csv")
   
   Feature_Cols=["StudyHours",
           "Attendance",
           "PreviousScore",
           "AssignmentsCompleted",
           "SleepHours"]
   
   label_Cols="FinalResult"
   
   print("Features are (X) :",Feature_Cols)
   print("labels are (Y) :",label_Cols)
   
   
   X=CSV[Feature_Cols]
   Y=CSV["FinalResult"]
   
   print("Shape of X are :",X.shape)#(30,5)
   print("Shape of Y are :",Y.shape)#(30)
   
   X_tain,X_test,Y_train,Y_test=train_test_split(X,Y, train_size=0.5,random_state=42)
  
   print(CSV.shape)
   print("X_train :",X_tain.shape)
   print("X_test :",X_test.shape)
   print("Y_train :",Y_train.shape)
   print("Y_test :",Y_test.shape)
   
   
   #Question 1----------------------------------
   
   
   model=DecisionTreeClassifier(max_depth=5,random_state=42)
   model=model.fit(X_tain,Y_train)
   print("----------------------------Question-1 -----------------------------------------")
   print("Model trained sucessfully")
   
   #Question 2----------------------------
   print("--------------------------------Question-2 -----------------------------------------")
   Y_pred=model.predict(X_test)
   
   print("Actual values are :")
   print(list(Y_test))
   print("Predicted value are :")
   print(Y_pred)
   
   
   
    #Question-3 -----------------------------------------
   print("---------------------------------Question-3 -----------------------------------------")
   accurancy=accuracy_score(Y_test,Y_pred)
   print("Accurancy are :",accurancy*100,"%","Model Size are :",CSV.shape)
   
   
   #Question 4----------------------------------------------------------------
   print("---------------------------------Question-4 -----------------------------------------")
   Cm=confusion_matrix(Y_test,Y_pred)
   print("Confusion Mattrix are :")
   print(Cm)
   
   
   #Question 5---------------------------------------------------
   print("---------------------------------Question-5 -----------------------------------------")
   
   #Trainning Accurancy------------------------
   
   Y_Tain_pred=model.predict(X_tain)
   print(f"Tranning accurancy are :{accuracy_score(Y_train,Y_Tain_pred)*100}")
#    print("Tranning actual (Y_train) ",list(Y_train))
#    print("Traning Predicted (Y_Train_pred) :",Y_Tain_pred)
   
   
   
   #Testing Accurancy---------------------------------------
   Y_test_pred=model.predict(X_test)
   print(f"Testing accurancy area :{accuracy_score(Y_test,Y_test_pred)*100} ")
   
   print("|-----------This model are slightly overfitting------------|")
#    print("Testing actual answer are (Y_test) :",list(Y_test))
#    print("Testing predicted answer are (Y_test_pred) :",Y_test_pred)
   
   
   
   
#Question-6---------------------------------------------------------------------------------------
   print("---------------------------------Question-6 -----------------------------------------")
   print("By changing max depth=1,3 and None ,  testing and training acuracy are still same for this case Study")

 
 
#Question-7--------------------------------------------------------------------------------
   print("---------------------------------Question-7 -----------------------------------------")
   
   data={"StudyHours":6,
         "Attendance":85,
         "PreviousScore":66,
         "AssignmentsCompleted":7,
         "SleepHours":7
         
       
   }

   data_df=pd.DataFrame([data])
   print("Newly added data :")
   print(data_df)
   print("Prediction of newly added data are :")
   Result=model.predict(data_df)
   if Result==1:
      print(f"Pass,{Result}")
   else:
      print(f"Fail,{Result}")
      
      
#Question 8----------------------------------------------
   print("----------------------Question 8--------------------------------")
   print("***Visualisation***")
   
   plt.bar(
        CSV["StudyHours"],
        CSV["FinalResult"],
        width=0.6,
        linewidth=1,
        alpha=0.8,
        label="Students",
        edgecolor="Red",
        
    
    )
   plt.legend()
   plt.xlabel("StudyHours")
   plt.ylabel("FinalResult")
   plt.show()
   
   
   
   #--------------------------Assignment 40----------------------------------
   info=model.feature_importances_
   print(info)
   
   
   stru=pd.DataFrame({
      "Features":Feature_Cols,
      "Contibutions(%)":info*100}
   )
   print(stru)
   
   
   #Question 2 in assignment 40--------------------------
   print("-"*60)
   print("-"*60,"\n")
   CSV.drop('SleepHours',axis=1,inplace=True)
   print("After deleting 'SleepHours' column",CSV.columns)
   
   updatedFeatures=['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted']
   X=CSV[updatedFeatures]
   
   X_tain,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)
   print("X_train shape after deleting 'SleepHours' column :",X_tain.shape)
   print("X_test shape after deleting 'SleepHours' column :",X_test.shape)
   print("Y_train shape after deleting 'SleepHours' column :",Y_train.shape)
   print("Y_test shape after deleting 'SleepHours' column :",Y_test.shape)
   
   model2=DecisionTreeClassifier(max_depth=5,random_state=42)
   Train=model2.fit(X_tain,Y_train)
   print("-"*30)
   Y_pred=model2.predict(X_test)
   accuracy2=accuracy_score(Y_test,Y_pred)*100
   print("After removing the column 'SleepHours' accuracy are still same ")
   
   print(f"Accuracy of Model after deleting 'SleepHours' column : {accuracy2} Model size are :{CSV.shape}")
 
   
   
   
   
   
   
   
#    plt.hist(
#        CSV["FinalResult"],
#        bins=10,color="skyblue",
#        edgecolor="black"
       
#    )
#    plt.xlabel("FinalResult")
#    plt.ylabel("Frequency")
#    plt.title("Histogram of Student Peformance dataset")
#    plt.show()
   
   
   
   
   
    
    
    
    
if __name__=="__main__":
    main()