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
					pos = passport.find("byr:")
					pos += 4

					thing = passport[pos:pos+4]

					if thing.isnumeric() == False:
						passport = ""
						continue

					thing = int(thing)
					if thing < 1920 or thing > 2002:
						passport = ""
						continue

					pos = passport.find("iyr:")
					pos += 4

					thing = int(passport[pos:pos+4])
					if thing < 2010 or thing > 2020:
						passport = ""
						continue

					pos = passport.find("eyr:")
					pos += 4

					thing = int(passport[pos:pos+4])
					if thing < 2020 or thing > 2030:
						passport = ""
						continue

					pos = passport.find("hgt:")
					pos += 4

					thing = ""
					while True:
						if passport[pos].isnumeric():
							thing += passport[pos]
							pos += 1
						else:
							break

					thing = int(thing)
					if passport[pos] == "c":
						if thing < 150 or thing > 193:
							passport = ""
							continue
					else:
						if thing < 59 or thing > 76:
							passport = ""
							continue


					pos = passport.find("hcl:")
					pos += 4

					thing = passport[pos:pos+7]
					if thing[0] != "#" or thing[1:].isalnum() == False:
						passport = ""
						continue

					pos = passport.find("ecl:")
					pos += 4
					ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

					thing = passport[pos:pos+3]
					if thing not in ecl_list:
						passport = ""
						continue

					pos = passport.find("pid:")
					pos += 4

					thing = passport[pos:pos+9]
					if thing.isnumeric() == False:
						passport = ""
						continue

					count += 1
					# print(passport)
					passport = ""


	print(count)
