from adicters import Adict
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

	""" gindl() receives a list and a datadic(dict) and returns a list of lists containing the entire information of given indexes """

	if isinstance(ind, list):

		results = []

		for i in ind:
			results.append(gind(i, datadict))

		return results


def columns(datadict):

	if isinstance(datadict, dict):

		for key in datadict.keys():
			print(key, end=", ")

		print()
	else:

		print("columns receives a dictionary as argument. not {type(datadict)}")


def list_all(lis):

	""" liss(), receives and list and prints formated list indexes """

	if isinstance(lis, list):

		for element in lis:

			it = iter(element)

			for el in element:

				print(f'{next(it)}', end=" ")

			print()
	else:

		print(f"liss function receives a list as argument. not {type(lis)}")

