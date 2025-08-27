from ortools.linear_solver import pywraplp

def solve_problem(N, M, b,L): #Ham giai bai toan
    solver = pywraplp.Solver.CreateSolver("SCIP") #Khoi tao solver
    if not solver:
        return

    #Bien quyet dinh
    X = {}
    for i in range(N):
        for j in L[i]:
            X[i,j] = solver.IntVar(0, 1, f'X_{i}_{j}')

    #Bien max_load
    max_load = solver.IntVar(0, N, 'max_load')

    #Moi bai bao can dung b nguoi phan bien
    for i in range(N):
        solver.Add(solver.Sum([X[i, j] for j in L[i]]) == b)

    #Tai cuc dai la max_load
    for j in range(1, M+1):
        solver.Add(solver.Sum([X[i, j] for i in range(N) if (i,j) in X]) <= max_load)

    #Muc tieu la toi thieu hoa max_load
    solver.Minimize(max_load)

    #Giai bai toan
    status = solver.Solve()
    #Ghi lai loi giai
    if status == pywraplp.Solver.OPTIMAL:
        assignment = [[] for _ in range(N)]
        for (i,j), var in X.items():
            if var.solution_value() == 1:
                assignment[i].append(j)

        return assignment
    else:
        return

def main():
    #Nhap input
    N, M, b = map(int, input().split())
    L = []
    for _ in range(N):
        line = list(map(int, input().split()))
        l = line[0]
        reviewers = line[1:]
        L.append(reviewers)

    #Goi ham giai bai toan
    assignment = solve_problem(N, M, b, L)

    #In ket qua
    print(N)
    for i in range(N):
        reviewers = assignment[i]
        print(b, *reviewers)

main()