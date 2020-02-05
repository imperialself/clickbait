import random as r
import requests
import json
import urllib.request
import urllib.parse
from config import *


#A bunch of lists containing parts of speech go here
nounPersonLive = ['The President', 'Donald Trump', 'Tom Cruise', 'Alex Noble', 'Barack Obama', 'Hillary Clinton', 'Ellen DeGeneres', 'Kesha', 'Regis Philbin', 'Tina Fey', 'Your Mom', 'Your Girlfriend', 'Your Grandma', 'Antonio Banderas', 'Penelope Cruz', 'R Kelly', 'Snoop Dogg', 'Kanye', 'Britney Spears', 'Kim Kardashian', 'George W. Bush', 'Arnold Schwarzenegger', 'Bob Saget', 'Oprah', 'Steve Martin', 'Steven Spielberg', 'Lady Gaga', 'Katy Perry', 'Bono', 'Justin Timberlake', 'George Clooney', 'Your Great Aunt Irma', 'Uncle Ted', 'Al Gore']
nounPersonDead = ['Hitler', 'Abraham Lincoln', 'Karl Marx', "Kierkegaard", 'Winston Churchill', 'Margaret Thatcher', 'Neil Armstrong', 'Stalin', 'Charles Darwin', 'Jane Austen', 'Charlotte Bronte', 'Edgar Allen Poe', 'Ernest Hemingway', 'Anthony Bourdain', 'George Washington', 'Thomas Jefferson', 'Francisco Franco', 'Princess Diana', 'Bob Ross']
nounTypeOfPerson = ['Walmart Employee', 'Cancer Survivor', 'Democrat', 'Decorated Veteran', 'Fundamentalist', 'Taxpayer', 'Police Officer', 'SNL Castmember', 'Disneyland Employee', 'Fitness Instructor', 'Child Actor', 'School Teacher', 'Tesla Driver', 'Cat Owner', 'Communist', 'Wedding DJ', 'Plumber', 'NASCAR fan', 'Suburban Mom', 'Homeowner', 'Millennial', 'Baby Boomer', 'Narcissist', 'Therapist', 'Chef', 'Youtuber', 'Blogger', 'Sex Worker', 'Immigrant', 'Expert', 'Researcher', 'Scientist']
goodThing = ['Winning The Lottery', 'Running A Marathon', 'Eating A Piece Of Pie', 'Calling Your Mother', 'Watching A Movie', 'Falling in Love', 'Getting Married', 'Having a Baby', 'Finding True Love', 'Getting Ripped', 'Finding a Kindred Spirit', 'Coming Home']
goodIdeal = ['Peace, Love, Respect and Unity', 'Body Positivity', 'Diversity', 'Women in Tech', 'Microfinancing', 'Paying it Forward', 'Mentorship', 'LGBTQ Pride', 'Sex Positivity', 'Open Borders', 'Sustainability', 'Free Love', 'Veganism', 'Civility', 'Transparency', 'Great Customer Support', 'Inclusion', 'Gun Control', 'Capitalism', 'Humane Euthanasia', 'Responsible Vaccination', 'Conservationism']
badAdjectives = ['Fake News', 'Staged', 'Overblown', 'a Big Sham', 'Trumped-Up', 'a Flop', 'a Let-Down', 'Illegal', 'Genetically Modified']
badThing = ['The Bees Dying', 'Genocide', 'Drone Strikes', 'The Holocaust', 'Global Warming', 'The Zombie Apocalypse', 'Economic Collapse', 'Trump', 'the Death of Free Speech', 'Russian Hackers', 'Election Meddling', 'Foreign Tax Shelters', 'the Gay Agenda', 'Abortion Clinic Bombings', 'the Westboro Baptist Church', 'Immigration Policy', 'Abortion', 'Voter Fraud', 'Alcoholism', 'the Refugee Crisis', 'Capitalism', 'the Trail of Tears', 'Vaccines', 'Euthanasia', 'Circumcision', 'Hurting Turtles']
startupTech = ['Bitcoin', 'Uber', 'TechCrunch', 'YCombinator', 'AirBnb', 'Alexa', 'Google Home', 'Google Maps', 'Facebook', 'Instagram', 'Slack', 'OKCupid', 'Tinder', 'Grindr', 'Yelp', 'UberEats', 'Google Docs', 'Microsoft Outlook', 'Microsoft Word', 'Bit.ly', 'GitHub', 'Amazon', 'Siri', 'Pinterest', 'Reddit', 'AI']
genericObject = ['Things', 'Tricks', 'Tips', 'Secrets', 'Little-Known Facts', 'Shocking Truths']
eventThing = ['Coronation', 'High School Prom', 'Graduation Ceremony', 'Election', 'Assassination', 'Arrest', 'Indictment', 'Wedding', 'Bachelorette Party', 'Baby Shower', 'Circumcision']
verbPast = ['Discovered', 'Did', 'Exposed', 'Revealed', 'Unmasked', 'Uncovered', 'Announced', 'Insists', 'Believes']
verbIng = ['Pooping', 'Vaping', 'Making A Phone Call', 'Taking A Nap', 'Going to Church', 'Partying', 'Getting Healthy', 'Getting Your Ultimate Beach Body', 'Getting a Job', 'Shopping at Target', 'Buying Dog Food', 'Getting a Vasectomy', 'Slowing Global Warming', 'Getting a Haircut', 'Eating Sushi', 'Buying Cryptocurrency', 'Improving Your Credit', 'Quitting Your Job', 'Diagnosing Autism', 'Moving to Silicon Valley', 'Moving Away from Silicon Valley', 'Retiring Early', 'Overeating', 'Getting Wasted', 'Pumping Iron', 'Going to the Emergency Room', 'Being Hit by Lightning', 'Stepping in Dog Poo', 'Playing Scrabble', 'Volunteering']
verbNiceThingToDo = ['Call Their Congressman', 'Quit Smoking', 'Hug Your Kids', 'Buy Your Mom Flowers', 'Go to Church', 'Donate to Charity', 'Buy the Next Round', 'Share Your Weed', 'Get Saved', 'Pet Your Dog', 'Spoil Your Lover', 'Go to the Gym', 'Get Circumcised', 'Save Thousands of Lives', 'Heal the Ocean',]
attentionGetter = ['Breaking:', 'Attention:', 'Urgent:', 'Call Your Congressman:', 'Hey You:', 'Listen Up:', "It's Time to Talk About It:"]
reaction = ['Make You Cry', 'Shock You', 'Floor You', 'Leave You Speechless', 'Take Your Breath Away', 'Make You Sick', 'Outrage You', 'Wake You Up', 'Have You Scratching Your Head', 'Leave You Furious', 'Gross You Out', 'Have You Jumping For Joy', 'Get You Excited', 'Get You Mad', 'Make You Fall in Love', 'Make You Laugh', 'Give You a Heart Attack', 'Punch You in the Gut', 'Get You Pumped', 'Leave You Wanting More']
number = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', '10','12', '13', '15', '20', '25', '30']
organization = ['Church', 'School', 'College', 'Town', 'Company', 'Community', 'Nonprofit', 'Country', 'Couple', 'Group of Moms', 'Women\'s Book Club', 'Group of Friends', 'Sorority', 'Fraternity', 'Prison', 'Inner-City Gang', 'Suburban Neighborhood']
item = ['Sparkling Water', 'Razors', 'Toothbrushes', 'Jeggings', 'Record Players', 'Stand-Up Desks', 'Knapsacks', 'Fedoras', 'Sensory Deprivation Tanks', 'Socks', 'Tide Pods', 'Fidget Spinners', 'Popsockets', 'Organic Cotton Tees', 'Reusable Tampons', 'Diva Cups', 'Bras', 'Boxers', 'USB Dongles', 'Rawhide Chews', 'Band-aids', 'Toe Separators', 'Orthotics', 'Purse Candy', 'Edibles', 'Succulents', 'Furbies', 'Beanie Babies', 'Deodorant', 'Antibiotics']
year = ['1920', '1935', '1947', '1952', '1968', '1971', '1978', '1983', '1990', '1997', '2001', '2005', '2016']
state = ['California', 'Florida', 'Alabama', 'Texas', 'Minnesota', 'Oklahoma', 'Louisiana', 'Kentucky']
characteristic = ['With No Life Insurance', 'Who Owe More Than 200,000', 'With Student Debt', 'With an Arrest Record', 'With Kids', 'Who Own a Home', 'Who Want to Pay Off Debt', 'Who Need Cosmetic Surgery', 'Who Value Liberty', 'Who Own Pets', 'With More Than One Car']
floridaMan = ['Alligator', 'Bath Salts', 'Meth', 'Riding Mower', 'PCP', 'Grizzly Bear', 'Half A Bushel Of Eggplant']

def ImageGetter(searchTerm):
    searchTermEncoded = urllib.parse.quote_plus(searchTerm)
    print(apiKey)
    imageSearch = "https://www.googleapis.com/customsearch/v1?q=" + searchTermEncoded + "&cx=014352846413195953642%3Aa2jzsrhjiqo&fileType=jpg&imgType=news&num=1&searchType=image&key=" + apiKey
    contents = urllib.request.urlopen(imageSearch).read()
    results = json.loads(contents)
    url = results
    print(url)


#Sentence Structures

def PickSentence():
    structure = r.randint(1, 15)
    #structure = 11
    if structure == 1:
        name123 = r.choice(nounPersonLive)
        result = r.choice(attentionGetter) + ' ' + name123 + ' Just Told This ' + r.choice(nounTypeOfPerson) + ' To ' + r.choice(verbNiceThingToDo) + ' Because Of ' + r.choice(badThing)
    elif structure == 2:
        result = 'Was The ' + r.choice(eventThing) + ' Of ' + r.choice(nounPersonDead) + ' Actually ' + r.choice(badAdjectives) + '? What ' + r.choice(nounPersonLive) + ' Thinks Will ' + r.choice(reaction)
    elif structure == 3:
        result = 'What This ' + r.choice(nounTypeOfPerson) + ' ' + r.choice(verbPast) + ' About ' + r.choice(item) + ' Will ' + r.choice(reaction)
    elif structure == 4:
        result = r.choice(number) + ' ' + r.choice(genericObject) + ' ' + r.choice(nounTypeOfPerson) + 's Don\'t Want You To Know About ' + r.choice(badThing)
    elif structure == 5:
        result = 'Some Will Call It ' + r.choice(goodThing) + '. ' + r.choice(nounPersonLive) + ' Simply Calls It ' + r.choice(verbIng) + '.'
    elif structure == 6:
        result = 'Is This The ' + r.choice(startupTech) + ' For ' + r.choice(verbIng) + '? What ' + r.choice(nounPersonLive) + ' Is Up To Will ' + r.choice(reaction) 
    elif structure == 7:
        result = r.choice(nounTypeOfPerson) + 's Hate This: ' + r.choice(number) + ' ' + r.choice(genericObject) + ' One ' + r.choice(nounTypeOfPerson) + ' Discovered About ' + r.choice(verbIng)
    elif structure == 8:
        result = 'Myth Buster: A ' + r.choice(nounTypeOfPerson) + ' Sets The Record Straight On ' + r.choice(badThing)
    elif structure == 9:
        result = 'This ' + r.choice(organization) + ' Wanted to Make a Point About ' + r.choice(badThing) + '. They Succeeded.'
    elif structure == 10:
        result = 'This Startup is Selling ' + r.choice(item) + ' by Celebrating ' + r.choice(goodIdeal)
    elif structure == 11:
        result = r.choice(state) + ' Residents Born Between ' + r.choice(year) + ' and ' + r.choice(year) + ' ' + r.choice(characteristic) + ' Must Read This. '
    elif structure == 12:
        result = r.choice(number) + ' ' + r.choice(genericObject) + ' About ' + r.choice(item) + ' That Will ' + r.choice(reaction)
    elif structure == 13:
        result = 'Why ' + r.choice(item) + ' Are Pretty Much the Worst, and What ' + r.choice(nounTypeOfPerson) + 's Are Doing About It'
    elif structure == 14:
        result = 'This ' + r.choice(nounTypeOfPerson) + ' is Taking on ' + r.choice(badThing) + ' Using ' + r.choice(goodIdeal) + ' And ' + r.choice(item) + '.'
    elif structure == 15:
        result = r.choice(nounTypeOfPerson) + 's Explain Why We\'re Seeing a Dramatic Increase in ' + r.choice(verbIng)
    elif structure == 16:
        flVerb = r.choice(verbPast)
        while (flVerb == 'Did' or flVerb == 'Unmasked'):
            flVerb = r.choice(verbPast)
        result = 'Florida Man ' + flVerb + ' ' + r.choice(verbIng) + ' With ' + r.choice(floridaMan) + ' Is The Key To ' + r.choice(goodIdeal) + ': His Reason Will ' + r.choice(reaction) 
    print(result)
    #ImageGetter(name123)



    #for adding new sentences
    #elif structure == [number]:
    #	result = 

PickSentence()
