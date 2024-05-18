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

# Create pairplot 
iris_pairplot = sns.pairplot(iris[['sepal length', 'sepal width','petal length', 'petal width', 'species']], hue='species', height=2)
plt.show()

# Correlation between Sepal Length & Petal Length 
# Compute Correlation
correlation = iris['sepal length'].corr(iris['petal length']).round(2)
print(f'Correlation Coefficient:{correlation}')

# Visualise Relationship
plt.figure(figsize=(8,6))
plt.scatter(iris['sepal length'], iris['petal length'])
plt.title('Sepal Length Vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel("Petal Length")
plt.show()

# Seaborn Scatter Plot w/ Regression Line
sns.lmplot(x = 'sepal length', y='petal length', data = iris, height = 6)
plt.title("Scatter plot with regression line of Sepal Length Vs Petal Length")
plt.show()

# Correlation between Sepal Length & Petal Width 
# Compute Correlation
correlation = iris['sepal length'].corr(iris['petal width']).round(2)
print(f'Correlation Coefficient:{correlation}')

# Visualise Relationship
plt.figure(figsize=(8,6))
plt.scatter(iris['sepal length'], iris['petal width'])
plt.title('Sepal Length Vs Petal Width')
plt.xlabel('Sepal Length')
plt.ylabel("Petal Width")
plt.show()

# Seaborn Scatter Plot w/ Regression Line
sns.lmplot(x = 'sepal length', y='petal width', data = iris, height = 6)
plt.title("Scatter plot with regression line of Sepal Length Vs Petal Width")
plt.show()

# Additional Analysis
# Plotting the boxplot
sns.boxplot(x='species', y='sepal length', data=iris, hue = 'species')
plt.show()

sns.boxplot(x='species', y='sepal width', data=iris, hue = 'species')
plt.show()

sns.boxplot(x='species', y='petal length', data=iris, hue = 'species')
plt.show()

sns.boxplot(x='species', y='petal width', data=iris, hue = 'species')
plt.show()

# Use GroupBy Function to Group different variables together 

mmm_sepal_length = iris.groupby('species')['sepal length'].agg(['min','max','mean']).round(1)
mmm_sepal_width = iris.groupby('species')['sepal width'].agg(['min','max','mean']).round(1)
mmm_petal_length = iris.groupby('species')['petal length'].agg(['min','max','mean']).round(1)
mmm_petal_width = iris.groupby('species')['petal width'].agg(['min','max','mean']).round(1)

print(f'Sepal Length Breakdown: \n {mmm_sepal_length}')
print(f'Sepal Width Breakdown: \n {mmm_sepal_width}')
print(f'Petal Length Breakdown: \n {mmm_petal_length}')
print(f'Petal Width Breakdown: \n {mmm_petal_width}')