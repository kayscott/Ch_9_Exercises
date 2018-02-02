inp = input("Type File Name: ")
try: 
    file = open(inp)
except: 
    print 'File cannot be opened:', inp
    exit()

em = dict()
for line in file: 
    words = line.split()
    words = words[1:2]
    if "From" not in line : continue 
    for email in words: 
        em[email] = em.get(email, -1) + 1
        #very unsure about line 14 being correct or if it's just adding tape to conceptual problem 
print em
for email in em: 
    print email, em[email]

        
    