import matplotlib.pyplot as plt
import numpy as np
import random
import os

data_path = './data/kmeans_data.txt'


def kmeans(k=3):
    data = []
    with open(data_path, 'r') as f:
        for line in f.readlines():
            data.append([float(v) for v in line.strip().split('   ')])
    # 1. choose k centroids randomly
    k_centroids = np.array(random.sample(data, k))
    data = np.array(data)

    # 2. assign each nodes to the k centroids based on distance to the centroids

    while True:
        cluster = {}
        for sample in data:
            distance = []
            for i, centroid in enumerate(k_centroids):
                distance.append(np.linalg.norm(sample - centroid))
            which_class = np.argsort(np.array(distance))[0]
            if which_class not in cluster:
                cluster[which_class] = [sample]
            else:
                cluster[which_class].append(sample)

        # 3. calculate new centroids of k clusters
        new_cluster_centroids = []
        for cluster_name in cluster.keys():
            new_cluster_centroids.append(np.mean(cluster[cluster_name], axis=0))
        if (np.array(k_centroids) == new_cluster_centroids).all():
            break
        else:
            k_centroids = new_cluster_centroids
            show_cluster(k_centroids, cluster)
    return k_centroids, cluster


def show_cluster(centroid_list, cluster_dict):
    color_mark = ['or', 'ob', 'og', 'ok', 'oy', 'ow']
    centroid_mark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw']

    plt.ion()
    for key in cluster_dict.keys():
        plt.plot(centroid_list[key][0], centroid_list[key][1], centroid_mark[key], markersize=12)  # 质心点
        for item in cluster_dict[key]:
            plt.plot(item[0], item[1], color_mark[key])
    plt.pause(1)
    plt.close()


if __name__ == '__main__':
    kmeans()
