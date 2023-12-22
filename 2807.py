n = int(input())


fib_sequence = [1, 1]

while len(fib_sequence) < n:
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)

if n <= 0:
    fib_sequence = []

if n == 1:
    fib_sequence = [1]

fib_sequence = fib_sequence[::-1]

fib_sequence = " ".join(map(str, fib_sequence))
print(fib_sequence)