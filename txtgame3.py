'''
every gameobject will have a list of events, and an iter to pass input over all events.
Txtgame will past lastInput to all objects, so they can past to all their events
GameObject iter will need (world.lastInput, world) ???
don't want to give objects the whole txtgame class. create seperate command class ???

we need managers? 
'''
#makes requests to other objects
#do i need or want this???
def command(a, b, w):
	if a == 'goroom':
		w.goRoom(b)

class Event(object):
	a = ''  #go ,, is looking for (go)
	b = ''  #north ,, if found (go), then also need (north)
	c = ''  #goroom ,, if have (north), then do (goroom)
	d = ''  #CAVE ,, then do (goroom) to target (CAVE)
	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

class EventManager(object):
	eventList = []
	def __init__(self):
		self.eventList

	def addEvent(self, e):
		self.eventList += e

	def iter(self, inp, w):
		for e in self.eventList:
			if e.a == inp[0]:
				if e.b == inp[1]:
					command(a=e.c, b=e.d, w=w)

class GameObject(object):
	name = ''
	desc = ''
	em = ''
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc
		self.em = EventManager()

class Room(GameObject):
	def __init__(self, name, desc):
		super().__init__(name, desc)


class World(object):
	lastInput = ''
	currRoom = ''
	currDesc = ''
	roomList = []
	def __init__(self, startRoom):
		self.lastInput = ''
		self.currRoom = startRoom

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

	def goRoom(self, newRoom):
		self.currRoom = newRoom

	def parse(self):
		inp = self.lastInput.split(' ')
		self.currRoom.em.iter(inp=inp, w=self)

	def addRoom(self, r):
		self.roomList += r


def driver():
	CLEARING = Room(name='Clearing', desc='This clearing looks stupid. There is a cave NORTH.')
	CAVE = Room(name='Cave', desc='A dim cave.')
	E = Event(a='go',b='north',c='goroom', d=CAVE)
	CLEARING.em.addEvent([E])
	WORLD = World(CLEARING)
	WORLD.addRoom([CLEARING, CAVE])
	while WORLD.lastInput != 'quit':
		WORLD.addToDesc(WORLD.currRoom.desc)
		WORLD.printDesc()
		WORLD.printLastInput()
		WORLD.awaitInput()
		WORLD.parse()

		#move this chunk in to a Txtgame.function
		#register all game objects and events to TxtGame
		#iter over all events
		# ?????
		'''
		testCom = Com(World.lastInput.split(' '))
		#print(testCom.c)
		#if c equals e then e.action
		testEv = Ev(['go', 'north', 'goroom'])
		if len(testCom.c) > 1:
			if (testCom.c[0] == testEv.e[0]) & (testCom.c[1] == testEv.e[1]):
				#print(testEv.e[2])
				World.goRoom(CAVE)
				'''
		WORLD.clearDesc()
	#CAVE.em.addEvent('e')

driver()