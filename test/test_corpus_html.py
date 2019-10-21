# -*- coding: utf-8 -*-
import sys

sys.path.insert(1, '/home/jericho/flask/jazzreal')

from jazzreal import list_titles

###TESTS###

def test_corpushtml():
	for i in list_titles:
		assert open('/home/jericho/flask/jazzreal/static/corpus-html/'+i+'.html','r')
