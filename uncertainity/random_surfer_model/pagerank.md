## Random Surfer Model with spider attack

```python
def pageRank(M, n):
    # Initialize rank vector
    r_new = r_prev = (1 / n) * [1<sub>n</sub>]<sup>T</sup>

    while True:  # Infinite loop
        r_new = M * r_prev

        # Check for convergence
        if r_new ≈ r_prev:
            break

        r_prev = r_new

    return r_new
```
