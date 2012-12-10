#! /usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import Connection

connection = Connection('localhost')
db_connection = connection.example


class project:

	test={}
	array=[]
	
	def __init__(self, db_connection, search_params, database):	
		"""
		Connection to database and setting parameters, by which we search.
		"""
		
		self._database = database
		self._db_connection = db_connection
		self.set_search_params(search_params)
		
	def set_search_params(self,search_params):
		"""
		Saves searching parameters.
		"""
		self.test = search_params

	def get_search_params(self):
		"""
		Returns dict, which contains searching parameters.
		"""
		return self.test

	def find_all_projects(self):
		"""	
		Loads items from database.
		At first, loads 20 items, then next 20 etc.
		Always returns one item, calling of yield is used.
		"""
		
		db = self._db_connection[self._database]

		fin = db.count()
		
		varskip = 0
		varlimit = 20
		
		while varskip <= fin:
		
			target = db.find(self.test).limit(varlimit).skip(varskip)
			for item in target:
				self.array.append(item)
				yield (item)
			
			varskip += varlimit
	
# end of class project

  
