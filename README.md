# pands-project

# Introduction
The following project contains my analysis of the Iris dataset. This dataset is very well know across the data science community and is looked at as a great starting point for those pursuing a career in data science. This widely known dataset contains five columns (sepal length, sepal width, petal length, petal width and target/species) and one hundred and fifty rows. 

# Data Cleaning
Before I was able to explore the dataset I first had to clean it to ensure any outcomes from my analysis were as accurate as possible. First up was converting the 'target' column to a category. This task is done for memory efficiency. For a dataset with 150 rows converting isn't essential but it is important to get into good habbits. Next up I had to account for null values. To do this I used the .fillna() function. This replaces or 'fills' any null values in the columns selected with the value put in the function. I used this rather than .dropna() as that would remove entire rows where there is a null value, due to the size of this dataset I didn't think that would be productive. In the dataset I downloaded there was another column called 'class' which contained null values and didn't contribute to my analysis so used .drop() to delete it and also changed the name of 'target' to 'species' using .rename() as it reads better. Once this data cleaning was complete I used .head() to ensure the changes I made were correctly executed and removed duplicates from dataframe using .drop_duplicates(). Once all this was complete I was happy to get started with my analysis.

# EDA
For this project there were three key deliverables: providing a text file summary of each key variable, save histograms of each variable to png files and output a scatter plot of each variables. When performing my analysis I first did it in a notebook (project.ipynb) to ensure all individual sections were working correctly. Once this was done I copied the code into analysis.py

1) Summary of each variable to a single text file
When providing a summary of the variables I had to use .describe() to generate descriptive statistics of the Iris dataset. I then converted the data type to a string as we were creating a text file. The final step then was using summary.txt to create the file.

2) Save a histogram of each variable to png files
In the Histogram section of the script I used matplotlib. I first created the histograms which involved highlighting the variable I am using and other key details like the number of bins, xlabel, title, etc. Once this was done I then used plt.savefig to save the file adn .png to ensure it was saved in the requested format. Once I did this once I then repeated several times changing the variable and the color.

3) Scatter Plots
When starting this section I originally created all scatter plots individually then discovered a more efficient way to approach the tast which is pairplots: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ 

Even though pairplots covered the requested deliverable I also wanted to showcase the scatter plots where there was a strong positive relationship and add a regression line. I did so using matplotlib.plplot fot the scatter plot and seaborn for the regression line.

# Additional Analysis - Box Plots

While learning about pairplots I also came across box plots which are used through the library seaborn. I created four of these using species as the X axis and the remaining variables as the Y axis.

# Sources 
For this project multiple libraries were used in different ways. The different methods I used were learned through lectures throughout the semester, Udemy Courses I had purschased before joining the course and articles read online. 

Articles: 
https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c

Udemy Courses:
Data Analysis with Pandas and Python by Boris Paskhaver
Python for Data Science and Machine Learning Bootcamp by Jose Portilla, Pierian Training