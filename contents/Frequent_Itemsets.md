# Frequent Item-sets

**Support** of Itemset I: How many I appears in baskets

**Frequent Item-sets**:	sets of items that appear in at least some support threshold s.

## Association Rules

{a, b, c, d} -> e means if a basket contains {a, b, c, d} then it is likely to contain e

***Confident*** of this association = support( {a, b, c, d} U e) / support({a, b, c, d})

***Relative Support*** possibility that {a, b, c ,d} occurs

---

## Interesting Association Rules

### Not all high-confidence rules are interesting

If {breed, bears}, poker always occurs which means the confident of this rule is high

But if the fraction of the occurrence of poker in baskets is also high, then we don't care about it.

**Interest** = Confident -  fraction of baskets that contain j 



## Find frequent Item-sets



### Brute Force

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_bf.png )

### Apriori

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_Aprior.png )



#### Bottleneck of Apriori

 Multiple database scans are costly 

 Mining long patterns needs many passes of scanning and generates lots of candidates  

***  Can we avoid candidate generation  ***



## FP growth

Key Idea: Grow longer patterns from short ones in an 'educated ' manner

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_transi.png )

**FP-Tree Construction**

Use a FP-Tree to store all the transaction information we care

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_HeaderTable.png )

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_FP.png )





## How do we get find all frequent patterns from the FP-Tree 

+ Find all frequent patterns contains one of the items in the header table
+ Then find all frequent patterns contains the next item but **NOT** contains the previous one
+ until we are out of items



**Conditional pattern Base of item p**

Contains transactions in which p occurs

For I5, CPB = {{I2,I1:1}, {I2, I1, I3:1}}

For I4, CPB = {{I2,I1:1}, {I2:1}}

For I3, CPB = {{I2,I1:2}, {I2:2}, {I1:2}}

For I1, PCB = {{I2:4}}



**Build Conditional FP-trees **

For I5 => {I2:2, I1:2}  **I3 been deleted** because violate the minimum support value

For I4 => {I2:2}

For I3 => {I2:4, I1:2}, {I2:2}

For I1 => {I2:4}



**Generate Frequent Pattern**

![](https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_Cond.png)





## Maximal Frequent Item-sets

An item is maximal frequent item-set if none of its **immediate supersets** is frequent

## Negative Border

Item-sets are not frequent but all their immediate frequent sets are frequent



**Border**

 Positive Border + Negative Border 

 Either the positive, or the negative border is sufficient to summarize all frequent item-sets. 



##  Closed Itemset 

 An itemset is closed if none of its immediate supersets has the same support as the itemset 

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/Frequent_Itemsets_maximal.png )







