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
DOB = []
SSN = []
State = []

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
#  Open the output file
output_file = os.path.join("EmployeeInfoMerged.csv")
csvfile_out = open(output_file, "w")

writer = csv.writer(csvfile_out, delimiter=",")

# Write the header row
writer.writerow(["EmployeeID", "First Name", "Last Name", "DOB", "SSN", "State"])

# Read each csv file
for csvfile in filelist:
    EmployData_csv = os.path.join("Resources", csvfile)

    with open(EmployData_csv, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        # loop through CSV to populate dictionary
        for row in csvreader:

            # Add employees
            EmployeeID = [row[0]]

            #Split firsta and last name
            EmployeeName = row[1]
            EmployeeName = EmployeeName.split(" ")
            FirstName = [EmployeeName.pop(0)]
            LastName = [EmployeeName.pop()]

            # Reformat DOB
            DOB = row[2]
            DOB = DOB.split("-")
            DOB = [str(DOB[1] + "/" + DOB[2] + "/" + DOB[0])]

            # Reformat SSN
            SSN = row[3]
            SSN = ["***-**-" + SSN[-4:]]

            # Reformat state name to abbreviation
            State = row[4]
            State = [us_state_abbrev[State]]
            


            # Zip lists together
            cleaned_csv = zip(EmployeeID, FirstName, LastName, DOB, SSN, State)
            # print(cleaned_csv)

# Set variable for output file

            

            # Write in zipped rows
            writer.writerows(cleaned_csv)

            # Close CSV files
csvfile.close()
csvfile_out.close()