import random

#A bunch of lists containing parts of speech go here
nounProper = ['The President','Trump', 'Tom Cruise', 'Alex Noble']
nounTypeOfPerson = ['Walmart employee', 'cancer survivor', 'Democrat']
pronounSubject = []
pronounObject = []
article = []
adjective = []
verbPast = ['discovered', 'did']
verbIng = ['pooping', 'vaping']
verbPresent = []
verbAction = ['take a chill pill', 'worship Satan', 'call their congressman']
qualifier = []
attentionGetter =['Breaking: ', 'Attention: ', 'Urgent: ']

#A bunch of functions containing template headlines that will pull random parts of speech into them, Madlibs style
def Sentence1():
	# Example: Breaking: Trump just told this Walmart employee to call their congressman
	result = random.choice(attentionGetter) + random.choice(nounProper) + ' just told this ' + random.choice(nounTypeOfPerson) + ' to ' + random.choice(verbAction)
	print(result)

def Sentence2():
	# Example: You will never guess what the President just said to a cancer suvivor
	result = 'You will never guess what this ' + random.choice(nounTypeOfPerson) + ' just ' + random.choice(verbPast) + ' when they were ' + random.choice(verbIng)
	print(result)

#A single function that will randomly select a template above
def PickSentence():
	structure = random.randint(1, 2)
	if structure == 1:
		Sentence1()
	if structure == 2:
		Sentence2()

#Run function
PickSentence()