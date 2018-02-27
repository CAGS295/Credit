<!-- page_number: true -->

# Logistic regression
* The model
* Error measure
* Learning algorithm

---
# Logistic regression
$$ s = \sum_{i=0}^dw_ix_i$$
* Linear regression
$$h(\mathrm x) = s$$
* Linear classification
$$h(\mathrm x) = \mathrm{sign}(s)$$
* Logistic regression
$$ h(\mathrm x) = \theta(s)$$

---
# The logistic function $\theta$
![center](../images/theta.png)

$$\theta(s) = \frac{e^s}{1+e^s} = \frac{1}{1 + e^{-s}}$$

---
# Probability interpretation
* $h(\mathrm x) = \theta(s)$ is interpreted as probability.
$$ P(y|\mathrm x) = 
\left\{
 \begin{array}{ll}
   h(\mathrm x) \,\,\,\,\,\,\,\,\,\,\, \mathrm{for}\, y = +1\\
   1-h(\mathrm x) \, \mathrm{for}\, y = -1
 \end{array}
\right.
$$

---
# Error measure
* Based on __likelihood__:
	* if $h = f$, how likely to get $y$ from $\mathrm x$?
$$ P(y|\mathrm x) = 
\left\{
 \begin{array}{ll}
   h(\mathrm x) \,\,\,\,\,\,\,\,\,\,\, \mathrm{for}\, y = +1\\
   1-h(\mathrm x) \, \mathrm{for}\, y = -1
 \end{array}
\right.
$$

* $P(y|\mathrm x) = \theta(y\mathrm w^\intercal\mathrm x)$, noting $\theta(-s) = 1 - \theta(s)$
* Likelihood of $D= (x_i, y_i)$
$$\prod_{n=1}^n P(y_n|\mathrm x_n) = \prod_{n=1}^N\theta(y_n\mathrm w^\intercal\mathrm x_n)$$

---
# Maximizing the likelihood
$$\frac{1}{N}\ln \left(\prod_{n=1}^N\theta(y_n\mathrm w^\intercal\mathrm x_n) \right) =
-\frac{1}{N} \sum_{n=1}^n \ln \left(\frac{1}{\theta(y_n\mathrm w^\intercal\mathrm x_n)} \right)$$
* Instead of maximizing, minimizing:
$$ E_{in}(\mathrm w) = 
\frac{1}{N} \sum_{n=1}^n \ln \left(\frac{1}{\theta(y_n\mathrm w^\intercal\mathrm x_n)} \right) =
\frac{1}{N}\sum_{n=1}^N\ln\left( 1 + e^{-y_n\mathrm w^\intercal \mathrm x_n} \right)$$
* __cross-entropy__ error.

---
# Gradient descent
$$ E_{\mathrm{in}}(\mathrm w) = 
\frac{1}{N}\sum_{n=1}^N\ln\left( 1 + e^{-y_n\mathrm w^\intercal \mathrm x_n} \right)$$
* __gradient descent__ (general method for nonlinear optimization).
	* Start at $\mathrm w(0)$
	* Take a step alog steepest slope.
	* Fixed step size: $\mathrm w(1) = w(0) + \eta \hat \mathrm v$.
	* Repeat.

---
# The direction of $\hat \mathrm v$
$$
 \begin{array}{ll}

\Delta E_{in} &= E_{in}(\mathrm w(0) + \eta \hat\mathrm v) - E_{in}(\mathrm w(0)) \\
&= \eta\nabla E_{in}(\mathrm w(0))^T\hat\mathrm v + O(\eta^2) \\
&\geq -\eta||\nabla E_{in}(\mathrm( w(0))||
 \end{array} 
$$
* Since $\hat\mathrm v$ is a unit vector,
$$ \hat\mathrm v = -\frac{\nabla E_{in}(\mathrm w(0))}{||\nabla E_{in}(\mathrm( w(0))||}$$

---
# Logistic regression algorithm
* Initialize the weights $t=0$ to $\mathrm w(0)$
* `for`$t = 0, 1, 2, ...$ `do`
	* Compute the gradient.
$$ \nabla E_\mathrm{in}=-\frac{1}{N}\sum_{n=1}^N\frac{y_n\mathrm x_n}{1 + e^{y_n\mathrm w^\intercal(t)\mathrm x_n}}	$$

*
    * Update the weights $\mathrm w(t+1) = w(t) - \eta\nabla E_\mathrm{in}$.
    * Iterate to the next step until it is time to stop.
* Return the final weights $\mathrm w$.
