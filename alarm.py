import datetime,time 
from AppKit import NSBeep

# Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
now = datetime.datetime.now()
"""

useStopwatch=True

while useStopwatch:
	try:
		useStopatch = input("If you would like to use the stopwatch, Enter Y in parantheses. Otherwise, enter N. To quit the program, enter q")
	except (NameError,SyntaxError,TypeError):
		print("Incorrect input. Try again.")
		continue
	if (useStopatch.upper()=="N"):
		useStopwatch = False
	if (useStopatch.upper()=="Y"):
		stopWatch = True
		while stopWatch:
			try:
				startButton = input("Enter start to begin recording the time, or stop to go back ")
			except (NameError,SyntaxError,TypeError):
				print("Incorrect Input. Try again. ")
				continue
			if (startButton=='stop'):
				stopWatch=False
				break
			if not (startButton.lower() == "start"):
				print("Incorrect Input. Try again. ")
				continue
			else:
				startTime = time.time()
				while True:
					try:
						inp = input("The stopwatch has started. Enter stop to stop the stopwatch and display the time elapsed.")
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


print("Alarm case")

while True:
	try: 
	alarm = input("Enter the month,day,hour,and minute you would like to set the alarm, seperated by backslashes. For example, 11/21/10/30 is an alarm for November 21, at 10:30 AM ")

	except (NameError,SyntaxError,TypeError):
		print("Incorrect Input. Try again.")

	if not (checkInput(alarm)):
		print("Incorrect Input. Try again.")

	if (checkInput(alarm)):

		alarmTime = datetime.time()
		# set alarm 





def checkInput(str):
	count=[0,0]
	if (len(str) != 11):
		print("ding")
		return False
	if not (list(str)[2]=="/" and list(str)[5]=="/" and list(str)[8]=="/"):
		print("ding1")
		return False
	for char in list(str):
		if (char=='/'):
			count[0]+=1
		if char.isdigit():
			count[1]+=1
	if not count[0] == 3:
		print("ding2")
		print(count[0])
		return False
	if not count[1] == 8:
		print(count[1])
		print("ding3")
		return False
	else:
		return True
"""

str="11/21/10/30"
anarr = str.split('/')
print(anarr)

alarmTime = datetime.datetime.time()

# alarmTime.month = anarr[0]

class timeObject:
	def __init__(self):
		self.month=0
		self.day=0
		self.hour=0
		self.minute=0

print now
#print(now.year)
#print(now.day)
#print(now.hour)
#print(now.minute)




# type(), dir(), id(), getattr(), hasattr(), globals(), locals(), callable()
