# USING IN TO SEARCH 
import os 
f = open(os.path.expanduser('~/Desktop/*Filename*.txt'))
for line in f:
    line = line.rstrip()
    if not ' *keyword*' in line:
        continue
    print line 