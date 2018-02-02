## OPENING THE FILE 
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fname = open(name)
counts = dict()

## READING THROUGH THE FILE 
for line in fname: 
    line = line.rstrip()
    if not line.startswith("From ") : continue
    words = line.split()
   ## print words[5]
    delimiter = ":"
    time = words[5].split(delimiter)
    hour = time[0]
   ## print hour
   ## COUNT THE NUMBER OF TIMES HOUR OCCURS
    counts[hour] = counts.get(hour, 0) + 1

## ADD VALUES AND KEY TO LIST
lst = list()
for key, val in counts.items():
    tup = (key, val)
    lst.append(tup)
lst = sorted(lst)

## SORT IN ORDER OF LEAST TO GREATEST

for key, val in lst:
    print key, val
    

#sorted( [ ( v, k) for k, v in counts.items() ] )
#print lst