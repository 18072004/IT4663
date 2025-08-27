#include <iostream>
#include <algorithm>
#include <climits>
#include <vector>
#include <functional>
using namespace std;

int N, M, b;
vector<vector<int>> L; //Danh sach nhung nguoi co the phan bien cac bai bao
vector<vector<int>> assign; //Danh sach phan cong nguoi phan bien cho cac bai bao
vector<int> load; //Tai cua moi nguoi
int best_max_load = INT_MAX; //Ghi nhan tai cuc dai toi thieu
vector<vector<int>> best_solution; //Ghi nhan loi giai tot nhat

void backtrack(int paper_idx) {
    if (paper_idx == N) { //Khi da phan cong du N bai 
        int curr = *max_element(load.begin()+1, load.end()); 
        if (curr < best_max_load) { //Cap nhat loi giai neu tot hon
            best_max_load = curr;
            best_solution = assign;
        }
        return;
    }

    vector<int> sorted_reviewer = L[paper_idx]; 
    //Sap xep danh sach nguoi co the phan bien theo thu tu tang dan tai
    sort(sorted_reviewer.begin(), sorted_reviewer.end(), [](int a, int b) { 
        return load[a] < load[b];
    });
     
    int k = sorted_reviewer.size();
    vector<int> comb;
    //Thu phan tong to hop b nguoi co tai thap nhat cho bai bao
    function<void(int,int)> Try_comb = [&](int start, int depth) { 
        if (depth == b) { //Neu da chon du b nguoi
            bool valid = true;
            for (int r : comb) {
                if (load[r]+1 >= best_max_load) { //Neu khong the dan den loi giai tot hon thi khong phan cong
                    valid = false;
                    break;
                }
            }
            if (!valid) return;
            for (int r : comb) load[r]++; //Phan cong b nguoi cho bai bao
            assign[paper_idx] = comb;
            backtrack(paper_idx+1); //Phan cong bai bao tiep theo
            for (int r : comb) load[r]--; //Tra lai trang thai
            assign[paper_idx].clear();
            return;
        }
        for (int i = start; i <= k - (b - depth); i++) { //Sinh cac to hop b nguoi
            comb.push_back(sorted_reviewer[i]);
            Try_comb(i+1, depth+1);
            comb.pop_back();
        }
    };
    Try_comb(0,0);
}
int main() {
    //Nhap input
    cin >> N >> M >> b;
    L.resize(N);
    assign.resize(N);
    best_solution.resize(N);
    load.resize(M+1, 0);
    for (int i = 0; i < N; i++) {
        int k; cin >> k;
        L[i].resize(k);
        for (int j = 0; j < k; j++) cin >> L[i][j];
    }
    //Thuc thi thuat toan
    backtrack(0);
    //In ket qua
    cout << N <<'\n';
    for (int i = 0; i < N; i++) {
        cout << b << ' ';
        for (int j = 0; j < b; j++) cout << best_solution[i][j] << ' ';
        cout <<'\n';
    }
    return 0;
}