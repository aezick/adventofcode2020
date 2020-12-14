import copy
import os

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.

with open("input.txt", "r") as f:
	loc = [0, 0]
	waypoint = [1, 10]

	for line in f:
		# print(loc, waypoint)
		line = line.strip()
		num = int(line[1:])

		if "N" in line:
			waypoint[0] += num
			continue
		elif "S" in line:
			waypoint[0] -= num
			continue
		elif "E" in line:
			waypoint[1] += num
			continue
		elif "W" in line:
			waypoint[1] -= num
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
				new_waypoint = copy.deepcopy(waypoint)
				new_waypoint[0] = waypoint[1]
				new_waypoint[1] = -waypoint[0]
				waypoint = new_waypoint
			if u_turn:
				new_waypoint = copy.deepcopy(waypoint)
				new_waypoint[0] = -waypoint[0]
				new_waypoint[1] = -waypoint[1]
				waypoint = new_waypoint
			if opposite_turn:
				new_waypoint = copy.deepcopy(waypoint)
				new_waypoint[0] = -waypoint[1]
				new_waypoint[1] = waypoint[0]
				waypoint = new_waypoint
			continue
		if "R" in line:
			if normal_turn:
				new_waypoint = copy.deepcopy(waypoint)
				new_waypoint[0] = -waypoint[1]
				new_waypoint[1] = waypoint[0]
				waypoint = new_waypoint
			if u_turn:
				new_waypoint = copy.deepcopy(waypoint)
				new_waypoint[0] = -waypoint[0]
				new_waypoint[1] = -waypoint[1]
				waypoint = new_waypoint
			if opposite_turn:
				new_waypoint = copy.deepcopy(waypoint)
				new_waypoint[0] = waypoint[1]
				new_waypoint[1] = -waypoint[0]
				waypoint = new_waypoint
			continue

		if "F" in line:
			loc[0] += waypoint[0] * num
			loc[1] += waypoint[1] * num
			continue

		print("error")

	print("Manhattan distance:", abs(loc[0]) + abs(loc[1]))
