import math


def is_gear(x):
	return x == "*"


def adjacent_entries_to(row_index, column_index, row_length, column_length):
	''' returns at most 8 adjacent coordinates of (row_index, column_index) '''
	top_left = (row_index - 1, column_index - 1) 
	top = (row_index - 1, column_index)
	top_right = (row_index - 1, column_index + 1)


	left = (row_index, column_index - 1)
	right = ((row_index, column_index + 1))

	bottom_left = (row_index + 1, column_index - 1)
	bottom = (row_index + 1, column_index)
	bottom_right = (row_index + 1, column_index + 1)

	adjacent_entries = filter(
		lambda x: x[0] in range(0, row_length) and x[1] in range(0, column_length), 
		(top_left, top, top_right, left, right, bottom_left, bottom, bottom_right)
	)

	return adjacent_entries


def get_nbhd_of(index, row, dxn=0):
	''' 
	returns a neighbourhood of row[index] from the given row
	a neighbourhood of a number is defined as an ordered collection of numbers around the number, including the number 
	'''
	if index == -1 or index == len(row) or not row[index].isdigit():
		return ""
	if dxn == -1:
		return get_nbhd_of(index-1, row=row, dxn=-1) + row[index] 
	if dxn == 1:
		return row[index] + get_nbhd_of(index+1, row=row, dxn=1)
	return get_nbhd_of(index-1, row=row, dxn=-1) + row[index] + get_nbhd_of(index+1, row=row, dxn=1)


with open("./input.txt", "r") as f:
	engine_schematic = f.read().strip("\n").split("\n")

	row_length = len(engine_schematic)
	column_length = len(engine_schematic[0])

	gears = {} # {gear_coordinate: set(adjacent_part_numbers)}
	for i in range(row_length):
		part_number = ""
		for j in range(column_length):
			if not is_gear(engine_schematic[i][j]):
				continue

			for (x, y) in adjacent_entries_to(i, j, row_length=row_length, column_length=column_length):
				adjacent_entry = engine_schematic[x][y]
				
				if adjacent_entry.isdigit():
					adjacent_part_numbers = gears.get((i, j), set())
					adjacent_part_numbers.add(get_nbhd_of(index=y, row=engine_schematic[x]))
					gears[(i, j)] = adjacent_part_numbers

	total_gear_ratio = 0
	for gear in gears:
		adjacent_part_numbers = gears[gear]
		if len(adjacent_part_numbers) == 2:
			gear_ratio = math.prod(map(lambda x: int(x), gears[gear]))
			total_gear_ratio += gear_ratio

	print(total_gear_ratio)
