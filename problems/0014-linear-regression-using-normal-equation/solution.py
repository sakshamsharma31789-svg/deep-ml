import torch

def linear_regression_normal_equation(X, y) -> torch.Tensor:
    """
    Solve linear regression via the normal equation using PyTorch.
    X: Tensor or convertible of shape (m,n); y: shape (m,) or (m,1).
    Returns a 1-D tensor of length n, rounded to 4 decimals.
    """
    X_t = torch.as_tensor(X, dtype=torch.float)
    y_t = torch.as_tensor(y, dtype=torch.float).reshape(-1,1)
    m1 = torch.matmul(X_t.T,X_t)
    m1 = torch.linalg.inv(m1)
    m2 = X_t.T@y_t
    theta = m1@m2
    return torch.round(theta,decimals=4)
    pass
