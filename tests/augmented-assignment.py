# https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements
# http://www.informit.com/articles/article.aspx?p=459269&seqNum=5
# https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations

n = 50
n += 2 # n = n + 2
n -= 2 # n = n - 2
n *= 3 # n = n * 3
n /= 3 # n = n / 3 => retorna sempre float
n //= 4 # n = n // 3 => faz divisão e arredonda pra baixo (floor division)
n **= 2 # n = n ** 2 => elevado a 2
n %= 5 # n = n % 5 => resto da divisão por 5
print(n)

a = 5
a &= 1
print(a)