# Data Mining

## 1. LDA

**LDA** is a linear classification model

IDEA:

​	Find a projection that maximizes the separation between classes, we want projected classes to be well separated and the projected classes to be compact, like this

![LDA]( https://github.com/ChrisWang10/DataMining/raw/master/img/LDA_1.png 'LDA')

### 1.1 well separated

Enforce separation of projected class means, we want $|m_1 - m_2|$ as large as possible

$m1, m_2$ are coordinates in the new axis, $w$ is the projection vector and $u_1,u_2$ are mean vector of each classes, the $m_1 = w^T * u_1$. (how do we get this?)

In this case, if want project $v$ onto $u$, then we can define the red line as $p$, so 

$\cos\theta=|p|/|v|$

and $\cos\theta = v^T*u/(|v|*|u|$, then we can get

$|p|/|v| = v^T*u/(|v|*|u|)$

$|p| = v^T*u/|u|$

$p = |p|*u/|u|=v^T*u/|u|*|u|$ and if u is a unit vector, then

$p = v^T*u$



![projection]( https://github.com/ChrisWang10/DataMining/raw/master/img/LDA_2.png )

### 1.2 compact











