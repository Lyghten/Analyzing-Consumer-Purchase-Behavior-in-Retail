import pandas as pd

# Load dataset
data = pd.read_csv('retail_customer_data.csv')

# Check for missing values
missing_values = data.isnull().sum()

# Fill missing values in Purchase_Amount with mean
data['Purchase_Amount'].fillna(data['Purchase_Amount'].mean(), inplace=True)

# Drop rows with missing categorical data
data.dropna(subset=['Gender', 'Income_Level', 'Product_Category'], inplace=True)