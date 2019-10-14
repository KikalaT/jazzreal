# -*- coding: utf-8 -*-

biography_dict = {\

'Charlie Parker':\
('American jazz saxophonist and composer. Born: 29 Aug 1920 in Kansas City, Kansas, USA. Died: 12 March 1955 in New York City, New York, USA (aged 34).\
Best known as simply \'Bird\' (a shortening of \'Yardbird\', Parker acquired the nickname early in his career with many contradictory stories regarding the name\'s origin). Widely considered to be one of the most influential of jazz saxophonists, jazz musicians, and indeed musicians in general.\
'),\

'Sonny Stitt':\
('American jazz musician, playing the alto and the tenor saxophone.\
Born: February 2, 1924, Boston, Massachusets, U.S.A.\
Died: July 22, 1982, Washington, D.C., U.S.A.\
Sonny Stitt established himself on the American jazz scene in the 60\'s before making an impact on the UK jazz funk scene during the mid-70\'s.\
Prior to these recordings, Sonny Stitt recorded in the 40\'s for [a=Tiny Bradshaw]\'s band.\
')

}

class biography:

	def init_biographyDB(self):
		biography.DB = []
		biography.DB = biography_dict
		return biography.DB
