# How to find frequent patterns from fp tree

## Intuitively Idea

* Find all frequent patterns containing one of its items
* Find all frequent patterns containing next item **BUT NOT** containing previous one



![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_FP_mining_1.png )



## Find conditional pattern base for 'P'

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_FP_mining_2.png )



We can get {m:2, a:2, c:2, f:2} and {b:1, c:1} which is CPB(conditional pattern base for 'p')

***To find all the frequent patterns containing 'p' , we need to find all the frequent patterns in the CPS of 'p' and then add 'p' to them***

### Recursively construct FP tree to find frequent patterns

* First filter all items <= min_support like we do in the first place

  * We get {c:3}, so generate frequent patterns by adding 'p' to it,
  * frequent patterns are {c:3, cp:3}

* Another more complex example

  * patterns with 'm' but not 'p'

  * First find all the path that contain 'm' but not 'p'

    * {f:4, c:3, a:3, m:2}, {f:4, c:3, a:3, b:1, m:1}

  * get PCB of m

    * {f:2, c:2, a:2} {f:1, c:1, a:1, b:1}

  * **build conditional FP tree base on PCB of m**

    * filter item that violates min_support requirement, we get {f:3, c:3, a:3}
* ![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_FP_mining_cpb_tree.png )
    * Recursively do the same process until there is one item left in the conditional tree



参考

>  http://www.cis.hut.fi/Opinnot/T-61.6020/2008/fptree.pdf 