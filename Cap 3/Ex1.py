times = ['PSG','Arsenal','Chelsea','Barcelona','Manchester City']

#1
print (times[0:3])

#2
print (times[3:5])

#3
times.sort()
print (times)

#4
i=0

for nome in times:
    i = i + 1
    if nome == 'Barcelona':
        print ("Barcelona está na posição:", i)
        break
