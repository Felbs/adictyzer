from adicters import Adict, AdictList


def read_csv(file, encoding="utf-8", sep=","):

	""" read_csv() turns a csv file into a python dictionary """

	doc = open(file, encoding=encoding).read()

	lines = doc.split('\n')

	if '' in lines:
		lines.remove('')

	words = [l.split(sep) for l in lines]

	tab = Adict()

	for head in words.pop(0):
		tab[head] = AdictList()

	for k in tab:
		for l in words:
			tab[k].append(l.pop(0))



	return tab

	del([doc, lines, words,  tab])
