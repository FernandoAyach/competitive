#include <bits/stdc++.h>
 
using namespace std;

#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
 
typedef long long ll;
typedef unsigned long long llu;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<pii> vpi;
const ll INF = 1e9+7;
const ll MAX = 1e4+7;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vi ans;
        unordered_map<int, int> hashmap;

        FOR(i, 0, nums.size()) {
            auto it = hashmap.find(target - nums[i]);
            if(it != hashmap.end()) {
                ans.push_back(hashmap[target - nums[i]]);
                ans.push_back(i);
                break;
            } else {
                hashmap[target - nums[i]] = i;
            }
        }
        
        return ans;
    }
};
