import random

#A bunch of lists containing parts of speech go here
nounPersonLive = ['The President', 'Donald Trump', 'Tom Cruise', 'Alex Noble']
nounPersonDead = ['Hitler', 'Abraham Lincoln', 'Karl Marx']
nounTypeOfPerson = ['Walmart Employee', 'Cancer Survivor', 'Democrat', 'Decorated Veteran']
goodThing = ['Winning The Genetic Lottery', 'Running A Marathon', 'Eating A Piece Of Pie', 'Calling Your Mother']
badThing = ['The Bees Dying', 'Genocide', 'Drone Strikes', 'The Holocaust']
genericObject = ['Things', 'Tricks', 'Tips']
event = ['Coronation', 'High School Prom', 'Graduation Ceremony']
verbPast = ['Discovered', 'Did', 'Accomplished', 'Exposed']
verbIng = ['Pooping', 'Vaping', 'Making A Phone Call']
verbNiceThingToDo = ['Call Their Congressman', 'Quit Smoking']
attentionGetter = ['Breaking:', 'Attention:', 'Urgent:', '']
youWontBelieve = []
reaction = ['Make You Cry', 'Shock You', 'FLoor You', 'Leave You Speechless']
number = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', '10','12', '13', '15', '20', '25', '30']

#Sentence Structures

def PickSentence():
	structure = random.randint(1, 5)
	if structure == 1:
		result = random.choice(attentionGetter) + ' ' + random.choice(nounPersonLive) + ' Just Told This ' + random.choice(nounTypeOfPerson) + ' To ' + random.choice(verbNiceThingToDo) + ' Because Of ' + random.choice(badThing)
		print(result)
	elif structure == 2:
		result = 'Was The ' + random.choice(event) + ' Of ' + random.choice(nounPersonDead) + ' Actually ' + random.choice(goodThing) + '? What ' + random.choice(nounPersonLive) + ' Thinks Will ' + random.choice(reaction)
		print(result)
	elif structure == 3:
		result = 'What This ' + random.choice(nounTypeOfPerson) + ' ' + random.choice(verbPast) + ' Will ' + random.choice(reaction)
		print(result)
	elif structure == 4:
		result = random.choice(number) + ' ' + random.choice(genericObject) + ' ' + random.choice(nounTypeOfPerson) + 's Don\'t Want You To Know About ' + random.choice(badThing)
		print(result)
	elif structure == 5:
		result = 'Some Will Call It ' + random.choice(goodThing) + '. ' + random.choice(nounPersonLive) + ' Simply Calls It ' + random.choice(verbIng)
		print(result)
	#for adding new sentences
	#else if structure == [number]:
	#	result = 
	#	print(result)

PickSentence()