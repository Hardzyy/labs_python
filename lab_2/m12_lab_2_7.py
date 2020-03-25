def leonardo_num(n):
    if n == 0 or n == 1:
        return 1
    fi = (1 + 5**0.5)*0.5
    phi = (1 - 5**0.5)*0.5
    leo = (2 / 5**0.5) * (fi**(n+1) - phi**(n-1)) - 1 
    return round(leo)