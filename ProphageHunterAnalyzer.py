import os
import os.path
import re
lines1 = ''
lines2 = ''
lines3 = []
files_path = 'C:/Users/valmi/Desktop/NZ_CP020896.1 Rhizobium phaseoli Brasil 5 strain Bra5 chromosome, complete genome/'
#equate 'files_path' to the directory where your input sequence/ Prophage Hunter output files are located on your computer
#both input .fasta and Prophage Hunter main output.txt files should be located in same folder
for filename in os.listdir(files_path):
    # specify the types of files we want this program to oversee
        if filename.__contains__('sequence'): # program looks for a whole genome fasta file labeled 'sequence'; this is the sequence input into Prophage Hunter
            #change 'sequence' to whatever your particular input sequence is labeled, sequences downloaded directly from GenBank are automatically called 'sequence'
            with open("{}/{}".format(files_path, filename)) as sequence:
                lines1 = "".join(sequence.read().splitlines())
        if filename.__contains__('output'):#program searches for main Prophage Hunter output file that is labeled as 'output'
            #change 'output' to whatever the main output file is named if different
            with open("{}/{}".format(files_path, filename)) as results:
                lines2 = results.read().splitlines()

cutoff = lines1.index('genome') #optimized for whole genome input sequences

lines1 = lines1[cutoff+6:]

strain = re.search('ref\|(.*?)\|:', lines2[2])
if strain:
    strainName = strain.group(1)

for v,i in enumerate(lines2):
    candidate = i[0:13]
    if i.__contains__('Active'):
        if i.__contains__(":"):
            start = i.index(":")
            startNum = start + 11
            startIndex = int(i[startNum:startNum+8])
            endIndex = int(i[startNum+8:startNum+15])
            selection = lines1[startIndex:endIndex+1]
            lines3.append(strainName + " " + candidate + " Active")
            lines3.append(selection)

for v,i in enumerate(lines2):
    candidate = i[0:13]
    if i.__contains__('Ambiguous'):
        if i.__contains__(":"):
            start = i.index(":")
            startNum = start + 11
            startIndex = int(i[startNum:startNum+8])
            endIndex = int(i[startNum+8:startNum+15])
            selection = lines1[startIndex:endIndex+1]
            lines3.append(strainName + " " + candidate + " Ambiguous")
            lines3.append(selection)

MyFile3= open(files_path+ " " + strainName + ' OUTPUT' + '.txt','w')

for e in lines3:
    MyFile3.write(e)
    MyFile3.write('\n')
MyFile3.close()




