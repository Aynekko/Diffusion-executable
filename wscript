#! /usr/bin/env python
# encoding: utf-8
# a1batross, mittorn, 2018

from waflib import Logs
import os
import sys

top = '.'

def options(opt):
	pass

def configure(conf):
	pass

def build(bld):
	source = ['game.cpp']
	includes = '.'
	libs = ['DL']

	bld.program(
		source   = source,
		target   = 'diffusion_run', # hl.exe
		includes = includes,
		defines  = 'strncpy_s=strncpy',
		use      = libs,
		install_path = bld.env.PREFIX,
	)
