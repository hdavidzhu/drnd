# The main code for my Deal or No Deal game.
# This code is meant of ease of reading.
# It is broken down into several systematic steps that are well-documented.

# ==============================
# IMPORTS
# ==============================
import random # Used to scramble our money boxes.

# ==============================
# DECLARATIONS
# ==============================

# Box Declarations.
boxes = [.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]

boxnumbers = range(1,27) # Box numbers to help determine chosen boxes.
print boxnumbers

# ==============================
# RANDOMIZER
# ==============================

random.shuffle(boxes) # Shuffle the boxes.
newboxes = dict(zip(boxnumbers,boxes)) # Zips together boxes and boxnumbers

# ==============================
# ACTIONS
# ==============================

# Pick your box.
chosen = raw_input("Choose your own box (ranging from 1 to 26): ")
print "\nBox "+chosen+" is your choice.\n"
chosen = int(chosen)
chosenvalue = newboxes[chosen]

# Remove box from taking averages.
del newboxes[chosen]
print str(len(newboxes)) + " boxes remaining."

# Round function.
def round(roundnumber):
	
	i = 1
	while i != range(7-roundnumber):
		print str(7-i) + " boxes remaining."
		pick = raw_input("Pick a box: ")
		pick = int(pick)
		if pick-1 in newboxes.keys():
			print "\nYou chose box "+str(pick)+".\n"
			del newboxes[pick-1]
			print newboxes.keys()
			i = i + 1
		else:
			print "Try again. You've already picked that box or your input is invalid."

# Dealer function.
def dealer(newboxes):
	average = 0
	for j in range(1,len(newboxes)+1):
		average = average + newboxes[j]
	average = average /  len(newboxes)
	deal = .9 * average
	print "The dealer offers $"+str(deal)+"."

dealer(newboxes)


# Gameplay function.
def gameplay(level):
	print "\nBegin Round "+str(level)+"."
	if level <= 6 and len(newboxes) > 1:
		round(level)
	elif level > 6 and len(newboxes) > 1:
		round(6)
	else:
		print "Endgame."