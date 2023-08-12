#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

int binarySearch(array<int, 10> array, int target) {
    int left = 0; 
    int right = array.size() - 1;

    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(target == array[mid]) return mid;
        if(target < array[mid]) right = mid - 1;
        else left = mid + 1;
    }
    return  - 1;
}

int binarySearchAlt(array<int, 10> array, int target) {
    int k = 0;
    int n = array.size();
    for(int b = n / 2; b >= 1; b /= 2) {
        while(k + b < n && array[k + b] <= target) k += b;
    }
    if(array[k] == target) return k;
    return -1;
}

int main() {
    array<int, 10> array = {1, 2, 3, 4, 5, 6, 7, 8};
}