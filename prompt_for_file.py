fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
count = 0 
for line in fhand: 
    if line.startswith('I love'):
        count = count + 1 
print 'There were', count, ' I loves in', fname 