from datetime import datetime
import os

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
			data = datetime.now()
			dataStr = current.strftime("%d %m %Y %H %M")
			output = open("3am_file.txt", 'w') 
			output.write(dataStr + " automatically overides this")
			output.close()
			os.system('git add .')
			os.system('git commit -m "Up"')
			os.system('git push')



