from bofhexcuse import bofh_excuse
from errbot import BotPlugin, botcmd


class Bofh(BotPlugin):

    @botcmd  # flags a command
    def bofh(self, msg, args):  # a command callable with !mittag
        """
        print random BOFH quote
        """
        return "The cause of the problem is: *{}*".format(bofh_excuse()[0])
