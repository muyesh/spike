#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Lock

def f(i):
	print 'hello world', i

if __name__=='__main__':

	for num in range(10000):
		Process(target=f, args=(num,)).start()

