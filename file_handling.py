xfile = open("file.txt")
inp = xfile.read()
print(len(inp))

yfile = open("file.txt")
for line in yfile:
    line = line.rstrip()
    print(line)

fname = input("Enter file name")

try:
    fhand = open(fname)
    line = line.upper()
except:
    print("file can not opened:",fname)
    quit()