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