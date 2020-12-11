import copy
import os

with open("input.txt", "r") as f:
	count = 0
	seats = []

	for line in f:
		line = line.strip()
		seats.append([i for i in line])

	moved = True
	while moved:
		moved = False

		new_seats = copy.deepcopy(seats)

		for i in range(0, len(seats)):
			for j in range(0, len(seats[0])):
				seat = seats[i][j]

				if seat == ".":
					continue

				new_seat = seat

				occupied_adj = 0
				for pos in [(-1,-1), (-1,0), (-1,1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
					try:
						# print(i, j, pos[0], pos[1])
						# print(seats[i + pos[0]])
						width = i + pos[0]
						length = j + pos[1]
						if width < 0 or width > len(seats):
							continue
						if length < 0 or length > len(seats[0]):
							continue

						if seats[i + pos[0]][j + pos[1]] == "#":
							occupied_adj += 1
					except Exception as e:
						# print(e)
						pass

				if new_seat == "#":
					if occupied_adj >= 4:
						new_seat = "L"
					else:
						new_seat = "#"
				elif new_seat == "L":
					if occupied_adj > 0:
						new_seat = "L"
					else:
						new_seat = "#"

				# if count == 1:
				# 	print(i, j, seat, new_seat, occupied_adj)
				# 	exit()

				new_seats[i][j] = new_seat

				if seat != new_seat:
					moved = True

		seats = new_seats
		# count += 1
		# if count > 4:
		# 	print(seats)
		# 	exit()

	count = 0
	for row in seats:
		for seat in row:
			if seat == "#":
				count += 1

	print("Seats:", count)
