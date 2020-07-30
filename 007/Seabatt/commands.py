# -*- coding: utf-8 -*-

from custom_exceptions import UserExitException

class ExitCommand(object):
    @staticmethod
    def label():
        return 'exit'
    @staticmethod
    def perform():
        raise UserExitException('See you next time!')