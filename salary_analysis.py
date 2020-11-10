import pandas as pd
import numpy as np

# Importing the data
salary_data = pd.read_csv('San Francisco Salaries.csv')

# ---------- Creating a calculated field for Total pay -------------- #
salary_data['Total Pay'] = salary_data['Base Pay'] + salary_data['Overtime Pay'] + salary_data['Other Pay']
# print(salary_data.head())

# Highest earners in terms of total pay
employee_pivot = salary_data.groupby(['Employee Name', 'Base Pay',
                                      'Overtime Pay', 'Other Pay', 'Job Title'],
                                     as_index=False)['Total Pay'].sum() \
                                    .sort_values(by='Total Pay', ascending=False)
# print(employee_pivot.head())

'''
    Judy Melinek      553101.94
    Mike Breiling     460094.45
    Thomas Abbott     452578.13
    John Haley Jr     448565.18
    William Lee       441408.73
'''
# Let's take a look at mean total pay in terms of Job title
job_title_pivot = salary_data.groupby(['Job Title'], as_index=False)['Base Pay'].mean() \
                                                    .sort_values(by='Base Pay', ascending=False)
# print(job_title_pivot.head(5))

'''
    The top 5 earners (Base Pay) are:
    Dep Chf Of Dept (Fire Dept)            270756.03
    Assistant Medical Examiner             257510.44
    Executive Contract Employee            249362.77
    Administrator, Sfgh Medical Center     245124.44
    Assistant Deputy Chief 2               239247.00
'''

# Highest earners in terms of total pay in 2013
employee_pivot_2013 = salary_data.query('Year == 2013').groupby(['Employee Name'],
                                                                as_index=False)['Total Pay'].sum() \
                                                                .sort_values(by='Total Pay', ascending=False)
# print(employee_pivot_2013)
'''
    Gary Altenberg          362844.66
    Patricia Jackson        297608.92
    Amy Hart                284720.43
    Judy Melinek            279330.73
    Michael R Bryant        276690.04
'''
# Digging deeper into Gary's records
gary = employee_pivot[employee_pivot['Employee Name'] == 'Gary Altenberg']
print(gary)
'''
   Gary is a fire fighter and earns a lot from overtime. 
   This makes sense as we expect a lot of overtime for a fire fighter
'''

