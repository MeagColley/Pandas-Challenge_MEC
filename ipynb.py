#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np
# File to Load (Remember to Change These)
school_data = "Resources/schools_complete.csv"
student_data = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data)
student_data = pd.read_csv(student_data)

# Combine the data into a single dataset
school_data_complete_df = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete_df.head()


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[2]:


# you don't need this 
school_data_complete_df.describe()


# In[3]:


# Remove the rows with missing data
school_data_complete_df = school_data_complete_df.dropna(how="any")
school_data_complete_df.count()


# In[4]:


# total number of schools
school_count=school_data_complete_df.groupby(["school_name"])
school_count.count()


# In[12]:


#summarize school count
school_count_summary=school_count.describe()
school_count_summary


# In[ ]:


# total number of students
student_count=school_data_complete_df.groupby(["student_name"])
# student_count.describe()
# if you describe this df it crashes everytime but we can see that there are 32,715 students


# In[ ]:


# total budget
budget_df=school_data_complete_df.groupby(["budget"])
budget_df.sum()


# In[ ]:


# average math score
average_math_score = school_data__complete_df["math_score"].mean()
average_math_score


# In[ ]:


# average reading score
average_reading_score = school_data__complete_df["reading_score"].mean()
average_reading_score


# In[ ]:


# average passing score
avg_passing_score=(average_math_score + average_reading_score)/2
avg_passing_score


# In[ ]:


# percent of students passing math
percent_math=(np.sum(school_data_complete_df['math_score'] > 70) /39170)*100
percent_math


# In[ ]:


# percent of students passing english
percent_reading=(np.sum(school_data_complete_df['reading_score'] > 70) /39170)*100
percent_reading


# In[ ]:


# create a data frame for findings
# Calculations can also be performed on Series and added into DataFrames as new columns

school_data_complete_df["school_count"] = school_count
school_data_complete_df["student_count"] = student_count
school_data_complete_df["budget_df"] = budget_df
school_data_complete_df["average_math_score"] = average_math_score
school_data_complete_df["average_reading_score"] = average_reading_score
school_data_complete_df["average_passing_score"] = avg_passing_score
school_data_complete_df["students_passing_math"] = percent_math
school_data_complete_df["students_passing_reading"] = percent_reading
school_date_complete_df.head()


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[13]:





# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[14]:





# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[15]:





# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[16]:





# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[17]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[18]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[19]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[20]:





# In[ ]:




