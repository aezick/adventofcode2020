import os

with open("input.txt", "r") as f:
	count = 0
	answers = set()

	for line in f:
		line = line.strip()
		if not line:
			# print(answers, len(answers))
			count += len(answers)
			answers.clear()
			# print(answers)
		else:
			for c in line:
				if c not in answers:
					answers.add(c)

	count += len(answers)

	print(count)