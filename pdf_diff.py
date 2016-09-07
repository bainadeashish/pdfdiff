import os,pdb
from itertools import izip
import difflib


file1 = "33.pdf"
file2 = "2.pdf"
textfile1 = file1.split('.')[0] + ".txt"
textfile2 = file2.split('.')[0] + ".txt"
cmd1 = "pdf2txt.py -o {}.txt {}" .format(file1.split('.')[0],file1)
cmd2 = "pdf2txt.py -o {}.txt {}" .format(file2.split('.')[0],file2)

os.system(cmd1)
os.system(cmd2)
text1 = open(textfile1,'r').read()
text2 = open(textfile2,'r').read()


# create a list of lines in text1
text1Lines = text1.splitlines(1)

text2Lines = text2.splitlines(1)
  
diffInstance = difflib.Differ()
diffList1 = list(diffInstance.compare(text1Lines, text2Lines))

str1_set=set()
str2_set=set()
print '-'*50
print "Lines different in text1 from text2:"
for line in diffList1:
    if line[0] == '-':
        print line
        # str1_set = set(line.split())
        # str1_set.remove('-')
        # diffwords = list(str1_set)
        # for item in diffwords:
            # if item in line:
                # line = line.translate(None, item)
			    
     
			    

		
			
    
