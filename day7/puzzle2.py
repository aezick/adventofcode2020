import os

with open("input.txt", "r") as f:
	count = 0
	bags = {}

	for line in f:
		line = line.strip()
		outer_bag = line.split(" bags contain")[0]
		outer_bag = outer_bag.replace(" ", "")

		# no other bags
		if "contain no other bags" in line:
			bags[outer_bag] = {}
			continue

		inner_bags = line.split(" bags contain")[1].split(" bag")

		bags[outer_bag] = {}

		for bag in inner_bags:
			# print(inner_bags)
			words = bag.strip("s,").strip("s.").split()
			# print(words)

			if len(words) == 0:
				continue

			num = words[0]
			desc = ""

			for i in range(0, len(words)):
				if len(words[i]) > 2:
					desc += words[i]

			# print(desc)
			if len(desc) > 3:
				bags[outer_bag][desc] = words[0]

		# if len(bags) > 3:
		# 	print(bags)
		# 	exit()
	# print(bags)
	# exit()


	contained_bags = {}
	queue = [("shinygold",1)]

	while queue:
		for b in bags[queue[0][0]].keys():
			if b in contained_bags:
				contained_bags[b] += int(bags[queue[0][0]][b]) * queue[0][1]
			else:
				contained_bags[b] = int(bags[queue[0][0]][b]) * queue[0][1]

			if b not in bags:
				continue
			else:
				queue.append((b, int(bags[queue[0][0]][b])  * queue[0][1]))			

		queue.pop(0)
		# print(bags)
		# print(queue)
		# print(contained_bags)
		# exit()

	count = 0
	for b in contained_bags:
		count += contained_bags[b]

	# print(contained_bags)
	# exit()

	print(count)
