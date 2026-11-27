import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X = np.array(X)
    y = np.array(y)
    m1 = np.linalg.inv(X.T@X)
    m2 = X.T@y 
    theta = m1 @ m2
    return np.round(theta,4)

    