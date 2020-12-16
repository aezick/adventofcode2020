import os

with open("input.txt", "r") as f:
	fields = []
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

	print(invalid_rate)
