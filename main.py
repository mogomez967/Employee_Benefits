import json
import pandas as pd
from statistics import mean

"""
RESOURCES:
https://www.askpython.com/python-modules/pandas/normalize-json-flat-table
https://www.kaggle.com/code/jboysen/quick-tutorial-flatten-nested-json-in-pandas/notebook
"""

# Your objectives are:
# 1. Read the provided JSON file to analyze the data.
# 2. Calculate the average total amount of benefits spending per user for each department.
# 3. Determine which department has the highest and the lowest average spending per employee.
#
# (Extra) 4. Calculate which benefit has been spent on the most across the company for the data.

file = open("employee_benefits_data.json")
data = json.load(file)

# load the employee data by department into panda dataframe
emp_data = pd.json_normalize(data['departments'])

# start parsing the nested JSON formats like the spending $$ per user id per category
emp_spending = pd.json_normalize(data = data['departments'], record_path=['users'], meta='name')

# Engineers
temp = emp_spending['name'].isin(['Engineering'])
engineer_only_data = emp_spending[temp]
# print(engineer_only_data)

# HR
temp = emp_spending['name'].isin(['HR'])
hr_only_data = emp_spending[temp]
hr_only_data.reset_index(drop=True, inplace=True)
# print(hr_only_data)

# Sales
temp = emp_spending['name'].isin(['Sales'])
sales_only_data = emp_spending[temp]
sales_only_data.reset_index(drop=True, inplace=True)
# print(sales_only_data)

# Marketing
temp = emp_spending['name'].isin(['Marketing'])
marketing_only_data = emp_spending[temp]
marketing_only_data.reset_index(drop=True, inplace=True)
# print(marketing_only_data)

# Operations
temp = emp_spending['name'].isin(['Operations'])
ops_only_data = emp_spending[temp]
ops_only_data.reset_index(drop=True, inplace=True)
# print(ops_only_data)

# Finance
temp = emp_spending['name'].isin(['Finance'])
finance_only_data = emp_spending[temp]
finance_only_data.reset_index(drop=True, inplace=True)
# print(finance_only_data)

# Customer Support
temp = emp_spending['name'].isin(['Customer Support'])
support_only_data = emp_spending[temp]
support_only_data.reset_index(drop=True, inplace=True)
# print(support_only_data)

# Product
temp = emp_spending['name'].isin(['Product'])
product_only_data= emp_spending[temp]
product_only_data.reset_index(drop=True, inplace=True)
# print(product_only_data)

# Design
temp = emp_spending['name'].isin(['Design'])
design_only_data = emp_spending[temp]
design_only_data.reset_index(drop=True, inplace=True)
# print(design_only_data)





"""

2. calc average benefits per user per department

"""
# Creates a list of IDs (tuples) for each department while calculating employee spending averages
def create_id_list(id_list, department_data):
    result = []
    for i in range(len(id_list)):
        # append to result[] ("department name", mean of data in row (because user is different each row) )
        result.append( (id_list[i], mean(department_data.loc[i]) ) )
    return result

# Prints the average spending per user per department (parses through list of tuples)
def print_department_spending(id_list):
    for i in id_list:
        print("Employee #", i[0], "Average Benefits: $", i[1])



# Engineering $$$ spent per user
eng_ids = engineer_only_data['id']
engineer_only_data = engineer_only_data.drop(columns=['id', 'name'], axis=1, inplace=False)

eng_id_list = create_id_list(eng_ids, engineer_only_data)

print("Engineering Average Spending")
print_department_spending(eng_id_list)

# HR $$$ spent per user
hr_ids = hr_only_data['id']
hr_only_data = hr_only_data.drop(columns=['id', 'name'], axis=1, inplace=False)

hr_id_list = create_id_list(hr_ids, hr_only_data)

print("\n\nHR Average Spending")
print_department_spending(hr_id_list)

# Sales $$$ spent per user
sales_ids = sales_only_data['id']
sales_only_data = sales_only_data.drop(columns=['id', 'name'], axis=1, inplace=False)

sales_id_list = create_id_list(sales_ids, sales_only_data)

print("\n\nSales Average Spending")
print_department_spending(sales_id_list)

# Marketing $$$ spent per user
marketing_ids = marketing_only_data['id']
marketing_only_data = marketing_only_data.drop(columns=['id', 'name'], axis=1, inplace=False)

marketing_id_list = create_id_list(marketing_ids, marketing_only_data)

print("\n\nMarketing Average Spending")
print_department_spending(marketing_id_list)

# Operations $$$ spent per user
ops_ids = ops_only_data['id']
ops_only_data = ops_only_data.drop(columns=['id', 'name'], axis=1, inplace=False)

ops_id_list = create_id_list(ops_ids, ops_only_data)

print("\n\nOperations Average Spending")
print_department_spending(ops_id_list)

# Finance $$$ spent per user
finance_ids = finance_only_data['id']
finance_only_data = finance_only_data.drop(columns=['id', 'name'], axis=1, inplace=False)

finance_id_list = create_id_list(finance_ids, finance_only_data)

print("\n\nFinance Average Spending")
print_department_spending(finance_id_list)

# Customer Support $$$ spent per user
support_ids = support_only_data['id']
support_only_data = support_only_data.drop(columns=['id', 'name'], axis=1, inplace=False)

support_id_list = create_id_list(support_ids, support_only_data)

print("\n\nCustomer Support Average Spending")
print_department_spending(support_id_list)

# Product $$$ spent per user
product_ids = product_only_data['id']
product_only_data = product_only_data.drop(columns=['id', 'name'], axis=1, inplace=False)

product_id_list = create_id_list(product_ids, product_only_data)

print("\n\nProduct Average Spending")
print_department_spending(product_id_list)

# Design $$$ spent per user
design_ids = design_only_data['id']
design_only_data = design_only_data.drop(columns=['id', 'name'], axis=1, inplace=False)

design_id_list = create_id_list(design_ids, design_only_data)

print("\n\nDesign Average Spending")
print_department_spending(design_id_list)





"""

3. Determine which department has the highest and the lowest average spending per employee

"""
# returns the mean spending per department
def dep_avg(id_list):
    # the ID_list consists of tuples(ID, avg_spending)
    # return the tuple (ID, avg_spending) of the highest avg spent
    temp = []
    for i in id_list:
        temp.append(i[1])
    return mean(temp)

department_avg_spent = []

department_avg_spent.append( ("Engineering ", dep_avg(eng_id_list)) )
department_avg_spent.append( ("HR ", dep_avg(hr_id_list)) )
department_avg_spent.append( ("Sales ", dep_avg(sales_id_list)) )
department_avg_spent.append( ("Marketing ", dep_avg(marketing_id_list)) )
department_avg_spent.append( ("Operations ", dep_avg(ops_id_list)) )
department_avg_spent.append( ("Finance ", dep_avg(finance_id_list)) )
department_avg_spent.append( ("Customer Support ", dep_avg(support_id_list)) )
department_avg_spent.append( ("Product ", dep_avg(product_id_list)) )
department_avg_spent.append( ("Design ", dep_avg(design_id_list)) )

print("\n\nDepartment with the highest average spending per employee: ", max(department_avg_spent, key=lambda x: x[1])[0], "at an average of $", max(department_avg_spent, key=lambda x: x[1])[1], "per employee")

print("\n\nDepartment with the lowest average spending per employee: ", min(department_avg_spent, key=lambda x: x[1])[0], "at an average of $", min(department_avg_spent, key=lambda x: x[1])[1], "per employee")





"""

4. Calculate which benefit has been spent on the most across the company for the data

"""
def max_benefit(dep_only_data):
    total_spending = 0
    dep_label = ""
    
    for i in dep_only_data.columns:
        temp_mean = dep_only_data[i].describe().loc['mean']

        # ugly way of getting the label of the benefit but removes "spending." in "spending.benefit"
        if temp_mean > total_spending:
            dep_label = i[9:]
            total_spending = temp_mean
            
    total_spending = round(total_spending, 2)

    return (dep_label, total_spending)
        
eng_max_benefit = max_benefit(engineer_only_data)
print("\n\nThe benefit that was spent on the most in Engineering was", eng_max_benefit[0], "at $"+ str(eng_max_benefit[1]) )

hr_max_benefit = max_benefit(hr_only_data)
print("The benefit that was spent on the most in HR was", hr_max_benefit[0], "at $"+ str(hr_max_benefit[1]) )

sales_max_benefit = max_benefit(sales_only_data)
print("The benefit that was spent on the most in Sales was", sales_max_benefit[0], "at $"+ str(sales_max_benefit[1]) )

mark_max_benefit = max_benefit(marketing_only_data)
print("The benefit that was spent on the most in Marketing was", mark_max_benefit[0], "at $"+ str(mark_max_benefit[1]) )

ops_max_benefit = max_benefit(ops_only_data)
print("The benefit that was spent on the most in Operations was",ops_max_benefit[0], "at $"+ str(ops_max_benefit[1]) )

fin_max_benefit = max_benefit(finance_only_data)
print("The benefit that was spent on the most in Finance was", fin_max_benefit[0], "at $"+ str(fin_max_benefit[1]) )

sup_max_benefit = max_benefit(support_only_data)
print("The benefit that was spent on the most in Customer Support was",sup_max_benefit[0], "at $"+ str(sup_max_benefit[1]) )

prod_max_benefit = max_benefit(product_only_data)
print("The benefit that was spent on the most in Product was",prod_max_benefit[0], "at $"+ str(prod_max_benefit[1]) )

design_max_benefit = max_benefit(design_only_data)
print("The benefit that was spent on the most in Design was", design_max_benefit[0], "at $"+ str(design_max_benefit[1]) )