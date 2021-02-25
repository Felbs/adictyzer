class Adict(dict):

	def __init__(self):

		self.result = []


	def cols(self):

		""" Returns columns (self.columns). """

		for col in self.keys():
			print(col, end=" ")

		print()


	def gind(self, ind):

		""" Returns choosen index of all columns. """

		if isinstance(ind, int):

			self.result.clear()

			for k in self:
				self.result.append(self[k][ind])

			return self.result



	def gindl(self, lis):

		""" Returns a list of lists. Each list contains indexes of all columns. """

		if isinstance(lis, list):

			for i in lis:
				self.result.append(self.gind(i))

			return self.result


class AdictList(list):

	def __init__(self):

		self.result = []


	def sum(self):

		""" """

		sum = 0

		try:

			treated_lis = list(map(lambda n: float(n), self))

			for number in treated_lis:
				sum += number

			return f"{sum:.2f}"

			del([sum, treated_lis])

		except ValueError:

			print(f"sum() only takes int, float or alphanumeric values, not {type(self[0])}")


	def mean(self):

		""" """

		try:

			su = sum(list(map(lambda n: float(n), self)))
			le = len(self)

			av = float(su) / float(le)

			return f"{av:.2f}"
			del([su, le, av])

		except ValueError:

			print(f"mean() takes only int, float or alphanumeric values, not {type(self[0])}")


	def med(self):

		""" """

		sor = sorted(self)
		indexes = []

		if isinstance(self, list):

			if len(sor) %2 == 0:

				for n in range(len(sor)):
					indexes.append(n)

				upper_val_index = int(len(indexes) / 2)
				lower_val_index = upper_val_index - 1

				upper = sor[upper_val_index]
				lower = sor[lower_val_index]

				return f'{(upper + lower) / 2}'

			else:

				le = len(sor)

				value_index = int(le / 2)

				return str(sor[value_index])
