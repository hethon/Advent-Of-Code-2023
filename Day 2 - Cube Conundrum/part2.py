import math

with open("./input.txt", "r") as f:
	games = map(lambda x: x[x.index(":")+2: ], f.read().strip("\n").split("\n"))
	
total_game_power = 0
for i, game in enumerate(games):
	game_id = (i+1)
	game_sets = game.split("; ")

	cubes_needed = {
		"red": 0,
		"green": 0, 
		"blue": 0
	} # minimum number of cubes of each color to make the game possible

	for game_set in game_sets:
		cubes = game_set.split(", ")

		for cube in cubes:
			cube_count = int(cube[ : cube.index(" ")])
			cube_color = cube[cube.index(" ")+1: ]

			cubes_needed[cube_color] = max(cubes_needed[cube_color], cube_count)

	game_power = math.prod(cubes_needed.values())
	total_game_power += game_power

print(total_game_power)
