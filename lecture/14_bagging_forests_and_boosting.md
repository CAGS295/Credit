# Bagging, Random Forests, Boosting
---
## Bootstrap
* Suppose we have a model fit to a stet of training data. We denote the training set by $\mathrm{Z} = (z_1, z_2, ..., z_N)$ where $z_i = (x_i, y_i)$.
* Randomly draw datasetws with __replacement__ from the training data, the same size as the original data. This is done B times.
* Refit the model to each bootstrap datasets.
* $S(\mathrm{Z})$ is any quantity computed from the data $Z$. From the bootstrap sampling we can estimate any aspect of the distribution of $S(\mathrm{Z})$. For example:
$$\hat\sigma[S(\mathrm{Z})]^2 = \frac{1}{B-1}\sum_{b=1}^B(S(\mathrm{Z}^{*b}) - S^*))^2 $$

---
## Bagging
We could calculate $\hat f^1(x), \hat f^2(x), ..., \hat f^B(x)$ using B separate traning sets, and average them to obtain a single low variance statistical learning model, given by

$$\hat f_{avg}(x) = \frac{1}{B}\sum_{b=1}^{B}\hat f^b(x)$$

---
## Random Forest
* Random forests provide an improvement over bagged trees by way of a small tweak that decorrelates the trees. As in bagging, we build a number of decision trees on bootstrapped training samples.
* But when building these decision trees, each time a split in a tree is considered, a random sample of $m$ predictors is chosen as split candidates from the full set of $p$ predictors. The split is allowed to use only one of those $m$ predictors. 
* A fresh sample of m predictors is taken at each split, and typically we choose $m \approx \sqrt p$ that is, the number of predictors considered at each split is approximately equal to the square root of the total number of predictors.

---
## Boosting
1. Set $\hat f(x)$ and $r_i=y_i$ for all $i$ in the training set.
2. For $b = 1,2,...,B$, repeat:
   1. Fit a tree $\hat f^b$ with $d$ splits ($d+1$ terminal nodes) to the training data $(X, r)$
   2. Update $\hat f$ by adding in a shrunken verson fo the new tree: $\hat f(x) \leftarrow \hat f(x) + \lambda\hat f^b(x)$
   3. Update the residuals: $r_i \leftarrow r_i - \lambda\hat f^b(x_i)$
3. Output the boosted model:
    $$\hat f(x) = \sum_{b=1}^B \lambda\hat f^b(x)$$