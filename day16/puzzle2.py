import os

with open("input.txt", "r") as f:
	fields = []
	valid_tickets = set()
	invalid_rate = 0	# sum of invalid numbers

	for line in f:
		# print(line)
		line = line.strip()
		if line == "\n" or line == " " or line == "":
			# print("new or empty")
			continue
		elif "your ticket" in line:
			skipped = f.readline()
			# print("skipped:"), skipped
		elif line == "nearby tickets:":
			continue

		elif " or " in line:
			# print("here",)
			lower, higher = line.split(": ")[1].split(" or ")
			fields.append(lower.split("-") + higher.split("-"))

		else:
			# all nearby tickets
			overall_valid = True
			for n in line.split(","):
				# print(i)
				n = int(n)
				# print(fields[i], n)
				valid = False
				for r in fields:
					if (n >= int(r[0]) and n <= int(r[1])) or \
						(n >= int(r[2]) and n <= int(r[3])):
						valid = True

				if not valid:
					# print("invalid", n, invalid_rate)
					invalid_rate += n
					overall_valid = False

			if overall_valid:
				valid_tickets.add(line)

	# every field is possible to start
	potential_fields = [[True for _ in range(len(fields))] for _ in range(len(fields))]

	valid_tickets = list(valid_tickets)
	valid_tickets.sort()
	# print(valid_tickets)
	# for v in valid_tickets:
	# 	print(v)
	# exit()

	for ticket in valid_tickets:
		# for each number in the ticket
		numbers = ticket.split(",")
		for i in range(0, len(numbers)):
			# can the "i" column on the ticket be the "j" field
			for j in range(0, len(potential_fields[i])):
				if potential_fields[i][j]:
					n = int(numbers[i])
					# print(i, j, fields[j], n)
					if (n >= int(fields[j][0]) and n <= int(fields[j][1])) or \
						(n >= int(fields[j][2]) and n <= int(fields[j][3])):
						# print("first", n >= int(fields[j][0]) and n <= int(fields[j][1]))
						# print("second", n >= int(fields[j][2]) and n <= int(fields[j][3]))
						pass
					else:
						potential_fields[i][j] = False
						# print(ticket, i, j, fields[j], n)
						# input()
			# print(potential_fields[i])
			# exit()


	print(potential_fields)