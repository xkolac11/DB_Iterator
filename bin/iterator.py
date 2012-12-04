#! /usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import Connection

db_connection = Connection('localhost')
search_params = "weight > 30", "name = orange"

class project:

	def __init__(self,db_connection,search_params):
		"""
		Pripojeni k databazi, zpracovani search_params
		"""
		db = db_connection['example']
		print search_params

	def set_search_params(search_params):
		pass

	def get_search_params():
		pass

	def find_all_projects():
		pass


# end of class project

#zavolame tridu pro testovani
project(db_connection,search_params)
