with open("./input.txt", "r") as f:
	games = map(lambda x: x[x.index(":")+2: ], f.read().strip("\n").split("\n"))

MAX_CUBE_COUNT = {
	"red": 12,
	"green": 13, 
	"blue": 14
}
	
possible_games_id = set()
for i, game in enumerate(games):
	game_id = (i+1)
	possible_games_id.add(game_id) # assume the game would have been possible

	game_sets = game.split("; ")
	for game_set in game_sets:
		cubes = game_set.split(", ")

		for cube in cubes:
			cube_count = int(cube[ : cube.index(" ")])
			cube_color = cube[cube.index(" ")+1: ]

			if cube_count > MAX_CUBE_COUNT[cube_color]:
				possible_games_id.discard(game_id)
				break

possible_games_id_sum = sum(possible_games_id)
print(possible_games_id_sum)
