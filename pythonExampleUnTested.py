#For this problem, we can apply Python’s elegant sequence indexing and slicing operations. Note, the use of number signs (#) indicate comments for the code (as shown below).

#Step 1: Generate a master accessory list from the union of all sets of accessory codes of each record

ifile = open(‘JM_Family.txt’,’r’) #create a file object for the actual dataset(the report)
reportread = csv.reader(ifile, delimiter = ‘t‘) #create a reader object from the file object
acclookup = []
for row in reportread:
if reportread.line_num >1: #excluding the header row

#Pieces all the values of the variable (second column in the dataset and indexed to 1) and make the #result a big list
acclookup.extend(row[1].split(“, “))
acclookup = (list(set(acclookup))) #remove duplicates
acclookup.sort()

#Step 2: Create dummy variables and populate with 0 and 1 from acclookup and write the result to the file

ofile = open(‘accw.txt’,’w’) #create a file object for writing the result
reportwriter = csv.writer(ofile) #create a writer object
ifile = open(‘JM_Family.txt’,’r’)
reportread = csv.reader(ifile, delimiter = ‘t’)
for row in reportread: #for each row in the read tab delimited file
if reportread.line_num == 1:
row.extend(acclookup)
reportwriter.writerow(row) #write column headers to the file
else:
accdummy = [0] * len(acclookup)
acclist = row[1].split(“, “) #read the 2nd column(2nd column is indexed to 1) and turn it into a list
n = len(acclist) #count how many items (accessory codes) there are in each list
for i in range(n):
pacdum = acclookup.index(acclist[i])
accdummy[pacdum] = 1 #write the dummy values ( 1 for occurrence and 0 for nonoccurrence)
row.extend(accdummy)
reportwriter.writerow(row)
ofile.close()
