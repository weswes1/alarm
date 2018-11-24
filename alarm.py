import datetime,time 
from AppKit import NSBeep
# Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.

now = datetime.datetime.now()
#for i in range(0,len(timeList)):
#	timeList[i]

timeList = [now.year,now.month,now.day,now.hour,now.minute]

def ringorRest(alarmtime):
	# Check if the time given for the alarm is in the past
	if (checkInput(alarmtime)):		# Check if the 
		anarr = alarmtime.split('/')
		for i in range(0,len(anarr)):
			anarr[i]=int(anarr[i])
		ringing = False
		while not ringing:
			count=0
			for i in range(0,len(anarr)):
				if anarr[i] == timeList[i]:
					print("yes")
					count+=1
					time.sleep(1)
					continue
				else:
					print("no")
					break
			if count == 4:
				NSBeep()
				ringing = True
def isBefore(datelist1,datelist2):
	if datelist1[0] < datelist2[0]:    		 	# datelist1 has a year less than datelist2. isBefore returns True
		return True
	if datelist1[0] == datelist2[0]:    		# Same Year
		print("same year")
		if datelist1[1] < datelist2[1]: 		# Datelist1 is at an earlier month than datelist2, isBefore returns True
			return True                 
		if datelist1[1] == datelist2[1]:		# Same year, same month
			print("same month")
			if datelist1[2] < datelist2[2]:		# Datelist1 is at an earlier day than datelist2, isBefore returns True
				return True
			if datelist1[2]==datelist2[2]:		# Same year, same month, same day
				print("same day")
				if datelist1[3] < datelist2[3]:
					return True
				if datelist1[3]==datelist2[3]:	# Same year, same month, same day, same hour
					print("same hour")
					if datelist1[4] < datelist2[4]:
						print("fewer minutes after the hour")
						return True
					else:
						print("1")
						return False
				else:
					print("2")
					return False
			else:
				print("3")
				return False
		else:
			print("4")
			return False				# datelist1 has the same year, but is at a later month than datelist2, return false
	else:
		print("5")						# datelist1 has a year after datelist 2, return false 
		return False
def intify(str):
	anarr = str.split("/")
	for i in range(0,len(anarr)):
		anarr[i]=int(anarr[i])
	return anarr
def checkInput(str):
	anarr = str.split('/')
	for i in range(0,len(anarr)):
		if not anarr[i].isdigit():
			return False
		anarr[i]=int(anarr[i])
	if (anarr[0] < now.year or anarr[1] > 12 or anarr[1] <= 0 or anarr[2] > 31):
		print("ding")
		return False
	if (anarr[2] <= 0 or anarr[3] > 24 or anarr[3]< 0 or anarr[4] > 60 or anarr[4]<0):
		print("ding1")
		return False
	else:
		return True

useStopwatch=True
alarm = "2018/08/23/11/30"

while useStopwatch:
	try:
		useStopatch = input("If you would like to use the stopwatch, Enter Y in parantheses. To use the alarm, enter A. To quit the program, enter q: ")
	except (NameError,SyntaxError,TypeError):
		print("Incorrect input. Try again.")
		continue
	if (useStopatch.upper()=="A"):
		useAlarm=True
		while useAlarm:

			try: 
				alarm = str(input("Enter the year, month, day, hour, and minute you would like to set the alarm, seperated by backslashes. Enter back to go back "))

			except (NameError,SyntaxError,TypeError):
				print("Incorrect Input. Try again.")

			if alarm.lower() == "back":
				useAlarm = False
				break

			if not (checkInput(alarm) and isBefore(intify(alarm),timeList)):
				print("Incorrect Input. Try again.")

			else:
				print("Valid Input")



	if (useStopatch.upper() == "Q"):
		exit()
	if (useStopatch.upper()=="Y"):
		stopWatch = True
		while stopWatch:
			try:
				startButton = input("Enter start to begin recording the time, or stop to go back ")
			except (NameError,SyntaxError,TypeError):
				print("Incorrect Input. Try again. ")
				continue
			if (startButton=='stop'):
				usestopWatch=False
				stopWatch=False
				useAlarm=True
				break
			if not (startButton.lower() == "start"):
				print("Incorrect Input. Try again. ")
				continue
			else:
				startTime = time.time()
				while True:
					try:
						inp = input("The stopwatch has started. Enter stop to stop the stopwatch and display the time elapsed. ")
					except (NameError,SyntaxError,TypeError):
						print("Incorrect Input. Try again.")
						continue
					if not (inp == "stop"):
						print("Incorrect Input. Try again.")
						continue
					else:
						timeElapsed = time.time()-startTime
						print("The time elapsed is {} hours {} minutes and {} seconds".format(round(timeElapsed/3600),round(timeElapsed/60),round(timeElapsed)%60))
						break


