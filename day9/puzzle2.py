import os
from itertools import chain, combinations

# from https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

with open("input.txt", "r") as f:
	index = 0
	numbers = []

	preamble_length = 25

	magic_number = 14360655	# 14360655

	for line in f:
		line = line.strip()
		num = int(line)
		numbers.append(num)

	exit("never finished")

	# n = len(numbers)

	# for i in range(n-1):
	# 	curr = numbers[i]
	# 	for j in range(i+1, n):
	# 		if curr == magic_number:
	# 			print(min(numbers[i: j]) + max(numbers[i: j]))

	# 		curr += numbers[j]
