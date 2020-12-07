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


	winners = set()
	for b in bags:
		queue = []
		if "shinygold" in bags[b]:
			# print(bags[b])
			winners.add(b)
			continue
		else:
			for k in bags[b].keys():
				queue.append(k)
			while queue:
				if queue[0] == "shinygold":
					winners.add(b)
					break
				else:
					# print(queue)
					for k in bags[queue[0]].keys():
						queue.append(k)
				queue.pop(0)
					
	print(len(winners))
