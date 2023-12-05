# Nhom09_BaiTap01
# Đậu Văn An - 21000659 - K66A2 Toán Tin
# Đặng Huy Hoàng - 21000680 - K66A2 Toán Tin
# Đỗ Mạnh Hùng - 21000682 - K66A2 Toán Tin
def list_positive_divisors(n):
    positive_divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            positive_divisors.append(i)
    return positive_divisors
n = int(input("Enter a positive integer: "))
divisors = list_positive_divisors(n)
print("The positive divisors of", n, "are:", divisors)
