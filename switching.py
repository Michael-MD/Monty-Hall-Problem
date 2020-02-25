import numpy as np
import random as r

num_of_doors = []
successful = []

for doorsNum in range(1,101):
	num_of_doors.append(doorsNum)
	success = 0
	fail = 0

	for play in range(1,101):
		doors_num = doorsNum
		doors = np.zeros(doors_num+1)
		luckyDoor = r.randint(1,doors_num)
		doors[luckyDoor] = 1

		guess1 = r.randint(1,doors_num)

		if guess1 == luckyDoor:
			guess2 = r.randint(1,doors_num)
		else:
			guess2 = luckyDoor

		if str(guess2) == str(luckyDoor):
			success = success+1
		else:
			fail = fail+1

	percent_success = success/(success+fail);
	successful.append(percent_success)





for x in range(0,100):
	print('['+str(num_of_doors[x])+','+str(successful[x])+'],')

