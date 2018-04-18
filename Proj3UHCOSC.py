### PROGRAMMING ASSIGNMENT 3 ###
### COSC 1306 ###
### PATRICK W KURTH ###
### UH ID: 1592681 ###
### patrickwkurth@gmail.com ###
import csv
filename = ("CFSpring2018Employers.csv")  # I assigned the file to a variable
# I couldn't leave it default due to UTF-8 error from orginial
f = open(filename)
reader = csv.reader(f)
f.close

# Dictionary for part 1 'Companies'
companies = {}
countComp = 0  # Sets the 'rows to 0

for row in reader:  # reader has assigned value to read csv info
    if row[0] == 'Company':  # Searches row called 'Company'
        for item in row:
            # Everytime it shows it puts it into the dictionary
            companies[countComp] = item
            countComp += 1
        break  # Break so it stops from going to the next instance of company

for i in companies:  # Allows me to print numbers next to the companies dict
    print(i, companies[i])

ReadyColumn = []  # Making a new list for cleaned up data
NumCow = 0
for row in reader:
    NumCow += 1
    # This will read the rows between 0-31, and if the row contains 'Nothing' it skips
    if NumCow < 31 and row[0] != '':
        ReadyColumn.append(row)  # Updates the list
rowNum = -1  # Resets the counter so that AIG starts at 0

for row in ReadyColumn:
    rowNum += 1
    # Joins the rows with each value separated by ,
    print(rowNum, ','.join(row))

data_employer = {'No': ('Column', 'Sum')}

for values in range(14):  # Their is 14 rows that need to be counted up
    sum = 0
    for row in ReadyColumn:
        if row[values] != '':
            sum += 1
        cleaner_employer = (companies[values], sum)
        data_employer[values] = cleaner_employer
for i in data_employer:
    cleaner_data = (i, data_employer[i][0], data_employer[i][1])

out_employer = []

for i in data_employer:
    row = []
    row.append(i)  # Adds the 'No' column
    row.append(data_employer[i][0])  # Adds the 'Column' column
    row.append(data_employer[i][1])  # Adds the 'Sum' column
    out_employer.append(row)

for k in data_employer:
    # Trying to figure out how to print the dictionary as a table as the question states
    print(list(data_employer.keys()).index(k),
          data_employer[k][0], data_employer[k][1])

# defines output file of program
employer_summary = open("CF-Spring2018-Employers_Summary.csv", 'w')
# Uses csv.writer to output into a excel format, lineterminator to remove spaces#
writer = csv.writer(employer_summary, lineterminator='\n')
writer.writerows(out_employer)  # Takes 2-dimensional data 'aka' multiple rows
# Closes my file that I wrote
employer_summary.close()
