#! /usr/bin/env python
# encoding: utf-8
# a1batross, mittorn, 2018

from waflib import Logs
import os
import sys

top = '.'

def options(opt):
	grp = opt.add_option_group('Game launcher options')

	grp.add_option('--disable-menu-changegame', action = 'store_true', dest = 'DISABLE_MENU_CHANGEGAME', default = False,
		help = 'disable changing the game from the menu [default: %default]')

def configure(conf):
	if conf.env.DEST_OS == 'win32':
		conf.load('winres')

	conf.define_cond('XASH_DISABLE_MENU_CHANGEGAME', conf.options.DISABLE_MENU_CHANGEGAME)

def build(bld):
	source = ['game.cpp']
	includes = '. ../common ../public'
	libs = []

	if bld.env.DEST_OS != 'win32':
		libs += [ 'DL' ]
	else:
		libs += ['USER32', 'SHELL32']
		source += ['game.rc']

	bld(
		source   = source,
		target   = 'xash3d', # hl.exe
		features = 'c cxx cxxprogram',
		includes = includes,
		use      = libs,
		install_path = bld.env.BINDIR,
		subsystem = bld.env.MSVC_SUBSYSTEM
	)
