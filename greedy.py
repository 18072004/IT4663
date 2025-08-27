import heapq

def main(): #Ham giai bai toan
    #Nhap input
    N, M, b = map(int, input().split())
    L = []

    for _ in range(N):
        info = list(map(int, input().split()))
        k_i = info[0]
        reviewers = info[1:]
        L.append(reviewers)

    load = [0] * (M+1) #Khoi tao mang luu tai cua moi nguoi

    assignments = [] #Mang 2 chieu luu danh sach phan cong cho cac bai bao

    for reviewers in L: #Duyet qua tung bai bao
        heap = [] #Hang doi uu tien nguoi co tai nho hon
        for r in reviewers:
            heapq.heappush(heap, (load[r], r))

        chosen = []
        for _ in range(b): #Phan cong b nguoi dau tien cho bai bao
            _, r = heapq.heappop(heap)
            chosen.append(r)
            load[r] += 1

        assignments.append(chosen) #Luu danh sach phan cong

    #In ket qua
    print(N)
    for assgined in assignments:
        print(b, *assgined)

main() #Goi ham giai bai toan