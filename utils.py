

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
