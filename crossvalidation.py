import pandas as pd
import warnings
import os
import numpy as np
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import average_precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.utils.multiclass import unique_labels
import matplotlib.pyplot as plt

lb = LabelBinarizer()

warnings.simplefilter(action='ignore', category=FutureWarning)

train_data_path = '../cancer-data-train.csv'
test_data_path = '../cancer-data-test.csv'

trainData = pd.read_csv(train_data_path, header=None)
testData = pd.read_csv(test_data_path, header=None)
X_train, Y_train = trainData.iloc[:, :-1], trainData.iloc[:, -1]
X_test, Y_test = testData.iloc[:, :-1], testData.iloc[:, -1]
class_name = unique_labels(Y_train)
Y_train, Y_test = lb.fit_transform(Y_train).flatten(), lb.fit_transform(Y_test).flatten()


def svm_configure():
    C = [0.01, 0.1, 1, 10, 100]
    average_f = []

    plt.xlabel('C')
    plt.xticks(C)
    plt.ylabel('Average F1')
    for c in C:
        clf = SVC(kernel='linear', C=c)

        scores = cross_val_score(
            clf, X_train, Y_train, cv=10, scoring='f1',
        )
        average_f.append(scores.mean())
    best_c = C[int(np.argmax(average_f))]
    plt.plot(C, average_f)
    plt.show()
    return best_c


def dt_configure():
    criterion = ['gini', 'entropy']
    K = [2, 5, 10, 20]
    best_k = []
    for i, c in enumerate(criterion):
        average_f = []
        plt.subplot(1, 2, i + 1)
        plt.title(c if i == 0 else 'IG')
        plt.xlabel('K')
        plt.xticks(K)
        plt.ylabel('Average F1')
        for k in K:
            clf = DT(criterion=c, max_leaf_nodes=k)
            scores = cross_val_score(
                clf, X_train, Y_train, cv=10, scoring='f1'
            )
            average_f.append(scores.mean())
        best_k.append(K[int(np.argmax(average_f))])
        plt.plot(K, average_f)
    plt.show()
    return best_k[0], best_k[1]


def compare_clf():
    c_for_svm = svm_configure()
    k_for_gini, k_for_ig = dt_configure()
    classifier = [
        SVC(kernel='linear', C=c_for_svm),
        DT(criterion='gini', max_leaf_nodes=k_for_gini),
        DT(criterion='entropy', max_leaf_nodes=k_for_ig),
        LDA()
    ]

    p, r, f = [], [], []
    metrics = ['average_precision_score', 'recall_score', 'f1_score']
    for i, clf in enumerate(classifier):
        y_pred = clf.fit(X_train, Y_train).predict(X_test)
        plot_confusion_matrix(Y_test, y_pred, classes=class_name, idx=i + 1)
        precision, recall, f1 = average_precision_score(Y_test, y_pred), \
                                recall_score(Y_test, y_pred, 'weighted'), \
                                f1_score(Y_test, y_pred, 'weighted')
        p.append(precision)
        r.append(recall)
        f.append(f1)
    plt.show()
    for j in range(3):
        plt.subplot(1, 3, j + 1)
        plt.bar(range(4), p)
        plt.xlabel(['SVM', 'DT-gini', 'DT-IG', 'LDA'])
        plt.title(metrics[j])
    plt.show()


def plot_confusion_matrix(y_true, y_pred, classes,
                          cmap=plt.cm.Blues, idx=0):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    clf_name = ['SVM', 'DT-gini', 'DT-IG', 'LDA']
    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           ylabel='True label',
           title=clf_name[idx - 1],
           xlabel='Predicted label'),

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


def main():
    # svm_configure()
    # dt_configure()
    compare_clf()


if __name__ == '__main__':
    main()
