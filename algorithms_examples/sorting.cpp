#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void showArray(vector<int> seq) {
    for(int i = 0; i < seq.size(); i++) {
        cout << seq[i] << " ";
    }
    cout << "\n";
}

// BUBBLE SORT - O(n2)
void bubbleSort(vector<int>& seq) {
    int n = seq.size();

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n - 1; j++) {
            if(seq[j] > seq[j + 1]) {
                swap(seq[j], seq[j + 1]);
            }
        }
    }
}

// MERGE SORT - O(n log n)

void merge(vector<int>& seq, int begin, int mid, int end) {  // O(n)
    int nLeft, nRight, k = begin, topLeft = 0, topRight = 0;
    vector<int> left, right;
   
    nLeft = mid - begin + 1;
    nRight = end - mid;

    for(int i = 0; i < nLeft; i++) {  // Fill left subarray
        left.push_back(seq[begin + i]);
    }

    for(int i = 0; i < nRight; i++) {  // Fill right subarray
        right.push_back(seq[mid + 1 + i]);
    }

    while(topLeft < nLeft && topRight < nRight) { // Get the smallest from each subarray
        if (left[topLeft] <= right[topRight]) {
            seq[k] = left[topLeft];
            topLeft++;
        } else {
            seq[k] = right[topRight];
            topRight++;
        }
        k++;
    }

    while(topLeft < nLeft) {       //extra element in left array
        seq[k] = left[topLeft];
        topLeft++; 
        k++;
    }

    while(nRight < nRight) {     //extra element in right array
        seq[k] = right[topRight];
        topRight++; 
        k++;
    }
   
}

void mergeSort(vector<int>& seq, int begin, int end) { // O(log n)
    if(begin < end) {  
        // Divide to conquer
        int mid = begin + (end - begin) / 2;
        mergeSort(seq, begin, mid);
        mergeSort(seq, mid + 1, end);
        merge(seq, begin, mid, end);
    }
}

// COUNTING SORT - O(n)

void countSort(vector<int>& seq) {
    int size = seq.size();
   
    vector<int> output(size);
    vector<int> count(size);
    int max = seq[0];

    // Find the largest element of the array
    for (int i = 1; i < size; i++) {
        if (seq[i] > max)
        max = seq[i];
    }

    // Store the count of each element
    for (int i = 0; i < size; i++) {
        count[seq[i]]++;
    }

    // Store the cummulative count of each array
    for (int i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    // Find the index of each element of the original array in count array, and
    // place the elements in output array
    for (int i = size - 1; i >= 0; i--) {
        output[count[seq[i]] - 1] = seq[i];
        count[seq[i]]--;
    }

    for (int i = 0; i < size; i++) {
        seq[i] = output[i];
    }
    
}

int main() {
    vector<int> seq = {9, 9, 8, 7, 6, 6, 5, 4, 3, 2, 1};
    showArray(seq);
    //bubbleSort(seq);
    //mergeSort(seq, 0, seq.size() - 1);
    countSort(seq);
    showArray(seq);
}
