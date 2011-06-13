#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

def info(title):
	print title
	print 'module name:', __name__
	print 'prarent process:', os.getppid()
	print 'process id:', os.getpid()

def f(name):
	print 'hello', name

if __name__=='__main__':
	info('main line')
	p=Process(target=f, args=('bob',))
	p.start()
	p.join()

