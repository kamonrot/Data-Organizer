import csv
import random

# Sample data for gender, congenital diseases, and blood groups
genders = ["Male", "Female"]
congenital_diseases = ["No Congenital Disease", "Hypertension", "Diabetes", "Asthma", "Heart Disease", "Other"]
blood_groups = ["A", "B", "O", "AB", "Other"]

# Generate data for 2000 patients
patients_data = []

for _ in range(2000):
    gender = random.choice(genders)
    age = random.randint(6, 85)

    nationality = random.choices(["Thai", "Other"], weights=[0.9, 0.1])[0]
    
    blood_group = random.choices(["A", "B", "O", "AB", "Other"], weights=[0.25, 0.2, 0.3, 0.15, 0.1])[0]
    
    if gender == "Male" and age <= 12:
        weight = round(random.uniform(30, 45), 2)
        height = round(random.uniform(100, 140))
    elif gender == "Male" and age > 12:
        height = round(random.uniform(140, 190))
        weight = round(random.uniform(45, 100), 2)
    elif gender == "Female" and age <= 12:
        height = round(random.uniform(100, 140))
        weight = round(random.uniform(18, 38), 2)
    else:
        height = round(random.uniform(140, 180))
        weight = round(random.uniform(40, 100), 2)
    
    # Make the distribution of Congenital Disease more equal
    congenital_disease = random.choice(congenital_diseases)
    
    patients_data.append([gender, age, nationality, blood_group, height, weight, congenital_disease])

# Write the data to a CSV file
with open('patient_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(["Gender", "Age", "Nationality", "Blood_Group", "Height", "Weight", "Congenital_Disease"])
    
    # Write patient data
    csv_writer.writerows(patients_data)
