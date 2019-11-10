import numpy as np
import math
import os

def IG(D, index, value):
	"""Compute the Information Gain of a split on attribute index at value
	for dataset D.
	
	Args:
		D: a dataset, tuple (X, y) where X is the data, y the classes
		index: the index of the attribute (column of X) to split on
		value: value of the attribute at index to split at

	Returns:
		The value of the Information Gain for the given split
	"""
	X, y = D[0], D[1]
	D_conc = np.concatenate((np.array(X), np.array([[v] for v in y])), axis=1)
	N, N_1 = len(D_conc), sum(D_conc[:, -1])
	H_D = sum([-N_1/N*math.log2(N_1/N), -(N-N_1)/N*math.log2((N-N_1)/N)])

	D_Y, D_N = D_conc[D_conc[:, index]<=value, :], D_conc[D_conc[:, index]>value, :]
	N_Dy, N_Dy1, N_Dn, N_Dn1 = len(D_Y), sum(D_Y[:, -1]), len(D_N), sum(D_N[:, -1])

	if N_Dy == N or N_Dn == N:
		return 0


	H_Dy = sum([0 if N_Dy1 == 0 else -(N_Dy1/N_Dy)*math.log2(N_Dy1/N_Dy), 0 if N_Dy == N_Dy1 else -((N_Dy-N_Dy1)/N_Dy)*math.log2((N_Dy-N_Dy1)/N_Dy)])
	H_Dn = sum([0 if N_Dn1 == 0 else -(N_Dn1/N_Dn)*math.log2(N_Dn1/N_Dn), 0 if N_Dn == N_Dn1 else -((N_Dn-N_Dn1)/N_Dn)*math.log2((N_Dn-N_Dn1)/N_Dn)])

	H_Dy_Dn = N_Dy/N*H_Dy + N_Dn/N*H_Dn

	Information_gain = H_D - H_Dy_Dn

	return Information_gain


	


def G(D, index, value):
	"""Compute the Gini index of a split on attribute index at value
	for dataset D.

	Args:
		D: a dataset, tuple (X, y) where X is the data, y the classes
		index: the index of the attribute (column of X) to split on
		value: value of the attribute at index to split at

	Returns:
		The value of the Gini index for the given split
	"""
	X, y = D[0], D[1]
	D_conc = np.concatenate((np.array(X), np.array([[v] for v in y])), axis=1)
	# N represent the number of sample,N_1 represents the number of sample belong to class 1
	N, N_1 = len(D_conc), sum(D_conc[:, -1])

	D_Y, D_N = D_conc[D_conc[:, index]<=value, :], D_conc[D_conc[:, index]>value, :]
	N_Dy, N_Dy1, N_Dn, N_Dn1 = len(D_Y), sum(D_Y[:, -1]), len(D_N), sum(D_N[:, -1])

	if N_Dy == N:
		return 1-sum([(N_Dy1/N_Dy)**2, ((N_Dy-N_Dy1)/N_Dy)**2])
	if N_Dn == N:
		return 1-sum([(N_Dn1/N_Dn)**2, ((N_Dn-N_Dn1)/N_Dn)**2])

	G_Dy, G_Dn = 1-sum([(N_Dy1/N_Dy)**2, ((N_Dy-N_Dy1)/N_Dy)**2]), 1-sum([(N_Dn1/N_Dn)**2, ((N_Dn-N_Dn1)/N_Dn)**2])
	G_Dy_Dn = (N_Dy/N)*G_Dy + (N_Dn/N)*G_Dn

	return G_Dy_Dn

	


def CART(D, index, value):
	"""Compute the CART measure of a split on attribute index at value
	for dataset D.

	Args:
		D: a dataset, tuple (X, y) where X is the data, y the classes
		index: the index of the attribute (column of X) to split on
		value: value of the attribute at index to split at

	Returns:
		The value of the CART measure for the given split
	"""
	X, y = D[0], D[1]
	D_conc = np.concatenate((np.array(X), np.array([[v] for v in y])), axis=1)
	N, N_1 = len(D_conc), sum(D_conc[:, -1])
	D_Y, D_N = D_conc[D_conc[:, index]<=value, :], D_conc[D_conc[:, index]>value, :]
	N_Dy, N_Dy1, N_Dn, N_Dn1 = len(D_Y), sum(D_Y[:, -1]), len(D_N), sum(D_N[:, -1])
	
	if N_Dy == N or N_Dn == N:
		return 0

	CART_Dy_Dn = 2*(N_Dy*N_Dn/(N**2))*sum([abs(N_Dy1/N_Dy - N_Dn1/N_Dn), abs((N_Dy-N_Dy1)/N_Dy - (N_Dn-N_Dn1)/N_Dn)])

	return CART_Dy_Dn
	


def bestSplit(D, criterion):
	"""Computes the best split for dataset D using the specified criterion

	Args:
		D: A dataset, tuple (X, y) where X is the data, y the classes
		criterion: one of "IG", "GINI", "CART"

	Returns:
		A tuple (i, value) where i is the index of the attribute to split at value
	"""

	#functions are first class objects in python, so let's refer to our desired criterion by a single name
	best, best_index, best_value = 0 if criterion != 'G' else float('inf'), 0, 0
	X, y = D[0], D[1]
	
	# res = []
	for i in range(len(X[0])):
		for v in set(np.array(X)[:, i]):
			measure_value = eval(criterion)(D, i, v)
			if criterion == 'G':
				if measure_value <= best:
					best = measure_value
					best_index, best_value = i, v
			else:
				if measure_value >= best:
					best = measure_value
					best_index, best_value = i, v

	print('best measure {}: {}'.format(criterion, best))

	return (best_index, best_value)



def load(filename):
	"""Loads filename as a dataset. Assumes the last column is classes, and 
	observations are organized as rows.

	Args:
		filename: file to read

	Returns:
		A tuple D=(X,y), where X is a list or numpy ndarray of observation attributes
		where X[i] comes from the i-th row in filename; y is a list or ndarray of 
		the classes of the observations, in the same order
	"""
	X, y = [], []
	with open(filename) as f:
		for line in f.readlines():
			X.append([float(v) for v in line.strip().split(',')[:-1]])
			y.append(int(line.strip().split(',')[-1]))
	D = (X, y)
	return D



def classifyIG(train, test):
	"""Builds a single-split decision tree using the Information Gain criterion
	and dataset train, and returns a list of predicted classes for dataset test

	Args:
		train: a tuple (X, y), where X is the data, y the classes
		test: the test set, same format as train

	Returns:
		A list of predicted classes for observations in test (in order)
	"""
	correct = 0
	best = bestSplit(train, 'IG')
	best_index, best_value = best[0], best[1]

	D_conc = np.concatenate((np.array(train[0]), np.array([[v] for v in train[1]])), axis=1)
	class_less_best_value = 1 if sum(D_conc[D_conc[:, best_index]<=best_value, -1]) >= len(D_conc[D_conc[:, best_index]<=best_value, -1])/2 else 0
	print('best split for IG is {} class_less_best_value is {}'.format(best, class_less_best_value))
	
	res = []
	for i, sample in enumerate(test[0]):
		predict = class_less_best_value if sample[best_index] <= best_value else class_less_best_value^1
		res.append(predict)
		if predict == test[1][i]:
			correct += 1
	print('Test Accuracy {}'.format(correct / len(test[1])))
	return res



def classifyG(train, test):
	"""Builds a single-split decision tree using the GINI criterion
	and dataset train, and returns a list of predicted classes for dataset test

	Args:
		train: a tuple (X, y), where X is the data, y the classes
		test: the test set, same format as train

	Returns:
		A list of predicted classes for observations in test (in order)
	"""
	correct = 0
	best = bestSplit(train, 'G')
	best_index, best_value = best[0], best[1]


	D_conc = np.concatenate((np.array(train[0]), np.array([[v] for v in train[1]])), axis=1)
	class_less_best_value = 1 if sum(D_conc[D_conc[:, best_index]<=best_value, -1]) >= len(D_conc[D_conc[:, best_index]<=best_value, -1])/2 else 0

	print('best split for GINI is {} class_less_best_value is {}'.format(best, class_less_best_value))
	
	res = []
	for i, sample in enumerate(test[0]):
		# predict = int(sample[best_index]<=best_value)^1
		predict = class_less_best_value if sample[best_index] <= best_value else class_less_best_value^1
		res.append(predict)
		if predict == test[1][i]:
			correct += 1
	print('Test Accuracy {}'.format(correct / len(test[1])))
	return res


def classifyCART(train, test):
	"""Builds a single-split decision tree using the CART criterion
	and dataset train, and returns a list of predicted classes for dataset test

	Args:
		train: a tuple (X, y), where X is the data, y the classes
		test: the test set, same format as train

	Returns:
		A list of predicted classes for observations in test (in order)
	"""
	correct = 0
	best = bestSplit(train, 'CART')
	best_index, best_value = best[0], best[1]

	D_conc = np.concatenate((np.array(train[0]), np.array([[v] for v in train[1]])), axis=1)
	class_less_best_value = 1 if sum(D_conc[D_conc[:, best_index]<=best_value, -1]) >= len(D_conc[D_conc[:, best_index]<=best_value, -1])/2 else 0
	print('best split for CART is {} class_less_best_value is {}'.format(best, class_less_best_value))

	res = []
	for i, sample in enumerate(test[0]):
		predict = class_less_best_value if sample[best_index] <= best_value else class_less_best_value^1
		res.append(predict)
		if predict == test[1][i]:
			correct += 1
	print('Test Accuracy {}'.format(correct / len(test[1])))
	return res



def main():
	"""This portion of the program will run when run only when main() is called.
	This is good practice in python, which doesn't have a general entry point 
	unlike C, Java, etc. 
	This way, when you <import HW2>, no code is run - only the functions you
	explicitly call.
	"""
	train_file_name, test_file_name = './train.txt', './test.txt'
	train_file, test_file = load(train_file_name), load(test_file_name)


	print('result of testsets for IG: {}\ntrue label of testsets {}\n============='.format(classifyIG(train_file, test_file), test_file[1]))
	print('result of testsets for GINI: {}\ntrue label of testsets {}\n============='.format(classifyG(train_file, test_file), test_file[1]))
	print('result of testsets for CART: {}\ntrue label of testsets {}\n============='.format(classifyCART(train_file, test_file), test_file[1]))

	


if __name__=="__main__": 
	"""__name__=="__main__" when the python script is run directly, not when it 
	is imported. When this program is run from the command line (or an IDE), the 
	following will happen; if you <import HW2>, nothing happens unless you call
	a function.
	"""
	main()