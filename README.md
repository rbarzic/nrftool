nrftool
=======

A tool to flash and erase nRF51 & nRF52  devices

Dependencies
------------

* J-Link programmer or J-Link OB microcontroller (on-board)
* [Segger's JLink software](http://www.segger.com/jlink-software.html) (`V4.80`)

Supported devices
-----------------

Currently, only the nRF51822 and nRF52832 chips are supported.

Usage
-----

To flash new firmware:

	$ nrftool [--verbose] --device=nrf51|nrf52 flash FIRMWARE ADDRESS 

To erase current firmware:

	$ nrftool [--verbose] erase 

If `JLinkExe` can't be found in your `PATH`, it can be specified using `--jlinkexe` option:

	$ nrftool --device=nrf51|nrf52 --jlinkexe path/to/your/JLinkExe erase
