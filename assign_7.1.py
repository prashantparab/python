# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fhand = open(fname)
    for line in fhand:
        line = line.rstrip()
        line = line.upper()
        print(line)
        
except:
    print("file can not opened:",fname)
    quit()
