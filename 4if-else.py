def comparison(n, m):
    if n == m:
        return "equal"
    elif n < m:
        return "lesser"
    else:
        return "greater"


n = int(input())
m = int(input())

print(comparison(n, m))