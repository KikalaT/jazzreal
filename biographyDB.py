# -*- coding: utf-8 -*-

biography_dict = {\

'Charlie Parker':\
('this is the biography of Charlie Parker'),\

'Sonny Stitt':\
('this is the biography of Sonny Stitt')

}

class biography:

	def init_biographyDB(self):
		biography.DB = []
		biography.DB = biography_dict
		return biography.DB
