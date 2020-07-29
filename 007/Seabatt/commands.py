# -*- coding: utf-8 -*-

from custom_exceptions import UserExitException

class ExitCommand(object):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, *args, **kwargs):
        raise UserExitException('See you next time!')