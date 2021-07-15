import socket
from sys import argv
import os	
import pickle
import pygame
import random

width = 500
height = 500
radius = 20
inc = 10
pygame.init()
font = pygame.font.SysFont('Arial', 20)

def pack(data):
	return pickle.dumps(data)

def unpack(data):
	return pickle.loads(data)

players = {}

def move(pid):
	global players
	keys = pygame.key.get_pressed()
	if(keys[pygame.K_LEFT]):
		players[pid]['x'] -= inc
	if(keys[pygame.K_RIGHT]):
		players[pid]['x'] += inc
	if(keys[pygame.K_UP]):
		players[pid]['y'] -= inc
	if(keys[pygame.K_DOWN]):
		players[pid]['y'] += inc


def draw_player(win, player):
	pygame.draw.circle(win, player['color'], (player['x'], player['y']), radius)
	win.blit(font.render(player['pid'], True, (0, 0, 0)), (player['x']-radius, player['y']+radius))

def redraw(win, players):
	win.fill((255, 255, 255))
	for pid in players:
		draw_player(win, players[pid])
	pygame.display.update()		

if __name__ == '__main__':
	if(len(argv) < 2):
		print("enter player name using command line")
		os._exit(0)

	pid = str(argv[1])
	print(pid)

	players[pid] = {}
	players[pid]['pid'] = pid
	players[pid]['x'] = random.randint(0, width)
	players[pid]['y'] = random.randint(0, height)
	players[pid]['color'] = (
								random.randint(100, 240),
								random.randint(100, 240),
								random.randint(100, 240)
							)

	s = socket.socket()		
	port = 12345				
	s.connect(('127.0.0.1', port))

	pygame.display.set_caption(pid)
	win = pygame.display.set_mode((width,height))

	clock = pygame.time.Clock()
	while(1):
		
		clock.tick(60)
		s.send(pack(players[pid]))
		players = unpack(s.recv(2048))

		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()

		move(pid)
		redraw(win, players)
	

		
	s.close()