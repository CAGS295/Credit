# Missing data
---

# Steps to deal with missing data
1. Identify patters/reasons for missing data
2. Understand distribution of missing data
3. Decide on best method

---
# Sources of missing data
- Attrition due to social/natural proces
	- School graduation, droupout, death
- Skip pattern
	- Certain data is only asked to married people
- Random data collecction issuoes
- Respondent refusal/non-response
---

# Missing 
- Missingnes completly at random (MCAR).
- Missingnes at random (MAR)
	- The probability of missing depends only on available information
- Missingnes that depends on unobserved predictors
- Missingnes that depends on the missing value itself.
	- earnings

---
# Methods

---
# Complete Case Analysis
- Only analize cases with available data on each variable:
- Advantages:
	- Simplicity
	- Comparability across analyses
- Disadvantages:
	- Reduces statistical power
	- Don't use all information
	- Estimates mad be biased if not MCAR

---
# Available Case Analysis
- Analysis witha ll cases is with the variable of interest is present
- Advantages:
	- Keeps as many cases as possible for each analysis
	- Uses all information possible with each analysis
- Disadvantage:
	- Can't compare analyses because sample is different

---
# Mean/Mode Substitition
- Replace missing value with sample mean or mode, run anasyses as if all complete cases
- Advantages:
	- Can use complete case analysis methods
- Disadvantages:
	- Reduces variability
	- Weakens covariance and correlation estimates in the data

---
# Dummy variable adjustment
- Create an indicator for missing value
	- Variable with 0 if value is observed or 1 if value is missing.
- Impute missing values to a constant
- Include missing indicator in regression
- Advantage:
	- Uses all available information about missing observation
- Disadvantage:
	- Results in biased estimates (unless a legitimate skip)
	- Not theoretically driven

---
# Regression Imputation
- Replaces missing values with predicted score fram a regression equation
- Advantage:
	- Uses information from observed data
- Disadvantages:
	- Overestimates model fit and correlation estimates
	- Weakens variance

---
# Maximum Likelihood Estimation
- Identifies the set of parameter values that produces the highest log-likelihood
	- ML estimate: value that is most likely to have resulted in the observed data
- Conceptoally, process the same with or without missing data
- Advantages:
	- Uses full information to calculate log likelihood
	- Unbiased parameter estimates with MCAR/MAR data
- Disadvantages:
	- Standard Error biased downward
