def is_symbol(x):
	return x != "."

def adjacent_entries(row_index, column_index, row_length, column_length):
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

	part_numbers = []
	for i in range(row_length):
		part_number = ""
		for j in range(column_length):
			if not engine_schematic[i][j].isdigit():
				if part_number:
					part_numbers.append(int(part_number))
					part_number = "" # reset part_number
				continue

			for (x, y) in adjacent_entries(i, j, row_length=row_length, column_length=column_length):
				adjacent_entry = engine_schematic[x][y]
				if x == i and adjacent_entry.isdigit():
					continue
				if is_symbol(adjacent_entry):
					part_number = get_nbhd_of(index=j, row=engine_schematic[i])
					break
			if (j == column_length - 1) and part_number:
				part_numbers.append(int(part_number))

	print(sum(part_numbers))

