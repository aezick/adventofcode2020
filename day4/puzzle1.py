import os

with open("input.txt", "r") as f:
	passport = ""
	count = 0

	for line in f:
		if line != "\n":
			passport += line
			continue
		else:
			if "byr:" in passport and "iyr:" in passport and "eyr:" in passport and "hgt:" in passport:
				if "hcl:" in passport and "ecl:" in passport and "pid:" in passport: 
					count += 1
			passport = ""

	print(count)
