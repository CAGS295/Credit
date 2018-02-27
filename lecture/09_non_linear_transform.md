# Non linear transformations

---
# Nonlinear Tranformation
## Linear is limited

* Credit line is affected by _years in residence_
	- but not in a linear way!

* Nonlinear $[[x_i < 1]] \mathrm{and} [[x_i > 5]]$ are better.

* Can we do linear models?

---
# Linear in what?
Linear regression implements 
$$ h(\mathrm x ) = \sum_{i=0}^d w_i x_i$$

Linear classification implemets
$$ h(\mathrm x) = \mathrm{sign}\left(\sum_{i=0}^d w_i x_i \right) $$

Algorithms works because linearities in the weights.

* Tranform the data nonlinearly
$$ (x_1, x_2) - \phi(\mathrm{x}) \rightarrow (x_1^2, x_2^2) $$

---
# Receiver Operating Characteristic
* Ilustrate the performance of a binary classifier.
* True Positive Rate $TP/P$ _vs_ False Positive Rate $FP/N$

![center](../images/roc.png)


---
# k-Fold Cross Validation
* Divide the observations in $k$ sub-samples of aprox. equal size.
* Repeat k times:
	* The k fold is treated as test set.
	* Train on the remaining k-1 sets.
$$ CV_{(k)} = \frac{1}{k}\sum_{i=1}^{k} I(\mathrm{y}_i \neq \mathrm{h}_i) $$

* Greater k => less bias
* Smaller k => less variance

---
# Bias-Variance Trade-Off
* The error can be decomposed in:
$$E(y_i - h(\mathrm x_i) )^2 = \mathrm{Var}(h(\mathrm x_i)) + \left[\mathrm{Bias}(h(\mathrm x_i))\right]^2 + Var(\epsilon) $$

* _Variance_: refers to the amount by which $h$ would chang if we estimated it using a different training data set.
* _Bias_: refers to the error that is introduced by aproximating a real-life problem by a much simpler model.