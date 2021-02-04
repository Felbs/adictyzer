from utils import *


def read_csv(file, encoding="utf-8", sep=","):

	""" read_csv() turns a csv file into a python dictionary """

	doc = open(file, encoding=encoding).read()

	lines = doc.split('\n')
	lines.remove('')

	words = [l.split(sep) for l in lines]

	tab = {k: [] for k in words.pop(0)}

	for k in tab:
		for l in words:
			tab[k].append(l.pop(0))

	return tab

	del([doc, lines, words,  tab])


def gind(ind, datadict):

	""" gind(): 'getindex', get chosen index for all keys in dictionary"""

	result = []

	if isinstance(ind, int):

		result.clear()

		for k in datadict:
			result.append(datadict[k][ind])

		return result
	
def gindl(ind, datadict):

	""" gindl() receives a list of indexes and returns a list containing lists of all given indexes """

	if isinstance(ind, list):

		results = []

		for i in ind:
			results.append(gind(i, datadict))

		return results
