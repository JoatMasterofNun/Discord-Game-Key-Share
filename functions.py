import os,json,discord,random

def read_json(file_name):
	if file_name.endswith('.json')==False:
		file_name=file_name+'.json'
	if not os.path.isfile(file_name):
		list_name=open(file_name,"w+")
		list_name=[]
	else:
		try:
			with open(file_name) as f:
				list_name = json.load(f)
		except ValueError:
			list_name=[]
	return list_name

def edit_json(file_name,items):
	if file_name.endswith('.json')==False:
		file_name=file_name+'.json'
	with open(file_name,"w") as f:
		f.write(json.dumps(items))

def on_open():
	global game_list
	game_list=dict(read_json('game_list'))

def add_key(game,key):
	game=game.lower()
	if game.lower() not in game_list.keys():
		game_list[game]=[]
	game_list[game].append(key)
	edit_json('game_list',game_list)

def get_game(game):
	if game.lower() in game_list.keys():
		key=random.choice(game_list[game])
		game_list[game].remove(key)
		if len(game_list[game])==0:
			del game_list[game]
		edit_json('game_list',game_list)
		return key
	else:
		return 'There are no keys for **{}** at this time :frowning:'.format(game)

def make_list():
	output=""
	for game,key in game_list.items():
		output=output+"{} -- ({})\n\n".format(game,len(key))
	embed=discord.Embed(title='Game -- (Keys)',description=output, color=0x00FF00)
	return embed

def help():
	commands={}
	commands['!add_key']="Lets you show your generosity by adding a game key :hugging:"
	commands['!list']='List of games and the amount of available keys for each game'
	commands['!get_game']="Pick a game from the list, don't be greedy :rage:"
	embed=discord.Embed(title='Bot Commands',color=0x0000FF)
	for cmd,desc in commands.items():
		embed.add_field(name=cmd,value=desc,inline=False)
	return embed

on_open()
