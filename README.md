Multiplayer Game:
-----------------

Common Area shared by players: (Game area)
------------------------------
```python
players = {
			pid1 : {
				"pid" : pid1,
				"x"   : 100,
				"y"   : 100,
				"color": (22, 24, 0)
			},
			pid2 : {
				"pid" : pid2,
				"x"   : 20,
				"y"   : 120,
				"color": (22, 24, 233)
			},
}
```

Serialize python object:
------------------------
```python
import pickle

def pack(data):
	return pickle.dumps(data)

def unpack(data):
	return pickle.loads(data)
```

Basic Pygame Code:
------------------
```python
pygame.display.set_caption(pid)
win = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
while(1):
	try:
		clock.tick(60)
		
		#code
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				
	except:
		print("some error")
		break
```


To display text in pygame:
--------------------------
```python
pygame.init()
font = pygame.font.SysFont('Arial', 20)
win.blit(font.render(text, True, color), (x, y))
```