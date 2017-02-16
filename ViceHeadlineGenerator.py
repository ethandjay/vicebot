import random, os
from OAuthSettings import settings    #import authorization settings
import sys
import twitter
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
	ans = ans[0].upper() + ans[1:]
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

	print "Iterating through stored tweet IDs and deleting corresponding tweets\n"
	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(__location__, 'TweetIDs.txt'), 'r') as file:
		for line in file.readlines():
			try:
				api.DestroyStatus(int(line))
			except:
				print "No tweet corresponds to this ID, moving on"

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
	'We sent $first_name $last_name to $action $vip1 in $place',
	'We sent $first_name $last_name to $action $vip1 in $place',
	'We sent $first_name $last_name to $place to $action $vip1',
	'We sent $first_name $last_name to $place to $action $vip1',
	'We sent $first_name $last_name to $place to $action $vip1',
	'$first_name $last_name took a trip to $place to $action $vip1',
	'We sent $first_name $last_name to $action $vip1 in $place',
	'$first_name $last_name set out to $place to $action $vip1',
	'$first_name $last_name travelled to $place to $action $vip1',
	'$first_name $last_name travelled to $place to study the conflict between $vip1 and $vip2',
	'$vip1 and $vip2 have been in conflict for years. We sent $first_name $last_name to $place to find out why',
	'$place has been in turmoil for years. We sent $first_name $last_name to the source to $action_list $vip1',
	'Why is $place so dangerous? $first_name $last_name reports in',
	'Why is it so hard to $action $vip1? $first_name $last_name uncovers the truth',
	'We wanted to know more about the lore surrounding $place, so we sent $first_name $last_name to report in',
	'Why is $place so closely tied to $vip1? We uncovered the reason',
	'$first_name $last_name, a native of $place, returns home to $action $vip1',
	'$vip1 travels to $place to $action $vip2 every week. Why?',
	'I went to $place with $first_name $last_name, who hates $vip1',
	'Inside $place, home of $vip1 and $vip2',
	str(random.randrange(2, 15)) + ' questions we have for $vip1',
	str(random.randrange(2, 15)) + ' questions we have for $vip1',
	str(random.randrange(2, 15)) + ' questions we have for $vip1',
	'$vip1 requested $vip2 $action our own $first_name $last_name. We didn\'t refuse',
	'Some photos of $vip1 in $place',
	'If $vip1 ran $place',
	'I tried to $action $vip1',
	'Did $vip1 just declare war on $vip2?',
	'Everything that happened in the first year after we asked $vip1 to $action $vip2',
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
	'Norm',
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
	'Jianna',
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
	'Lincoln',
	'Fogarty',
	'Shapiro',
	'West',
	'Gringots',
	'Tripth',
	'Godfrey',
	'Footman',
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
	'Hitler (no relation)',
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
	'the Messier 92 stellar cluster',
	'the 2007 World Cup of Pool in Rotterdam, Netherlands',
	'a hole',
	'the underground French rave scene',
	'a Jacuzzi in the Sicilian hills',
	'the underground Slovakian fishing scene',
	'the underground Scottish knitting scene',
	'the Garden of Eden',
	'the Taj Mahal',
	'a slightly less gentrified area of Cherokee St., St. Louis',
	'Joseph Kony\'s summer home',
	'Aleppo',
	'the slums of Cape Town',
	'the lower ionosphere',
	'Section 2 of CSE131: Introduction to Computer Science',
	'Compton',
	'the Catacombs of the Vatican',
	'Sauer St. in Houston',
	'Anchorage, Alaska',
	'the Witches Hut in the Black Forest',
	'the borean tundra',
	'the Navajo plains',
	'the Blackfoot Reservation',
	'a Lady Boy Strip-club in Southeast Bangkok',
	'the orgy clubs of 1960\'s Moscow',
	'a sauerkraut cafe in Warsaw\'s Zoliborz Ghetto',
	'Medellin, Columbia\'s most exclusive cartel hideout',
	'Sarah Lawrence\'s Annual Coffee & Cloitus Student Faculty meeting',
	'a Bicycle Smoothie Shop in North Portland',
	'Bill Belichick\'s Cape Cod summer house patio',
	'Mobile, Alabama\'s Oldest KKK-sponsored Church',
	'a Theravada Buddhist Temple in Cheyenne, Montana',
	'Prague\'s premier underground absinthe bar',
	'the backseat of a Toyota Tundra in an Isis Camp in Raqua, Syria',
	'Mussolini\'s fetish dungeon in Italian wine country',
	'Manilla, Philippines at a Lady Boy auction',
	'Oslo, Norway at a Nobel Price Pregame',
	'an Albanian "Supreme" Sweatshop',
	'the "Furry Hamster IPA" brewery in San Francisco',
	'a protest concering Walmart\'s inaugural superstore in Brooklyn',
	'an eskimo rehab center in Carrot River, Saskatchewan',
	'the second-cleanest oxygen bar in Machala, Ecuador',
	'1995 Kiev at the city\'s grand opening of a Kentucky Fried Chicken',
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
	'a massive labyrinth under the North Dakota State Capitol',
	'God\'s larynx',
	'the black market for nondeterministic finite automata',
	'a meme factory buried under the foothills of North Carolina',
	'an abandoned uranium mine in the region of the former Adal Sultanate',
	'James Buchanan\'s childhood home in Mercersberg, Pennsylvania',
	'Ruth Bader Ginsberg\'s sensory deprivation chamber',
	'an isolation tank in Aspen, Colorado',
	'Bernie Sanders\' campaign headquarters',
	'Tony Robbins\' self worship chapel',
	'a Sigma Chi "Snowglobe" Party',
	'a suspiciously sanitary Venice Beach fish taco stand',
	'a Western Union call reception center in Mumbai, India',
	'Buzzfeed\'s BDSM dungeon',
	'DraftKings\' headquarters in Mordor',
	'a Neutral Milk Hotel Concert in Seattle',
	'Moscow\'s Red Square Mayday Parade',
	'Boko Haram\'s Annual Poker and Pizza Party in Chad',

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
	'talk with',
	'talk with',
	'talk with',
	'talk with',
	'interview',
	'interview',
	'interview',
	'interview',
	'consult with',
	'consult with',
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
	'Brandon Wardell',
	'Jan Michael Vincent',
	'a disgusting mess of a man',
	'XXXTentacion',
	'Bilbo Baggins\'s handservant',
	'three members of Amon Duul II',
	'Pepe the Frog',
	'Black Hat from XKCD',
	'the Sublime Society of Beefsteak',
	'the Soulseek bird',
	'Qin Shi Huang',
	'Jack Kevorkian',
	'Che Guevera',
	'Carl Sagan',
	'Neil DeGrasse Tyson',
	'Milton Friedman',
	'your mom',
	'Gary Johnson',
	'a sentient hashtable',
	'Saidash Mongush',
	'Eric Andre\'s foreskin',
	'Vegan Sicarios',
	'the ghost of Leonard Cohen (may he rest in peace)',
	'Scott Walker, the music one',
	'Michael Gira\'s pet iguana, Pain',
	'Pope John Paul II',
	'Pope Innocent III',
	'Pope Francis',
	'Emperor Nero',
	'"Popeye" Vasquez',
	'Lee Harvey Oswald\'s Aunt',
	'Martin Shkreli' ,
	'Colonel Sanders',
	'Somalian Pirates',
	'Tom Cruise',
	'Bordertown Coyotes',
	'Iranian Kidney Donors',
	'Al Gore, the inventor of the Internet',
	'the existential concept of Peter Griffin',
	'Wendy (the fast food one, not the Peter Pan one)',
	'a used condom',
	'gangrenous flesh',
	'Michinomiya Hirohito',
	'Terracotta Warriors',
	'British Necromancers',
	'East Indian Shamans',
	'Lynard Skynard\'s personal pilot',
	'Pablo Escobar\'s great grandmother',
	'Canadian ultranationalists',
	'bodyart suspension gurus',
	'Lizards and Wizards',
	'a vegan, transgender, pansexual Catholic Nun',
	'the Witoto Tribe of Northern Peru',
	'Keanu Reeves',
	'alt-right anime twitter avatars',
	'Richard Spencer\'s one black friend',
	'Reese Witherspoon\'s chin',
	'Martin Scorsese',
	'the Black Hand Revivalist Gang',
	'Tulsa\'s Kitchenware turned cocaine distributors',
	'a South Korean Professional Starcraft Team',
	'Bernie bros',
	'Bill Clinton\'s Wife',
	'People for the Ethical Treatment of Animals',
	'Jimmy McMillin',
	'Mike Huckabee',
	'the ghost of Steve Jobs',
	'Larry the Cable Guy',
	'the Ghost of Princess Diana',
	'pre-conversion Saint Paul',
	'3/8\'s of the Hapsburg Royal Family',
	'Orlando\'s Aryan Brotherhood chapter',
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
	'Angela Merkel\'s harem of underage Syrian refugees',
	'several Crips from Greenwich, Connecticut',
	'Ron Jeremy',
	'Mahatma Gahndi\'s thread dealer',
	'Taipei\'s Second Oldest Youth for Reunification and Gentrification Club',
	'Robert Oppenheimer',
	'Nikola Tesla\'s favorite pigeon',
	'prominent Atheist Richard Dawkins',
	'the Amish',
	'Anderson Cooper\'s string of ex-lovers',
	'1/10 of the McCoy Family',
	'courteous lumberjacks',
	'the only survivors of the 1990\'s "visors as casual headwater" movement',
	'cross-dressing fringe hipsters',
	'Floyd Mayweather\'s translator',
	'homophobic sports mascots',
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
	'Japanese dog masseuses',
	'Lebanese noise-punks',
	'the Swiss Alps\'s least likely cryptologists',
	'Berlin\'s oldest Anarchists',
	'Siberian conjoined twins',
	'Rastafarian scrapbookers',
	'rainforest foothippies',
	'United Steelworkers Union members',
	'Macedonian card sharks',
	'members of the Italian Food Mob',
	'Columbus State Community College dropouts',
	'The Illuminati',
	'a Jordanian Uber driver',
	'a hip-hop producer turned undercover Jehovah\'s witness',
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
	'a Pennsylvanian death squad',
	'the curator of Mike Pence\'s extensive hentai collection',
	'John Boehner\'s skin care specialist',
	'death',
	'Ivan the Terrible',
	'Dijkstra\'s Shortest Path Algorithm',
	'Dave',
	'Sean Spicer',
	'the proletariat',
	'the price of a gallon of crude oil',
	'a washed-up Hoodie Allen',
	'Breakdancing Cop',
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