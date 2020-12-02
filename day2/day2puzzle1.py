import os

with open("input.txt", "r") as f:
	valid_count = 0

	for line in f:
		# r for range, c for character, p for password
		r, c, p = line.split()
		count = 0

		minimum, maximum = r.split("-")
		minimum = int(minimum)
		maximum = int(maximum)
		c = c[0]

		# l for letter
		for l in p:
			if l == c:
				count += 1

		if count >= minimum and count <= maximum:
			valid_count += 1

	print("valid count:", valid_count)