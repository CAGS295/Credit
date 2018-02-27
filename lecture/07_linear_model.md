<!-- page_number: true -->

# The Linear Model
* Input representation
* Linear Classification
* Linear Regression
* Nonlinear Tranformation
    
---
# The non-linear-separable case
* Perceptron Learning Algorithm will not converge.
	- It will continue moving the boundary.
* Evolution of $E_{in}$ and $E_{out}$
	- Will continue changing.

---
# Evolution of $E_{in}$ and $E_{out}$
* From perceptron exercice

---
# The _pocket_ algorithm
* Put the best solution so far in your __pocket__
	- Stop after a defined number of iterations.

---
# Linear Regression
__regression == real-valued output.__
* We have our data:
	* Characteristics/features: $\mathrm{x}$
	* Credit line: $y$

---
# Credit again
* Classification: Credit approval (yes/no)
* Regression: Credit line (dollar amount)

Linear regression output:
$$h(x) = \sum_{i=0}^{d} w_i x_i = \mathrm{w}^\intercal \mathrm{x}$$

---
# The data set
Credit officers decide on credit lines:
$$(\mathrm x_1, y_1), (\mathrm x_2, y_2), ... , (\mathrm x_N, y_N)$$

$y_n \in R$ is the credit line for customer $\mathrm x_n$

Linear regression tries to estimate $f(\mathrm x)$

---
# How to measure the error
* How well does $h(\mathrm{x}) = \mathrm{w}^\intercal \mathrm{x}$ approximate $f(\mathrm{x})$?
* In linear regression, we use squared error $(h(\mathrm{x}) - f(\mathrm{x}))^2$

* in-sample error: 
 $$E_{in}(h) = \frac{1}{N} \sum_{i=0}^N (h(\mathrm x_n) - y_n)^2$$

---
# The espression for $E_{in}$
$$E_{in}(\mathrm{w}) = \frac{1}{N}\sum_{n=1}^{N} (\mathrm w^T \mathrm x_n - y_n)^2 
            = \frac{1}{N} | X\mathrm{w} - \mathrm{y} |^2$$

where, 
```
X = [ [x_11, x_12, ..., x_1n],
      [x_21, x_22, ..., x_2n],
      ...
      [x_N1, x_N2, ..., x_Nn] ]

y = [ [y_1],
      [y_2],
      ...,
      [y_n] ]
```

---
# Minimizing $E_{in}$
$$ E_{in} = \frac{1}{N} | X\mathrm{w} - \mathrm{y} |^2$$

derivating,
$$ \nabla E_{\mathrm{in}}(\mathrm{w}) = \frac{2}{N} X^\intercal(X\mathrm{w} - y) = \mathbf{0} $$

$$X^\intercal X w = X^\intercal y$$

$$w = X^\dagger y$$ 
where,

$X^\dagger = (X^\intercal X)^{-1}X^\intercal$ , is the __pseudo-inverse__ of $X$

---
# The pseudo-inverse
$$ X^\dagger = (X^\intercal X)^{-1} X^\intercal $$
![](../images/pseudo_inverse.png)

---
# The linear regression algorithm
1. Construct the matrix $X$ and the vector $\mathrm{y}$ for the datea set $(x_1, y_1), ..., (x_N, y_N)$ as follows
```
X = [ [x_11, x_12, ..., x_1n],
      [x_21, x_22, ..., x_2n],
      ...
      [x_N1, x_N2, ..., x_Nn] ]

y = [ [y_1],
      [y_2],
      ...,
      [y_n] ]
```
2. Coumpute the pseudo-inverse $X^\dagger = (X^\intercal X)^{-1}X^\intercal$
3. Return $\mathrm{w} = X^\dagger \mathrm{y}$

---
# Linear regression for classification
* Linear regression learns a real-valued function $y = f(\mathrm{x}) \in R$
* Binary-valued functions are real-valued! $\pm 1  \in R$
* Use linear regression to get $\mathrm{w}$ where $w^\intercal \mathrm{x}_n \approx y_n = \pm 1$
* In this case, $\mathrm{sign}(\mathrm{w}^\intercal \mathrm{x}_n)$ is likely to agree with $y_n = \pm 1$
* Good initial weights for classification