def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_fractions(N):
    fractions = []

    for numerator in range(2, 2*N + 1):
        for denominator in range(1, numerator):
            if gcd(numerator, denominator) == 1:
                fractions.append((numerator, denominator, numerator // denominator))

    fractions.sort(key=lambda x: x[2], reverse=True)

    selected_fractions = []
    used_denominators = set()

    for fraction in fractions:
        if fraction[1] not in used_denominators:
            selected_fractions.append(fraction)
            used_denominators.add(fraction[1])

        if len(selected_fractions) == N:
            break

    return selected_fractions

def main():
    N_values = [10]

    for N in N_values:
        result = generate_fractions(N)
        print(f"For N = {N}, selected fractions:")
        for fraction in result:
            print(f"{fraction[0]}/{fraction[1]}")

if __name__ == "__main__":
    main()
