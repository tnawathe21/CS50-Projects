from sys import argv, exit
import csv

### LOADING DNA DATABASE (CSV FILE) INTO MEMORY ###
# file name of csv
database = argv[1]

# prepare to read heading titles and rows into a list
titles = []
people = []
peoplenum = 0 # store number of people in the database
STRnum = 0 # store number of STRs to parse

with open(database, 'r') as csvfile:
    # create a csv reader
    csvreader = csv.reader(csvfile)

    # get heading titles
    titles = next(csvreader)

    # load data into rows
    for row in csvreader:
        people.append(row)

    # store number of people in the database
    peoplenum =  csvreader.line_num - 1

# determine number of STRs to parse
STRnum = len(titles) - 1

### LOADING DNA SEQUENCE (TXT FILE) INTO MEMORY ###
with open(argv[2], 'r') as txtfile:
  # reads txt file, which contains DNA sequence, into a string
  seq = txtfile.read()

  # close txt file
  txtfile.close()

### FILLING STR FREQUENCY LIST ARRAY (EACH ELEMENT IN EACH LIST ROW IS STR REPEAT NUMBER AT THAT POSITION) ###
repeatsarr = [] # multidimensional array: each STR and within it, number of repeats for each position
temp = [] # 1D array to temporarily keep track of repeats for each position, soon gets transferred to repeats multiD array
count = 0 # keeps track of the number of STR repeats for each position in the DNA sequence string
seqlength = len(seq) # length of DNA sequence

for STR in titles[1:]: # leave out first element since it's just 'name'
    temp.clear()
    for i in range(seqlength):
        count = 0
        j = i
        while seq[j:j+(len(STR))] == STR: # counts number of STR repeats starting from i position in the DNA sequence
            count+= 1
            j += len(STR)
        temp.append(count) # adds that number to end of temp integer array
    tobeadded = temp.copy()
    repeatsarr.append(tobeadded)

### FIND LARGEST REPEAT IN EACH NUMBER ARRAY WITHIN REPEATSARR ###
largest = 0 # keeps track of largest repeat for each STR
STRarr = [] # contains the largest repeat of the STRs

for array in range(STRnum): # iterates over each array (corresponding to each STR)
    largest = repeatsarr[array][0] # first number in array that is in repeatsarr
    for i in repeatsarr[array]: # finds the largest element in the array
        if i > largest:
            largest = i
    STRarr.append(largest)

### FIND PERSON IN THE DATABASE WHO IS A MATCH FOR THE GIVEN DNA SEQUENCE ###
# we need STRarr and people
matchcount = 0
for i in range(len(people)):
    matchcount = 0
    for j in range(1, len(people[i])): # from 1st element to last element in STRs
        if int(people[i][j]) == int(STRarr[j-1]):
            matchcount += 1
    if matchcount == STRnum:
        print(people[i][0])
        exit()
print('NO MATCH')