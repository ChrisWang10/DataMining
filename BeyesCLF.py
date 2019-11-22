import pandas as pd
import numpy as np
import math
import os
from numpy.linalg import inv
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelBinarizer
from sklearn.utils.multiclass import unique_labels

train_data_path = './data/cancer-data-train.csv'
test_data_path = './data/cancer-data-test.csv'


class Bayesian:
    def __init__(self):
        self.train, self.test = preprocess_data()
        self.unique_lables = unique_labels(self.train[1])
        self.prior, self.mean, self.covariance_matrix = [], [], []
        self.FullBayesFit()

    def FullBayesFit(self):
        n = self.train[0].shape[0]
        for label in self.unique_lables:
            class_specific_subsets = self.train[0].loc[self.train[1] == label, :]
            self.prior.append(class_specific_subsets.shape[0] / n)
            subsets_mean = class_specific_subsets.mean(axis=0)
            self.mean.append(subsets_mean)
            centered_data = class_specific_subsets - subsets_mean
            self.covariance_matrix.append(centered_data.T.dot(centered_data))
        self.evaluate()

    def NaiveBayesFit(self):
        pass

    def predict(self, x):
        """
        :param x: instance
        :return:  label
        """
        result = []
        for lable in self.unique_lables:
            result.append(self.prior[lable] * (1 / (np.sqrt(2 * math.pi) ** len(self.unique_lables) *
                                               np.sqrt(np.linalg.norm(self.covariance_matrix[lable])))) *
                          math.exp(-np.dot(np.dot(np.array(x - self.mean[lable]), inv(self.covariance_matrix[lable])),
                                           np.array(x - self.mean[lable]))
                                   ))
        return np.argmax(result)

    def evaluate(self):
        predict = []
        target = self.test[1].values
        for i in range(self.test[0].shape[0]):
            predict.append(self.predict(np.array(self.test[0].iloc[i, :])))
        accuracy = accuracy_score(target, predict)
        cm = confusion_matrix(target, predict)
        print(cm)
        print('accuracy is {}'.format(accuracy))


def preprocess_data():
    lb = LabelBinarizer()
    trainData, testData = pd.read_csv(train_data_path, header=None), pd.read_csv(test_data_path, header=None)
    X_train, Y_train = trainData.iloc[:, :-1], trainData.iloc[:, -1]
    X_test, Y_test = testData.iloc[:, :-1], testData.iloc[:, -1]
    Y_train_lb, Y_test_lb = lb.fit_transform(Y_train), lb.fit_transform(Y_test)
    return [X_train, pd.Series(np.squeeze(Y_train_lb))], [X_test, pd.Series(np.squeeze(Y_test_lb))]


def main():
    CLF = Bayesian()


if __name__ == '__main__':
    main()
