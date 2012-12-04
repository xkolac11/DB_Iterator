#! /usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import Connection

connection = Connection('localhost')
db_connection = connection.example


class project:

	test={}
	array = []
	
	def __init__(self, db_connection, search_params, database):
		self._database = database
		self._db_connection = db_connection
		self.set_search_params(search_params)
		
	def set_search_params(self,search_params):
		self.test = search_params

	def get_search_params(self):
		return self.test

	def find_all_projects(self):
			
		db = self._db_connection[self._database]

		target = db.find(self.test).limit(20)
		for item in target:
			self.array.append(item)
			yield (item)
		

	
	
# end of class project

#zavolame tridu pro testovani
obj = project(db_connection, {"weight": {'$gt' : 10}, "item": "apple"}, "export")
for var in obj.find_all_projects():
  print var
  
