from ortools.sat.python import cp_model
def solve_problem(N, M, b, L): #Ham giai bai toan
    model = cp_model.CpModel() #Khoi tao model

    #Bien quyet dinh
    X = {}
    for i in range(N):
        for j in L[i]:
            X[(i,j)] = model.NewIntVar(0, 1, f'X[({i}, {j})]')

    #Them rang buoc moi bai bao can dung b nguoi phan bien
    for i in range(N):
        model.Add(sum(X[(i,j)] for j in L[i]) == b)

    #Bien max_load
    max_load = model.NewIntVar(0, N, 'max_load')

    #Them rang buoc max_load la tai cuc dai
    for j in range(1, M+1):
        model.Add(sum(X[(i, j)] for i in range(N) if (i, j) in X) <= max_load)

    #Muc tieu toi thieu hoa max_load
    model.Minimize(max_load)
    #Khoi tao solver va giai bai toan
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        assignment = [[] for _ in range(N)]
        for i in range(N): #Ghi lai loi giai
            for j in L[i]:
                if solver.Value(X[(i, j)]) == 1:
                    assignment[i].append(j)
        return assignment
    else:
        return
def main():
    #Nhap input
    N,M, b = map(int, input().split())
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