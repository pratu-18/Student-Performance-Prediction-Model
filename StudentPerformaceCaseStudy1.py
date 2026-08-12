import pandas as pd
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def main():
    #-------------------------------------Assignment 38---------------------------------------------
    
    #Question 1-------------------------------
    data=pd.read_csv("student_performance_ml.csv")
    print("first 5 records")
    print(data.head())
    print("\n")

    
    print("Last 5 records")
    print(data.tail(5))
    
    print("Total number of columns:",len(data.columns))
    print("Total number rows are :",len(data["StudyHours"]))
    print("List of column name are :",data.columns)
    
    for values in data["StudyHours"]:
            type1=type(values)
    print("Data type of column StudyHours :",type(data["StudyHours"]), " : Type of values inside this colum: ",type1)
   
    for values in data["Attendance"]:
        type2=type(values)
    print("Data type of column Attendance :",type(data["Attendance"]), " : Type of values inside this colum: ",type2)
    
    for values in data["PreviousScore"]:
        type3=type(values)
    print("Data type of column PreviousScore :",type(data["PreviousScore"])," : Type of values inside this colum: ",type3)
    
    for values in data["AssignmentsCompleted"]:
        type4=type(values)
    print("Data type of column AssignmentsCompleted :",type(data["AssignmentsCompleted"])," : Type of values inside this colum: ",type4 )
    
    for values in data["SleepHours"]:
        type5=type(values)
    print("Data type of column SleepHours :",type(data["SleepHours"])," : Type of values inside this colum: ",type5)
    
    for values in data["FinalResult"]:
        type6=type(values)
    print("Data type of column FinalResult :",type(data["FinalResult"])," : Type of values inside this colum: ",type6)
    
    
    #Question 2----------------------------------------------------------
    print("Total number of student in dataset : ",len(data["FinalResult"]))
    
    Count_Pass=0
    Count_Fail=0
    for values in data["FinalResult"]:
        if values==1:
            Count_Pass=Count_Pass+1
            
        else:
            Count_Fail=Count_Fail+1
            
            
    print("Total number of passed Student : ",Count_Pass)
    print("Total number of failed student : ",Count_Fail)
    
    
    #Question-3------------------------------
    print("Average of Study hour column :",data["StudyHours"].mean())
    print("Average of attendance :",data["Attendance"].mean())
    print("Maximum value in PreviousScore column: ",data["PreviousScore"].max())
    print("Manimum value in sleepHour column: ",data["SleepHours"].min())
    
    
    #Question-4----------------------------------------
    print("Distribution of final result(Binary class classification were 2 options are present in Final result)",data["FinalResult"].value_counts())
    
    
    TotalStudents=len(data["Attendance"])
    
    pass_percentage=(Count_Pass/TotalStudents)*100
    print("How many students are passed in % :",pass_percentage)
    
    Fail_percentage=(Count_Fail/TotalStudents)*100
    print("How many students are Fail in % :",Fail_percentage)
    
    
    #Question-5--------------------------------------------
    
    
    
    
    #Question-6---------------------------------
    
    plt.scatter(
        data["StudyHours"],
        data["PreviousScore"],
        s=100,
        marker="o",
        edgecolors="black",
        linewidths=1,                  #border line of circle
        label="Score"
        
        
        
    )
    plt.title("Student Performance")
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.grid(True)
    plt.legend()
    plt.show()
    
    #Question-8 --------------------------------------------------
    plt.boxplot(
        data["Attendance"]
        
        
    )
    plt.show()
    
    
    #Question 9-----------------------------------------------------
    plt.bar(
        data["AssignmentsCompleted"],
        data["FinalResult"],
        width=0.6,
        edgecolor="black",
        linewidth=1,
        alpha=0.8,
        label="Students"
        
        
    )
    
    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult")
    plt.legend()
    plt.show()
    
    
    #Question 10-----------------------------------------
    
    
    plt.bar(
        data["SleepHours"],
        data["FinalResult"],
        width=0.6,
        linewidth=1,
        alpha=0.8,
        label="Students",
        edgecolor="Red",
        
    
    )
    plt.legend()
    plt.xlabel("SleepHours")
    plt.ylabel("FinalResult")
    plt.show()
if __name__=="__main__":
    main()