#
# weldanbot.py
# a basic irc bot
# accept commands:
# !sayhi - will respond hi
# !uptime - will show system uptime
# !uname - will show uname 
# !quit - will quit 
#############################################################

import irclib
import sys
import subprocess

from time import sleep

# uncomment this to debug / see raw output on terminal
#irclib.DEBUG = True

network = 'irc.freenode.net'
port = 6667
channel = '#weldan'
nick = 'weldanbot'
name = 'weldan bot test 123'

irc = irclib.IRC()

server = irc.server()
server.connect(network, port, nick, ircname = name)
server.join(channel)

def handle_command(connection, event):
	# respond hi!
	if event.arguments()[0] == "!sayhi":
		server.privmsg(channel, "Hi!")
	
	# quit	
	elif event.arguments()[0] == "!quit":
		server.disconnect()
		sys.exit()
	
	# uptime 
	elif event.arguments()[0] == "!uptime":
		output = subprocess.check_output(["uptime"])
		server.privmsg(channel, output)

	# uname 
	elif event.arguments()[0] == "!uname":
		output = subprocess.check_output(["uname", "-a"])
		server.privmsg(channel, output)
	
irc.add_global_handler('pubmsg', handle_command)

while True:
	try:
		irc.process_forever(timeout=10.0)
	except irclib.ServerNotConnectedError:
		sleep(10)

