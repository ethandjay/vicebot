import random, os
from OAuthSettings import settings    #import authorization settings
import twitter
import sys
from sys import exit


# Constructs tweet from parameters

def make_tweet(sentence, first_name, last_name, place, action, vip1, vip2):
	ans = sentence
	ans = ans.replace('$first_name', first_name)
	ans = ans.replace('$last_name', last_name)
	ans = ans.replace('$place', place)
	ans = ans.replace('$action', action)
	ans = ans.replace('$vip1', vip1)
	ans = ans.replace('$vip2', vip2)
	return ans

# Deletes all tweets with IDs taken from TweetIDs.txt, clears that file and then clears Tweets.txt

def DESTROY():
	consumer_key = settings['consumer_key']
	consumer_secret = settings['consumer_secret']
	access_token_key = settings['access_token_key']
	access_token_secret = settings['access_token_secret']

	try:
		api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)	
	except twitter.TwitterError:
		print api.message

	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(__location__, 'TweetIDs.txt'), 'r') as file:
		for line in file.readlines():
			try:
				api.DestroyStatus(int(line))
			except:
				print api.message

	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	open(os.path.join(__location__, 'TweetIDs.txt'), 'w')

	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	open(os.path.join(__location__, 'Tweets.txt'), 'w')

	print "All tweets wiped"
	exit()





# Sets API parameters from OAuthSettings (private)

consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']

# Check for special DESTROY argument that wipes all tweets from twitter / Tweets.txt / TweetIDs.txt

if (len(sys.argv) > 1 and sys.argv[1] == "DESTROY"):
	DESTROY();

	
sentence_list = [
	'$first_name $last_name travelled to $place to $action $vip1',
	'We sent $first_name $last_name to $action $vip1 in $place',
	'We sent $first_name $last_name to $place to $action $vip1',
	'We sent $first_name $last_name to $action $vip1 in $place',
	'We sent $first_name $last_name to $place to $action $vip1',
	'We sent $first_name $last_name to $action $vip1 in $place',
	'We sent $first_name $last_name to $place to $action $vip1',
	'$first_name $last_name took a trip to $place to $action $vip1',
	'We sent $first_name $last_name to $action $vip1 in $place',
	'$first_name $last_name set out to $place to $action $vip1',
	'$first_name $last_name travelled to $place to $action $vip1',
	'$first_name $last_name travelled to $place to study the conflict between $vip1 and $vip2',
	'$vip1 and $vip2 have been in conflict for years. We sent $first_name $last_name to $place to find out why',
	'$place had been in turmoil for years. We sent $first_name $last_name to the source to $action with $vip1',
	'Why is $place so dangerous? $first_name $last_name reports in',
	'Why is it so hard to $action $vip1? $first_name $last_name finds out why',
	'We wanted to know more about the lore surrounding $place, so we sent $first_name $last_name to report in',
	'Why is $place so closely tied to $vip1? We found out why',
	'$first_name $last_name, a native of $place, returns home to $action $vip1',
	'$vip1 travels to $place to $action $vip2 every week. Why?',
	'I went to $place with $first_name $last_name, who hates $vip1',
	'Inside $place\'s, home of $vip1 and $vip2',
	str(random.randrange(2, 10)) + ' questions we have for $vip1',
	str(random.randrange(2, 10)) + ' questions we have for $vip1',
	str(random.randrange(2, 10)) + ' questions we have for $vip1',
	'$vip1 wants $vip2 to $action our own $first_name $last_name. We didn\'t refuse',
	'Some photos of $vip1 in $place',
	'If $vip1 ran $place',
	'How $vip1 is waging war on $vip2',
	
]

first_name_list = [
	'Dr.',
	'Professor',
	'Ben',
	'David',
	'Josh',
	'Saul',
	'Eliach',
	'Audi',
	'Tanya',
	'Tanvi',
	'Sneha',
	'Ben',
	'Charles',
	'David',
	'Herman',
	'Isaac',
	'Raj',
	'Krish',
	'Sash',
	'Jacob',
	'Louis',
	'Maxwell',
	'Nathan',
	'Samuel',
	'Mort',
	'Arthur',
	'Normal',
	'Philip',
	'Walter',
	'Amit',
	'Meghan',
	'Rahul',
	'Rakesh',
	'Leah',
	'Anjali',
	'Sakshi',
	'Juvina',
	'Kwame',
	'Anna',
	'Maria',
	'Hirschel',
	'Marianna',
	'Sofia',
	'Pratik',
	'Malcom',
	'Eli',
	'Paulina',
	'Antonia',
	'Ester',
	'Ruth',
	'Barbara',
	'Hamilton',
	'Steven',
	'Franc',
	'Kristoff',
	'Brion',
	'Brittany',
	'Kile',
	'Brunden',
	'Scooter',
	'Sudeshna',
	'Anders',
	'Klaus',
	'Bran',
	'Pip',
	'Godfrey',
]

last_name_list = [
	'Schectmann',
	'Mirowitz',
	'Mendel',
	'Goldberg',
	'Hirschowitz',
	'Goodstein',
	'Goodman',
	'Rosenberg',
	'Freidman',
	'Epstein',
	'Cohen',
	'Lewin',
	'Chanda',
	'Dhar',
	'Dasgupta',
	'Gupta',
	'Caudhry',
	'Maghar',
	'Mann',
	'Andreotti',
	'Ludovico',
	'Briglioni',
	'Dimagio',
	'Kaplan',
	'Freidmann',
	'Schwartz',
	'Finkelstein',
	'Schneider',
	'Streisand',
	'Kohn',
	'Gordon',
	'Bernstein',
	'Lebowitz',
	'Hernandez',
	'Ramirez',
	'Conseco',
	'Shapiro',
	'West',
	'Gringots',
	'Tripth',
	'Godfrey',
	'Dangus',
	'Brunt',
	'Merkel',
	'Kasi',
	'Desu',
	'Parikh',
	'Wheaton',
	'Clarke',
	'Cytron',
	'Gill',
	'Armstrong',
	'Gonzalez',
	'Stalin (no relation)',
	'White',
	'Jackson',
	'Smith',
	'Martinez',
	'Sanchez',
	'Washington',
	'Ford',
	'Guildenstern',
	'Rosencrantz',

]

place_list = [
	'a hole',
	'underground French rave scene',
	'underground Slovakian fishing scene',
	'underground Scottish knitting scene',
	'the Garden of Eden',
	'the Taj Mahal',
	'a slightly less gentrified area of Cherokee St., St. Louis',
	'Joseph Kony\'s summer home',
	'Aleppo',
	'the slums of capetown',
	'lower ionosphere',
	'Section 2 of CSE131: Introduction to Computer Science',
	'Compton',
	'the Catacombs Vatican',
	'Sauer St. in Houston',
	'Anchorage, Alaska',
	'the Witches Hut in the Black Forest',
	'the Boorian Tundra',
	'Navaho Plains',
	'Blackfoot Reservation',
	'a Lady Boy Strip-club in Southeast Bangkok',
	'the orgy clubs of 1960\'s Moscow',
	'a sauerkraut cafe in Warsaw\'s Zoliborz Ghetto',
	'Medellin Columbia\'s most exclusive cartel hideout',
	'Sarah Lawrence\'s Annual Coffee & Cloitus Student Faculty meeting',
	'a Bicycle Smoothie Shop in North Portland',
	'Bill Belichick\'s Cape Code Summerhouse Patio',
	'Mobile, Alabama\'s Oldest KKK-sponsored Church',
	'a Theravada Buddhist Temple in Cheyenne, Montana',
	'Prague\'s Premier Underground Absinthe Bar',
	'the backseat of a Toyota Tundra in an Isis Camp in Raqua, Syria',
	'Mussolini\'s fetish dungeon in Italian Wine Country',
	'Manilla, Philippines at a Lady Boy auction',
	'Oslo, Norway at a Nobel Price Pregame',
	'an Albanian "Supreme" Sweatshop',
	'the "Furry Hamster IPA" brewery in San Francisco',
	'a protest concering Walmart\'s inaugural superstore in Brooklyn',
	'an eskimo rehab center in Carrot River, Saskatchewan',
	'the second-cleanest oxygen bar in Machala, Ecuador',
	'1995 Kiev at the city\'s grand opening of Kentucky Fried Chicken',
	'Martin Shkreli\'s Greek Bath House',
	'Gwyneth Paltrow\'s personal driver\'s basement',
	'the Ball Pit at Apple\'s Newest Headquarters in Astana, Kazakhstan',
	'the Northern Hemisphere',
	'a Do-It-Yourself Everest basecamp',
	'Liberty University\'s Draw Muhammad Contest',
	'a silent disco party in Buenos Aires',
	'the food truck feeding China\'s Boxer Rebellion',
	'Tripoli\'s Red Castle Museum',
	'a Coachella PortaPotty',
	'Narnia',
	'an RPG Dispensary in Cairo\'s Bulaq neighborhood',
	'the Deaf A Cappella World Championship',
	'Tokyo\'s most flamboyant drifting club\'s Trap House',
	'Planned Parenthood at the Summit of Mount Fuji',
	'the nation\'s most dangerous Chuck E Cheese in Camden, New Jersey',
	'the ADX Florence Maximum Security Prison',
	'Monsanto\'s underground greenhouse complex',
	'the cabin of a 73 foot yacht at 34.4238 degrees North, 118.5971 degrees West',
	'Barbara Steisand\'s dog\'s 3500 sq. foot penthouse',
	'Michael Jackson\'s coffin',
	'James Buchanan\'s childhood home in Mercersberg, Pennsylvania',
	'Ruth Bader Ginsberg\'s sensory deprivation chamber',
	'an isolation tank in Aspen Colorado',
	'Bernie Sanders\' campaign headquarters',
	'Tony Robbins\' self worship chapel',
	'a Sigma Chi "Snowglobe" Party',
	'a suspiciously sanitary Venice Beach fish taco stand',
	'a Western Union call reception center in Mumbai, India',
	'a Neutral Milk Hotel Concert in Seattle',
	'Moscow\'s Red Square Mayday Parade',
	'Boko Haram\'s Annual Poker and Pizza Party in Chad'
]

action_list = [
	'play Mahjong with',
	'play poker with',
	'play checkers with',
	'shoot Krokodil with',
	'speak to',
	'speak to',
	'speak to',
	'speak to',
	'smoke weed with',
	'chat with',
	'find out more about',
	'find out more about',
	'find out more about',
	'find out more about',
	'chill with',
	'talk politics with',
	'talk politics with',
	'talk politics with',
	'talk politics with',
	'talk politics with',
	'interview',
	'interview',
	'interview',
	'interview',
	'try experimental opiates with',
	'drop acid with',
	'learn the ancient traditions of',
	'learn the ancient traditions of',
	'learn the ancient traditions of',
	'try the traditional food of',
	'test the knowledge of',
	'explore the sacred culture of',
	'explore the sacred culture of',
	'explore the sacred culture of',
	
]

vip_list = [
	'XXXTentacion',
	'the Soulseek bird',
	'Qin Shi Huang',
	'Jack Kevorkian',
	'Che Guevera',
	'Carl Sagan',
	'Neil DeGrasse Tyson',
	'Milton Friedman'
	'your mom',
	'Gary Johnson'
	'a sentient hashtable',
	'Saidash Mongush',
	'Eric Andre\'s foreskin',
	'Vegan Sicarios',
	'the ghost of Leonard Cohen, may he rest in peace',
	'Scott Walker, the music one',
	'Michael Gira\'s pet iguana, Pain',
	'Pope Saint John Paul II',
	'Pope Innocent III',
	'Emperor Nero',
	'"Popeye" Vasquez',
	'Lee Harvey Oswald\'s Aunt',
	'Martin Shkreli' ,
	'Colonel Sanders',
	'Somalian Pirates',
	'Tom Cruise',
	'Bordertown Coyotes',
	'Iranian Kidney Donors',
	'Al Gore',
	'Michinomiya Hirohito',
	'Terracotta Warriors',
	'British Necromancers',
	'East Indian Shamans',
	'Lynard Skynard\'s Personal Pilot',
	'Pablo Escobar\'s Great Grandmother',
	'Canadian Ultranationalists',
	'Bodyart Suspension Gurus',
	'Lizards and Wizards',
	'a vegan, transgender, pansexual Catholic Nun',
	'the Witoto Tribe of Northern Peru',
	'Keanu Reeves',
	'Reese Witherspoon\'s chin',
	'Martin Scorsese',
	'the Black Hand Revivalist Gang',
	'Tulsa\'s Kitchenware turned cocaine distributors',
	'a South Korean Professional Starcraft Team',
	'Bernie bros',
	'Bill Clinton\'s Wife',
	'Jimmy McMillin',
	'Mike Huckabee',
	'The Ghost of Princess Diana',
	'pre-conversion Saint Paul',
	'3/8\'s of the Hapsburg Royal Family',
	'Orlando\'s Aryan Brotherhood Chapter',
	'Mike D of the Beastie Boys',
	'Ghostface Killah',
	'the Shanghai Center of Commerce Executive Board',
	'the New Branchwick Heroin Appreciation club',
	'a Yale Psychology Major turned Starbucks Barista',
	'William Wallace',
	'The Pixies',
	'Lil Ugly Mane\'s mom',
	'Iggy Pop of The Stooges',
	'The Gimp',
	'Thom Yorke\'s lazy eye',
	'Merzbow',
	'Kazumodo Endo',
	'The Gerogerigegege',
	'Coco the Gorrilla',
	'a MacArthur Genius Grant recipient',
	'Vladimir Putin\'s Horse',
	'Angela Merkel\'s harem of Underage Syrian Refugees',
	'Several Greenwich, Connecticut\'s Crips',
	'Ron Jeremy',
	'Mahatma Gahndi\'s thread dealer',
	'Taipei\'s Second Oldest Youth for Reunification and Gentrification Club',
	'Robert Oppenheimer',
	'Nikola Tesla\'s favorite pigeon',
	'prominent Atheist Richard Dawkins',
	'the Amish',
	'Anderson Cooper\'s String of Ex-Lovers',
	'1/10 of the McCoy Family',
	'courteous lumberjacks',
	'the only survivors of the 1990\'s "visors as casual headwater" movement',
	'cross-dressing fringe hipsters',
	'Floyd Mayweather\'s translator',
	'homophobic Nigerians',
	'that Nice Jewish Girl that your Grandma tries to set you up with',
	'Saint West\'s ex-butler',
	'Syrian Rebels',
	'an allegedly "really nice guy"',
	'the founder of Saudi Arabia\'s "Women Behind the Wheel" movement',
	'Arianna Huffington',
	'preteen Arctic Monkeys fans',
	'Jeopardy-winning computer, Watson',
	'Scandinavia\'s last vikings',
	'Ghengis Khan descendant John McDowel',
	'Australian base jumpers',
	'Father John Nasty, Orthodox priest turned prolific stripper',
	'AK-47-toting Blood Diamond children',
	'ironic highschoolers',
	'the Iowa/Nebraska/Missouri Tristate Corn Hole Team',
	'Appalachian coal miners',
	'the Milwaukee Police Department',
	'the Lads of Liverpool',
	'Bill Nye\'s opium dealer',
	'Air Bud and his now-middle aged owner',
	'an Orthodox Rabbi',
	'Kobayashi',
	'a non-ironic Nicolas Cage fan club',
	'the full lineup of Nickelback and an unassuming cocktail waitress',
	'Napa Valley yoga moms',
	'Godspeed You! Black Emperor fangirls',
	'Guamanian crust punks',
	'Japanese Dog Masuses',
	'Lebanese Noise Punks',
	'the Swiss Alps\' least likely cryptologists',
	'Berlin\'s oldest Anarchists',
	'Siberian conjoined twins',
	'Rastafarian scrapbookers',
	'rainforest foothippies',
	'United Steelworkers Union members',
	'Macedonian card sharks',
	'Italian Food Mob members',
	'Columbus State Community College dropouts',
	'The Illuminati',
	'a Jordanian Uber driver',
	'a Hip-Hop Producer turned undercover Jehova\'s witness',
	'New York\'s Wiccan construction workers',
	'Bangladeshi basket weavers',
	'Hong Kong Freemasons',
	'Indonesian curry smugglers',
	'Wayne Fromm, inventor of the selfie stick',
	'Venetian Anime Addicts Anonymous',
	'Chesley "Sully" Sullenberger',
	'Elon Musk\'s brother-in-law',
	'Johnny Mar',
	'"that asshole" Thomas Edison',
	'Fleet Foxes groupies',
	'J.D. Salinger',
	'Harper Lee\'s personal aid',
	'Danny Brown\'s orthodontist',
	'Moot, founder of 4Chan',
	'Donald Trump',
	'Mike Pence\'s extensive hentai collection',
	'John Boehner\'s skin care specialist',
	'death',
	'Ivan the Terrible',
	'Dave',
	'Sean Spicer',
	'the proletariat',
	'the price of a gallon of crude oil',
]


os.system('cls' if os.name=='nt' else 'clear')

#Randomly choose tweet elements

too_long = True

while (too_long == True):
	sentence = sentence_list[random.randrange(0, len(sentence_list))]
	first_name = first_name_list[random.randrange(0, len(first_name_list))]
	last_name = last_name_list[random.randrange(0, len(last_name_list))]
	place = place_list[random.randrange(0, len(place_list))]
	action = action_list[random.randrange(0, len(action_list))]
	vip1 = vip_list[random.randrange(0, len(vip_list))]
	vip2 = vip_list[random.randrange(0, len(vip_list))]

	tweet = make_tweet(sentence, first_name, last_name, place, action, vip1, vip2)

	if (len(tweet) <= 140):
		too_long = False
	else:
		print "Tweet too long, retrying...\n"


try:
	api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)	
	print '\n' + tweet + '\n'

	#LOCAL argument prints generated tweet but doesn't post it
	if (not (len(sys.argv) > 1 and sys.argv[1] == "LOCAL")):
		print 'posting to Twitter...'
		status = api.PostUpdate(tweet)
		print '  post successful!\n'
		tweet_id = status.id 

		# Adding tweets / tweet ID's to respective files

		__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		with open(os.path.join(__location__, 'Tweets.txt'), 'a') as file:
			file.write(tweet + '\n')

		__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		with open(os.path.join(__location__, 'TweetIDs.txt'), 'a') as file:
			file.write(str(tweet_id) + '\n')

except twitter.TwitterError:
	print api.message


exit()