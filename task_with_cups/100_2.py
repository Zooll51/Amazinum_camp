def calculate_drops(N):
    return N + (N * (N + 1) * (N - 1)) // 6


# Перевірка для N від 1 вгору
N = 1
while True:
    P = calculate_drops(N)
    if P >= 1000:
        break
    N += 1

print(f"Мінімальна кількість кидків: {N} для {P} поверхів")
