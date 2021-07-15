import socket	
import threading	
import pickle

def pack(data):
	return pickle.dumps(data)

def unpack(data):
	return pickle.loads(data)

players = {} # game area

def handle_client(c):
	global players
	print('new client')
	while(1):
		try:
			data = unpack(c.recv(2048))
			# print(data)
			pid = data['pid']
			players[pid] = data

			if not data:
				print('Disconnected')
				break

			c.send(pack(players))

		except Exception as e:
			print(e)
			break
		
	c.close()

s = socket.socket()
print ("Socket successfully created")
port = 12345
s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")			

while True:
	c, addr = s.accept()	
	print ('Got connection from', addr )
	t1 = threading.Thread(target = handle_client, args=(c, ))
	t1.start()
		
