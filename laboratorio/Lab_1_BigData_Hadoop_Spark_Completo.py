# Big Data Hadoop and Spark Laboratory Notebook

This notebook contains executable code examples, data transformations, Spark SQL queries, and exercises for the Big Data Hadoop and Spark laboratory.

## 1. Introduction

This notebook serves as a comprehensive guide for students and practitioners to understand and practice Big Data concepts using Hadoop and Spark.

## 2. Setting Up Your Environment

Ensure that you have the following installed:
- Python 3.x
- Apache Spark
- Hadoop
- Jupyter Notebook (for interactive sessions)

## 3. Sample Data

We will use a sample data set containing user information, which includes `id`, `name`, `age`, and `city`.

```python
# Sample Data Creation
data = [  
    (1, 'Alice', 34, 'New York'),  
    (2, 'Bob', 23, 'Los Angeles'),  
    (3, 'Cathy', 29, 'Chicago'),  
    (4, 'David', 40, 'Miami')  
]

columns = ['id', 'name', 'age', 'city']

# Create DataFrame
import pandas as pd

pdf = pd.DataFrame(data, columns=columns)
pdf
```

## 4. Working with Spark

```python
# Import Spark libraries
from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName('BigDataLab').getOrCreate()

# Create Spark DataFrame from Pandas DataFrame
sdf = spark.createDataFrame(pdf)
sdf.show()
```

## 5. Data Transformations

### 5.1 Filtering Data

```python
# Filter users older than 30
filtered_df = sdf.filter(sdf.age > 30)
filtered_df.show()
```

### 5.2 Grouping Data

```python
# Group users by city and count them
grouped_df = sdf.groupBy('city').count()
grouped_df.show()
```

## 6. Spark SQL Queries

```python
# Register DataFrame as a SQL temporary view
sdf.createOrReplaceTempView('users')

# Query using Spark SQL
sql_df = spark.sql("SELECT city, COUNT(*) as count FROM users GROUP BY city")
sql_df.show()
```

## 7. Exercises

1. Modify the filtering condition to find users younger than 25.
2. Add a new column to the data that calculates age in months.
3. Write a SQL query to find the user with the maximum age.

## 8. Conclusion

This notebook provides a basic overview and serves as a foundation for more advanced Big Data processing and analysis techniques using Spark.