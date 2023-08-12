#include <iostream>
#include <stack>

using namespace std;

int main() {
    stack<int> myStack;

    myStack.push(1);
    myStack.push(2);
    myStack.push(3);
    myStack.push(-1);
    myStack.pop();
    
    if(myStack.empty()) cout << "Stack is empty\n";
    else cout << "Stack is not empty\n";

    cout << "Stack size: " << myStack.size() << "\n";

    while(!myStack.empty()) {
        cout << myStack.top() << " ";
        myStack.pop();
    }
    cout << "\n";
}