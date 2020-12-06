import os

with open("input.txt", "r") as f:
	count = 0
	answers = {"lines": 0}

	for line in f:
		line = line.strip()
		if not line:
			# print(answers, len(answers))
			people = answers["lines"]
			answers["lines"] = 0

			for key in answers:
				if answers[key] == people:
					count += 1

			answers = {"lines": 0}
			# print(answers)
		else:
			answers["lines"] += 1
			for c in line:
				if c not in answers:
					answers[c] = 1
				else:
					answers[c] += 1

	people = answers["lines"]
	answers["lines"] = 0

	for key in answers:
		if answers[key] == people:
			count += 1

	print(count)