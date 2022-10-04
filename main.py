import json
import os
import time
from tkinter import *
from tkinter import ttk
import termcolor
from termcolor import colored # Dont forget to sign out from your PC 

olivia = colored("\nOlivia:","red")
olivia2 = colored("Olivia","red")
axel = colored("\nAxel:","green")
reuben = colored("\nReuben:","magenta")

#waits 4 seconds
def wait():
	time.sleep(4.0)

#clears your screen depending on your OS
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
    
	clear_screen()
	print(intro_speech)
	time.sleep(20.0)
	
	print("Chapter 1, Part 1\n")

	while True:
		print("Your name is Jesse. You're in a treehouse that you and your only friends live in. It's made of oak and spruce wood, with red carpeting and spruce pillars in the corners. As you're slashing at an armour stand practicing your sword fighting skills, your good friend Olivia holds a small piece of redstone and peeks out the window.\n")
		time.sleep(8.0)
		zombieorchicken = input(f"{olivia} 'Would you rather fight a hundred chicken-sized zombies, or ten zombie-sized chickens? Just to be clear, you wouldn't have any weapons or armor. So you'd have to fight them with your hands.' \n\n[1: 'Huh?' 2: 'Chicken-sized zombies.' 3: 'Zombie-sized chickens.' 4: '...'] ")
		if zombieorchicken == "1":
            place["zombiesizedchicken"]=False
            place["chickensizedzombie"]=False
			with open(save + "/" + save + ".json", 'w') as f:
				json.dump(place, f)
			print("\n'Huh?'")
			wait()
			print(olivia,"'Huh?' She mocks you acting like a zombie and hunching over.")
			wait()
			print(olivia,"'It's just a dumb question. Forget it.'")
			break
		elif zombieorchicken == "2":
			place["zombiesizedchicken"]=False
			place["chickensizedzombie"]=True
			with open(save + "/" + save + ".json", 'w') as f:
				json.dump(place, f)
			print("\n'That's easy. I'll take the little tiny... little zombies.'")
			wait()
			print(olivia,"'A hundred of them... crawling all over you, with their tiny hands.' She sways her arms in front of herself and drones.")
			wait()
			print("\n'All I'd need is, like, a shovel. I'm telling you, way too easy.'")
			break
		elif zombieorchicken == "3":
			place["zombiesizedchicken"]=True
			place["chickensizedzombie"]=False
			with open(save + "/" + save + ".json", 'w') as f:
				json.dump(place, f)
			print("\n'I'd have to go with the giant chickens. Not because I want to or because I think it would be easy, but because they would be an abomination.'")
			wait()
			print(olivia,"'Imagine their giant feet.'")
			wait()
			print("\n'Like I said... an abomination.'")
			break
		elif zombieorchicken == "4":
            place["zombiesizedchicken"]=False
            place["chickensizedzombie"]=False
			with open(save + "/" + save + ".json", 'w') as f:
				json.dump(place, f)
			print("\n'...'")
			wait()
			print(olivia,"'It's just a hypothetical question, Jesse.'")
			break
	wait()
	print(olivia,"'Soo... I've got a daylight sensor on the roof...'")
	wait()
	print("\n'Mmhm...'")
	wait()
	print(olivia,"'And if I did this right, these lamps should turn on once it gets dark.'")
	wait()
	print("\n'Mmm-Hmm...'")
	wait()
	print(olivia,"'I didn't want to just leave Reuben here with nothing while we're at the building competition-'")
	wait()
	print("\n'He's coming with us.' Your pet Reubon nudges his head into the armour stand.")
	wait()
	print(olivia,"'Really?'")
	wait()
	print("\n'What kind of question is that? Of course he is.' You say this as you stop practicing and put your wooden sword in your inventory.")
	wait()
	print(olivia,"'Okay. I'm not saying he shouldn't come. I'm not... but don't you think it's a little weird that you take him with you everywhere you go?'")
	wait()
	while True:
		reubenchoice = input(f"{olivia} 'He kind of makes us look like... I don't know... amateurs.' \n\n[1: 'Reuben's my best friend.' 2: 'People love pigs!' 3: 'It's not weird at all.' 4: '...'] ")
		if reubenchoice == "1":
			print("\n'Reuben's my best friend.'")
			wait()
			print(olivia,"'I thought I was your best friend?'")
			wait()
			print("\n'Both of you are.'")
			break
		elif reubenchoice == "2":
			print("\n'He's my wingman. People always wanna talk to the girl with the pig.'")
			wait()
			print(olivia,"'You mean talk ABOUT the girl with the pig.'")
			wait()
			print(olivia,"'Like, ''Look at the weird girl with the weird pig. How weird.'' ' Your smile forms into a stern look.")
			wait()
			break
		elif reubenchoice == "3":
			print("\n'It's not weird at all.'")
			wait()
			print("\n'Reuben is the best pet I could ask for. Obedient, loyal, and always happy to see me at the end of a long day.' Your pig glares at you from behind.")
			wait()
			print("\n'Friend. I should have said ''friend,'' not pet.' Your friend nods smiles with valor.")
			break
		elif reubenchoice == "4":
			print("\n'...'")
			wait()
			print(olivia,"'All right. I was just making a point.'")
			break
	wait()
	print(olivia,"'I didn't mean anything by it. I'm glad he's coming.'")
	wait()
	print(olivia,"'I just don't want to give people one more reason to call us ''losers.'' '")
	wait()
	print(olivia,"'I'm getting tired of it.'")
	wait()
	while True:
		losers = input(f"{olivia} 'I'm tired of being a laughing stock.' \n\n[1: 'Who cares what they think?' 2: 'Just embrace it.' 3: 'We aren't losers.' 4: '...'] ")
		if losers == "1":
			print("\n'Who cares what other people think?' *Olivia will remember that.*")
			wait()
			print(f"{olivia} 'I know, I know. I'm just... it wears you down.' she slumps over")
			wait()
			print("\n'You say you're not a loser, Olivia... so win.'")
			wait()
			print(f"{olivia} 'Okay. Fine.' She grins.")
			break
		elif losers == "2":
			print("\n'Embrace being a loser, Olivia. And if you do that, you can be whatever you want to be.'")
			wait()
			print(f"{olivia} 'What if I wanna be a winner?'")
			wait()
			print("\n'Except that.' You let out an unsure giggle, 'Anything else though.'")
			wait()
			print(f"\n{olivia2} laughs")
			wait()
			print(f"{olivia} 'All right, fine.'")
			break
		elif losers == "3":
			wait()
			print("\n'We are not losers, Olivia'")
			wait()
			print(f"{olivia} 'We lose all the time. It's what we do.'")
			wait()
			print("\n'Okay... Okay! That might be true...'")
			wait()
			print(f"{olivia} 'I can't remember the last time we've won anything.'")
			wait()
			print("\n'But if that's the case... it means we win at being losers.'")
			wait()
			print(f"{olivia} '...All right, fine'")
			break
		elif losers == "4":
			print("\n'...'")
			wait()
			print(f"{olivia} '...Real nice Jesse.'")
			wait()
			print(f"{olivia} 'Glad I have a friend like you around.' She says this while unamused and blankly staring")
			break

	wait()
	print("\n???: 'Ssssssss...'")
	wait()
	print("\n'Do you hear that?' You walk over to the trapdoor on the floor which is also the exit.")
	wait()
	print("\n???: 'Sssssssssssss...'")
	wait()
	print(f"{olivia} 'Oh, no.' You kneel down about to open the trapdoor.")
	wait()
	print("\n???: 'BOO'")
	wait()
	print(f"\nYou and {olivia2}: 'AHHH!' Reuben falls over onto the floor out of fear.")
	wait()
	print(f"{axel} 'Ha! I totally freaked all of you out! That was awso- Ow!' Reuben has just rammed into Axel's stomach.")
	wait()
	print(f"{olivia} 'Axel! What's the matter with you?!'")
	wait()
	print(f"{axel} 'Great, now I'm going to smell like a pig at Endercon.'")
	wait()
	while True:
		axel_intro = input(f"{axel} 'I thought we were buddies!' He looks down at Reuben. \n\n[1: 'Cool mask.' 2: 'You had that coming.' 3: 'Not funny, Axel.' 4: '...'] *unfinished* ")
		if axel_intro == "1":
			print("\n'Cool mask.'")
			wait()
			print(f"{axel} 'It is, isn't it?' *Axel will remember that*")
			wait()
			print("\n'Yeah, very convincing.' You put you hands on your hips and glare at Axel in a disaproving matter.")
			wait()
			print(f"{axel} 'The look on your faces...' Axel laughs.")
			break
		elif axel_intro == "2":
			print("\n'That's what you get Axel.'")
			wait()
			print(f"{axel} 'I brought you good times, and now I'm being punished for it? He waves his hands around in lashing anger. *Axel will remember that.*'")
			wait()
			print(f"\n'You scared us half to death.' You lash out and throw your arms behind you to exaggerate your message.")
			wait()
			print(f"{axel} 'Nothing is fun if you're not scared half to death.'")
			break
		elif axel_intro == "3":
			print("\n'That wasn't funny Axel!' You point at him dissaprovingly.")
			wait()
			print(f"{axel} 'I brought you good times, and now I'm being punished for it? He waves his hands around in lashing anger.' *Axel will remember that.*")
			wait()
			print(f"\n'You scared us half to death.' You lash out and throw your arms behind you to exaggerate your message.")
			wait()
			print(f"{axel} 'Nothing is fun if you're not scared half to death.'")
			break
		elif axel_intro == "4":
			print("\n'...'")
			break
	wait()
	print(f"{olivia} 'Did you bring the fireworks?'")
	wait()
	print(f"{axel} 'Of course I did. I even brought something for the little guy' Axel pulls out a pig-sized ender dragon costume, perfect for Reuben.")
	wait()
	print("\n'Nice!'")
	wait()
	print(f"{olivia} 'You brought Reuben a disguise?'")
	wait()
	print(f"{axel} 'We're going to a convention. SOMEbody's gotta wear a costume.' Axel stuffs the costume onto Reuben, Reuben runs around in enjoyment.")
	wait()
	while True:
		reuben_looks = input(f"\n\n[1: 'If he's happy, I'm happy.' 2: 'He looks awesome!' 3: 'He looks ridiculous.' 4: '...'] ")
		if reuben_looks == "1":
			print("\n'As long as Reuben's happy, I'm happy.' Reuben is joyfully dashing around the room in his awesome dragon costume")
			wait()
			print(f"{axel} 'Happy?'")
			wait()
			print(f"{reuben} 'Oink!'")
			wait()
			print(f"{axel} 'Well zippity do dah!' Reuben rubs up against Axel with his head.")
			wait()
			print(f"{axel} 'Okay, relax. It's fine.'")
			break
		elif reuben_looks == "2":
			break
		elif reuben_looks == "3":
			break
		elif reuben_looks == "4":
			print("\n'...'")
			break
	wait()
	print(f"{olivia} 'You definetely brought the fireworks right?'")
	wait()
	print(f"{axel} 'Yes. I'm ready. Waiting on you guys.'")
	wait()
	print(f"{axel} 'Hurry up and grab your stuff.'")
	wait()
	print(f"{olivia} 'We'll meet you downstairs, okay?' Axel and Olivia both head off down the tree house and wait for you below.")
	wait()
	print("\n'Okay!' You then begin ''grabbing your stuff''.")
	wait()

	done_1 = False
	done_2 = False
	done_3 = False
	done_4 = False
	done_5 = False
	done_6 = False

	while True:
		grabbing_stuff = input(f"\nWhat would you like to look at? (type 'E' to check inventory) \n\n[1: Chest to the left of the tree house. 2: Gabriel banner. 3: Chest below the tree house window. 4: Banner with a pear on it that says 'E C'. 5: Armor stand with a pumpkin head on it. 6: Reuben.] Type 'exit' to exit. ").lower()
		
		if grabbing_stuff == "1":
			
			if done_1 == False:
				print("\nYou walk up to the chest and begin scrambling inside. 'Hm. Flint and steel, not too shabby'")
				wait()
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
				wait()
				print("\n'It's not impossible... maybe I'll get famous for my sweet poster collection.'")
				wait()
				done_2 = True
			else:
				print("You've already looked at this!")
			continue
		elif grabbing_stuff == "3":
			
			if done_3 == False:
				print("\nYou walk up to the chest and begin scrambling inside. 'Shears. Definetely taking these. Never know when I might need to shear some sheep.'")
				wait()
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
				wait()
				print("\n'And when we do, people will look at us and say, ''Hey, there goes Jesse and Reuben, winners of the Endercon Building Competition''... '")
				wait()
				done_4 = True
			else:
				print("You've already looked at this!")
			continue
		elif grabbing_stuff == "5":

			if done_5 == False:
				print("\nYou walk up to the armor stand. 'I got this stand as a gift, but don't have any armor to put on it. Maybe someday.'")
				wait()
				done_5 = True
			else:
				print("You've already looked at this!")
			continue
		elif grabbing_stuff == "6":

			if done_6 == False:
				print("\nYou kneel down to Reuben's level.")
				wait()
				print("\n'Gimme a dragon roar, Reuben.'")
				wait()
				print("\nReuben squeals.")
				wait()
				print("\n'That'll do Reuben, that'll do.")
				wait()
			else:
				print("\nYou've already looked at this!")
			continue
		elif grabbing_stuff == "e":
			
			print(f"\nInventory:\n{inventory}")
			wait()
			continue
		elif grabbing_stuff == "exit":
			break
			
	print("\nReuben runs around you in a ring. You stop his wrath by grabbing him, and carrying him with you down the tree house.")
	wait()
	print("\nAxel and Olivia are waiting for you at the bottom.")
	wait()
	print(f"{olivia} 'That's everything.")
	wait()
	print(f"{axel} 'Let's roll.' He punches his fist in the air.")
	wait()
	print(f"{olivia} 'Yeah. Dude. Roll.' This is very clearly judgemental.")
	wait()
	print(f"\n'Let's go.' You command everyone.")
	wait()
	print("\nEveryone begins walking to the competition now.")
	wait()
	print(f"{axel} 'I heard a pretty juicy rumor about the building competition, but you guys have to promise not to say anything.' ")
	wait()
	print(f"{olivia} 'Okay.' ")
	wait()
	print(f"{axel} 'Also, it's in two parts, each part more exciting than the last!")
	wait()
	print(f"\n'Spit it out Axel.' You eyebrows burrow.")
	wait()
	print(f"{axel} 'Part one. The special guest at this year's Endercon is none other than Gabriel the Warrior him-freaking-self!' ")
	wait()
	print(f"\n'Whoa! What's part two?!' ")
	wait()
	print(f"{axel} 'Part two. According to my sources, the winner of the building competition's gonna meet him!' ")
	wait()
	print(f"{axel} 'It's not gonna mean anything if we lose.' ")
	wait()
	print(f"{axel} 'But if we win...oh man, this would make up for all the losing.' ")
	wait()
	while True:
		makeupforlosing = input(f"\n\n[1: 'I wish the rest of the were there.' 2: 'It's not a big deal, is it?' 3: 'I'd love to meet Gabriel!' 4: '...'] ")
		if makeupforlosing == "1":
			print(f"\n'I wish they were all going to be there.' ")
			wait()
			print(f"\n{axel} 'Does nothing please you?! You have to meet ALL of the super secret, super legendary Order of the Stone?'")
			wait()
			print(f"\n'I wasn't saying it wasn't cool. I was just saying, that would be cool -- too.' ")
			break
		elif makeupforlosing == "2":
			break
		elif makeupforlosing == "3":
			break
		elif makeupforlosing == "4":
			print("\n'...'")
			break
			
	wait()
	print(f"{olivia} 'Soooo, does this ''source'' of yours make posters for a living?'")
	wait()
	print(f"{axel} 'Huh?' All of you stumble upon a forest full of posters with Gabriels face on them, along with other neat designs. You deduct this is how Axel knew all this.")
	wait()
	print(f"{axel} 'Yeah. My source, uhhh, doesn't... uh... exist. You guys are my only friends.'")
	wait()
	print(f"\n'Guys, lets stay focused. We have a competition to win.'")
	wait()
	print(f"{olivia} 'We never win. And this year we've got Reuben with us.'")
	wait()
	print(f"{olivia} 'We basically have no chance.'")
	wait()
	while True:
		nochance = input(f"\n\n[1: 'We'll win this time.' 2: 'Have a little faith, Olivia' 3: 'Anything can happen.' 4: '...'] ")
		if nochance == "1":
			
			break
		elif nochance == "2":
			print(f"\n'Have a little faith, Olivia.'")
			wait()
			print(f"{olivia} 'What?'")
			wait()
			print(f"\n'A little slice. A sliver. A portion. Just a little faith. That's all we need. Also, I'm hungry. To win' ")
			wait()
			print(f"{axel} 'No, no. I'm with that.' ")
			wait()
			print(f"{olivia} 'All right.' She has a worried smile.")
			break
		elif nochance == "3":
			break
		elif nochance == "4":
			print("\n'...'")
			break
	wait()
	print(f"\n'Wait a minute...wait a minute...we're thinking about this all wrong.' ")
	wait()
	print(f"\n'The point of the building competition isn't just to build something. You have to get noticed by the judges.' ")
	wait()
	print(f"{olivia} 'Okay, then. So how do we do this?'")
	wait()
	print(f"\n'We don't just build something functional. We build something fun.' ")
	wait()
	print(f"\n'After we finish the fireworks machine, like we planned -- then we build something cool on top of it.' ")
	wait()
	print(f"{olivia} 'You might be onto something.' ")
	wait()
	print(f"{axel} 'If you wanna build something to get a reaction out of the judges, you build something scary. So I say we build a creeper...' ")
	wait()
	print(f"{olivia} 'Wouldn't an enderman be better? I'm more scared of enderman than creepers.' ")
	wait()
	print(f"{axel} 'They both have their moments. Both pretty scary.' ")
	wait()
	print(f"{olivia} 'Then again, you scared the crap out of us with a creeper today.' ")
	wait()
	while True:
		choosemob = input(f"\n\n[1: 'How about a zombie?' 2: 'Enderman are cool' 3: 'Let's build a creeper!' 4: '...'] ")
		if choosemob == "1":
			print(f"\n'Let's build a zombie.' ")
			wait()
			print(f"{axel} 'I guess that's kind of like a creeper.'")
			wait()
			print(f"{olivia} 'Eh. It's a monster it's fine.' ")
			wait()
			print(f"{axel} 'We are so ready.' ")
			
			place["competition_mob"]="zombie"
			with open(save + "/" + save + ".json", 'w') as f:
				json.dump(place, f)
			break
		elif choosemob == "2":
			print(f"\n'Endermen are cool.'")
			place["competition_mob"]="enderman"
			with open(save + "/" + save + ".json", 'w') as f:
				json.dump(place, f)
			break
		elif choosemob == "3":
			print(f"\n'All right, Let's build the creeper.'")
			wait()
			print(f"{olivia} 'You're going with Axel's idea?' She's furious about your decision.")
			wait()
			print(f"{axel} 'What's wrong with my idea?'")
			wait()
			print(f"{olivia} 'Nothing. It could totally be cool.'")
			wait()
			print(f"{axel} 'It is cool.'")
			wait()
			
			place["competition_mob"]="creeper"
			with open(save + "/" + save + ".json", 'w') as f:
				json.dump(place, f)
			break
		elif choosemob == "4":
			print("\n'...'")
			break
	wait()
	print(f"{olivia} 'Yeah. I think this is the first time we decided on something before the competition.' ")
	wait()
	print(f"{olivia} 'Think we've got everything we need?'")
	wait()
	print(f"\n'It wouldn't hurt to grab a little more.'")
	wait()
	print(f"{axel} 'Let's get grabbin', then.'")
	wait()
	print(f"\n'We're so prepared. We can't lose. Cannot. Bring it in.' Everyone puts their hands together on top of eachother like a pact.")
	wait()
	print(f"\n' ''Dare to prepare'' on three. No. ''Preparing is daring'' Nope, That's the same thing. Forget it. ''Team'' on three. One, two, three... ''Team!'' ' Everyone raises their hands and says team in unison (except Axel, who says ''prepare'').")
	wait()
	print(f"\nA preperation montage begins, including things like you doing pushups (why??), You punching a block of oak. \nYou digging up sand. \nYou tackling a squid. \nYou doing pushups but a little harder this time. \nYou running through a field and attacking red flowers (Although they make the player damage sound). You doing sit ups. ")
	wait()
	print(f"")

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
			sure = input("\nAre you sure about this (y/n)? ").lower()
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