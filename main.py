import json
import os
import time

print('''					***	MINECRAFT STORYMODE	***

Welcome player to a version of minecraft storymode runnable entirely in replit

This is not complete, but once it is it will include saving, loading, every chapter,
and slightly branching paths, although generally no matter what you do the outcome 
stays the same...

*I do not own minecraft storymode nor am I affilliated with Telltale games*\n\n''')
time.sleep(3.0)

while True:
	saveorload = input("Would you like to load a game or start from the beginning? (load or start)	").lower()
	if saveorload == "start":
		episode = "1"
		part = "1 - 1"
		save = input("What do you want to name your save file (you have one chance to do this)?	")
		open(save+".json", "x")
		print("\nAlright, You adventure will start... NOW!")
		time.sleep(1.5)
		break
	elif saveorload == "load":
		print("Oops! This is still a work in progress, and since there's so little done right now loading is a little pointless right now!")
		continue

os. system('clear')
print('''Nothing built can last forever.

And every legend, no matter how great, fades with time, until all that remains are myths, half truths...to put it simply, lies.

And yet in all the known universe, from here to the Farlands, the legend of the Order of the Stone endures, unabridged, as self-evident fact.

Indeed, it is only a troubled land that is in need of heroes, and ours was fortunate enough to have heroes such as these:

Gabriel, The Warrior, before whose sword all combatants would tremble.

Ellegaard, the Redstone Engineer, whose creations would spark an era of invention.

Magnus, the Rogue, who would channel his destructive creativity for the benefit of all.

Soren, the Architect, Builder of Worlds, and leader of the Order of the Stone.

These FOUR friends would do anything to gain their rightful place as FOUR heroes. Their greatest quest would take them on a dangerous journey to fight the mysterious creature known as the Ender Dragon.

In the end, the Order of the Stone emerged victorious, and the dragon was defeated. Their story complete, they slipped away into the pages of legend...

But when one story ends, another one begins.''')
time.sleep(5.0)

while True:
	zombieorchicken = input("Your name is Jesse. You're in a treehouse that you and your only friends live in. As you're slashing at an armour stand practicing your sword fighting skills, your good friend Olivia looks up from her small redstone contraption to talk to you.\nOlivia: 'Would you rather fight one hundred chicken sized zombies (enter 1), or ten zombie-sized chickens (enter 2)?'	")
	if zombieorchicken == "1":
		zombiesizedchicken=0
		chickensizedzombie=1
	elif zombieorchicken == "2":
		zombiesizedchicken=1
		chickensizedzombie=0