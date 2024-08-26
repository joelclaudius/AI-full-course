## Random Surfer Model with Spider Attack

```python
def pageRank(M, n):
    # Initialize rank vector
    r_new = r_prev = (1 / n) * [1ₙ]ᵀ

    while True:  # Infinite loop
        r_new = M * r_prev

        # Check for convergence
        if r_new ≈ r_prev:
            break

        r_prev = r_new

    return r_new
```

## Random Surfer Model with Teleportation

```python
def pageRank(M, n, beta):
    # Initialize rank vector
    c =  (1-beta) * (1 / n) * [1ₙ]ᵀ
    r_new = r_prev = (1 / n) * [1ₙ]ᵀ

    while True:  # Infinite loop
        r_new = beta * M * r_prev + c

        # Check for convergence
        if r_new ≈ r_prev:
            break

        r_prev = r_new

    return r_new
```
