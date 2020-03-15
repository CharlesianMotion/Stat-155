def make_binary_dict(x):
	binary = {}
	i = 0
	while x > 0:
		x, binary[i] = x//2, x%2
		i += 1
	return binary


def nim_add_bi_dict(a,b):
	summ = {}
	maxx = max(len(a),len(b)) 
	minn = min(len(a),len(b)) 
	for i in range(0,minn):
		summ[i] = (a[i] + b[i]) % 2
	if len(a) > len(b):
		for i in range(minn,maxx):
			summ[i] = a[i]
	elif len(a) < len(b):
		for i in range(minn,maxx):
			summ[i] = b[i]

	return summ


def keep_values_then_reverse(d):
	listt = d.values()
	listt.reverse()
	return listt


def nim_sum(*args):
	result = {0:0}
	for i in args:
		result = nim_add_bi_dict(make_binary_dict(i),result)
	return keep_values_then_reverse(result)



josh = nim_sum(9,3)
print(josh)






