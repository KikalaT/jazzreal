# -*- coding: utf-8 -*-

album_dict = {\

'Charlie Parker':\
('Billies Bounce Now\'s The Time--Savoy Records--1945','Red Cross / Tiny\'s Tempo--Savoy Records--1945','Lover Man / Shaw \'Nuff--Guild Records (2)--1945'),\

'Sonny Stitt':\
('All God\'s Children (Got Rhythm) / Sunset--Prestige--1949','Blues Up And Down / You Can Depend On Me--Prestige--1950','Sonny Stitt And Bud Powell Quartet--New Jazz--1951')

}

class album:

	def init_albumDB(self):
		album.DB = []
		album.DB = album_dict
		return album.DB
