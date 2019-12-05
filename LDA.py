# the main idea of LDA is find a projection that
# can maximize inter-class variance and minimize intra-class distance
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelBinarizer
from sklearn.utils.multiclass import unique_labels

train_data_path = './data/cancer-data-train.csv'
test_data_path = './data/cancer-data-test.csv'


class LDA:
    def __init__(self, train, test):
        self.train = train
        self.test = test
        self.unique_classes = list(set(train['label']))
        self.projection = self.lda_fit()

    def lda_fit(self):
        specific_subsets = []
        centered_subsets = []
        u_s = []
        S = []
        for specific_class in self.unique_classes:
            # class specific subsets
            specific_subset = self.train[self.train['label'] == specific_class].iloc[:, :-1]
            specific_subsets.append(specific_subset)

            # class means
            u = np.mean(specific_subset, axis=0)
            u_s.append(u)
            center = specific_subset - u.T

            # center class matrix
            centered_subsets.append(center)

            # class scatter matrix, N*N N is # of features
            scatter_matrix = (center.T).dot(center)

            S.append(scatter_matrix)
        between_class_scatter_matrix = np.dot(np.array(u_s[0] - u_s[1]).reshape(len((u_s[0] - u_s[1])), 1),
                                              np.array(u_s[0] - u_s[1]).reshape(1, len((u_s[0] - u_s[1]))))
        within_class_scatter_matrix = S[0] + S[1]
        eigenvalue, eigenvector = np.linalg.eig(np.linalg.inv(np.array(within_class_scatter_matrix)) *
                                                between_class_scatter_matrix
                                                )
        return eigenvector[list(eigenvalue).index(max(eigenvalue))]


def preprocess_data():
    """
    :return: convert category to binary
    """
    lb = LabelBinarizer()
    trainData, testData = pd.read_csv(train_data_path, header=None), pd.read_csv(test_data_path, header=None)
    X_train, Y_train = trainData.iloc[:, :-1], trainData.iloc[:, -1]
    X_test, Y_test = testData.iloc[:, :-1], testData.iloc[:, -1]
    Y_train_lb, Y_test_lb = lb.fit_transform(Y_train), lb.fit_transform(Y_test)
    X_train['label'] = pd.Series(np.squeeze(Y_train_lb))
    X_test['label'] = pd.Series(np.squeeze(Y_test_lb))

    return X_train, X_test


def main():
    train, test = preprocess_data()
    LDA(train, test)
    # shape of train (2,) train[0] is data and train[1] is label


if __name__ == '__main__':
    main()
