import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
import heapq

X = np.array([[5, 3],
              [10, 15],
              [15, 12],
              [24, 10],
              [30, 30],
              [85, 70],
              [71, 80],
              [60, 78],
              [70, 55],
              [80, 91], ])


class HierarchicalClustering:
    def __init__(self, data, k):
        """
        :param data: input data
        :param k: split data into k clusters
        """
        self.data = data
        self.k = k
        self.dimension = len(data)
        assert 0 < self.k < self.dimension

    def translate(self, cluster_records):
        partition = cluster_records[-self.k]
        clusters = set(partition)
        result = partition
        for i, c in enumerate(clusters):
            for j, v in enumerate(partition):
                if v == c:
                    result[j] = i
        return result

    def show_data(self):
        plt.subplot(1, 2, 1)
        plt.scatter(X[:, 0], X[:, 1])
        plt.xticks(X[:, 0])
        for a, b, c in zip(X[:, 0], X[:, 1], range(len(X))):
            plt.annotate(
                '(%s)' % str(int(c) + 1), xy=(a, b), xytext=(-20, 10), textcoords='offset points'
            )

    def visualize(self, label):
        colors = ['b', 'g', 'r', 'orange']
        self.show_data()
        plt.subplot(1, 2, 2)
        for i, v in enumerate(set(label)):
            x, y = self.data[label == v, 0], self.data[label == v, 1]
            plt.scatter(x, y, c=colors[i])
        plt.show()

    def pairwise_distances(self):
        """
        :return: priority_queue [(dist, [index1, index2]), ...]
        """
        result = []
        for i in range(self.dimension):
            for j in range(i + 1, self.dimension):
                dist = euclidean(self.data[i], self.data[j])
                result.append((dist, [i, j]))
        return result

    def single_link_clustering(self):
        """
        :return: labels of each point . eg. [1, 0, 0, 1, 1, 1] if clusters=2, dimension=6
        """
        distances = self.pairwise_distances()
        heapq.heapify(distances)
        length = len(distances)
        cluster_record = [[i for i in range(self.dimension)]]
        while len(cluster_record) <= length:
            dist, point_index = heapq.heappop(distances)
            print('Merge {} {} {}{}, dist {}'.format(point_index[0], point_index[1],
                                                     self.data[point_index[0]],
                                                     self.data[point_index[1]], dist))
            record = np.array([i for i in cluster_record[-1]])
            if sum(record == record[point_index[0]]) > sum(record == record[point_index[1]]):
                for i, v in enumerate(record == record[point_index[1]]):
                    if v:
                        record[i] = record[record[point_index[0]]]
            else:
                for i, v in enumerate(record == record[point_index[0]]):
                    if v:
                        record[i] = record[record[point_index[1]]]
            cluster_record.append(list(record))

        result = []
        for record in cluster_record:
            if record not in result:
                result.append(record)
        result = self.translate(result)
        self.visualize(np.array(result))
        return result


def main():
    hc = HierarchicalClustering(X, k=2)
    label = hc.single_link_clustering()
    print(label)


if __name__ == '__main__':
    main()
