# DBSCAN

## Density Based Spatial Clustering of Applications with Noise

### Why DBSCAN

Clustering algorithm like K-Means and hierarchical clustering are only suited for compact , well separated data like dataset1

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/DBSCAN_data.png )



### What is DSCAN

this algorithm is density based, so we can define the range of density so wen can group nodes within the range together.

First, we need to define how large the distance within which we can scan,**eps**

Second, we need to decide how many points with **eps** radius are enough to be considered to be dense. **MinPts**, As a general rule, the minimum MinPts can be derived from the number of dimensions D in the dataset as, MinPts >=D+1

Therefore, we can get 3 types of nodes.

**Core points**

​	Nodes have more than MinPts points within its eps

**Border points**

​	Nodes that have fewer than MinPts within eps, but it is in the eps of a core point

**Noise**

​	not a core point, nor a border point

**directly density-reachable**

​	a, b is directly reachable if b is a core point and a is in the epsilon neighborhood of b

​	this relationship is not symmetrical , like a border and a core, border is directly density-reachable to core, but core is not directly density-reachable to border because border is not core.

**density-reachable**

​	a,b,c, are core points and d is border point, if b is directly density-reachable from a, c in directly density-reachable from b, then *c is density-reachable from a*, so as d(indirectly density-reachable from a). But a is not density-reachable from d because ***density-reachability is asymmetric*** either.

​	

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/DBSCAN_eps_update.png )

---

### How to Group nodes

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/DBSCAN_procedure.png )

### How to choose eps

**K distance graph**

 The idea is to calculate, the average of the distances of every point to its k nearest neighbors 

 Next, these k-distances are plotted in an ascending order. The aim is to determine the “knee”, which corresponds to the optimal *eps* parameter.

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/DBSCAN_eps_decide.png )





