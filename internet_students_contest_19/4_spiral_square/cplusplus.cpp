#include <iostream>
#include <array>
using namespace std;

array<int,2> get_ru(int i, int n){
    array<int,2> ru;
    int middle = 0;
    if(i == n * n && n % 2 == 1){
        middle = n / 2 + 1;
        ru[0] = middle;
        ru[1] = middle;
        return ru;
    }
    int S = 0;
    int layer = n;
    int layerStorage = 0;
    while(S <= n * n){
        layerStorage = 4 * (layer - 1);
        S += layerStorage;

        if(i <= S){
            break;
        }

        layer -= 2;
    }

    int r = 0, u = 1;
    int surpass = layerStorage - (S - i);
    for(int i = 1; i <= surpass; i++){
        if(i <= layer){
            r += 1;
        }else if(i <= 2 * layer - 1){
            u += 1;
        }else if(i <= 3 * layer - 2){
            r -= 1;
        }else{
            u -= 1;
        }
    }
    int shift = (n - layer) / 2;
    ru = {r + shift, u + shift};
    return ru;
}

int main(){
    // ru = get_ru(14, 5);
    int s, d, n;
    array<int, 2> s_ru, d_ru;
    cin >> n >> s >> d;
    s_ru = get_ru(s, n);
    d_ru = get_ru(d, n);
    // cout << d_ru[0] << " " << d_ru[1] << endl;
    // cout << s_ru[0] << " " << s_ru[1] << endl;
    int rDiff = d_ru[0] - s_ru[0];
    int uDiff = d_ru[1] - s_ru[1];
    if(rDiff != 0){
        if(rDiff > 0){cout << rDiff << " R\n";}
        else{cout << -1 * rDiff << " L\n";}
    }
    if(uDiff != 0){
        if(uDiff > 0){cout << uDiff << " U\n";}
        else{cout << -1 * uDiff << " D\n";}
    }
    // cout << ru[0] << " " << ru[1] << endl;
}
