fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

count = 0
fh = open(fname)


for line in fh:
     line = line.rstrip()
     if line.startswith('From'):
        if line.startswith('From:') : continue
        words = line.split() 
        count = count+1
        print(words)
        print(words[1])


print("There were", count, "lines in the file with From as the first word")
