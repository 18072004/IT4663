from collections import defaultdict
import heapq
import copy
import random

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

def hill_climbing(N, M, b, papers, L, iterations=100): #Ham thuc thi leo doi
    def calculate_load(assign): #Ham tinh tai
        load = [0] * (M + 1)
        for assigned in assign:
            for r in assigned:
                load[r] += 1
        return load

    def max_load(load): #Ham tim tai cuc dai
        return max(load)

    #Cac bien ghi nhan loi giai tot nhat
    best_solution = copy.deepcopy(L)
    best_load = calculate_load(best_solution)
    best_max_load = max_load(best_load)

    for _ in range(iterations): #Lap trong pham vi so vong toi da
        i = random.randint(0, N - 1) #Chon ngau nhien 1 bai bao
        j = random.randint(0, b - 1) #Chon ngau nhien 1 nguoi da phan cong cho bai bao
        candidates = [r for r in papers[i] if r not in L[i]] #Tim nhung nguoi co the phan bien nhung chua duoc phan cong
        if not candidates:
            continue
        candidates.sort(key=lambda r: best_load[r]) #Sap xep theo thu tu tang dan tai
        new_reviewer = candidates[0] #Chon nguoi ung vien co tai nho nhat
        #Cac bien ghi nhan loi giai moi
        new_solution = copy.deepcopy(best_solution)
        new_solution[i][j] = new_reviewer
        new_load = calculate_load(new_solution)
        new_max_load = max_load(new_load)

        #Neu tot hon thi ghi nhan la loi giai tot nhat moi
        if new_max_load < best_max_load:
            best_solution = new_solution
            best_load = new_load
            best_max_load = new_max_load

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

    initial_assignments = greedy_assignment(N, M, b, L) #Khoi tao loi giai ban dau
    final_assignments = hill_climbing(N, M, b, L, initial_assignments) #Goi ham thuc thu leo doi
    #In ket qua
    print(N)
    for assigned in final_assignments:
        print(b, *assigned)

main()
