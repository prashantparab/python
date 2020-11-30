# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 1
addition = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    val = line[line.find(':')+1:]
    ntext = val.strip()
    fval = float(ntext)
    addition = addition+fval
    avg = addition/count
    count = count+1
    
print("Average spam confidence:",avg)