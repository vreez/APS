n = int(input())

def func(n_n, m_n):
    if n_n > m_n:
        return
    print(n_n, end=" ")
    func(n_n+2, m_n)

if n % 2 != 0:
    func(1, n)
else:
    func(2, n)
