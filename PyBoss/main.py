# Dependencies
import os
import csv

#Files in folder
filelist = os.listdir("Resources")

# Create employee dictionary
# EmployeeSummary= {}
EmployeeID = []
FirstName = []
LastName = []
DOB2 = []
SSN2 = []
State2 = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}




# Read each csv file
for csvfile in filelist:
    EmployData_csv = os.path.join("Resources", csvfile)

    with open(EmployData_csv, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        # loop through CSV to populate dictionary
        for row in csvreader:

            # Add employees
            EmployeeID.append(row[0])

            #Split firsta and last name
            EmployeeName = row[1]
            EmployeeName = EmployeeName.split(" ")
            FirstName.append(EmployeeName.pop(0))
            LastName.append(EmployeeName.pop())

            # Reformat DOB
            DOB = row[2]
            DOB = DOB.split("-")
            DOB2.append(str(DOB[1] + "/" + DOB[2] + "/" + DOB[0]))

            # Reformat SSN
            SSN = row[3]
            SSN2.append("***-**-" + SSN[-4:])

            # Reformat state name to abbreviation
            State = row[4]
            State2.append(us_state_abbrev[State])
            


            # Zip lists together
            cleaned_csv = zip(EmployeeID, FirstName, LastName, DOB2, SSN2, State2)
            # print(cleaned_csv)
#  Open the output file
output_file = os.path.join("EmployeeInfoMerged2.csv")

# Set variable for output file
with open(output_file, 'w', newline="") as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write the header row
        csvWriter.writerow(["EmployeeID", "First Name", "Last Name", "DOB", "SSN", "State"])

        # Write the zipped lists to a csv
        csvWriter.writerows(cleaned_csv)


csvfile.close()
