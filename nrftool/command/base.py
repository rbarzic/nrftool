# coding: utf-8

"""
Copyright (c) 2014 Paulo Sérgio Borges de Oliveira Filho

Check LICENSE for details.
"""

class Command(object):
	def __init__(self, device='nrf51',verbose=False, jlinkexe='JLinkExe', **kwargs):
		self.verbose = verbose
		self.jlinkexe = jlinkexe
		self.device = device
