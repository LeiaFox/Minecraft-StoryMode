import json
import os
import time

intro_speech = '''
Nothing built can last forever.

And every legend, no matter how great, fades with time, until all that remains are myths, half truths...to put it simply, lies.

And yet in all the known universe, from here to the Farlands, the legend of the Order of the Stone endures, unabridged, as self-evident fact.

Indeed, it is only a troubled land that is in need of heroes, and ours was fortunate enough to have heroes such as these:

Gabriel, The Warrior, before whose sword all combatants would tremble.

Ellegaard, the Redstone Engineer, whose creations would spark an era of invention.

Magnus, the Rogue, who would channel his destructive creativity for the benefit of all.

Soren, the Architect, Builder of Worlds, and leader of the Order of the Stone.

These FOUR friends would do anything to gain their rightful place as FOUR heroes. Their greatest quest would take them on a dangerous journey to fight the mysterious creature known as the Ender Dragon.

In the end, the Order of the Stone emerged victorious, and the dragon was defeated. Their story complete, they slipped away into the pages of legend...

But when one story ends, another one begins...\n\n'''



def chapter_1_part_1():
	os.system('clear')
	print(intro_speech)
	time.sleep(10.0)
	
	while True:
		zombieorchicken = input("Your name is Jesse. You're in a treehouse that you and your only friends live in. As you're slashing at an armour stand practicing your sword fighting skills, your good friend Olivia looks up from her small redstone contraption to talk to you.\nOlivia: 'Would you rather fight one hundred chicken sized zombies (enter 1), or ten zombie-sized chickens (enter 2)?'	")
		if zombieorchicken == "1":
			zombiesizedchicken={"zombiesizedchicken" : 0}
			chickensizedzombie={"chickensizedzombie" : 1}
			with open(save+".json", 'w') as f:
				json.dump(zombiesizedchicken, f)
				json.dump(chickensizedzombie, f)
			print("\n'100 zombie sized chickens. Figure it'd be easier.'")
			print("\nOlivia: 'Nice choice, I chose that one too, actually.'")
		elif zombieorchicken == "2":
			zombiesizedchicken={"zombiesizedchicken" : 1}
			chickensizedzombie={"chickensizedzombie" : 0}
			with open(save+".json", 'w') as f:
				json.dump(zombiesizedchicken, f)
				json.dump(chickensizedzombie, f)
			print("'10 zombie sized chickens. I ought to practice my skills on those tiny zombies!'")
			print("\nOlivia: 'Interesting choice, but I would've gone with the other one.'")
#CHAPTER 1 PART 1



#below is the first thing people see
print('''					***	MINECRAFT STORYMODE	***

Welcome player to a version of minecraft storymode runnable entirely in replit

This is not complete, but once it is it will include saving, loading, every chapter,
and slightly branching paths, although generally no matter what you do the outcome 
stays the same...

*I do not own minecraft storymode nor am I affilliated with Telltale games*\n\n''')
time.sleep(3.0)




while True:
	while True:
		saveorload = input("Would you like to load a game or start from the beginning? (load or start)	").lower()
		if saveorload == "start":
			break
		elif saveorload == "load":
			break
		else:
			continue
	if saveorload == "start":
		place = {}
		place["episode"] = {"episode" : 1}
		place["part"] = {"part" : 1}
		while True:
			save = input("\n\nWhat do you want to name your save file (if it already exists an error will show if you enter it here)?	")
			sure = input("\nAre you sure about this (y/n)?").lower()
			if sure == "y":
				open(save+".json", "x")
				with open(save+".json", 'w') as f:
					json.dump(place, f)
					#dumps chapters into newly made json file
				break
			elif sure == "n":
				print("Alright, I'll ask again\n\n")
				continue

		print("\nAlright, You adventure will start... NOW!")
		time.sleep(1.5)
		break
	elif saveorload == "load":
		print("Oops! This is still a work in progress, and since there's so little done right now loading is a little pointless right now!")
		while True:
			save = input("What was the name of your save file?	")
			sure = input("\nAre you sure about this (y/n)?").lower()

			if sure == "y":
				open(save+".json", "x")
				with open(save+".json", 'w') as f:
					f = open(save+".json")
					load = json.load(f)
				break
			elif sure == "n":
				print("Alright, I'll ask again\n\n")
				continue
		print("Alright, you'll start from where you left off, toodles!")
	break

f = open(save+".json")
load = json.load(f)
if load["episode"] == {"episode" : 1}:
	if load["part"] == {"part" : 1}:
		chapter_1_part_1()
