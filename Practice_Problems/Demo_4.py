'''Reading Files and Writing Files'''

fhand = open('files/information.txt')
count = 0

'''for line in fhand:
    count += 1

print('Line Count:', count)
'''

for line in fhand:
    line = line.rstrip()
    if 'Lenore' in line:
        print(line)


fhand.close()