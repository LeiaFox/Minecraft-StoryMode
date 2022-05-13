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
reuben = colored("\nReuben:","magenta")

def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

#places you at the part you were at, or at the start
def load_game():
	global f
	global f2
	global place
	global load
	global loadinv
	global inventory
	
	f = open(save + "/" + save + ".json")
	f2 = open(save + "/inventory.json")
	
	filesize = (os.path.getsize(save + "/" + save + ".json") + os.path.getsize(save + "/inventory.json"))
	if filesize != 0:
		load = json.loads(f.read())
		loadinv = json.loads(f2.read())
	
	if load["episode"] == 1:
		if load["part"] == 1:
			inventory = loadinv
			place = load
			chapter_1_part_1()


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
		print("Your name is Jesse. You're in a treehouse that you and your only friends live in. It's made of oak and spruce wood, with red carpeting and spruce pillars in the corners. As you're slashing at an armour stand practicing your sword fighting skills, your good friend Olivia holds a small piece of redstone and peeks out the window.\n")
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
			place["zombiesizedchicken"]=False
			place["chickensizedzombie"]=True
			with open(save + "/" + save + ".json", 'w') as f:
				json.dump(place, f)
			print("\n'That's easy. I'll take the little tiny... little zombies.'")
			time.sleep(4.0)
			print(olivia,"'A hundred of them... crawling all over you, with their tiny hands.' She sways her arms in front of herself and drones.")
			time.sleep(4.0)
			print("\n'All I'd need is, like, a shovel. I'm telling you, way too easy.'")
			break
		elif zombieorchicken == "3":
			place["zombiesizedchicken"]=True
			place["chickensizedzombie"]=False
			with open(save + "/" + save + ".json", 'w') as f:
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
			print("\n'We are not losers, Olivia'")
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
			print("\n'...'")
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
		axel_intro = input(f"{axel} 'I thought we were buddies!' He looks down at Reuben. \n\n[1: 'Cool mask.' 2: 'You had that coming.' 3: 'Not funny, Axel.' 4: '...'] *unfinished* ")
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
			print("\n'That's what you get Axel.'")
			time.sleep(4.0)
			print(f"{axel} 'I brought you good times, and now I'm being punished for it? He waves his hands around in lashing anger. *Axel will remember that.*'")
			time.sleep(4.0)
			print(f"\n'You scared us half to death.' You lash out and throw your arms behind you to exaggerate your message.")
			time.sleep(4.0)
			print(f"{axel} 'Nothing is fun if you're not scared half to death.'")
			break
		elif axel_intro == "3":
			print("\n'That wasn't funny Axel!' You point at him dissaprovingly.")
			time.sleep(4.0)
			print(f"{axel} 'I brought you good times, and now I'm being punished for it? He waves his hands around in lashing anger.' *Axel will remember that.*")
			time.sleep(4.0)
			print(f"\n'You scared us half to death.' You lash out and throw your arms behind you to exaggerate your message.")
			time.sleep(4.0)
			print(f"{axel} 'Nothing is fun if you're not scared half to death.'")
			break
		elif axel_intro == "4":
			print("\n'...'")
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
		reuben_looks = input(f"\n\n[1: 'If he's happy, I'm happy.' 2: 'He looks awesome!' 3: 'He looks ridiculous.' 4: '...'] ")
		if reuben_looks == "1":
			print("\n'As long as Reuben's happy, I'm happy.' Reuben is joyfully dashing around the room in his awesome dragon costume")
			time.sleep(4.0)
			print(f"{axel} 'Happy?'")
			time.sleep(4.0)
			print(f"{reuben} 'Oink!'")
			time.sleep(4.0)
			print(f"{axel} 'Well zippity do dah!' Reuben rubs up against Axel with his head.")
			time.sleep(4.0)
			print(f"{axel} 'Okay, relax. It's fine.'")
			break
		elif reuben_looks == "2":
			break
		elif reuben_looks == "3":
			break
		elif reuben_looks == "4":
			print("\n'...'")
			break
	time.sleep(4.0)
	print(f"{olivia} 'You definetely brought the fireworks right?'")
	time.sleep(4.0)
	print(f"{axel} 'Yes. I'm ready. Waiting on you guys.'")
	time.sleep(4.0)
	print(f"{axel} 'Hurry up and grab your stuff.'")
	time.sleep(4.0)
	print(f"{olivia} 'We'll meet you downstairs, okay?' Axel and Olivia both head off down the tree house and wait for you below.")
	time.sleep(4.0)
	print("\n'Okay!' You then begin ''grabbing your stuff''.")
	time.sleep(4.0)

	done_1 = False
	done_2 = False
	done_3 = False
	done_4 = False
	done_5 = False
	done_6 = False
	
	while True:
		grabbing_stuff = input(f"\nWhat would you like to look at (type 'E' to check inventory)? \n\n[1: Chest to the left of the tree house. 2: Gabriel banner. 3: Chest below the tree house window. 4: Banner with a pear on it that says 'E C'. 5: Armor stand with a pumpkin head on it. 6: Reuben.] Type 'exit' to exit. ").lower()
		
		if grabbing_stuff == "1":
			
			if done_1 == False:
				print("\nYou walk up to the chest and begin scrambling inside. 'Hm. Flint and steel, not too shabby'")
				time.sleep(4.0)
				inventory.update({"flint_and_steel" : 1})
				with open(save + "/inventory.json", 'w') as f:
					json.dump(inventory, f)
				done_1 = True
			else:
				print("You've already looked at this!")
			continue
		elif grabbing_stuff == "2":
			
			if done_2 == False:
				print("\nYou walk up to the banner. 'Gabriel the warror. You think we'll ever get that famous?' you turn to look at Reuben")
				time.sleep(4.0)
				print("\n'It's not impossible... maybe I'll get famous for my sweet poster collection.'")
				time.sleep(4.0)
				done_2 = True
			else:
				print("You've already looked at this!")
			continue
		elif grabbing_stuff == "3":
			
			if done_3 == False:
				print("\nYou walk up to the chest and begin scrambling inside. 'Shears. Definetely taking these. Never know when I might need to shear some sheep.'")
				time.sleep(4.0)
				inventory.update({"shears" : 1})
				with open(save + "/inventory.json", 'w') as f:
					json.dump(inventory, f)
				done_3 = True
			else:
				print("You've already looked at this!")
			continue
		elif grabbing_stuff == "4":
			
			if done_4 == False:
				print("\nYou walk up to the banner. 'One of these days we're going to win the Endercon building competition.' You turn to look at Reuben.")
				time.sleep(4.0)
				print("\n'And when we do, people will look at us and say, ''Hey, there goes Jesse and Reuben, winners of the Endercon Building Competition''... '")
				time.sleep(4.0)
				done_4 = True
			else:
				print("You've already looked at this!")
			continue
		elif grabbing_stuff == "5":

			if done_5 == False:
				print("\nYou walk up to the armor stand. 'I got this stand as a gift, but don't have any armor to put on it. Maybe someday.'")
				time.sleep(4.0)
				done_5 = True
			else:
				print("You've already looked at this!")
			continue
		elif grabbing_stuff == "6":

			if done_6 == False:
				print("\nYou kneel down to Reuben's level.")
				time.sleep(4.0)
				print("\n'Gimme a dragon roar, Reuben.'")
				time.sleep(4.0)
				print("\nReuben squeals.")
				time.sleep(4.0)
				print("\n'That'll do Reuben, that'll do.")
				time.sleep(4.0)
			else:
				print("\nYou've already looked at this!")
			continue
		elif grabbing_stuff == "e":
			
			print(f"\nInventory:\n{inventory}")
			print(f"\n\nplaceholder\n{place}")
			time.sleep(4.0)
			continue
		elif grabbing_stuff == "exit":
			break
			
	print("\nReuben runs around you in a ring. You stop his wrath by grabbing him, and carrying him with you down the tree house.")
	time.sleep(4.0)
	print("\nAxel and Olivia are waiting for you at the bottom.")
	time.sleep(4.0)
	print(f"{olivia} 'That's everything.")
	time.sleep(4.0)
	print(f"{axel} 'Let's roll.' He punches his fist in the air.")
	time.sleep(4.0)
	print(f"{olivia} 'Yeah. Dude. Roll.' This is very clearly judgemental.")
	time.sleep(4.0)
	print(f"\n'Let's go.' You command everyone.")
	time.sleep(4.0)
	print("\nEveryone begins walking to the competition now.")
	time.sleep(4.0)
	print(f"{axel} 'I heard a pretty juicy rumor about the building competition, but you guys have to promise not to say anything.' ")
	time.sleep(4.0)
	print(f"{olivia} 'Okay.' ")
	time.sleep(4.0)
	print(f"{axel} 'Also, it's in two parts, each part more exciting than the last!")
	time.sleep(4.0)
	print(f"\n'Spit it out Axel.' You eyebrows burrow.")
	time.sleep(4.0)
	print(f"{axel} 'Part one. The special guest at this year's Endercon is none other than Gabriel the Warrior him-freaking-self!' ")
	time.sleep(4.0)
	print(f"\n'Whoa! What's part two?!' ")
	time.sleep(4.0)
	print(f"{axel} 'Part two. According to my sources, the winner of the building competition's gonna meet him!' ")
	time.sleep(4.0)
	print(f"{axel} 'It's not gonna mean anything if we lose.' ")
	time.sleep(4.0)
	print(f"{axel} 'But if we win...oh man, this would make up for all the losing.' ")
	time.sleep(4.0)
	while True:
		winforlosing = input(f"\n\n[1: 'I wish the rest of the were there.' 2: 'It's not a big deal, is it?' 3: 'I'd love to meet Gabriel!' 4: '...'] ")
		if winforlosing == "1":
			print(f"\n'I wish they were all going to be there.' ")
			time.sleep(4.0)
			print(f"\n{axel} 'Does nothing please you?! You have to meet ALL of the super secret, super legendary Order of the Stone?'")
			time.sleep(4.0)
			print(f"\n'I wasn't saying it wasn't cool. I was just saying, that would be cool -- too.' ")
			break
		elif winforlosing == "2":
			break
		elif winforlosing == "3":
			break
		elif winforlosing == "4":
			print("\n'...'")
			break
			
	time.sleep(4.0)
	print(f"{olivia} 'Soooo, does this ''source'' of yours make posters for a living?'")
	time.sleep(4.0)
	print(f"{axel} 'Huh?' All of you stumble upon a forest full of posters with Gabriels face on them, along with other neat designs. You deduct this is how Axel knew all this.")
	time.sleep(4.0)
	print(f"{axel} 'Yeah. My source, uhhh, doesn't... uh... exist. You guys are my only friends.'")
	time.sleep(4.0)
	print(f"\n'Guys, lets stay focused. We have a competition to win.'")
	time.sleep(4.0)
	print(f"{olivia} 'We never win. And this year we've got Reuben with us.'")
	time.sleep(4.0)
	print(f"{olivia} 'We basically have no chance.'")
	time.sleep(4.0)
	while True:
		winforlosing = input(f"\n\n[1: 'We'll win this time.' 2: 'Have a little faith, Olivia' 3: 'Anything can happen.' 4: '...'] ")
		if winforlosing == "1":
			
			break
		elif winforlosing == "2":
			print(f"\n'Have a little faith, Olivia.'")
			time.sleep(4.0)
			print(f"{olivia} 'What?'")
			time.sleep(4.0)
			print(f"\n'A little slice. A sliver. A portion. Just a little faith. That's all we need. Also, I'm hungry. To win' ")
			time.sleep(4.0)
			print(f"{axel} 'No, no. I'm with that.' ")
			time.sleep(4.0)
			print(f"{olivia} 'All right.' She has a worried smile.")
			break
		elif winforlosing == "3":
			break
		elif winforlosing == "4":
			print("\n'...'")
			break
	time.sleep(4.0)
	print(f"\n'Wait a minute...wait a minute...we're thinking about this all wrong.' ")
	time.sleep(4.0)
	print(f"\n'The point of the building competition isn't just to build something. You have to get noticed by the judges.' ")
	time.sleep(4.0)
	print(f"{olivia} 'Okay, then. So how do we do this?'")
	time.sleep(4.0)
	print(f"\n'We don't just build something functional. We build something fun.' ")
	time.sleep(4.0)
	print(f"\n'After we finish the fireworks machine, like we planned -- then we build something cool on top of it.' ")
	time.sleep(4.0)
	print(f"{olivia} 'You might be onto something.' ")
	time.sleep(4.0)
	print(f"{axel} 'If you wanna build something to get a reaction out of the judges, you build something scary. So I say we build a creeper...' ")
	time.sleep(4.0)
	print(f"{olivia} 'Wouldn't an enderman be better? I'm more scared of enderman than creepers.' ")
	time.sleep(4.0)
	print(f"{axel} 'They both have their moments. Both pretty scary.' ")
	time.sleep(4.0)
	print(f"{olivia} 'Then again, you scared the crap out of us with a creeper today.' ")
	time.sleep(4.0)
	while True:
		winforlosing = input(f"\n\n[1: 'How about a zombie?' 2: 'Enderman are cool' 3: 'Let's build a creeper!' 4: '...'] ")
		if winforlosing == "1":
			break
		elif winforlosing == "2":
			break
		elif winforlosing == "3":
			break
		elif winforlosing == "4":
			print("\n'...'")
			break
	time.sleep(4.0)
#CHAPTER 1 PART 1



#below is the first thing people see
print('''
					***	MINECRAFT STORYMODE	***

Welcome player to a version of minecraft storymode runnable entirely in replit

This is not complete, but once it is it will include saving, loading, every chapter,
and slightly branching paths, although generally no matter what you do the outcome 
stays the same...

*I do not own minecraft storymode nor am I affilliated with Telltale games*\n\n''')
time.sleep(3.0)




while True:
	while True:
		saveorload = input("Would you like to load a game or start from the beginning? (load or start) ").lower()
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
		inventory = {}
		inventory.update({"wooden_sword" : 1})
		while True:
			save = input("\n\nWhat do you want to name your save file (if it already exists an error will show if you enter it here)? ")
			sure = input("\nAre you sure about this (y/n)?").lower()
			if sure == "y":
				if not os.path.exists(save):
					os.makedirs(save)
					with open(save + "/" + save + ".json", 'w') as f:
						json.dump(place, f)
					with open(save + "/inventory.json", 'w') as f:
						json.dump(inventory, f)
					break
				else:
					print("Exception: Save file name already exists!")
					continue
			elif sure == "n":
				print("Alright, I'll ask again\n\n")
				continue

		print("\nAlright, You adventure will start... NOW!")
		time.sleep(2.0)
	elif saveorload == "load":
		print("*WARNING* this is still a WIP, so loading doesn't do much since there's only a small percent of the full game complete")
		while True:
			save = input("What was the name of your save file? ")
			sure = input("\nAre you sure about this (y/n)? ").lower()

			if sure == "y":
				break
			elif sure == "n":
				print("Alright, I'll ask again\n\n")
				continue
		print("\nAlright, you'll start from where you left off, mine ya later!")
		time.sleep(2.0)
	load_game()