import copy, math, random, heapq
from random import randint


def greedy_assignment(N, M, b, L): #Ham khoi tao loi giai tham lam
    load = [0] * (M + 1)
    assignments = []

    for reviewers in L: #Duyet tung bai bao
        heap = []
        for r in reviewers: #Uu tien nguoi co tai nho hon
            heapq.heappush(heap, (load[r], r))

        chosen = []
        for _ in range(b): #Phan cong b nguoi co tai nho nhat
            _, r = heapq.heappop(heap)
            chosen.append(r)
            load[r] += 1

        assignments.append(chosen)

    return assignments #Tra ve phuong an phan cong tham lam

def simulated_annealing(N, M, b, L, assignments, iterations = 10000, T_init = 1000, alpha = 0.9): #Ham thuc thi mo phong luyen thep
    def calculate_load(assign): #Ham tinh tai
        load = [0] * (M+1)
        for assigned in assign:
            for r in assigned:
                load[r] += 1
        return load
    def max_load(load): #Ham tim tai cuc dai
        return max(load)
    #Cac bien ghi nhan loi giai tot nhat
    best_solution = copy.deepcopy(assignments)
    best_load = calculate_load(best_solution)
    best_max_load = max_load(best_load)

    T = T_init
    for _ in range(iterations): #Lap trong pham vi so vong toi da
        i = randint(0, N - 1) #Chon ngau nhien 1 bai bao
        j = randint(0, b - 1) #Chon ngau nhien 1 nguoi da phan cong cho bai bao
        curr = best_solution[i][j]
        current_reviewers = set(best_solution[i])
        candidates = [r for r in L[i] if r not in current_reviewers or r == curr] #Tim nhung nguoi co the phan bien nhung chua phan cong
        candidates.remove(curr)
        if not candidates:
            continue
        current_load = calculate_load(best_solution)
        candidates.sort(key=lambda r: current_load[r]) #Sap xep ung vien theo thu tu tang dan tai
        new_reviewer = candidates[0] #Chon ung vien co tai nho nhat
        #Cac bien ghi nhan loi giai moi
        new_solution = copy.deepcopy(best_solution)
        new_solution[i][j] = new_reviewer
        new_load = calculate_load(new_solution)
        new_max_load = max_load(new_load)
        delta = new_max_load - best_max_load #Tinh hieu so giua loi giai moi va loi giai hien tai
        if delta < 0 or random.random() < math.exp(-delta / T): #Ghi nhan loi giai moi neu tot hon hoac te hon nhung voi mot xac suat nao do
            best_solution = new_solution
            best_load = new_load
            best_max_load = new_max_load
        T *= alpha #Giam nhiet do
        if T < 1e-3: #Ket thuc neu nhiet do qua nho
            break
    return best_solution

def main():
    #Nhap input
    N, M, b = map(int, input().split())
    L = []

    for _ in range(N):
        info = list(map(int, input().split()))
        k_i = info[0]
        reviewers = info[1:]
        L.append(reviewers)

    initial_assignments = greedy_assignment(N, M, b, L) #Goi ham khoi tao loi giai ban dau
    final_assignments = simulated_annealing(N, M, b, L, initial_assignments) #Goi ham cai thien loi giai

    #In ket qua
    print(N)
    for assigned in final_assignments:
        print(b, *assigned)

main()