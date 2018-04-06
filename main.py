"""
 * Copyright (C) PyDO Team - All Rights Reserved
 * Written by the PyDO Team, April 4, 2018
 * Licensing information can found in 'LICENSE', which is part of this source code package.
"""

import os,  sys, __builtin__, argparse, thread
from panda3d.core import loadPrcFile, ConfigVariableString

from otp.util.InternalLogger import InternalLogger

# Stop Panda3D from opening a game window.
ConfigVariableString("window-type", "none").setValue("none")

from direct.directbase.DirectStart import *

notify = InternalLogger('Main')

def main():
	# Load the main configuration file.
	loadPrcFile('config/ConfigMain.prc')

	# Get passed command line options.
	parser = argparse.ArgumentParser(description = 'PyDO Command Line Config')
	parser.add_argument('--server-host', help = 'The IP address to open the server on.', type = str, default = '127.0.0.1')
	parser.add_argument('--md-port', help = 'The MessageDirector port to bind to.', type = int, default = 7101)
	parser.add_argument('--ca-port', help = 'The ClientAgent port to bind to.', type = int, default = 6667)
	parser.add_argument('--game-config', help = 'The game specific config file to load.', type = str, default = 'Config.prc')
	parser.add_argument('--el-port', help = 'The EventLogger port to bind to.', type = int, default = 7102)
	args = parser.parse_args()

	notify.info("PyDO Starting...")

	# If the second prc file exists, load it.
	if os.path.isfile('./game/config/%s' % args.game_config):
		loadPrcFile('./game/config/%s' % args.game_config)
		notify.info("Game config '%s' loaded." % args.game_config)
		
	else:
		notify.warning('No game config specified. Make sure to place the config file in the game/config folder.')

	
	# Start all the main server components.
	# We really shouldn't be doing threading like this, but because this is
	# only intended to be used in testing, it's ok.

	# Next, the message director (as other servers connect to it).
	thread.start_new_thread(startMessageDirectorThreaded, (args.server_host, args.md_port))

	# Next, the client agent (what incoming clients connect to).
	thread.start_new_thread(startClientAgentThreaded, (args.server_host, args.ca_port, args.md_port))

	# Next, the state server (manages all the do's in memory).
	thread.start_new_thread(startStateServerThreaded, (args.server_host, args.md_port))

	# Finally, the database server (and inherently the database state server). Pretty self explanitory.
	thread.start_new_thread(startDatabaseServerThreaded, (args.server_host, args.md_port))

	notify.info("PyDO Started!")

	base.run()

def startMessageDirectorThreaded(serverHost, mdPort):
	messageDirector = MessageDirector(serverHost, mdPort)
	messageDirector.setup()

def startClientAgentThreaded(serverHost, caPort, mdPort):
	clientAgent = ClientAgent(serverHost, caPort, mdPort)
	clientAgent.setup()

def startStateServerThreaded(serverHost, mdPort):
	stateServer = StateServer(serverHost, mdPort)
	stateServer.setup()

def startDatabaseServerThreaded(serverHost, mdPort):
	databaseServer = DatabaseServer(serverHost, mdPort)
	databaseServer.setup()

if __name__ == '__main__':
    main()