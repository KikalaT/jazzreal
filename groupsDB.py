# -*- coding: utf-8 -*-

groups_dict = {\

'Charlie Parker':\
('this is group1 of Charlie Parker','this is group2 of Charlie Parker','this is group3 of Charlie Parker'),\

'Sonny Stitt':\
('this is group1 of Charlie Parker','this is group2 of Charlie Parker','this is group3 of Charlie Parker'),\

}

class groups:

	def init_groupsDB(self):
		groups.DB = []
		groups.DB = groups_dict
		return groups.DB
