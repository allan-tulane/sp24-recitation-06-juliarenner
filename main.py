def fib_recursive(n, counts):
  if n == 0:
    counts[n] += 1
    return 0
  if n == 1:
    counts[n] += 1
    return 1
  else:
    counts[n] += 1
    return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)


def fib_top_down(n, fibs):
  ###TODO
  if n == 0:
    fibs[n] = 0
    return 0
  if n == 1:
    fibs[n] = 1
    return 1
  else:
    if fibs[n - 1] == -1:
      fibs[n - 1] = fib_top_down(n - 1, fibs)
    if fibs[n - 2] == -1:
      fibs[n - 2] = fib_top_down(n - 2, fibs)
    return fibs[n - 1] + fibs[n - 2]


def fib_bottom_up(n):
  fibs = [0] * (n + 1)
  fibs[0] = 0
  fibs[1] = 1
  for i in range(2, n + 1):
    fibs[i] = fibs[i - 1] + fibs[i - 2]
  return fibs[n]
