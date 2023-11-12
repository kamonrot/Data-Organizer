import pandas as pd
import matplotlib.pyplot as plt

list_format = ["Bar Chart","Pie Chart","Line Chart"]
list_of_comparison = ["Compare data from various groups (columns) : Enter 1","Compare single group data (one column) : Enter 2","Analalyze relationship between Groups : Enter 3"]
list_column = []
list_unique_column = []
check_column = []
dict_sum_unique = {}
dict_sum = {}

#input file name
while True:
    file_name = input("Enter your file name : ") 
    try:
        dt = pd.read_csv(f"{file_name}")
        break
    except:
        print("Invalid input , please enter again") 
        
print(list_of_comparison)  #show lost of format of comparison

#input type of comparison
while True:
    try:
        type_of_comparison = int(input("Enter type of comparison : number "))
        if type_of_comparison == 1 or type_of_comparison == 2 or type_of_comparison == 3:
            break
    except:
        print("Invalid input , please enter again") 
   
#column_managing   
df = pd.DataFrame(dt)
all_columns = df.columns
for column in all_columns:
    check_column.append(column)
number_column = len(check_column)

if type_of_comparison == 1: # for 1 , compare overview (total number)
    while True:
        try:
            n = int(input("Enter number of column : "))
            if n > 1 and n <= number_column:
                break
        except:
            print("Invalid input , please enter again")            
    for i in range(n):
        while True:
            column = input(f"Enter Column No.{i+1} name : ") 
            if column in check_column and column not in list_column:
                list_column.append(str(column))
                break
            else:
                print("Invalid input , please enter again")
                
elif type_of_comparison == 2: # for 2 , compare and analyze in one column only
    while True:
        column = input(f"Enter Column name : ")
        if column in check_column:
            list_unique_column.append(str(column))
            break
        else:
            print("Invalid input , please enter again")
            
elif type_of_comparison == 3: # for 3 , input only 2 columns 
    while True:
        column = input(f"Enter Column name (sum column or y-axis) : ")
        if column in check_column and column not in list_column:
            column_data_type = df[column].dtype
            if column_data_type == "float" or column_data_type == "int64":
                compare_col = column
                column2 = input(f"Enter Column name (group by column or x-axis) : ")
                if column2 in check_column and column2 != compare_col:
                    groupby_col = column2
                    break
                else:
                    print("Inappropriate information")
            else:
                print("Need to be int or float type column")
        else:
            print("Invalid input , please enter again")
        
print("Choose Your Display Format") # show all display format
print(list_format)

while True:
    display_format = input("Enter Display Format : ")
    if display_format in list_format:  
            break
    else:
        print("Invalid input , please enter again")
        
#normal_function
def get_unique(): #just for type == 2
    for i in list_unique_column:
        unique = df[f"{i}"].unique()
    return unique

def get_sum(): #just for type == 1 or 2
    if type_of_comparison == 1:
        for i in list_column:
            if i not in dict_sum:
                dict_sum[i] = df[i].sum()
        return dict_sum
    else:
        for j in list_unique_column:
            for i in get_unique():
                if i not in dict_sum_unique:
                    dict_sum_unique[i] = sum(df[j] == f"{i}")
                else:
                    dict_sum_unique[i] += sum(df[j] == f"{i}")
            return dict_sum_unique

def get_key(): #just for type == 1 or 2
    if type_of_comparison == 1:
        key_list = list(dict_sum.keys())
    else:
        key_list = list(dict_sum_unique.keys())
    return key_list

def get_value(): #just for type == 1 or 2
    if type_of_comparison == 1:
        value_list = list(dict_sum.values())
    else:
        value_list = list(dict_sum_unique.values())
    return value_list

#chart_fuction
def get_linechart():
    if type_of_comparison == 3:
        df[groupby_col] = df[groupby_col].astype(str)
        df[groupby_col] = df[groupby_col].str.strip("(),'")
        relation = df.groupby(groupby_col)[compare_col].sum()
        plt.plot(relation.index, relation.values, marker='o', linestyle='-', color='b')
        plt.ylabel(f"Total {compare_col}")
        plt.xlabel(groupby_col)
        plt.title(f"Sum of {compare_col} by {groupby_col}")
        plt.grid(True)
        plt.show()
    elif type_of_comparison == 2:
        for i in list_unique_column:
            df[i] = df[i].astype(str)
            df[i] = df[i].str.strip("(),'")
            relation = df.groupby(i)[i].size().sort_index()
            plt.figure(figsize=(10, 6))
            relation.plot(kind='line', marker='o', color='b')
            plt.ylabel('Total Number')
            plt.title(f"Sum of {i} by {i}")
            plt.xticks(range(len(relation.index)), relation.index, rotation=45)  # Set x-axis labels
            plt.tight_layout()
            plt.show()
    elif type_of_comparison == 1:
        get_sum()
        title_name = ''
        sum_df = pd.DataFrame(dict_sum,index = ["Total"])
        plt.figure(figsize=(10, 6))
        plt.plot(sum_df.columns, sum_df.loc['Total'], marker='o', linestyle='-', color='b')
        plt.ylabel('Total')
        k = 0
        for i in list_column:
            if k < len(list_column)-1:
                title_name += f"Sum of {i} and "
                k += 1
            else:
                title_name += f"Sum of {i}"
        plt.title(title_name)
        plt.grid(True)
        plt.show()
    return plt.show()
    
#format_function
def get_barchart():
    if type_of_comparison == 1:
        get_sum()
        plt.bar(get_key(),get_value())
        for i, value in enumerate(get_value()):
            plt.text(i, value, str(value), ha='center', va='bottom')
        title_name = ""
        k = 0
        for i in list_column:
            if k < len(list_column)-1:
                title_name += f"Sum of {i} and "
                k += 1
            else:
                title_name += f"Sum of {i}"
        plt.title(title_name)
        plt.show()
    elif type_of_comparison == 2:
        for i in list_unique_column:
            data_type = df[i].dtypes
            if data_type == 'int64' or data_type == 'float64':
                plt.figure(figsize=(10, 6))
                df[i].value_counts().sort_index().plot(kind='bar', color='b')
                plt.xlabel(f'{i}')
                plt.ylabel('Total Count')
                plt.title(f'Count of {i}')
                plt.xticks(rotation=0)  # Adjust rotation based on your preference
                plt.show()
            else:
                get_sum()
                title_name = ""
                plt.bar(get_key(),get_value())
                for i, value in enumerate(get_value()):
                    plt.text(i, value, str(value), ha='center', va='bottom')
                key = get_key()
                for i, key in enumerate(key):
                    if i < len(key)-1:
                        title_name += f"Sum of {key} and "
                    else:
                        title_name += f"Sum of {key}"
                plt.title(title_name)
                plt.show()
    else:
        relation = df.groupby(groupby_col)[compare_col].sum()
        plt.figure(figsize=(10, 6))
        relation.plot(kind='bar', color='skyblue')
        plt.xlabel(f'{groupby_col}')
        plt.ylabel(f'{compare_col}')
        plt.title(f"Sum of {compare_col} by {groupby_col}")
        plt.xticks(rotation=45)  
        plt.tight_layout()
        plt.show()
    return plt.show()

def get_piechart():
    if type_of_comparison == 1:
        get_sum()
        plt.pie(get_value(),labels=get_key(),autopct='%1.f%%')
        plt.show()
    elif type_of_comparison == 2:
        for i in list_unique_column:
            data_type = df[i].dtypes
            if data_type == 'int64'or data_type == 'float64':
                numeric_column = i 
                data = df[numeric_column] 
                plt.pie(data, labels=df[f'{i}'], autopct='%1.1f%%', startangle=140)
                plt.axis('equal') 
                plt.show()  
            else:
                get_sum()
                plt.pie(get_value(),labels=get_key(),autopct='%1.f%%')
                plt.show() 
    else:
        relation = df.groupby(groupby_col)[compare_col].sum()
        plt.figure(figsize=(8, 8))
        plt.pie(relation.values, labels=relation.index, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.show()
    return plt.show()

#display_format  
if display_format == "Bar Chart":
    if type_of_comparison == 2:
        try:
            get_barchart()
        except:
            print("Inappropriate information") 
    else:
        count_int = 0
        while True:
            for i in list_column:
                data_type = df[i].dtypes
                if data_type == 'int64'or data_type == 'float64':
                    count_int += 1
            break    
        if count_int < len(list_column):
            print("Inappropriate information")
        else:
            try:
                get_barchart()
            except:
                print("Inappropriate information") 
            
elif display_format == "Pie Chart":
    if type_of_comparison == 2:
        try:    
            get_piechart()
        except:
            print("Inappropriate information")
    else:
        count_int = 0
        while True:
            for i in list_column:
                data_type = df[i].dtypes
                if data_type == 'int64'or data_type == 'float64':
                    count_int += 1
            break    
        if count_int < len(list_column):
            print("Inappropriate information")
        else:
            try:
                get_piechart()
            except:
                print("Inappropriate information")     
else:
    try:
        get_linechart()
    except:
        print("Inappropriate information")
