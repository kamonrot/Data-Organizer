import pandas as pd
pd.options.mode.chained_assignment = None  # Suppress SettingWithCopyWarning
import matplotlib.pyplot as plt

file_name = input("Enter your file name : ")
dt = pd.read_csv(f"{file_name}")
df = pd.DataFrame(dt)

#BMI_Part
bmi_dt = dt[["Height","Weight"]]
bmi_dt.loc[:, "BMI"] = round(((bmi_dt["Weight"]) / (bmi_dt["Height"] / 100) ** 2), 2)
bmi_dt.to_csv("bmi.csv", index=False)
df_bmi = pd.DataFrame(bmi_dt)

function
def Get_male():
    sum_male = sum(df.Gender == "Male")
    return sum_male

def Get_female():
    sum_female = sum(df.Gender == "Female")
    return sum_female

def Get_Children():
    sum_children = sum(df.Age < 18)
    return sum_children

def Get_Adult():
    sum_adult = sum(df.Age >= 18)
    return sum_adult

def Normal_BMI():
    bmi_min = 18.5
    bmi_max = 24
    normal_bmi = ((df_bmi.BMI >= bmi_min)&(df_bmi.BMI <= bmi_max)).sum()
    return normal_bmi

def Bad_BMI():
    bmi_min = 18.5
    bmi_max = 24
    bad_bmi = ((df_bmi.BMI < bmi_min)|(df_bmi.BMI > bmi_max)).sum()
    return bad_bmi

def Get_Thai():
    sum_thai = sum(df.Nationality == "Thai")
    return sum_thai

def Get_Others():
    sum_others = sum(df.Nationality == "Others")
    return sum_others

def Get_Blood_A():
    group_a = sum(df.Blood_Group == "A")
    return group_a

def Get_Blood_B():
    group_b = sum(df.Blood_Group == "B")
    return group_b

def Get_Blood_O():
    group_o = sum(df.Blood_Group == "O")
    return group_o

def Get_Blood_AB():
    group_ab = sum(df.Blood_Group == "AB")
    return group_ab

def Get_Blood_Other():
    group_other = sum(df.Blood_Group == "Other")
    return group_other

def Get_Hypertension():
    count_hypertension = sum(df.Congenital_Disease == "Hypertension")
    return count_hypertension

def Get_Diabetes():
    count_diabetes = sum(df.Congenital_Disease == "Diabetes")
    return count_diabetes

def Get_Asthma():
    count_asthma = sum(df.Congenital_Disease == "Asthma")
    return count_asthma

def Get_Heart_Disease():
    count_heart_disease = sum(df.Congenital_Disease == "Heart Disease")
    return count_heart_disease

def Get_Other_Disease():
    count_other_disease = sum(df.Congenital_Disease == "Other")
    return count_other_disease



