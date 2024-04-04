# Import pandas to work with dataframes
import pandas as pd

# Import matplotlib.pyplot for Histograms
import matplotlib.pyplot as plt

# Import seaborn for scatter plots with regression line 
import seaborn as sns

#Load the data
iris = pd.read_excel('/Users/davidosullivan/Desktop/pands/pands-project/pands-project/iris_dataset.xlsx')

# Clean the data

# Convert certain columns to categories for memory efficiency
iris['target'] = iris['target'].astype('category') 

# Use fillna function to account for null values
iris['sepal length'] = iris['sepal length'].fillna(0) 
iris['sepal width'] = iris['sepal width'].fillna(0)
iris['petal length'] = iris['petal length'].fillna(0) 
iris['petal width'] = iris['petal width'].fillna(0)

# Change 'target' to 'species' and drop class column 
# 'inplace=True' is used to alter the existing dataframe rather than making a copy
iris.rename(columns={'target':'species'},inplace=True)
iris.drop(columns={'class'}, inplace=True)

# Remove "Iris-" from the 'species' column
iris['species'] = iris['species'].str.replace('Iris-', '')

# Use .head to ensure changes were implemented properly
print(iris.head())

# Generate Histograms for all variables (4)
# Generate Sepal Length Histogram

plt.hist(iris['sepal length'], bins = 20, color = 'skyblue', edgecolor = 'black')

# Add title and labels
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')

# Save the plot as a PNG file
plt.savefig('histogram_sepal_length.png') 

# Show the plot
plt.show()

# Generate Sepal Width Histogram
plt.hist(iris['sepal width'], bins = 20, color = 'pink', edgecolor = 'black')

# Add title and labels
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width')
plt.ylabel('Frequency')

# Save the plot as a PNG file
plt.savefig('histogram_sepal_width.png')

# Show the plot
plt.show()

# Generate Petal Length Histogram
plt.hist(iris['petal length'], bins = 20, color = 'green', edgecolor = 'black')

# Add title and labels
plt.title('Histogram of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')

# Save the plot as a PNG file
plt.savefig('histogram_petal_length.png')

# Show the plot
plt.show()

# Generate Petal Width Histogram
plt.hist(iris['petal width'], bins = 20, color = 'yellow', edgecolor = 'black')

# Add title and labels
plt.title('Histogram of Petal Width')
plt.xlabel('Petal Width')
plt.ylabel('Frequency')

# Save the plot as a PNG file
plt.savefig('histogram_petal_width.png')

# Show the plot
plt.show()

# 1) Sepal Length and Sepal Width - Weak Negative Relationship
# Compute Correlation
correlatrion_1 = iris['sepal length'].corr(iris['sepal width']).round(1)
print(f'Correlation coefficient: {correlatrion_1}')

# Visualize the relationship
plt.figure(figsize=(8,6))
plt.scatter(iris['sepal length'], iris['sepal width'])
plt.title('Sepal Length Vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

# 2) Sepal Length Vs Petal Length - Strong Positive Relationship
# Compute Correlation
correlatrion_2 = iris['sepal length'].corr(iris['petal length']).round(1)
print(f'Correlation coefficient: {correlatrion_2}')

# Visualize the relationship
plt.figure(figsize=(8,6))
plt.scatter(iris['sepal length'], iris['petal length'])
plt.title('Sepal Length Vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()

# Add in regression line as there is a strong correlation (0.9)
sns.lmplot(x='sepal length', y= 'petal length', data = iris, height = 8)
plt.title('Scatter Plot w/ Regression Line of Sepal Length and Petal Length')
plt.show()

# 3) Sepal Length and Petal Width - Strong Positive Relationship
# Compute Correlation
correlatrion_3 = iris['sepal length'].corr(iris['petal width']).round(1)
print(f'Correlation coefficient: {correlatrion_3}')

# Visualize the relationship
plt.figure(figsize=(8,6))
plt.scatter(iris['sepal length'], iris['petal width'])
plt.title('Sepal Length Vs Petal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')
plt.show()

# Add in regression line as there is a strong correlation (0.8)
sns.lmplot(x='sepal length', y= 'petal width', data = iris, height = 6)
plt.title('Scatter Plot w/ Regression Line of Sepal Length and Petal Width')
plt.show()

# 4) Petal Width Vs Sepal Length - Strong Positive Relationship
# Compute Correlation
correlatrion_4 = iris['petal width'].corr(iris['sepal length']).round(1)
print(f'Correlation coefficient: {correlatrion_4}')

# Visualize the relationship
plt.figure(figsize=(8,6))
plt.scatter(iris['petal width'], iris['sepal length'])
plt.title('Petal Width vs Sepal Length')
plt.xlabel('Petal Width')
plt.ylabel('Sepal Length')
plt.show()

# Add in regression line as there is a strong correlation (0.8)
sns.lmplot(x='petal width', y= 'sepal length', data = iris, height = 6)
plt.title('Scatter Plot w/ Regression Line of Petal Width & Sepal Length')
plt.show()

# 5) Petal Width Vs Sepal Width - Moderate Negative Relationship
# Compute Correlation
correlatrion_5 = iris['petal width'].corr(iris['sepal width']).round(1)
print(f'Correlation coefficient: {correlatrion_5}')

# Visualize the relationship
plt.figure(figsize=(8,6))
plt.scatter(iris['petal width'], iris['sepal width'])
plt.title('Petal Width vs Sepal Width')
plt.xlabel('Petal Width')
plt.ylabel('Sepal Width')
plt.show()

# 6) Sepal Width Vs Petal Length - Moderate Negative Relationship
# Compute Correlation
correlatrion_6 = iris['sepal width'].corr(iris['petal length']).round(1)
print(f'Correlation coefficient: {correlatrion_6}')

# Visualize the relationship
plt.figure(figsize=(8,6))
plt.scatter(iris['sepal width'], iris['petal length'])
plt.title('Sepal Width vs Petal Length')
plt.xlabel('Sepal Width')
plt.ylabel('Petal Length')
plt.show()