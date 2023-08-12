#include <iostream>
#include <queue>

using namespace std;

void printQueue(queue<int> myQueue) {
    while(!myQueue.empty()) {
        cout << myQueue.front() << " ";
        myQueue.pop();
    }
    cout << "\n";
}

int main() {
    queue<int> myQueue;
    myQueue.push(1);
    myQueue.push(2);
    myQueue.push(3);

    cout << "Size " << myQueue.size() << endl;
    cout << "First element " << myQueue.front() << endl;
    cout << "Last element " << myQueue.back() << endl;

    printQueue(myQueue);
}