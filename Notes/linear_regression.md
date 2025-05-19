**SL1 regression**: value -> value  
**SL2 classification**: value -> category  
**UL1 clustering**: values -> patterns  
**UL2 anomaly detection**: values -> outliers  
**UL3 dimensionality reduction**: high dimensional values -> low dimensional values  

## Linear regression
model: `f(x) = wx + b`  
parameters: `w, b`  
cost function: `J(w, b) = 1/2m * ∑(f(xi) - yi)^2` where (xi, yi) is a data set member  
objective: **minimize cost function**

## Gradient descent
From a point on the plot of J, move downhill along the direction of steepest slope, until minimum, updating both parameters simultaneously.  
1. choose learning rate a
2. temp_w = w - a * dJ/dw
3. temp_b = b - a * dJ/db
4. w = temp_w
5. b = temp_b
6. repeat until convergence

**if a is too small, takes too long**  
**if a is too big, may never converge**  

batch gradient descent computes dJ/dw by considering all (xi, yi) in the data set.