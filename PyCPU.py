#!/usr/bin/env python
# -*- coding: utf-8 -*-4

import os
import time

pycpu_logo = """
                  Function Key
                  /
              __n___
              I    I                   _________
      Main  _ I    I   Floppy disk     I  ___  I
     Storage  I    I  '                I=(___)=I   - Application Software
              I    I I                 I_/  /__I 
              I    I I    INPUT        ~~\  \~~~
              (____) I     |             /__/ 
                II   I___________             
                I(___/___________) - User Interface         Debugging Tool
                (__             I                                    \ __
                   I            /                                      II
                    \          / - Central                             II
                     )        /   Processing                           II
         OUTPUT --  I        (       Unit           .-._               II
                    I_________`,                  o_oo'_)              II
                    ~~~~~***&%~                   `._ `._              II
                        ###@^&&&                     `,  \            |  |
       ._____._        &&&%%## - Overflow            //_(_)_/         ~~~~
       I      o)                (I/O error)         ~~
       (_____,-'                                         Mouse
      
        Backup System
"""

# ascii image design reference --> http://artscene.textfiles.com/asciiart/cpu.txt

def author():
	author = """
	Central Processing Unit Information Gathering Tool
			Ismail Tasdelen
     github.com/ismailtasdelen linkedin.com/in/ismailtasdelen
	"""
	print author

# Author : Ismail Tasdelen
# https://github.com/ismailtasdelen
# https://www.linkedin.com/in/ismailtasdelen/

def pycpu_menu():
	pycpu_menu = """
	[1] CPU All Information Gathering
	[2] Default Information Gathering
	[3] CPU Vulnerability Check
	[4] Exit 
"""
	print pycpu_menu

def logo():
	print pycpu_logo
	time.sleep(5)
	os.system("clear")

def all_cpu():
	os.system("cat /proc/cpuinfo")

def cpu_info():
	info_1 = "cat /proc/cpuinfo | grep 'vendor' | uniq && cat /proc/cpuinfo | grep 'model name'  | uniq" # information 1
	info_2 = "cat /proc/cpuinfo | grep 'microcode' | uniq && cat /proc/cpuinfo | grep 'cpu MHz' | uniq"  # information 2
	info_3 = "cat /proc/cpuinfo | grep 'cache size' | uniq" # information 3
	os.system(info_1 + "&&" + info_2 + "&&" + info_3) # go to function and run

def cpu_vulncheck():
	vulncheck = "cat /proc/cpuinfo | grep 'bugs' | uniq" # cpu vulnerability check bash script code
	os.system(vulncheck) # go to function and run

logo()

# multi function use

def run(all_cpu, cpu_info, cpu_vulncheck,author,pycpu_menu):
	
	author()
	pycpu_menu()

	choice = input("Which option number : ")

	if choice == 1:
		all_cpu()

	elif choice == 2:
		cpu_info()

	elif choice == 3:
		cpu_vulncheck()

# batch arguments
run(all_cpu, cpu_info, cpu_vulncheck,author,pycpu_menu)
