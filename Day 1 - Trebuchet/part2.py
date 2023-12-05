import re

digit_words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


with open("./input.txt", "r") as f:
	lines = f.readlines()

	total_calibration_value = 0
	for line in lines:
		calibration_value = ""

		for i in range(len(line)):
			if line[i].isdigit():
				right_calibration_value = line[i]
				calibration_value += right_calibration_value
				break
			elif (digit_word := re.findall("|".join(digit_words.keys()), line[i :5+i])):
				if digit_word[0] in ("one", "two", "six") and (_ := re.search(r"\d", line[i :5+i])) and line[i :5+i].index(digit_word[0]) > _.start():
					continue

				right_calibration_value = digit_words[digit_word[0]]
				calibration_value += right_calibration_value
				break
			
		for i in range(len(line), -1, -1):
			if line[i-1].isdigit():
				left_calibration_value = line[i-1]
				calibration_value += left_calibration_value
				break
			elif (digit_word := re.findall("|".join(digit_words.keys()), line[i-5: i])):
				if digit_word[0] in ("one", "two", "six") and (_ := re.search(r"\d", line[i-5: i])) and line[i-5: i].index(digit_word[0]) < _.start():
					continue

				left_calibration_value = digit_words[digit_word[0]]
				calibration_value += left_calibration_value
				break

		total_calibration_value += int(calibration_value)
		

	print(total_calibration_value)
