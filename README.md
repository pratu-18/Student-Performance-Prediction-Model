# STUDENT PERFORMANCE DATA ANALYSIS

1. PROJECT DESCRIPTION

---

This project performs basic data analysis and visualization on a student
performance dataset using Python.

The project analyzes student academic and behavioral information such as:

* Study Hours
* Attendance
* Previous Score
* Assignments Completed
* Sleep Hours
* Final Result

The analysis includes dataset inspection, statistical calculations, binary
classification distribution analysis, and data visualization.

2. PROJECT OBJECTIVE

---

The main objectives of this project are:

* Load the student performance dataset.
* Inspect the structure and contents of the dataset.
* Identify the number of rows and columns.
* Display column names and data types.
* Calculate the number of passed and failed students.
* Calculate averages and minimum/maximum values.
* Analyze the distribution of the FinalResult column.
* Calculate pass and fail percentages.
* Visualize relationships between different student performance features.

3. DATASET

---

Dataset file:

student_performance_ml.csv

The dataset contains student performance-related information.

Input columns:

1. StudyHours
2. Attendance
3. PreviousScore
4. AssignmentsCompleted
5. SleepHours

Target column:

FinalResult

FinalResult is a binary classification variable:

0 = Fail
1 = Pass

4. TECHNOLOGIES USED

---

Programming Language:

Python 3.10 or higher

Development Environment:

Visual Studio Code (VS Code)

Libraries:

* Pandas
* Matplotlib

5. PYTHON LIBRARIES

---

Pandas:

Used for:

* Reading the CSV dataset
* Data inspection
* Data analysis
* Calculating mean, minimum and maximum values
* Counting class distributions

Matplotlib:

Used for:

* Scatter plot
* Box plot
* Bar charts
* Data visualization

6. PROJECT ANALYSIS

---

The project performs the following analysis.

6.1 Dataset Inspection

The program displays:

* First 5 records
* Last 5 records
* Total number of columns
* Total number of rows
* List of column names
* Data types of selected columns

6.2 Student Count Analysis

The program calculates:

* Total number of students
* Total number of passed students
* Total number of failed students

6.3 Statistical Analysis

The program calculates:

* Average Study Hours
* Average Attendance
* Maximum Previous Score
* Minimum Sleep Hours

6.4 Final Result Distribution

The program analyzes the distribution of the FinalResult column.

The FinalResult column contains two possible classes:

0 = Fail
1 = Pass

The program also calculates:

* Pass percentage
* Fail percentage

7. DATA VISUALIZATION

---

The project contains the following visualizations.

7.1 Scatter Plot

The scatter plot represents the relationship between:

X-axis:
StudyHours

Y-axis:
PreviousScore

7.2 Box Plot

The box plot is created for:

Attendance

It helps visualize the distribution and spread of attendance values and
identify potential outliers.

7.3 Bar Chart

A bar chart is created to visualize the relationship between:

AssignmentsCompleted

and

FinalResult

7.4 Sleep Hours Bar Chart

A bar chart is created to visualize the relationship between:

SleepHours

and

FinalResult

8. PROJECT STRUCTURE

---

Student-Performance-Analysis/
|
|-- student_performance_ml.csv
|-- student_performance_analysis.py
|-- README.txt
|-- requirements.txt

9. INSTALLATION

---

Requirement:

Python 3.10 or higher

Verify the Python installation:

python --version

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install project dependencies:

pip install -r requirements.txt

10. EXECUTION

---

Open the project in Visual Studio Code.

Run the Python program using:

python student_performance_analysis.py

The program will display analysis results in the terminal and generate
visualizations using Matplotlib.

11. EXPECTED OUTPUT

---

The program displays:

* First 5 dataset records
* Last 5 dataset records
* Number of rows
* Number of columns
* Column names
* Data types
* Total number of students
* Number of passed students
* Number of failed students
* Average Study Hours
* Average Attendance
* Maximum Previous Score
* Minimum Sleep Hours
* Final Result distribution
* Pass percentage
* Fail percentage

The program also displays:

* Study Hours vs Previous Score scatter plot
* Attendance box plot
* Assignments Completed vs Final Result bar chart
* Sleep Hours vs Final Result bar chart

12. LEARNING OUTCOMES

---

This project provides practical experience with:

* Python programming
* Pandas
* CSV file handling
* DataFrame operations
* Data inspection
* Basic statistical analysis
* Conditional statements
* Loops
* Data visualization
* Matplotlib
* Binary classification data analysis

13. FUTURE ENHANCEMENTS

---

Possible improvements include:

* Add missing value analysis.
* Add duplicate record detection.
* Add correlation analysis.
* Add additional visualizations.
* Use Seaborn for advanced visualization.
* Build a Machine Learning model to predict FinalResult.
* Split the dataset into training and testing data.
* Evaluate the prediction model using accuracy, confusion matrix,
  precision, recall and F1-score.

14. AUTHOR

---

Author:

Pratiksha Mahale

Project Type:

Student Performance Data Analysis

Domain:

Data Analysis and Machine Learning
