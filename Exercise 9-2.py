inp = input("Type File Name: ")
try: 
    file = open(inp)
except: 
    print 'File cannot be opened:', inp
    exit()

days = dict()
for line in file: 
    words = line.split()
    words = words[2:3]
    if "From" not in line : continue 
    for day in words: 
        days[day] = days.get(day, 0) + 1
print days
        
    