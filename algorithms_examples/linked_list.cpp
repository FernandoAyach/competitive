#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node() {
        data = 0;
        next = NULL;
    }

    Node(int data) {
        this->data = data;
        this->next = NULL;
    }
};

class LinkedList {
public:
    Node* head;

    LinkedList() {
        this->head = NULL;
    }

    LinkedList(Node* head) {
        this->head = head;
    }

    void printList() {
        Node* current = head;
        while(current) {
            cout << current->data << "\n";
            current = current->next;
        }
    }

    void emplace_back(int data) {
       
    }

    void push_back(int data) {
        Node* newNode = new Node(data);
        
        if (head == NULL) {
            head = newNode;
            return;
        }
    
        Node* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
    
        temp->next = newNode;
    }

    void insert() {
        
    }
};

int main() {
    Node* head = new Node(2);
    LinkedList* linkedList = new LinkedList(head);

    linkedList->push_back(1);

    linkedList->printList();

}