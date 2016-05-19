def binomial(n):
	if n == 0:
		coefficients_n = [1]
	else:
		coefficients_n = []
		coefficients_n.append(1)
		previous = binomial(n-1)
		for i in range(1, n):
			term = previous[i-1] + previous[i]
			coefficients_n.append(term)
		coefficients_n.append(1)
	return coefficients_n