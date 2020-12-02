import os

with open("input.txt", "r") as f:
	numbers = []
	for line in f:
		numbers.append(int(line))

	i = 0
	while i < len(numbers):
		j = 0
		while j < len(numbers):
			if (numbers[i] + numbers[j]) == 2020:
				print(numbers[i], numbers[j])
				print(numbers[i] * numbers[j])
				exit(0)
			j += 1
		i += 1
