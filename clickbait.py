import random as r

#A bunch of lists containing parts of speech go here
nounPersonLive = ['The President', 'Donald Trump', 'Tom Cruise', 'Alex Noble', 'Barack Obama', 'Hillary Clinton', 'Ellen DeGeneres', 'Kesha', 'Regis Philbin', 'Tina Fey', 'Your Mom', 'Your Girlfriend', 'Your Grandma', 'Antonio Banderas', 'Penelope Cruz', 'R Kelly', 'Snoop Dogg', 'Kanye', 'Britney Spears', 'Kim Kardashian', 'George W. Bush', 'Arnold Schwarzenegger', 'Bob Saget']
nounPersonDead = ['Hitler', 'Abraham Lincoln', 'Karl Marx', "Kierkegaard", 'Winston Churchill', 'Margaret Thatcher', 'Neil Armstrong', 'Stalin', 'Charles Darwin', 'Jane Austen', 'Charlotte Bronte', 'Edgar Allen Poe', 'Ernest Hemingway', 'Anthony Bourdain', 'George Washington', 'Thomas Jefferson', 'Francisco Franco', 'Princess Diana']
nounTypeOfPerson = ['Walmart Employee', 'Cancer Survivor', 'Democrat', 'Decorated Veteran', 'Fundamentalist', 'Taxpayer', 'Police Officer', 'SNL Castmember', 'Disneyland Employee', 'Fitness Instructor']
goodThing = ['Winning The Lottery', 'Running A Marathon', 'Eating A Piece Of Pie', 'Calling Your Mother', 'Watching A Movie', 'Falling in Love', 'Getting Married', 'Having a Baby']
goodIdeal = ['Peace, Love, Respect and Unity', 'Body Positivity', 'Diversity', 'Women in Tech', 'Microfinancing', 'Paying it Forward', 'Mentorship', 'LGBTQ Pride', 'Sex Positivity', 'Open Borders', 'Sustainability', 'Free Love', 'Veganism', 'Civility', 'Transparency', 'Great Customer Support', 'Inclusion']
badAdjectives = ['Fake News', 'Staged', 'Overblown', 'a Big Sham', 'Trumped-Up', 'a Flop', 'a Let-Down', 'Illegal']
badThing = ['The Bees Dying', 'Genocide', 'Drone Strikes', 'The Holocaust', 'Global Warming', 'The Zombie Apocalypse', 'Economic Collapse', 'Trump', 'the Death of Free Speech', 'Russian Hackers', 'Election Meddling', 'Foreign Tax Shelters', 'the Gay Agenda', 'Abortion Clinic Bombings', 'the Westboro Baptist Church', 'Immigration Policy', 'Abortion', 'Voter Fraud', 'Alcoholism']
startupTech = ['Bitcoin', 'Uber', 'TechCrunch', 'YCombinator', 'AirBnb', 'Alexa', 'Google Home', 'Google Maps', 'Facebook', 'Instagram', 'Slack', 'OKCupid', 'Tinder', 'Grindr', 'Yelp', 'UberEats', 'Google Docs', 'Microsoft Outlook', 'Microsoft Word', 'Bit.ly', 'GitHub', 'Amazon', 'Siri', 'Pinterest', 'Reddit']
genericObject = ['Things', 'Tricks', 'Tips', 'Secrets', 'Little-Known Facts', 'Misunderstood Truths']
event = ['Coronation', 'High School Prom', 'Graduation Ceremony', 'Election', 'Assassination', 'Arrest', 'Indictment', 'Wedding', 'Bachelorette Party', 'Baby Shower']
verbPast = ['Discovered', 'Did', 'Accomplished', 'Exposed', 'Revealed', 'Unmasked', 'Uncovered', 'Announced', 'Insists', 'Believes']
verbIng = ['Pooping', 'Vaping', 'Making A Phone Call', 'Taking A Nap', 'Going to Church', 'Partying', 'Getting Healthy', 'Getting Your Ultimate Beach Body', 'Getting a Job', 'Shopping at Target', 'Buying Dog Food', 'Getting a Vasectomy', 'Healing the Ocean', 'Slowing Global Warming', 'Getting a Haircut', 'Eating Sushi', 'Buying Cryptocurrency', 'Improving Your Credit', 'Identifying a Narcissist', 'Quitting Your Job', 'Diagnosing Autism']
verbNiceThingToDo = ['Call Their Congressman', 'Quit Smoking', 'Hug Your Kids', 'Buy Your Mom Flowers', 'Go to Church', 'Donate to Charity', 'Buy the Next Round', 'Share Your Weed', 'Get Saved', 'Pet Your Dog', 'Spoil Your Lover', 'Going to the Gym']
attentionGetter = ['Breaking:', 'Attention:', 'Urgent:', 'Call Your Congressman:', 'Hey You:', 'Listen Up:', "It's Time to Talk About It:"]
reaction = ['Make You Cry', 'Shock You', 'Floor You', 'Leave You Speechless', 'Take Your Breath Away', 'Make You Sick', 'Outrage You', 'Wake You Up', 'Have You Scratching Your Head', 'Leave You Furious']
number = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', '10','12', '13', '15', '20', '25', '30']
organization = ['Church', 'School', 'College', 'Town', 'Company', 'Community', 'Nonprofit', 'Country', 'Couple', 'Group of Moms', 'Women\'s Book Club', 'Group of Friends', 'Sorority', 'Fraternity', 'Prison', 'Inner-City Gang', 'Suburban Neighborhood']
item = ['Sparkling Water', 'Razors', 'Toothbrushes', 'Jeggings', 'Record Players', 'Stand-Up Desks', 'Knapsacks', 'Fedoras', 'Sensory Deprivation Tanks', 'Socks', 'Tide Pods', 'Fidget Spinners', 'Popsockets', 'Organic Cotton Tees', 'Reusable Tampons', 'Diva Cups', 'Bras', 'Boxers', 'USB Dongles']

#Sentence Structures

def PickSentence():
	structure = r.randint(1, 10)
	#structure = 10
	if structure == 1:
		result = r.choice(attentionGetter) + ' ' + r.choice(nounPersonLive) + ' Just Told This ' + r.choice(nounTypeOfPerson) + ' To ' + r.choice(verbNiceThingToDo) + ' Because Of ' + r.choice(badThing)
		print(result)
	elif structure == 2:
		result = 'Was The ' + r.choice(event) + ' Of ' + r.choice(nounPersonDead) + ' Actually ' + r.choice(badAdjectives) + '? What ' + r.choice(nounPersonLive) + ' Thinks Will ' + r.choice(reaction)
		print(result)
	elif structure == 3:
		result = 'What This ' + r.choice(nounTypeOfPerson) + ' ' + r.choice(verbPast) + ' Will ' + r.choice(reaction)
		print(result)
	elif structure == 4:
		result = r.choice(number) + ' ' + r.choice(genericObject) + ' ' + r.choice(nounTypeOfPerson) + 's Don\'t Want You To Know About ' + r.choice(badThing)
		print(result)
	elif structure == 5:
		result = 'Some Will Call It ' + r.choice(goodThing) + '. ' + r.choice(nounPersonLive) + ' Simply Calls It ' + r.choice(verbIng) + '.'
		print(result)
	elif structure == 6:
		result = 'Is This The ' + r.choice(startupTech) + ' For ' + r.choice(verbIng) + '? What ' + r.choice(nounPersonLive) + ' Is Up To Will ' + r.choice(reaction) 
		print(result)
	elif structure == 7:
		result = r.choice(nounTypeOfPerson) + 's Hate This: ' + r.choice(number) + ' ' + r.choice(genericObject) + ' One ' + r.choice(nounTypeOfPerson) + ' Discovered About ' + r.choice(verbIng)
		print(result)
	elif structure == 8:
		result = 'Myth Buster: A ' + r.choice(nounTypeOfPerson) + ' Sets The Record Straight On ' + r.choice(badThing)
		print(result)
	elif structure == 9:
		result = 'This ' + r.choice(organization) + ' Wanted to Make a Point About ' + r.choice(badThing) + '. They Succeeded.'
		print(result)
	elif structure == 10:
		result = 'This Startup is Selling ' + r.choice(item) + ' by Celebrating ' + r.choice(goodIdeal)
		print(result)

	#for adding new sentences
	#elif structure == [number]:
	#	result = 
	#	print(result)
PickSentence()