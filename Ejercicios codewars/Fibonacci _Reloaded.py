def fib(n):
      if n == 1:
        return 0
      a = 0
      b = 1
      contador = 2
      while contador < n:
        c = a + b
        a = b
        b = c
        contador += 1
      return b