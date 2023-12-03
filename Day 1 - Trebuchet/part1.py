
with open("./input.txt", "r") as f:
	lines = f.readlines()
	total_calibration_value = 0
	for line in lines:
		calibration_value = ""
		for char in line:
			if char.isdigit():
				calibration_value += char
				break
		for char in line[::-1]:
			if char.isdigit():
				calibration_value += char
				break

		total_calibration_value += int(calibration_value)

	print(total_calibration_value)
