# coding: utf-8

"""
Copyright (c) 2014 Paulo Sérgio Borges de Oliveira Filho

Check LICENSE for details.
"""

import os

from .jlink import ExecJLinkScriptCommand

class Flash(ExecJLinkScriptCommand):
	# SCRIPT = "flash.jlink"

	def __init__(self, firmware, address,device, **kwargs):
		super(Flash, self).__init__(device,**kwargs)
                self.device = device
		self.firmware = self.format_firmware(firmware)
		self.address = self.format_address(address)
                self.script = 'flash' + '_' + self.device + '.jlink'
                
	def execute(self):
		return super(Flash, self).execute(self.script,
			firmware=self.firmware,
			address=self.address
		)

	def format_firmware(self, firmware):
		return os.path.abspath(firmware)

	def format_address(self, address):
		try:
			return hex(int(address))
		except ValueError:
			return address
