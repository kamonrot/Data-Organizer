import pandas as pd
import matplotlib.pyplot as plt

list_format = ["Bar Chart","Pie Chart"]
list_of_comparison = ["Compare between columns : Enter 1","Compare within column : Enter 2"]
list_column = []
list_unique_column = []
check_column = []
list_unique = []
dict_sum_unique = {}
dict_sum = {}
key_list = []
value_list = []

#input
while True:
    file_name = input("Enter your file name : ") 
    try:
        dt = pd.read_csv(f"{file_name}")
        break
    except:
        print("Invalid input , please enter again") 
        
print(list_of_comparison)  

while True:
    try:
        type_of_comparison = int(input("Enter type of comparison (number):"))
        if type_of_comparison == 1 or type_of_comparison == 2:
            break
    except:
        print("Invalid input , please enter again") 
        
df = pd.DataFrame(dt)
column_names = df.columns
for column in column_names:
    check_column.append(column)
number_column = len(check_column)

if type_of_comparison == 1:
    while True:
        try:   
            n = int(input("Enter number of column : "))
            if n > 0 and n < number_column:
                break
        except:
            print("Invalid input , please enter again")            
    for i in range(n):
        while True:
            column = input(f"Enter Column No.{i+1} name : ") 
            if column in check_column:
                list_column.append(str(column))
                break
            else:
                print("Invalid input , please enter again")
else:
    while True:
        column = input(f"Enter Column name : ") 
        if column in check_column:
            list_unique_column.append(str(column))
            break
        else:
            print("Invalid input , please enter again")
        
print("Choose Your Display Format")
print(list_format)

while True:
    display_format = input("Enter Display Format : ")
    try: 
        if display_format in list_format:  
            break
    except:
        print("Invalid input , please enter again")
        
#function
def get_unique():
    for i in list_unique_column:
        unique = df[f"{i}"].unique()
    return unique

def get_sum():
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

def get_key():
    if type_of_comparison == 1:
        key_list = list(dict_sum.keys())
    else:
        key_list = list(dict_sum_unique.keys())
    return key_list

def get_value():
    if type_of_comparison == 1:
        value_list = list(dict_sum.values())
    else:
        value_list = list(dict_sum_unique.values())
    return value_list

#display_format  
if display_format == "Bar Chart":
    get_sum()
    plt.bar(get_key(),get_value())
    for i, value in enumerate(get_value()):
        plt.text(i, value, str(value), ha='center', va='bottom')
    plt.show()
else:
    get_sum()
    plt.pie(get_value(),labels=get_key(),autopct='%1.f%%')
    plt.show()




