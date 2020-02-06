from datetime import datetime

timetable = open("timetable.txt", 'r')
datelist = timetable.readlines()
for i in range(len(datelist)):
	datelist[i] = datelist[i].rstrip('\n')

print(datelist)

Found = True;

while Found == True:
	current = datetime.now()
	currentStr = current.strftime("%H %M")
	for i in range(len(datelist)):
		if datelist[i] == currentStr:
			Found = False;
			print(datelist[i])


