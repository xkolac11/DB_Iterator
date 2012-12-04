#! /usr/bin/python
# -*- coding: utf-8 -*-

""" file that inserts random data to database example
	@author Petr Kolacek
	@email xkolac11@stud.fit.vutbr.cz
"""

from pymongo import *
import random

#connection to database 'example'
connection = Connection('localhost') 
db = connection.example

#delete all from collection'export'
db.export.remove()


fruits=['apple','pear','banana','orange','peach','apricot','strawberry','raspberry','kiwi','cherry','blueberry','mango','grapes','plum','lemon','ananas']
countries=['CZE','ESP','ITA','FRA','ENG','GER','GRE','SVK','PLN','FIN','SWE','MAL','CRO','SLO']

i = 0
while (i != 100):
	fruit = random.randint(0,(len(fruits) -1))
	country = random.randint(0,(len(countries) - 1))
	kilos = random.randint(1,100)
	fr = fruits[fruit]
	ctr = countries[country]
	db.export.insert({ '_id': i, 'item': fr, 'country': ctr, 'weight': kilos})
	i = i + 1

#uncomment to print inserted items (with some defined query)
#"""
target = db.export.find({ 'weight': 50 })
j = 0
for x in target:
	j += 1
	print x

print "query count",j
print db.export.count()
#"""
