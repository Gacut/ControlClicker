from pyautogui import press, position
from time import sleep
from sys import exit
from os import system


system('mode con: cols=60 lines=10')
counter = 0



while True:
	try:
		x, y = position()
		print('CTRL + C to exit')
		print('Process repeated ' + str(counter) + ' times')
		print('Cursor position  x: ' + str(x) + ', y: ' + str(y) + '\n',)
		press('ctrl')
		counter += 1
		sleep(100)



	except KeyboardInterrupt:
		exit()
	