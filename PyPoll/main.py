# Dependencies
import os
import csv

#Files in folder
filelist = os.listdir("Resources")

# Create candidate dictionary
CandidateSummary= {}
TotalVotes = 0
winner = "none"

# Read each csv file
for csvfile in filelist:
    PollingData_csv = os.path.join("Resources", csvfile)

    with open(PollingData_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

# loop through CSV to populate dictionary
        for row in csvreader:

            # Add candidates
            CandidateName = row[2]
            if CandidateName not in CandidateSummary:
                CandidateSummary[CandidateName] = 1
                
            elif CandidateName in CandidateSummary:
                votes = CandidateSummary[CandidateName]
                CandidateSummary[CandidateName] = votes + 1
            
            TotalVotes = TotalVotes + 1
# Close CSV files
    csvfile.close()

# Determine winner 
for Candidate in CandidateSummary:
    if winner == "none":
        winner = Candidate
        winnervotes = CandidateSummary[Candidate]
    elif winner != "none":
        evalvotes = CandidateSummary[Candidate]
        if evalvotes > winnervotes:
            winner = Candidate
            winnervotes = CandidateSummary[Candidate]

#Print election results
print("Election Results")
print("=================")
print("Total Votes:" + str(TotalVotes))
print("=================")
for Candidate in CandidateSummary:
    print(Candidate + ": " + str(round(CandidateSummary[Candidate]/TotalVotes * 100,1)) + "%" + " (" + str(CandidateSummary[Candidate]) + ")")
print("=================")
print("Winner: " + winner)
print("=================")


output_file = os.path.join("PollResults.txt")
f = open(output_file, "w")
f.write("Election Results" + "\n")
f.write("=================" + "\n")
f.write("Total Votes:" + str(TotalVotes) + "\n")
f.write("=================" + "\n")
for Candidate in CandidateSummary:
    f.write(Candidate + ": " + str(round(CandidateSummary[Candidate]/TotalVotes * 100,1)) + "%" + " (" + str(CandidateSummary[Candidate]) + ")" + "\n")
f.write("=================" + "\n")

f.write("Winner: " + winner + "\n")
f.write("=================" + "\n")
f.close()
