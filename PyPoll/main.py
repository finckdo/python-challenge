import os
import csv

# use csv file from the Resources directory
csvpath = os.path.join('..', 'Resources', 'election_data.csv')  # read csv from Resources directory


# Open csv file from
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    csv_header = next(csvreader)  # skip header row from csv file
    # print(csv_header)

    # Declare 3 new lists that are empty
    voterid = []
    county = []
    candidate = []

    # for each row in the csv file, append values from the first index to the new voterid list, the second index to the new county list, and the thrid index to the new candidate list
    for row in csvreader:
        voteridvalue=row[0]
        countyvalue=row[1]
        candidatevalue=row[2]

        voterid.append(voteridvalue)
        county.append(countyvalue)
        candidate.append(candidatevalue)

    voteridrecordcnt = len(voterid)

    candidatefreq = {}
    for row in candidate:
        if row in candidatefreq:
            candidatefreq[row] = candidatefreq[row] + 1
        else:
            candidatefreq[row] = 1

    candidatesort = dict(sorted(candidatefreq.items(), key=lambda x: x[1], reverse=True))

    maxcandidate = max(candidatefreq.items(), key=lambda x: x[1])
    maxcandidatename = maxcandidate[0]
    mincandidate = min(candidatefreq.items(), key=lambda x: x[1])



    print('')
    print('Election Results')
    print('-------------------------')
    print(f"Total Votes: {voteridrecordcnt}")
    print('-------------------------')
    for key, value in candidatesort.items(): 
        percentage = (value/voteridrecordcnt) * 100
        print(key, round(percentage, 3),"%", "(",value,")")
    print('-------------------------')
    print(f"Winner: {maxcandidatename}")
    print('-------------------------')

output_file = os.path.join("PyPoll_output.txt")

with open(output_file, "w", encoding='utf-8') as datafile:
    writer = csv.writer(datafile, delimiter=' ')
    
    writer.writerow(['Election Results'])
    writer.writerow(['-------------------------'])
    writer.writerow([f'Total Votes: {voteridrecordcnt}'])
    writer.writerow(['-------------------------'])
    for key, value in candidatesort.items(): 
        percentage = (value/voteridrecordcnt) * 100
        writer.writerow([key, round(percentage, 3),"%", "(",value,")"])
    writer.writerow(['-------------------------'])
    writer.writerow([f"Winner: {maxcandidatename}"])
    writer.writerow(['-------------------------'])


    # print(maxcandidate)
    # print(mincandidate)


        # print (key, value)

    # for row in candidatefreq:
    #     print(row)



    # for key, value in candidatesort.items():
    #     test = candidatesort[value] / voteridrecordcnt
    #     print(key, value)

# countyrecordcnt = len(county)
# candidatecnt = len(candidate)


# print(voteridrecordcnt)
# print(countyrecordcnt)
# print(candidatecnt)

# print(voterid[0], voterid[-1])
# print(county[0], county[-1])
# print(candidate[0], candidate[-1])



# print('')
# print('Election Results')
# print('-------------------------')
# print(f"Total Votes: {voteridrecordcnt}")
# print('-------------------------')
# print(f"{candidatesort}")
# print('-------------------------')
# print(f"Winner: {maxcandidatename}")
# print('-------------------------')
