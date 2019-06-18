#include <bits/stdc++.h>
#define N 200005
using namespace std;

struct Node{
    int l, r;
    int id;
}node[N];

bool cmp(Node a, Node b){
    if(a.l == b.l)
        return a.r > b.r;
    return a.l < b.l;
}
int n, m;
deque<int> q;

int main(){
    cin >> n >> m;
    for(int i = 0 ; i < n ; i++){
        // cin >> node[i].l >> node[i].r;
        scanf("%d%d",&node[i].l, &node[i].r);
        node[i].id = i;
    }
    sort(node, node+n, cmp);
    int last = 0;
    int begin = 0;
    int end = 0;
    int k = 0;
    for(int i=0;i<n && end < m;i++){
        int flag = 0;
        int p;
        while(end+1 >= node[i].l && i < n){
            if(node[i].r > last){
                last = node[i].r;
                p = node[i].id;
            }
            i++;
            flag = 1;
        }
        if(flag){
            i--;
            end = max(end, last);
            k++;
            q.push_back(p);
        }else{
            break;
        }
    }

    if(end < m){
        cout << "NO" << endl;
    }else{
        cout << "YES" << endl;
        cout << k << endl;
        while(!q.empty()){
            // cout <<q.front()+1<<" ";
            printf("%d ", q.front()+1);
            q.pop_front();
        }
        cout <<endl;
    }
    return 0;
}