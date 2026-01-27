#include<iostream> // Header File
#include<string>
using namespace std; // namespace


int main() {
    cout << "Hello World!" << endl;

    // int age = 24;
    // float height = 170.5;
    // string name = "Akshay Rao";

    int age;
    float height;
    string name;

    cout << "Enter your name: ";
    cin >> name;
    cout << "Enter your age: ";
    cin >> age;
    cout << "Enter your height(In cms): ";
    cin >> height;

    cout << "My name is " << name << ", and I'm " << age << " years old! And I'm " << height << " cms taller."; 
}