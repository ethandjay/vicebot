import random, os
from OAuthSettings import settings    #import authorization settings
import twitter
import sys
from sys import exit


# Constructs tweet from parameters

def make_tweet(sentence, first_name, last_name, place, vip):
	ans = sentence
	ans = ans.replace('$first_name', first_name)
	ans = ans.replace('$last_name', last_name)
	ans = ans.replace('$place', place)
	ans = ans.replace('$vip', vip)
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
	'$first_name $last_name travelled to $place to speak to $vip',
	'We sent $first_name $last_name to smoke weed with $vip in $place',
	'We sent $first_name $last_name to $place to chat with $vip',
	'We sent $first_name $last_name to to chat with $vip in $place',
	'$first_name $last_name set out to $place to chat with $vip',
	'$first_name $last_name travelled to $place to chill with $vip',
]

first_name_list = [
	'Ben' ,
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
	'Steven'
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
	'Conseco'
]

place_list = [
	'The slums of capetown',
	'Compton',
	'the Catacombs Vatican',
	'Sauer St. in Houston',
	'Anchorage, Alaska',
	'The Witches Hut in the Black Forest',
	'Boorian Tundra',
	'Navaho Plains',
	'Blackfoot Reservation',
	'Quin Shi Huang ',
	'A Lady Boy Strip-club in Southeast Bangcock',
	'The orgy clubs of 1960\'s Moscow',
	'A sauerkraut cafe in Warsaw\'s Zoliborz Ghetto',
	'Medellin Columbia\'s Most Exclusive Cartel Hideout',
	'Sarah Lawrence\'s Annual Coffee & Coitus Student Faculty meeting',
	'A Bicycle Smoothie Shop in North Portland',
	'Bill Belichick\'s Cape Code Summerhouse Patio',
	'Mobile, Alabama\'s Oldest KKK Sponsored Church ',
	'A Theravada Budhist Temple in Cheyenne, Montana',
	'Prague\'s Premier Underground Absinthe Bar',
	'At the Backseat of a Toyota Tundra in an Isis Camp in Raqua, Syria',
	'Mussolini\'s Fetish Dungeon in Italian Wine Country',
	'Manilla, Philippines at a Lady Boy auction',
	'Oslo, Norway at a Nobel Price Pregame',
	'An Albanian "Supreme" Sweatshop',
	'The "Furry Hamster IPA" brewery in San Francisco',
	'A Protest Concerning Walmarts Inaugural Superstore in Brooklyn',
	'An eskimo rehab center in Carrot River, Saskatchewan',
	'The 2nd cleanest oxygen bar in Machala, Ecuador',
	'1995 Kiev at the city\'s grand opening of Kentucky Fried Chicken',
	'Martin Shkreli\'s Greek Bath House',
	'Gwyneth Paltrow\'s personal driver\'s basement',
	'The Ball Pit at Apple\'s Newest Headquarter in Astana, Kazakhstan',
	'The Northern Hemisphere',
	'A Do-It-Yourself Everest Base Camp',
	'Liberty University\'s Draw Muhammad Contest',
	'A Silent Disco Party in Buenos Aires',
	'China\'s Boxer Rebellion',
	'Tripoli\'s Red Castle Museum',
	'A Coachella PortalaPotty',
	'Narnia',
	'An RPG Dispensary in Cario\'s Bulaq Neighborhood',
	'The Deaf A Cappella World Championship',
	'Tokyo\'s Most Fictitious Drifting Club\'s Trap House',
	'Planned Parenthood at the Summit of Mount Fuji',
	'The Nation\'s most dangerous Chuck E Cheese in Camden, New Jersey',
	'The ADX Florence Maximum Security Prison',
	'Monsanto\'s underground greenhouse complex',
	'the cabin of a 73 foot yacht at 34.4238 degrees North, 118.5971 degrees West',
	'Barbara Steisand\'s Dog\'s 3500 sq. foot penthouse',
	'Michael Jackson\'s coffin',
	'James Buchanan\'s Childhood Home in Mercersberg, Pennsylvania',
	'Ruth Bader Ginsberg\'s Sensory Deprivation Room',
	'An Isolation Tank in Aspen Colorado',
	'Bernie Sanders Campaign headquarters',
	'Tony Robbins\' self worship chapel',
	'A Sigma Chi "Snowglobe" Party',
	'A Seemingly Sanitary Venice Beach Fish Taco Stand ',
	'A Western Union Call Reception Center in Mumbai, India',
	'Seattle at a Neutral Milk Hotel Concert',
	'Moscow\'s Red Square Mayday Parade',
	'Chad at Boko Haram\'s Anuual Poker and Pizza Party'
]

vip_list = [
	'Vegan Sicarios',
	'Pope Saint John Paul II',
	'Pope Innocent III',
	'Emperor Nero',
	'"Popeye" Vasquez',
	'Lee Harvey Oswald\'s Aunt',
	'Martin Shkreli\'s' ,
	'Colonel Sanders',
	'Somalian Pirates',
	'Tom Cruise',
	'Bordertown Coyotes',
	'Iranian Kidney Donors',
	'Al Gore',
	'Empire of the Sun',
	'Michinomiya Hirohito',
	'Terracotta Warriors',
	'British Necromancers',
	'East Indian Shamans',
	'Pablo Escobar\'s Great Grandmother',
	'Canadian Ultranationalists',
	'Bodyart Suspension Gurus',
	'Lizard People',
	'A Vegen, Transgendered, Pansexual Catholic Priest',
	'The Witoto Tribe of Northern Peru',
	'Keannu Reeves',
	'Reese Witherspoon\'s Chin',
	'Martin Scorsese',
	'The Black Hand Revivalist Gang',
	'Tulsa\'s Kitchenware turned cocaine distributors',
	'A South Korean Professional Starcraft Team',
	'Bernie bros',
	'Bill Clinton\'s Wife',
	'Mike Huckabee',
	'The Ghost of Princess Diana',
	'Preconversion Saint Paul',
	'3/8\'s of the Hapsburg Royal Family',
	'Orlando\'s Aryan Brotherhood Chapter',
	'Mike D of the Beastie Boys',
	'Ghostface Killah',
	'The Shanghai Center of Commerce Executive Board',
	'The New Branchwick Heroine Appreciation club',
	'A Yale Psychology Major turned Starbucks Barista',
	'William Wallace',
	'The Pixies',
	'Coco the Gorrilla',
	'MacArthur Genius Grant Recipient',
	'Vladimir Putin\'s Horse',
	'Angela Merkel\'s harem of Underage Syrian Refugees',
	'Several Greenwich, Connecticut\'s Crips',
	'Ron Jeremy',
	'Mahatma Gahndi\'s thread dealer',
	'Taipei\'s Youth for Reunification and Gentrification Club',
	'Robert Oppenheimer',
	'Nikola Tesla\'s favorite pigeon',
	'Prominent Atheist Richard Dawkins',
	'The Amish',
	'Anderson Cooper\'s String of Ex-Lovers',
	'1/10 of the McCoy Family',
	'Courteous Lumberjacks',
	'Survivors of the 1990\'s "visors as casual headwater" movement',
	'Cross Dressing Fringe Hipsters',
	'Floyd Mayweather\'s Translator',
	'Homophobic Nigerians',
	'That Nice Jewish Girl that your Grandma tries to set you up with',
	'Saint West\'s future butler',
	'Syrian Rebels',
	'An allegedly "really nice guy"',
	'The Founder of Saudi Arabia\'s Women Behind the Wheel Movement',
	'Arianna Huffington',
	'Preteen Arctic Monkeys Fans',
	'Jeopardy-winning Computer, Watson',
	'Scandinavia\'s last vikings',
	'Ghengis Khan descendant John McDowel',
	'Australian Base Jumpers',
	'Father John Nasty, Orthodox Priest turned Prolific Stripper',
	'AK-47 Toting Blood Diamond Children',
	'Ironic High Schoolers',
	'The Iowa/Nebraska/Missouri Tristate Corn Hole Team',
	'Appalachian Coal Miners',
	'The Milwaukee Police Department',
	'The Lads of Liverpool',
	'Bill Nye\'s Opium Dealer',
	'Air Bud and his now Middle Aged Owner',
	'An Orthodox Rabbi',
	'Kobayashi',
	'a non-ironic Nicolas Cage fan club',
	'Nickelback and an unassuming cocktail waitress',
	'Napa Valley Yoga Moms',
	'Japanese Dog Massuses',
	'Lebanese Noise Punks',
	'The Swiss Alp\'s least likely Cryptologists',
	'Berlin\'s Oldest Anarchists',
	'Siberian Conjoined Twins',
	'Rastafarian Scrapbookers',
	'Rainforest Gurus',
	'United Steelworkers Union Members',
	'Macedonian Card Sharks',
	'Italian Food Mob Members',
	'Columbus State Community College Dropouts',
	'The Illuminati',
	'A Joradanian Uber Driver',
	'An Hip Hop Producer turned Undercover Imagineer',
	'New York\'s Wikkan Construction Workers',
	'Bangladeshi Basket Weavers',
	'Hong Kong Freemasons',
	'Indonesian Curry Smugglers',
	'Wayne Fromm, Inventor of the selfie stick',
	'Venetian Anime Addicts',
	'Chesley "Sully" Sullenberger',
	'Elon Musk\'s Brother-in-law',
	'Johnny Mar',
	'"That Asshole" Thomas Edison',
	'Fleet Foxes Groupies',
	'J.D. Salinger',
	'Harper Lee\'s Personal Aid',
	'Danny Brown\'s Orthodontist',
	'Moot, Founder of 4 Chan'
]

os.system('cls' if os.name=='nt' else 'clear')

#Randomly choose tweet elements

too_long = True

while (too_long == True):
	sentence = sentence_list[random.randrange(0, len(sentence_list))]
	first_name = first_name_list[random.randrange(0, len(first_name_list))]
	last_name = last_name_list[random.randrange(0, len(last_name_list))]
	place = place_list[random.randrange(0, len(place_list))]
	vip = vip_list[random.randrange(0, len(vip_list))]

	tweet = make_tweet(sentence, first_name, last_name, place, vip)

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