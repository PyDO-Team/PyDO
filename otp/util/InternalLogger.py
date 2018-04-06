"""
 * Copyright (C) PyDO Team - All Rights Reserved
 * Written by the PyDO Team, April 4, 2018
 * Licensing information can found in 'LICENSE', which is part of this source code package.
"""

from datetime import datetime
from direct.directnotify.DirectNotifyGlobal import directNotify

class InternalLogger:

    def __init__(self, name):
        self.name = name
        self.logger = directNotify.newCategory(self.name)

    def info(self, message):
        now = datetime.now().strftime("%H:%M:%S")
        self.logger.warning("[%s] [INFO]: %s" % (now, message))

    def debug(self, message):
        now = datetime.now().strftime("%H:%M:%S")
        self.logger.warning("[%s] [DEBUG]: %s" % (now, message))

    def warning(self, message):
        now = datetime.now().strftime("%H:%M:%S")
        self.logger.warning("[%s] [WARNING]: %s" % (now, message))

    def error(self, message):
        now = datetime.now().strftime("%H:%M:%S")
        self.logger.warning("[%s] [ERROR]: %s" % (now, message))