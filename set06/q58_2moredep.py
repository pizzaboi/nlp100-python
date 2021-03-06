#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
USAGE: cat japanese.txt.cabocha | python q58_2moredep.py
"""

from chunkreader import *

def unpunctuate(chunk):
	morph = chunk.morphs[-1]
	if morph.pos == '記号':
		return ''.join([m.surface for m in chunk.morphs[:-1]])
	return ''.join([m.surface for m in chunk.morphs])

def print_dependency():
	for S in reader():
		for chunk in S:
			if len(chunk.srcs) >= 2:
				for i in chunk.srcs:
					src = S[i]
					print unpunctuate(src) + '\t' + unpunctuate(chunk)
		print #end of sentence

if __name__ == '__main__':
	print_dependency()