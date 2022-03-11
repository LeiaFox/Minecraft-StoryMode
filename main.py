import json
import os
import time
from tkinter import *
from tkinter import ttk
import termcolor
from termcolor import colored

olivia = colored("\nOlivia:","red")
olivia2 = colored("Olivia","red")
axel = colored("\nAxel:","green")

def load_game():
	
	global f
	global place
	global load
	f = open(save+".json")
	load = json.loads(f.read())
	if load["episode"] == 1:
		if load["part"] == 1:
			place = {}
			place["zombiesizedchicken"] = load["zombiesizedchicken"]
			place["chickensizedzombie"] = load["chickensizedzombie"]
			place["episode"] = 1
			place["part"] = 1
			with open(save+".json", 'w') as f:
				json.dump(place, f)
			chapter_1_part_1()
#places you at the part you were at, or at the start

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

But when one story ends, another one begins...\n\n\n\n
'''


def player_death(reason):

	print(f"{reason}. Better luck next time.")
	#prints reason for death
	while True:

		give_up = input("Do you give up? (y/n) ")
		if give_up == "y":
			print("Alright. Seeya")
			time.sleep(2.0)
			exit(0)
		elif give_up == "n":
			print("Nice, get back here.")
			time.sleep(2.0)
			load_game()



def chapter_1_part_1():
	
	os.system('clear')
	print(intro_speech)
	time.sleep(20.0)

	print("Chapter 1, Part 1\n")

	while True:
		print("Your name is Jesse. You're a treehouse that you and your only friends live in. It's made of oak and spruce wood, with red carpeting and spruce pillars in the corners. As you're slashing at an armour stand practicing your sword fighting skills, your good friend Olivia holds a small piece of redstone and peeks out the window.\n")
		time.sleep(8.0)
		zombieorchicken = input(f"{olivia} 'Would you rather fight a hundred chicken-sized zombies, or ten zombie-sized chickens? Just to be clear, you wouldn't have any weapons or armor. So you'd have to fight them with your hands.' \n\n[1: 'Huh?' 2: 'Chicken-sized zombies.' 3: 'Zombie-sized chickens.' 4: '...'] ")
		if zombieorchicken == "1":
			print("\n'Huh?'")
			time.sleep(4.0)
			print(olivia,"'Huh?' She mocks you acting like a zombie and hunching over.")
			time.sleep(4.0)
			print(olivia,"'It's just a dumb question. Forget it.'")
			break
		elif zombieorchicken == "2":
			place["zombiesizedchicken"]=0
			place["chickensizedzombie"]=1
			with open(save+".json", 'w') as f:
				json.dump(place, f)
			print("\n'That's easy. I'll take the little tiny... little zombies.'")
			time.sleep(4.0)
			print(olivia,"'A hundred of them... crawling all over you, with their tiny hands.' She sways her arms in front of herself and drones.")
			time.sleep(4.0)
			print("\n'All I'd need is, like, a shovel. I'm telling you, way too easy.'")
			break
		elif zombieorchicken == "3":
			place["zombiesizedchicken"]=1
			place["chickensizedzombie"]=0
			with open(save+".json", 'w') as f:
				json.dump(place, f)
			print("\n'I'd have to go with the giant chickens. Not because I want to or because I think it would be easy, but because they would be an abomination.'")
			time.sleep(4.0)
			print(olivia,"'Imagine their giant feet.'")
			time.sleep(4.0)
			print("\n'Like I said... an abomination.'")
			break
		elif zombieorchicken == "4":
			print("\n'...'")
			time.sleep(4.0)
			print(olivia,"'It's just a hypothetical question, Jesse.'")
			break
	time.sleep(4.0)
	print(olivia,"'Soo... I've got a daylight sensor on the roof...'")
	time.sleep(4.0)
	print("\n'Mmhm...'")
	time.sleep(4.0)
	print(olivia,"'And if I did this right, these lamps should turn on once it gets dark.'")
	time.sleep(4.0)
	print("\n'Mmm-Hmm...'")
	time.sleep(4.0)
	print(olivia,"'I didn't want to just leave Reuben here with nothing while we're at the building competition-'")
	time.sleep(4.0)
	print("\n'He's coming with us.' Your pet Reubon nudges his head into the armour stand.")
	time.sleep(4.0)
	print(olivia,"'Really?'")
	time.sleep(4.0)
	print("\n'What kind of question is that? Of course he is.' You say this as you stop practicing and put your wooden sword in your inventory.")
	time.sleep(4.0)
	print(olivia,"'Okay. I'm not saying he shouldn't come. I'm not... but don't you think it's a little weird that you take him with you everywhere you go?'")
	time.sleep(4.0)
	while True:
		reubenchoice = input(f"{olivia} 'He kind of makes us look like... I don't know... amateurs.' \n\n[1: 'Reuben's my best friend.' 2: 'People love pigs!' 3: 'It's not weird at all.' 4: '...'] ")
		if reubenchoice == "1":
			print("\n'Reuben's my best friend.'")
			time.sleep(4.0)
			print(olivia,"'I thought I was your best friend?'")
			time.sleep(4.0)
			print("\n'Both of you are.'")
			break
		elif reubenchoice == "2":
			print("\n'He's my wingman. People always wanna talk to the girl with the pig.'")
			time.sleep(4.0)
			print(olivia,"'You mean talk ABOUT the girl with the pig.'")
			time.sleep(4.0)
			print(olivia,"'Like, ''Look at the weird girl with the weird pig. How weird.'' ' Your smile forms into a stern look.")
			time.sleep(4.0)
			break
		elif reubenchoice == "3":
			print("\n'It's not weird at all.'")
			time.sleep(4.0)
			print("\n'Reuben is the best pet I could ask for. Obedient, loyal, and always happy to see me at the end of a long day.' Your pig glares at you from behind.")
			time.sleep(4.0)
			print("\n'Friend. I should have said ''friend,'' not pet.' Your friend nods smiles with valor.")
			break
		elif reubenchoice == "4":
			print("\n'...'")
			time.sleep(4.0)
			print(olivia,"'All right. I was just making a point.'")
			break
	time.sleep(4.0)
	print(olivia,"'I didn't mean anything by it. I'm glad he's coming.'")
	time.sleep(4.0)
	print(olivia,"'I just don't want to give people one more reason to call us ''losers.'' '")
	time.sleep(4.0)
	print(olivia,"'I'm getting tired of it.'")
	time.sleep(4.0)
	while True:
		losers = input(f"{olivia} 'I'm tired of being a laughing stock.' \n\n[1: 'Who cares what they think?' 2: 'Just embrace it.' 3: 'We aren't losers.' 4: '...'] ")
		if losers == "1":
			print("\n'Who cares what other people think?' *Olivia will remember that.*")
			time.sleep(4.0)
			print(f"{olivia} 'I know, I know. I'm just... it wears you down.' she slumps over")
			time.sleep(4.0)
			print("\n'You say you're not a loser, Olivia... so win.'")
			time.sleep(4.0)
			print(f"{olivia} 'Okay. Fine.' She grins.")
			break
		elif losers == "2":
			print("\n'Embrace being a loser, Olivia. And if you do that, you can be whatever you want to be.'")
			time.sleep(4.0)
			print(f"{olivia} 'What if I wanna be a winner?'")
			time.sleep(4.0)
			print("\n'Except that.' You let out an unsure giggle, 'Anything else though.'")
			time.sleep(4.0)
			print(f"\n{olivia2} laughs")
			time.sleep(4.0)
			print(f"{olivia} 'All right, fine.'")
			break
		elif losers == "3":
			time.sleep(4.0)
			print("\n'We are not loser, Olivia'")
			time.sleep(4.0)
			print(f"{olivia} 'We lose all the time. It's what we do.'")
			time.sleep(4.0)
			print("\n'Okay... Okay! That might be true...'")
			time.sleep(4.0)
			print(f"{olivia} 'I can't remember the last time we've won anything.'")
			time.sleep(4.0)
			print("\n'But if that's the case... it means we win at being losers.'")
			time.sleep(4.0)
			print(f"{olivia} '...All right, fine'")
			break
		elif losers == "4":
			print("\n'...''")
			time.sleep(4.0)
			print(f"{olivia} '...Real nice Jesse.'")
			time.sleep(4.0)
			print(f"{olivia} 'Glad I have a friend like you around.' She says this while unamused and blankly staring")
			break

	time.sleep(4.0)
	print("\n???: 'Ssssssss...'")
	time.sleep(4.0)
	print("\n'Do you hear that?' You walk over to the trapdoor on the floor which is also the exit.")
	time.sleep(4.0)
	print("\n???: 'Sssssssssssss...'")
	time.sleep(4.0)
	print(f"{olivia} 'Oh, no.' You kneel down about to open the trapdoor.")
	time.sleep(4.0)
	print("\n???: 'BOO'")
	time.sleep(4.0)
	print(f"\nYou and {olivia2}: 'AHHH!' Reuben falls over onto the floor out of fear.")
	time.sleep(4.0)
	print(f"{axel} 'Ha! I totally freaked all of you out! That was awso- Ow!' Reuben has just rammed into Axel's stomach.")
	time.sleep(4.0)
	print(f"{olivia} 'Axel! What's the matter with you?!'")
	time.sleep(4.0)
	print(f"{axel} 'Great, now I'm going to smell like a pig at Endercon.'")
	time.sleep(4.0)
	while True:
		axel_intro = input(f"{axel} 'I thought we were buddies!' He looks down at Reuben. \n\n[1: 'Cool mask.' 2: 'You had that coming.' 3: 'Not funny, Axel.' 4: '...'] *unfinished*")
		if axel_intro == "1":
			print("\n'Cool mask.'")
			time.sleep(4.0)
			print(f"{axel} 'It is, isn't it?' *Axel will remember that*")
			time.sleep(4.0)
			print("\n'Yeah, very convincing.' You put you hands on your hips and glare at Axel in a disaproving matter.")
			time.sleep(4.0)
			print(f"{axel} 'The look on your faces...' Axel laughs.")
			break
		elif axel_intro == "2":
			break
		elif axel_intro == "3":
			print("\n'That wasn't funny Axel!' You point at him dissaprovingly.")
			time.sleep(4.0)
			print(f"{axel} 'I brought you good times, and now I'm being punished for it? He waves his hands around in lashing anger. *Axel will remember that.*'")
			time.sleep(4.0)
			print(f"\n'You scared us half to death.' You lash out and throw your arms behind you to exaggerate your message.")
			break
		elif axel_intro == "4":
			break
	time.sleep(4.0)
	print(f"{olivia} 'Did you bring the fireworks?'")
	time.sleep(4.0)
	print(f"{axel} 'Of course I did. I even brought something for the little guy' Axel pulls out a pig-sized ender dragon costume, perfect for Reuben.")
	time.sleep(4.0)
	print("\n'Nice!'")
	time.sleep(4.0)
	print(f"{olivia} 'You brought Reuben a disguise?'")
	time.sleep(4.0)
	print(f"{axel} 'We're going to a convention. SOMEbody's gotta wear a costume.' Axel stuffs the costume onto Reuben, Reuben runs around in enjoyment.")
	time.sleep(4.0)
	while True:
		reuben_looks = input(f"[1: 'If he's happy, I'm happy.' 2: 'He looks awesome!' 3: 'He looks ridiculous.' 4: '...']")
		if reuben_looks = "1":
			print("\n'As long as Reuben's happy, I'm happy.' Reuben is joyfully dashing around the room in his awesome dragon costume")
			break
		elif reuben_looks = "2":
			break
		elif reuben_looks = "3":
			break
		elif reuben_looks = "4":
			break
	exit(0)
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
		place["episode"] = 1
		place["part"] = 1
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
		time.sleep(2.0)
	elif saveorload == "load":
		print("*WARNING* this is still a WIP, so loading doesn't do much since there's only a small percent of the full game complete")
		while True:
			save = input("What was the name of your save file?  ")
			sure = input("\nAre you sure about this (y/n)?  ").lower()

			if sure == "y":
				break
			elif sure == "n":
				print("Alright, I'll ask again\n\n")
				continue
		print("\nAlright, you'll start from where you left off, mine ya later!")
		time.sleep(2.0)
	load_game()