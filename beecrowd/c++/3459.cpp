#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;
 
#define FOR(i, n) for(int i = 0; i < (int) n; i++)
#define PB push_back
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define F first
#define S second
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int MOD = 1e9+7;
const int MAX = 507;
const int INF = 0x3f3f3f3f;

bool eh_delimitador(char c){
    return c==' '||c=='.'||c==',';
}

// dado uma string da forma regex (\d+\*)*\d+
// e retorna ele em inteiro long long ou -1 se n for numero
ll get_num(string s){
    ll ans = 0;
    for(auto& c : s){
        if(isalpha(c)) return -1;
        if(c=='*') continue;
        ans = ans*10 + (c-'0');
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(0);

    int n; cin >> n;
    cin.ignore(1);
    vector<ll> numeros;
    FOR(_, n){
        string line;
        getline(cin, line);

        //Passo 1: transformar para letra numeros com palavras
        // e.g.: 123blue => aaablue, fast123 => fastaaa, a2a => aaa
        int k = line.size();
        for(int i = 1; i < k; ++i)
            if(isalpha(line[i-1])&&isdigit(line[i]))
                line[i]='a';
        for(int i = k-2; i>=0; --i)
            if(isalpha(line[i+1])&&isdigit(line[i]))
                line[i]='a';

        //Passo 2: juntar digitos com delimitador com *
        // e.g.: 2,5 412.6 => 2*5*412*6
        for(int i = 1; i < k-1; ++i)
            if(isdigit(line[i-1])
								&&eh_delimitador(line[i])
								&&isdigit(line[i+1]))
                line[i]='*';

        //Passo 3: trocar todos os delimitadores por espaço
				// (isso vai facilitar nossa vida quando usarmos o iss)
        for(int i = 0; i < k; ++i)
            if(eh_delimitador(line[i])) line[i]=' ';

        istringstream iss(line);
        string palavra;
        while(iss >> palavra){
            ll num = get_num(palavra);
            if(num!=-1) numeros.PB(num);
        }
    }

    //Procurando alguma tripla (X-1, X, X+1)
    bool tem_resposta = false;
    FOR(i, numeros.size()){
        bool tem_menos_um=false, tem_mais_um=false;

        for(int j = i-1; j >=0 && !tem_menos_um; --j)
            tem_menos_um = (numeros[j] == numeros[i]-1);

        for(int j = i+1; j<(int)numeros.size() 
                && !tem_mais_um; ++j)
            tem_mais_um = (numeros[j] == numeros[i]+1);

        if(tem_mais_um&&tem_menos_um){
            tem_resposta = true;
            break; // sai do for
        }
    }

    if(tem_resposta) cout << "123\n";
    else cout << ":)\n";

    return 0;
}