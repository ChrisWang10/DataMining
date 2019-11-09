import matplotlib.pyplot as plt
import numpy as np

y = [1, 1, 1, 1, 1, -1, -1, -1, -1, 1]
hx = [5.0, 3.8, 2.8, -16.8, -4.3, -2.2, -5.7, 0.7, 6.8, -2.2]


def roc_pr(label, score, mode='roc'):
    sorted_index = np.argsort(score)[::-1]
    sorted_score = [hx[i] for i in sorted_index]
    sorted_label = [label[i] for i in sorted_index]

    tpr, fpr, precision = [], [], []
    for i, s in enumerate(sorted_score):
        predict = [1 if v >= s else -1 for v in sorted_score]
        true_positive = sum([1 if predict[j] == 1 and sorted_label[j] == 1 else 0 for j in range(len(predict))])
        true_negative = sum([1 if predict[j] == -1 and sorted_label[j] == -1 else 0 for j in range(len(predict))])
        false_negative = sum([1 if predict[j] == -1 and sorted_label[j] == 1 else 0 for j in range(len(predict))])
        false_positive = sum([1 if predict[j] == 1 and sorted_label[j] == -1 else 0 for j in range(len(predict))])
        tpr.append(true_positive / (true_positive + false_negative))
        fpr.append(false_positive / (false_positive + true_negative))
        precision.append(true_positive / (true_positive + false_positive))
    if mode == 'roc':
        plt.xlabel('fpr')
        plt.ylabel('tpr')
        plt.plot(fpr, tpr)
    else:
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.plot(tpr, precision)
    plt.show()


if __name__ == '__main__':
    roc_pr(y, hx, 'pr')
