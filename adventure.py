######################
#                    #
#   Adventure Game   #
#  Written in python #
#                    #
######################

# Editing the source code may break your game.

# Current version: v0.2

# Will always have good quality :D

# Please don't edit this

location = 'startup'
player_dead = 'false' # This variable is for a future version.

# Customize your starting HP.

player_hp = '10' # This variable is for a future version.

print('HOMEUSER3 STUDIOS 2019 (est. 2017)') # Don't change this part
print('')
print('')
print('Welcome to Adventure Game v0.2! I hope you enjoy!')

name = input('First, I need to know your name. >> ')

print('Hello,', name, ".")
print('I hope you enjoy my game!')
print('Your current HP is', player_hp, ". HP is currently not fully implemented into the game yet.")

print('First, let us find out where you want to go.')
print('Locations are, as followed:')
print('Swamp')
print('Town')
print('Mountain')
print('Forest')
location = input('Let us find out which of these you want to go to. Just tell me right here. >> ')

# Unpacking and recoding the code below can result in a game crash. Use this at your own risk.

if location.lower() == 'swamp':
	print('Well, we are at the swamp.')
	print('Hey... I think I heard something...')
	print('It is a snake!! Lots of them!!')
	whatwanttodo_swamp = input('What do you want to do now? Run or fight? >> ')
	
	if whatwanttodo_swamp.lower() == 'run':
		print('Wow, that was close... I wonder what is next...')
		print('Just casually walking, nothing happening right now...')
		print('SNAKE!! Oh wait... Just a rabbit...')
		
		whatwanttodo_swamp2 = input('Now there is more... What to do now... Run or fight? >> ')
		
		if wantwanttodo_swamp2.lower() == 'run':
			quit = input('OK. I am done. The game is over! Just type "quit" into this message box >> ')
			
			if quit.lower() == 'quit':
				print('Closing... You are not intended to see this message.')
				
	if whatwanttodo_swamp.lower() == 'fight':
		print('Fight!!! *fight music intensifies*')
		whatwanttodo_swamp3 = input('What do you want to do? Kick or punch? >> ')
		
		
		if whatwanttodo_swamp3.lower() == 'kick':
			print('Haha! I got them all! All the snakes are dead and all the people here are safe from the poisonus snakes.')
			print('Wait.. Is that ANOTHER scream?')
			print('Oh... I just heard that there have been snakes everywhere, all day long!')
			whatwanttodo_swamp4 = input('Well, do you want to fight or run? >> ')
			
			if whatwanttodo_swamp4.lower() == 'run':
				quit2 = input('I am done, just dooooooone. Type "quit" to exit the game. >> ')
				
				if quit2.lower() == 'quit':
					print('Closing... You are not intended to see this message.')
							
			if whatwanttodo_swamp4.lower() == 'fight':
				print('Yep, time for another fight.')
				whatwanttodo_swamp5 = input('Fun, right? Anyways, what do you want to do, punch or kick? >> ')
					
				if whatwanttodo_swamp5.lower() == 'punch':
					print('That... That (hopefully) was the last snake.')
					
					quit3 = input('Anyways, I am d o n e. Type "quit" to quit. >> ')
					
					if quit3.lower() == 'quit':
						print('Closing... You are not intended to see this message.')
						
				if whatwanttodo_swamp5.lower() == 'kick':
					print('Now they are alll gone.')
					quit4 = input('I am done, type "quit" to quit. >> ')
					
					if quit4.lower() == 'quit':
						print('Closing... You are not intended to see this message.')
						
		if whatwanttodo_swamp3.lower() == 'punch':
			print('You killed all the snakes!')
			print('You also found a easter egg that makes the game shorter :P')
			quit5 = input('"quit" to quit the game. >> ')
			
			if quit5.lower() == 'quit':
				print('Closing... You are not intended to see this message.')
				

if location.lower() == 'town':
	print('Back at the town, eh?')
	print('Does not look like there is much to do here...')
	print('Wait... Is that an alarm?')
	whatwanttodo_town = input('What are we going to do now? Are we going to run or fight? >> ')
	
	if whatwanttodo_town.lower() == 'fight':
		print('fighting!')
		whatwanttodo_town4 = input('What do you want to do? Punch or kick? >> ')
		
		if whatwanttodo_town4.lower() == 'kick':
			print('Annnnnnd we are done.')
			print('Maybe.')
			print('I heard another burgler!')
			whatwanttodo_town7 = input('Do you want to run or fight? >> ')
			
			if whatwanttodo_town7.lower() == 'fight':
				print('Fighting.. again...')
				whatwanttodo_town8 = input('Do you want to punch or kick? >> ')
				
				if whatwanttodo_town8.lower() == 'punch':
					print('Should be em all.')
					quit_town6 = input('Type "quit" to quit. >> ')
					
					if quit_town7.lower() == 'quit':
						print('Closing...')
				
				if whatwanttodo_town8.lower() == 'kick':
					print('Kicked em! That should be the last of them.')
					quit_town8 = input('Type "quit" to quit. >> ')
					
					if quit_town8.lower() == 'quit':
						print('Closing...')
			
			if whatwanttodo_town7.lower() == 'run':
				print('I am done. NOPPPPPPPE.')
				quit_town9 = input('Type "quit" to quit. >> ')
				
				if quit_town9.lower() == 'quit':
					print('Closing...')
		
		if whatwanttodo_town4.lower() == 'punch':
			print('Annnnnnd we are done.')
			print('Maybe.')
			print('I heard another burgler!')
			whatwanttodo_town5 = input('Do you want to run or fight? >> ')
			
			if whatwanttodo_town5.lower() == 'fight':
				print('Fighting.. again...')
				whatwanttodo_town6 = input('Do you want to punch or kick? >> ')
				
				if whatwanttodo_town6.lower() == 'punch':
					print('Should be em all.')
					quit_town6 = input('Type "quit" to quit. >> ')
					
					if quit_town6.lower() == 'quit':
						print('Closing...')
				
				if whatwanttodo_town6.lower() == 'kick':
					print('Kicked em! That should be the last of them.')
					quit_town5 = input('Type "quit" to quit. >> ')
					
					if quit_town5.lower() == 'quit':
						print('Closing...')
			
			if whatwanttodo_town5.lower() == 'run':
				print('I am done. NOPPPPPPPE.')
				quit_town4 = input('Type "quit" to quit. >> ')
				
				if quit_town4.lower() == 'quit':
					print('Closing...')

	
	if whatwanttodo_town.lower() == 'run':
		print('I hope the police will take care of that...')
		print('Anyways, it does not look like much is happening here. No more burglers.')
		print('Wait! I heard a burgler! There!')
		whatwanttodo_town2 = input('What do you want to do now? Run or fight? >> ')
		
		if whatwanttodo_town2.lower() == 'fight':
			print('fighting!!')
			whatwanttodo_town3 = input('What move do you want to do? Punch or kick? >> ')
			
			if whatwanttodo_town3.lower() == 'kick':
				print('All done, no more burglers!')
				print('Hopefully...?')
				print('Yeah, no more!')
				quit_town3 = input('Type "quit" to quit. >> ')
				
				if quit_town3.lower() == 'quit':
					print('Closing...')
			
			if whatwanttodo_town3.lower() == 'punch':
				print('All done!')
				print('No more burglers!')
				quit_town2 = input('Type "quit" to quit. >> ')
				
				if quit_town2.lower() == 'quit':
					print('Closing...')
		
		if whatwanttodo_town2.lower() == 'run':
			print('I am done. NOPENOPENOPE.')
			quit_town = input('Type "quit" to quit. >> ')
			
			if quit_town.lower() == 'quit':
				print('Closing...')


if location.lower() == 'mountain':
	print('This view is pretty...')
	print('Although, it does not look like much to do here.')
	print('Wait... What is that? LOOK!')
	whatwanttodo = input('What are we going to do now? Are we going to run or fight? >> ')
	
	if whatwanttodo.lower() == 'fight':
		print('fighting! yeah!')
		whatwanttodo1 = input('What do you want to do? Punch or kick? >> ')
		
		if whatwanttodo1.lower() == 'kick':
			print('Annnnnnd we are done.')
			print('Maybe.')
			print('I heard another!')
			whatwanttodo2 = input('Do you want to run or fight? >> ')
			
			if whatwanttodo2.lower() == 'fight':
				print('Fighting.. again... yeah..!')
				whatwanttodo3 = input('Do you want to punch or kick? >> ')
				
				if whatwanttodo3.lower() == 'punch':
					print('Should be em all.')
					quit1 = input('Type "quit" to quit. >> ')
					
					if quit1.lower() == 'quit':
						print('Closing...')
				
				if whatwanttodo3.lower() == 'kick':
					print('Kicked em! That should be the last of them.')
					quit2 = input('Type "quit" to quit. >> ')
					
					if quit2.lower() == 'quit':
						print('Closing...')
			
			if whatwanttodo2.lower() == 'run':
				print('I am done. NOPE.')
				print('No more of this for me, k thx')
				quit3 = input('Type "quit" to quit. >> ')
				
				if quit3.lower() == 'quit':
					print('Closing...')
		
		if whatwanttodo1.lower() == 'punch':
			print('Annnnnnd we are done.')
			print('Maybe.')
			print('I heard another...')
			print('Why tho')
			whatwanttodo4 = input('Do you want to run or fight? >> ')
			
			if whatwanttodo4.lower() == 'fight':
				print('Fighting.. again...')
				whatwanttodo5 = input('Do you want to punch or kick? >> ')
				
				if whatwanttodo5.lower() == 'punch':
					print('Should be em all.')
					quit4 = input('Type "quit" to quit. >> ')
					
					if quit4.lower() == 'quit':
						print('Closing...')
				
				if whatwanttodo5.lower() == 'kick':
					print('Kicked em! That should be the last of them.')
					quit5 = input('Type "quit" to quit. >> ')
					
					if quit5.lower() == 'quit':
						print('Closing...')
			
			if whatwanttodo4.lower() == 'run':
				print('I am done. NOPPPPPPPE.')
				quit6 = input('Type "quit" to quit. >> ')
				
				if quit6.lower() == 'quit':
					print('Closing...')

	
	if whatwanttodo.lower() == 'run':
		print('I hope someone will take care of that...')
		print('Anyways, it does not look like much else is happening here.')
		print('Wait! I heard something! Over there!')
		whatwanttodo6 = input('What do you want to do now? Run or fight? >> ')
		
		if whatwanttodo6.lower() == 'fight':
			print('fighting!! (maybe i like this)')
			whatwanttodo7 = input('What move do you want to do? Punch or kick? >> ')
			
			if whatwanttodo7.lower() == 'kick':
				print('All done, no more!')
				print('Hopefully...?')
				print('Yeah, no more!')
				quit7 = input('Type "quit" to quit. >> ')
				
				if quit7.lower() == 'quit':
					print('Closing...')
			
			if whatwanttodo7.lower() == 'punch':
				print('All done!')
				print('No more!')
				quit8 = input('Type "quit" to quit. >> ')
				
				if quit8.lower() == 'quit':
					print('Closing...')
		
		if whatwanttodo6.lower() == 'run':
			print('I am done. NOPEEEEEEEE.')
			quit9 = input('Type "quit" to quit. >> ')
			
			if quit9.lower() == 'quit':
				print('Closing...')
				
if location.lower() == 'forest':
        print('The national forest. Where all the lumberjacks go to kill animals and cut down trees.')
        print('It is true, what they say about this forest.')
        print('It is truly beautiful, but, as they say, there are dangerous animals here.')
        whatwanttodo_forest = input('I heard a bear! What should I do now??  Run or fight? >> ')

        if whatwanttodo_forest.lower() == 'fight':
                print('fighting! yeah!')
                whatwanttodo_forest1 = input('What do you want to do? Punch or kick? >> ')
		
                if whatwanttodo_forest1.lower() == 'kick':
                        print('Annnnnnd we are done.')
                        print('Maybe.')
                        print('I heard another bear!')
                        whatwanttodo_forest2 = input('Do you want to run or fight? >> ')
			
                        if whatwanttodo_forest2.lower() == 'fight':
                                print('Fighting.. again... yeah..!')
                                whatwanttodo3 = input('Do you want to punch or kick? >> ')
				
                                if whatwanttodo_forest3.lower() == 'punch':
                                        print('Should be em all.')
                                        quit_forest1 = input('Type "quit" to quit. >> ')
					
                                        if quit_forest1.lower() == 'quit':
                                                print('Closing...')
				
                                if whatwanttodo_forest3.lower() == 'kick':
                                        print('Kicked em! That should be the last of them.')
                                        quit_forest2 = input('Type "quit" to quit. >> ')
					
                                        if quit_forest2.lower() == 'quit':
                                                print('Closing...')
			
                        if whatwanttodo_forest2.lower() == 'run':
                                print('I am done. NOPE.')
                                print('No more of this for me, k thx')
                                quit_forest3 = input('Type "quit" to quit. >> ')
				
                                if quit_forest3.lower() == 'quit':
                                        print('Closing...')
		
                if whatwanttodo_forest1.lower() == 'punch':
                        print('Annnnnnd we are done.')
                        print('Maybe.')
                        print('I heard another freaking BEAR...')
                        print('Why tho')
                        whatwanttodo_forest4 = input('Do you want to run or fight? >> ')
			
                        if whatwanttodo_forest4.lower() == 'fight':
                                print('Fighting.. again... why')
                                whatwanttodo_forest5 = input('Do you want to punch or kick? >> ')
				
                                if whatwanttodo_forest5.lower() == 'punch':
                                        print('Should be em all. Maybe.')
                                        quit_forest4 = input('Type "quit" to quit. >> ')
					
                                        if quit_forest4.lower() == 'quit':
                                                print('Closing...')
				
                                if whatwanttodo_forest5.lower() == 'kick':
                                        print('Kicked em! That should be the last of them. Idk tho... hm')
                                        quit_forest5 = input('Type "quit" to quit. >> ')
					
                                        if quit_forest5.lower() == 'quit':
                                                print('Closing...')
			
                        if whatwanttodo_forest4.lower() == 'run':
                                print('I am done. NOPPPPPPPE.')
                                quit6 = input('Type "quit" to quit. >> ')
				
                                if quit_forest6.lower() == 'quit':
                                        print('Closing...')

                if whatwanttodo_forest.lower() == 'run':
                        print('I hope someone will take care of that...')
                        print('Anyways, it does not look like much else is happening here.')
                        print('Wait! I heard something! Over there!')
                        whatwanttodo_forest6 = input('What do you want to do now? Run or fight? >> ')
		
                        if whatwanttodo_forest6.lower() == 'fight':
                                print('fighting!! (maybe i like this)')
                                whatwanttodo7 = input('What move do you want to do? Punch or kick? >> ')
			
                                if whatwanttodo_forest7.lower() == 'kick':
                                        print('All done, no more!')
                                        print('Hopefully...?')
                                        print('Yeah, no more!')
                                        quit_forest7 = input('Type "quit" to quit. >> ')
				
                                        if quit_forest7.lower() == 'quit':
                                                print('Closing...')
			
                                if whatwanttodo_forest7.lower() == 'punch':
                                        print('All done!')
                                        print('No more!')
                                        quit_forest8 = input('Type "quit" to quit. >> ')
				
                                        if quit_forest8.lower() == 'quit':
                                                print('Closing...')
		
                        if whatwanttodo_forest6.lower() == 'run':
                                print('I am done. NOPEEEEEEEE.')
                                quit_forest9 = input('Type "quit" to quit. >> ')
			
                                if quit_forest9.lower() == 'quit':
                                        print('Closing...')
