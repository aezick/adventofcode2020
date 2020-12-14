import os

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.

with open("input.txt", "r") as f:
	facing = "E"
	loc = [0, 0]
	turn_order = ["N", "W", "S", "E"]	# left

	for line in f:
		line = line.strip()
		num = int(line[1:])

		if "N" in line:
			loc[0] += num
			continue
		elif "S" in line:
			loc[0] -= num
			continue
		elif "E" in line:
			loc[1] += num
			continue
		elif "W" in line:
			loc[1] -= num
			continue

		normal_turn = False
		u_turn = False
		opposite_turn = False
		num = num % 360

		# turn or u_turn
		if num == 90:
			normal_turn = True
		elif num == 180:
			u_turn = True
		elif num == 270:
			opposite_turn = True

		if "L" in line:
			if normal_turn:
				facing = turn_order[turn_order.index(facing) - 3]
			if u_turn:
				facing = turn_order[turn_order.index(facing) - 2]
			if opposite_turn:
				facing = turn_order[turn_order.index(facing) - 1]
			continue
		if "R" in line:
			if normal_turn:
				facing = turn_order[turn_order.index(facing) - 1]
			if u_turn:
				facing = turn_order[turn_order.index(facing) - 2]
			if opposite_turn:
				facing = turn_order[turn_order.index(facing) - 3]
			continue

		if "F" in line:
			if facing == "N":
				loc[0] += num
			elif facing == "E":
				loc[1] += num
			elif facing == "S":
				loc[0] -= num
			elif facing == "W":
				loc[1] -= num
			continue

		print("error")

	print("Manhattan distance:", abs(loc[0]) + abs(loc[1]))
