import os

with open("input.txt", "r") as f:
	valid_count = 0

	for line in f:
		# r for range, c for character, p for password
		r, c, p = line.split()
		count = 0

		p1, p2 = r.split("-")
		p1 = int(p1)
		p2 = int(p2)
		c = c[0]

		# no concept of index zero, so need to "shift" left one spot
		# xor condition
		if p[p1 - 1] == c and p[p2 - 1] != c:
			valid_count += 1

		if p[p1 - 1] != c and p[p2 - 1] == c:
			valid_count += 1

	print("valid count:", valid_count)