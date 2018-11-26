import datetime,time 
from AppKit import NSBeep
# Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
def isBefore(datelist1):
	if datelist1[0] < datetime.datetime.now().replace(second=0,microsecond=0).year:		 	# datelist1 has a year less than datelist2. isBefore returns True
		return True
	if datelist1[0] == datetime.datetime.now().replace(second=0,microsecond=0).year:    		# Same Year
		if datelist1[1] < datetime.datetime.now().replace(second=0,microsecond=0).month: 		# Datelist1 is at an earlier month than datelist2, isBefore returns True
			return True                 
		if datelist1[1] == datetime.datetime.now().replace(second=0,microsecond=0).month:		# Same year, same month
			if datelist1[2] < datetime.datetime.now().replace(second=0,microsecond=0).day:		# Datelist1 is at an earlier day than datelist2, isBefore returns True
				return True
			if datelist1[2]==datetime.datetime.now().replace(second=0,microsecond=0).day:		# Same year, same month, same day
				if datelist1[3] < datetime.datetime.now().replace(second=0,microsecond=0).hour:
					return True
				if datelist1[3]==datetime.datetime.now().replace(second=0,microsecond=0).hour:	# Same year, same month, same day, same hour
					if datelist1[4] < datetime.datetime.now().replace(second=0,microsecond=0).minute:
						return True
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False				# datelist1 has the same year, but is at a later month than datelist2, return false
	else:					# datelist1 has a year after datelist 2, return false 
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
	if (anarr[0] < datetime.datetime.now().replace(second=0,microsecond=0).year or anarr[1] > 12 or anarr[1] < 1 or anarr[2] > 31 or anarr[2] <= 0 or anarr[3] > 23 or anarr[3] < 0 or anarr[4]>59 or anarr[4]<0):
		return False
	else:
		return True

useStopwatch=True
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
			if not checkInput(alarm):
				print("Incorrect Input. Try again. jj ")

			if isBefore(intify(alarm)):
				print ("Enter an alarm that is after the current time. ")

			else:
				alarma=intify(alarm)
				adate = datetime.datetime(alarma[0],alarma[1],alarma[2],alarma[3],alarma[4])

				while not isBefore(alarma):
					print(adate)
					print(datetime.datetime.now().replace(second=0,microsecond=0))
					time.sleep(1)

					if (adate==datetime.datetime.now().replace(second=0,microsecond=0)):
						print("ALARM RING")
						NSBeep()
						break

# Stopwatch

	if (useStopatch.upper() == "Q"):
		exit()
	if (useStopatch.upper() == "Y"):
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
					inp = None
					while not inp=="stop":
						print(datetime.datetime.now())
						time.sleep(1)
						break
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




				

