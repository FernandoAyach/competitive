#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
 
using namespace std;
 
void getTablesOrdered(vector<int>& boards, int n) {
    int table;
    for(int i = 0; i < n; i++) {
        cin >> table;
        boards.emplace_back(table * 100); 
    }
    sort(boards.begin(), boards.end());
}

pair<bool, int> verifyBoards(
    unsigned int widthFloor, unsigned int lengthFloor, 
    unsigned int n, vector<int>& boards, unsigned int totalArea, unsigned int widthBoard
) {
    unsigned int currentArea = 0;
    int left = 0;
    int right = n - 1;
    int totalBoards = 0;

    while(currentArea < totalArea) {

        if(left > right) {
            return {false, 0};
        }

        if(boards[right] == lengthFloor) {
            currentArea += widthBoard * boards[right];
            totalBoards++;
            right--;
        } else if((boards[right] + boards[left] == lengthFloor) && (right != left)) {
            currentArea += widthBoard * (boards[right] + boards[left]);    
            totalBoards += 2;
            right--;
            left++;
        } else {
            right--;
        }
    }
    return {true, totalBoards};
}

int main() {
    unsigned int widthFloor, lengthFloor, widthBoard, n, totalArea;
   
    while(cin >> widthFloor >> lengthFloor && widthFloor != 0 && lengthFloor != 0) {
        cin >> widthBoard >> n;
        vector<int> boards;
        widthFloor *= 100;
        lengthFloor *= 100;
        totalArea = widthFloor * lengthFloor;

        getTablesOrdered(boards, n);
        
        pair<bool, int> vertical, horizontal;
        vertical = verifyBoards(widthFloor, lengthFloor, n, boards, totalArea, widthBoard);
        horizontal = verifyBoards(lengthFloor, widthFloor, n, boards, totalArea, widthBoard);

        bool verticalPossible = vertical.first;
        bool horizontalPossible = horizontal.first;
        bool impossible = !(verticalPossible || horizontalPossible);

        if(impossible) {
            cout << "impossivel" << endl;
        } else if(verticalPossible) {
            if(vertical.second < horizontal.second) {
                cout << vertical.second << endl;
            }
        } else if (horizontalPossible){
            if(horizontal.second < vertical.second) {
                cout << horizontal.second << endl;
            }
        }
    }
    
    return 0;
}