# HW2 - Using Functions

##### Final grade: 7/7  

-0: Thanks for updating the code according to my previous comments. However, you are using complex functions (such as pd.Series) to achieve something that is easily achievable with if tests. Consider simplifying your code further.     


Grade: 6/7

-1: Your test implicitly depended on the order of the columns. But in reality, two dataframes should be considered "equal" if they have the same columns but in different orders.

-----

Create a python module (a file with extension ‘.py’) with the following functions:

1. (4 points) Find an on-line data source (e.g., from data.gov). Write python codes that read the on-line file and create a data frame that has at least 3 columns.

1. (3 points) Create the function test_create_dataframe that takes a pandas DataFrame as input and returns True if the following conditions hold:

   1. The DataFrame contains only the columns that you specified in #1.
   1. The columns contain the correct data type
   1. There are at least 10 rows in the DataFrame.
