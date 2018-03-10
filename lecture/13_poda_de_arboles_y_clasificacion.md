# Tree Pruning
Cost complexity:

For each value of $\alpha$ there corresponds a subtree $T \subset T_0$ such that

$$\sum_{m=1}^T \sum_{i: x_i \in R_m} (y_i - \hat y_{R_m})^2 + \alpha |T|$$

is as small as possible. $|T|$ indicates the number of terminal nodes of the tree $T$, $R_m$ is the rectangle (i.e. the subset of predictor space) corresponding to the $m$th terminal node, and $\hat y_{R_m}$ is the predicted response associated with $R_m$. 

---
# Tree Pruning
* To find $T_\alpha$ we use __weakest link prunning__: we successively collapse the internal node that produces the smallest per-node increase in
$$\sum_m N_m Q_m(T)$$
and continue until we produce the single-node (root) tree.
This gives a _finite_ sequence of subtrees, and one can show this sequence must contain $T_\alpha$
[Pattern Recognition and Neural Networks. B.D. Ripley (1996)](http://www.stats.ox.ac.uk/~ripley/PRbook/)

---
# Building a Regression Tree
1.- Use __recursive binary splitting__ to grow a large tree on the training data, stopping only when each terminal node has fewer than some minimim number of observations. 
2.- Apply cost complexity prunnig to the large tree in order to obtain a sequence of best subtrees, as a function of $\alpha$  
3.- Use the _validation_ set to choose $\alpha$

---
# Tree Models
* What is the model space?
* What is the training method?

---
# Classification Trees

* In the classification setting, RSS cannot be used as a criterion for making the binary splits.

A natural alternative to RSS is the classification error rate. Since we plan to assign an observation in a given region to the most commonly occurring error rate class of training observations in that region, the classification error rate is simply the fraction of the training observations in that region that do not belong to the most common class.

---
# Classification error rate
$$E = 1- \mathrm{max}_k(\hat p_{mk})$$

$\hat p_{mk}$ represents the proportion of training observations in the $m$th region that are from the $k$th class.

* However, it turns out that classification error is not sufficiently sensitive for tree-growing, and in practice two other measures are preferable.

---
# Criterions for classification trees
* Gini index, a measure of total variance across the $K$ classes.
$$G = \sum_{k=1}^K \hat p_{mk}(1-\hat p_{mk})$$

* Cross entropy

$$ D = -\sum_{k=1}^K \hat p_{mk}\log \hat p_{mk} $$
---
# Advantages and Disadvatages of Trees
* Trees are very easy to explain to people. (Maybe even easier than linear regression)
* Some people believe that decision trees more closely mirror human decision-making than do other regression/classificiation approaches.
* Trees can be displayed graphically, and are easily interpreted even by a non-expert (especially if they are small).
* Generally do not have the same level of predictive accuracy.
    