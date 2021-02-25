

def sum(lis):

	""" sum() sums all  elements of an list and returns the result as a string """

	sum = 0

	if isinstance(lis, list):

		treated_lis = [float(n) for n in lis]

		for number in treated_lis:
			sum += number

		return f"{sum:.2f}"
		del([sum, lis, treated_lis])
	else:

		print("This functions requires a list")


def avg(lis):

	""" avg() returns the arithmetic average of a list of values. returns a string """

	if isinstance(lis, list):

		su = sum(lis)
		le = len(lis)

		av = float(su) / float(le)

		return f"{av:.2f}"
		del([su, le, av])


def med(lis):

	""" """

	sor = sorted(lis)
	indexes = []

	if isinstance(lis, list):

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

