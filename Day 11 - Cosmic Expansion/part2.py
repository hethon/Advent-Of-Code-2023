def is_galaxy(x):
	return x == "#"


def produce_pairs(galaxies):
	''' produces every possible pair of galaxies '''
	for i in range(len(galaxies)):
		for j in range(i+1, len(galaxies)):
			yield (galaxies[i], galaxies[j])


def manhattan_distance(point1, point2):
	return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


def shortest_path(galaxy1, galaxy2):
	distance_before_expansion = manhattan_distance(galaxy1, galaxy2)
	distance_after_expansion = distance_before_expansion
	EXPANSION_RATE = 999_999 # the number of rows/columns added for every empty row/column	

	for i in range(galaxy1[0]+1, galaxy2[0]):
		if i in empty_rows:
			distance_after_expansion += EXPANSION_RATE

	start, end = (galaxy1[1]+1, galaxy2[1]) if galaxy1[1] <= galaxy2[1] else (galaxy2[1]+1, galaxy1[1])
	for i in range(start, end):
		if i in empty_columns:
			distance_after_expansion += EXPANSION_RATE

	return distance_after_expansion


with open("./input.txt", "r") as f:
	universe = f.read().strip("\n").split("\n")
	galaxies = []

	rows = len(universe)
	columns = len(universe[0])

	empty_rows = [i for i in range(rows)]
	empty_columns = [i for i in range(columns)]

	for row in range(rows):
		for column in range(columns):
			if is_galaxy(universe[row][column]):
				galaxies.append((row, column))
				if row in empty_rows: empty_rows.remove(row)
				if column in empty_columns: empty_columns.remove(column)

	shortest_path_sum = 0
	for galaxy1, galaxy2 in produce_pairs(galaxies):
		shortest_path_sum += shortest_path(galaxy1, galaxy2)

	print(shortest_path_sum)
