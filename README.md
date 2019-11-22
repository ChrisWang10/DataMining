# Data Mining

## 1. LDA

**LDA** is a linear classification model

IDEA:

​	Find a projection that maximizes the separation between classes, we want projected classes to be well separated and the projected classes to be compact, like this

![LDA]( https://github.com/ChrisWang10/DataMining/raw/master/img/LDA_1.png 'LDA')

### 1.1 well separated

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/LDA_explain.png )



![projection]( https://github.com/ChrisWang10/DataMining/raw/master/img/LDA_2.png )

### 1.2 compact means minimizes the class variances

$s_i=\sum_{x_i\in{D_i}}(a_i-m_i)^2$



## Fisher objective

$\arg\max_{w}J(w)=\frac{(m_1-m_2)^2}{{s_1}^2+{s_2}^2}$

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/LDA_objective.png )

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/LDA_objective1.png )

![]( https://github.com/ChrisWang10/DataMining/raw/master/img/LDA_in_steps.png )









