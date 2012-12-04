#! /usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import Connection

db_connection = Connection('localhost')

search_params = {"weight": {'$gt' : 10}, "item": "apple"} #priklad

class project:

	def __init__(self,db_connection,search_params):

		db = db_connection.export
		self.params = search_params
		
		self.set_search_params(self.params)
		
		self.find_all_projects(db)
		
		
	def set_search_params(self,search_params):
		pass

	def get_search_params(self):
		return search_params

	def find_all_projects(self,db):
		
		"""
		load=[]
		
		target = db.find(search_params).limit(20)
		for item in target:
			load.append(item)
		
		for i in load:
			yield i
		"""
		pass
	
	
# end of class project

#zavolame tridu pro testovani
project(db_connection,search_params)
