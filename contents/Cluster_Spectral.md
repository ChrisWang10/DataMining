# Spectral Clustering

## graph partition

1. how to define a good partition

   ![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Cluster_Spectral.png )

   1. Maximize the number of within group connections
   2. Minimize the between-group connections

2. **criterion**

   1. Normalize cuts

      ![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Cluster_Spectral_criterion.png )**asso(A, V) is the total connection from nodes in A to all the nodes in the graph**

      ![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Cluster_Spectral_criterion_example.png )

   2. Ratio cuts

      Change asso(A, V) and asso(B, V) by the size of each partitions(the number of nodes in each partition)

   ***we can see ratio cut is the special case of Ncut by assign all the weights between nodes into 1.***



## Spectral Solution

#### 1. Use matrix to represent the graph

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Cluster_Spectral_adjacent_matrix.png )

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Cluster_Spectral_degree_matrix.png )

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Cluster_Spectral_Laplacian_matrix.png )



#### 2. Decomposition

​	compute eigenvalues and eigenvectors of the matrix

​	**the eigenvalues represent how tightly connected the nodes are in the graph** 

​	Map each point to a lower-dimensional representation based on one or more eigenvectors.

#### 3. TO DO

