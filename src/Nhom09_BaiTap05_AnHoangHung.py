"""
Optimize a model with 26 rows, 16 columns and 70 nonzeros
Model fingerprint: 0x6589a5e5
Variable types: 0 continuous, 16 integer (16 binary)
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [0e+00, 0e+00]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 2e+00]
Found heuristic solution: objective 0.0000000

Explored 0 nodes (0 simplex iterations) in 0.00 seconds (0.00 work units)
Thread count was 1 (of 12 available processors)

Solution count 1: 0

Optimal solution found (tolerance 1.00e-04)
Best objective 0.000000000000e+00, best bound 0.000000000000e+00, gap 0.0000%
Bài toán tô màu có kết quả tối ưu:
Số 1 được tô màu 2
Số 2 được tô màu 2
Số 3 được tô màu 1
Số 4 được tô màu 2
Số 5 được tô màu 1
Số 6 được tô màu 1
Số 7 được tô màu 1
Số 8 được tô màu 1
"""
# Nhom09_BaiTap05
# Đậu Văn An - 21000659 - K66A2 Toán Tin
# Đặng Huy Hoàng - 21000680 - K66A2 Toán Tin
# Đỗ Mạnh Hùng - 21000682 - K66A2 Toán Tin
import gurobipy as gp
from gurobipy import GRB

def solve_coloring_problem(N, k):
    m = gp.Model("Coloring")

    # Tạo biến x[i, j] - số nguyên i được tô màu j
    x = m.addVars(N, k, vtype=GRB.BINARY, name="x")

    # Mỗi số chỉ thuộc một tập màu
    for i in range(N):
        m.addConstr(sum(x[i, j] for j in range(k)) == 1)

    # Các số a, b, c không thỏa mãn a + b = c
    for a in range(1, N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                if a + b == c:
                    for j in range(k):
                        m.addConstr(x[a-1, j] + x[b-1, j] + x[c-1, j] <= 2)

    # Tối ưu hoá mô hình
    m.optimize()

    # In kết quả
    if m.status == GRB.OPTIMAL:
        print("Bài toán tô màu có kết quả tối ưu:")
        for i in range(N):
            for j in range(k):
                if x[i, j].x > 0.5:
                    print(f"Số {i + 1} được tô màu {j + 1}")
    else:
        print("Không tìm thấy kết quả tối ưu.")

# Giải bài toán Color(8, 2)
solve_coloring_problem(8, 2)
