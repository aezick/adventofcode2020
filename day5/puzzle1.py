import os

with open("input.txt", "r") as f:
	highest = 0

	for line in f:
		# print(line)
		seats = [n for n in range(0,128)]
		columns = [n for n in range(0,8)]
		# print(seats)
		# print(columns)
		# exit()
		
		for i in range(0,7):
			# print(i, line[i])
			if line[i] == "F":
				seats = seats[:len(seats) // 2]
			else:
				seats = seats[len(seats) // 2:]
			# print(seats)

		for i in range(7,10):
			# print(i, line[i])
			if line[i] == "L":
				columns = columns[:len(columns) // 2]
			else:
				columns = columns[len(columns) // 2:]
			# print(columns)

		score = (seats[0] * 8) + columns[0]
		# print(seats[0], columns[0])
		
		if highest < score:
			highest = score

	print(highest)