import numpy as np
import random as r

doors_num = 3
doors = np.zeros(doors_num+1)
luckyDoor = r.randint(1,doors_num)
doors[luckyDoor] = 1

guess1 = input('Door between 1 and '+str(doors_num)+'? ')

if guess1 == luckyDoor:
	guess2 = input('Switch? Door '+str(guess1)+' or '+str(r.randint(1,doors_num))+'? ')
else:
	guess2 = input('Switch? Door '+str(guess1)+' or '+str(luckyDoor)+'? ')

if str(guess2) == str(luckyDoor):
	print('correct')
else:
	print(guess2)
	print('incorrect, Door '+str(luckyDoor))