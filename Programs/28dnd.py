"""
1. You are a mage with the Fire Bolt spell. This does 1d10 damage, or 5.5 
points of damage on average. If you have the Elemental Adept feat, damage 
rolls of 1 become 2. How much more damage do you do on average if you are 
an Elemental Adept?

2. If you have the "Piercer" feat, you may re-roll a damage die. You must 
take the new roll regardless if it was lower than the previous roll. Assume 
you have a weapon that does 1d8 damage. Clearly, you should re-roll any die 
with an initial roll of 1 damage. But what about higher rolls? Your friend 
Jorg re-rolls 1-6. But Gastin says that's too high and re-rolls 1-3. Who 
does more damage on average, and when is it optimal to re-roll?

3. One of the core mechanics of D&D is the "saving throw". When certain 
events happen, you need to roll a d20 to figure out if you succeed or not. 
For example, you are walking across a frozen lake and it begins to crack 
underfoot. If you make a saving throw, you step aside. If you fail, you 
fall in. Some saving throws are more difficult than others. If the ice 
is very thick, the "difficulty class" (DC) may be only 5. This means you
only need to roll a 5 or higher to succeed. However, if the ice is thin 
and has a DC of 15, you will need a roll of 15 or higher to succeed. 
Certain events may give you "advantage" or "disadvantage". For example, 
if you have a rope tied around your waist and a friend is instructed to 
pull you aside if anything bad happens, you could have "advantage". This 
allows you to roll two d20s and take the larger value. You may also have 
disadvantage, for example another "friend" pushes you from behind, causing 
you to stumble forward. In this case, you have "disadvantage" and must take 
the lower of two d20 rolls. Write a program that simulates saving throws. 
Make the DC from 1 to 20. What is the probability of success with a normal 
roll? What about advantage or disadvantage? Make a table with DC and the 
three probabilities.

4. You have just beaten the big boss monster and there is loot to choose. 
There are two very interesting items. The "Fire Ring" grants its wearer +5 
to saving throws against fire. The "Fire Cloak" grants its wearer advantage 
on all saving throws against fire. Which of these is better?

5. Death saves are a little different than normal saving throws. If your 
health drops to 0 or below, you are unconscious and may die. Each time it 
is your turn, roll a d20 to determine if you get closer to life or fall 
deeper into death. If the number is less than 10, you record a "failure". 
If the number is 10 or greater, you record a "success". If you collect 3 
failures, you "die". If you collect 3 successes, you are "stable" but 
unconscious. If you are unlucky and roll a 1, it counts as 2 failures. 
If you're lucky and roll a 20, you gain 1 health and have "revived". 
Write a program that simulates death saves. What is the probability you 
die, stabilize, or revive?

6. Halflings are "lucky". When rolling a saving throw and the d20 comes 
up as a 1, they can re-roll that die and take the new value, whatever 
that is. What are the chances a halfling dies, stabilizes, or revives?
"""

# 1.
print("1.)")
avg_damage = (2+2+3+4+5+6+7+8+9+10)/10
print(f'Elemental Adept will do average of {avg_damage} damage, which is {avg_damage-5.5:.2f} more damage on average')
print()

# 2.
print("2.)")
from random import randint

jorge_roll = [1,2,3,4,5,6]
gastin_roll = [1,2,3]

print("Jorg's probability of optimal reroll:")
for roll in jorge_roll:
	j_higher_reroll_count = 0
	for i in range(100):
		jorge_reroll = randint(1,6)
		if (jorge_reroll > roll):
			j_higher_reroll_count += 1
	j_prob_higher_reroll = j_higher_reroll_count / 100
	print(f"{roll} {j_higher_reroll_count} {j_prob_higher_reroll}")
print("It is optimal for Jorg to re-roll if he initially rolls a 1 or 2")

print("Gastin's probability of optimal reroll:")			
for roll in gastin_roll:
	g_higher_reroll_count = 0
	for i in range(100):
		gastin_reroll = randint(1,3)
		if (gastin_reroll > roll):
			g_higher_reroll_count += 1
	g_prob_higher_reroll = g_higher_reroll_count / 100
	print(f"{roll} {g_higher_reroll_count} {g_prob_higher_reroll}")
print("It is optimal for Gastin to re-roll only if he initially rolls a 1.")

jorg_avg = (sum(jorge_roll))/6
gastin_avg = (sum(gastin_roll))/3
if (jorg_avg > gastin_avg):
	print ("Jorge has higher avg damage of " + str(jorg_avg) + 
		" vs Gastin's avg damage of " + str(gastin_avg))
else:
	print("Gastin has higher avg damage of " + str(gastin_avg) + 
		" vs Jorge's avg damage of " + str(jorg_avg))
print()

# 3.
print("3.)")
DC = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("Diff. Class\t" +"Normal\t" + "Advantage\t" + "Disadvantage")
for diff_class in DC:
	norm_success_count = 0
	adv_success_count = 0
	dis_success_count = 0
	for roll in range(100):
		roll_1 = randint(1,20)
		roll_2 = randint(1,20)
		# normal
		if (roll_1 > diff_class):
			norm_success_count += 1
		
		# 2 roll scenarios
		if (roll_1 > roll_2):
			higher_roll = roll_1
			lower_roll = roll_2
		else:
			higher_roll = roll_2
			lower_roll = roll_1
		# advantage
		if (higher_roll > diff_class):
			adv_success_count += 1
		
		# disadvantage
		if (lower_roll > diff_class):
			dis_success_count += 1
			
	norm_success_prob = norm_success_count / 100
	adv_success_prob = adv_success_count / 100
	dis_success_prob = dis_success_count / 100
	

	print(f'{diff_class} \t\t {norm_success_prob} \t {adv_success_prob} \t\t {dis_success_prob}')
print()

# 4.
print("4.)")
ring_sum = 0
cloak_sum = 0
for i in range (101):
	roll1 = randint(1,20)
	roll2 = randint(1,20)
	
	ring_savingthrow = roll1 + 5
	if (roll1 > roll2):
		cloak_savingthrow = roll1
	else:
		cloak_savingthrow = roll2
	ring_sum += ring_savingthrow
	cloak_sum += cloak_savingthrow

print(f'Ring average saving throw: {ring_sum/100:.2f} Cloak average saving throw: {cloak_sum/100:.2f}')

if (ring_sum/100 > cloak_sum/100):
	print("The ring is better as it has a higher average saving throw.")
else:
	print("The cloak is better as it has a higher average saving throw.")
print()

# 5.
print("5.)")
fail_count = 0
success_count = 0

dead = 0
stabilize = 0
revive = 0

for i in range (101):
	roll = randint(1,20)
	if (roll == 1):
		fail_count += 2
		if (fail_count > 2):
			dead += 1
			fail_count = 0
	elif (roll < 10):
		fail_count += 1
		if (fail_count > 2):
			dead += 1
			fail_count = 0
	elif (roll == 20):
		revive += 1
	elif (roll >= 10):
		success_count += 1
		if (success_count > 2):
			stabilize += 1
			success_count = 0
			
print(f'Probability of Death = {dead/(dead+stabilize+revive):.2f} of Stabilizing = {stabilize/(dead+stabilize+revive):.2f} of Reviving = {revive/(dead+stabilize+revive):.2f}')
print()

# 6.
print("6.)")
fail_count = 0
success_count = 0

dead = 0
stabilize = 0
revive = 0

for i in range (101):
	roll = randint(1,20)
	if (roll == 1):
		reroll = randint(1,20)
		if (reroll == 1):
			fail_count += 2
		if (fail_count > 2):
			dead += 1
			fail_count = 0
	elif (roll < 10):
		fail_count += 1
		if (fail_count > 2):
			dead += 1
			fail_count = 0
	elif (roll == 20):
		revive += 1
	elif (roll >= 10):
		success_count += 1
		if (success_count > 2):
			stabilize += 1
			success_count = 0
			
print(f'Probability of Death = {dead/(dead+stabilize+revive):.2f} of Stabilizing = {stabilize/(dead+stabilize+revive):.2f} of Reviving = {revive/(dead+stabilize+revive):.2f}')
print()	
		
