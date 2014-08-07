#change the current room
#w= world object
#r= room to move to
def comGoRoom(w, r):
	w.currRoom = r

def comChangeDesc():
	pass

'''
-how to handle synonyms? want to handle synonyms?
-will need a second class of events that activate without user input
--gameobject should have states? setup as a dictionary?
'''

#event object
class Event(object):
	def __init__(self, searchTerm, termParameter, func, funcParameter):
		self.searchTerm = searchTerm
		self.termParameter = termParameter
		self.func = func
		self.funcParameter = funcParameter

#used by GameObject
class EventManager(object):
	def __init__(self):
		self.eventList = []

	def addEvent(self, e):
		self.eventList += e

	#inp is a list
	#world is the world object
	def serve(self, inp, world):
		for e in self.eventList:
			if e.searchTerm == inp[0]:
				if e.termParameter == inp[1]:
					e.func(world, e.funcParameter)

class GameObject(object):
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc
		self.em = EventManager()

class Room(GameObject):
	def __init__(self, name, desc):
		super().__init__(name, desc)

class World(object):
	def __init__(self, startRoom):
		self.lastInput = ''
		self.currRoom = startRoom
		self.currDesc = ''
		self.roomList = []

	def awaitInput(self):
		self.lastInput = input('--->')

	def printLastInput(self):
		print('=' + self.lastInput)

	def addToDesc(self, desc):
		self.currDesc += desc

	def printDesc(self):
		print('[' + self.currDesc + ']')

	def clearDesc(self):
		self.currDesc = ''

	def parse(self):
		inp = self.lastInput.split(' ') #split user input to a list
		self.currRoom.em.serve(inp=inp, world=self)

	def addRoom(self, r):
		self.roomList += r

#game driver
'''
	maybe have an object list(s) as a parameter, rather than defining the game objects within the driver
'''
def driver():
	#define rooms
	CLEARING = Room(name='Clearing', desc='This clearing looks stupid. There is a cave NORTH.')
	CAVE = Room(name='Cave', desc='A dim cave.')

	#define the world
	WORLD = World(CLEARING) #world start room is CLEARING

	#define triggers
	#E = Event(a='go',b='north',c='goroom', d=CAVE)

	#add triggers to objects
	CLEARING.em.addEvent([Event(searchTerm='go',termParameter='north',func=comGoRoom, funcParameter=CAVE)])

	#add rooms to world
	WORLD.addRoom([CLEARING, CAVE])

	#begin of game loop
	#loop ends when user inputs 'quit'
	while WORLD.lastInput != 'quit':
		#current description is empty
		WORLD.addToDesc(WORLD.currRoom.desc) #add the current room's description to the current description
		WORLD.printDesc() #output the current description
		WORLD.printLastInput() #print last user input, for debug purposes
		WORLD.awaitInput() #prompt user for input
		WORLD.parse() #do work on user's last input

		#prep for next loop
		WORLD.clearDesc() #clear the current description
	#end of game loop

driver()