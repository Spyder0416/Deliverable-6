import pandas as pd
import numpy as np
import seaborn as sns

# Load iris dataset into dataframe
iris = sns.load_dataset('iris')

# Drop the "species" column
iris = iris.drop(columns='species')

# Add two new columns "sepal_sum" and "petal_sum"
iris['sepal_sum'] = iris['sepal_length'] + iris['sepal_width']
iris['petal_sum'] = iris['petal_length'] + iris['petal_width']

# Create a summary dataframe
summary_df = pd.DataFrame({
    'mean': iris.mean(),
    'std': iris.std(),
    'min': iris.min(),
    'max': iris.max()
})

# Print the summary dataframe
print(summary_df)

