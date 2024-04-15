# pands-project

# Introduction
The following project contains my analysis of the Iris dataset. This dataset is very well know across the data science community and is looked at as a great starting point for those pursuing a career in data science. This widely known dataset contains five columns (sepal length, sepal width, petal length, petal width and target/species) and one hundred and fifty rows.

# Data Cleaning
Before I was able to explore the dataset I first had to clean it to ensure any outcomes from my analysis were as accurate as possible. First up was converting the 'target' column to a category. This task is done for memory efficiency. For a dataset with 150 rows converting isn't essential but it is important to get into good habbits. Next up I had to account for null values. To do this I used the .fillna() function. This replaces or 'fills' any null values in the columns selected with the value put in the function. I used this rather than .dropna() as that would remove entire rows where there is a null value, due to the size of this dataset I didn't think that would be productive. In the dataset I downloaded there was another column called 'class' which contained null values and didn't contribute to my analysis so used .drop() to delete it and also changed the name of 'target' to 'species' using .rename() as it reads better. Once this data cleaning was complete I used .head() to ensure the changes I made were correctly executed and removed duplicates from dataframe using .drop_duplicates(). Once all this was complete I was happy to get started with my analysis.

# EDA
