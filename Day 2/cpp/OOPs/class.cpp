#include<iostream>
using namespace std;

// Syntax: 
// class className{

// };

class Student{
    // Data Members & Member Functions
    // Variables within a class is called as Data Members
    // Functions which uses data members are called as Member Functions
    // Access Modifiers: public, private & protected
    public:
    string name;
    int grade, age;
    char section;

    void printData(string n, int g, int a, char sec){
        cout << "The Student Details are as follows: \n";
        cout << "Name: " << n << endl;
        cout << "Age: " << a << endl;
        cout << "Grade: " << g << endl;
        cout << "Section: " << sec << endl;
    }
};

int main(){
    // Creation of Object
    Student s1, s2; 
    cout << "Enter your name: ";
    cin >> s1.name;
    cout << "Enter your age: ";
    cin >> s1.age;
    cout << "Enter your grade: ";
    cin >> s1.grade;
    cout << "Enter your section: ";
    cin >> s1.section;

    s1.printData(s1.name, s1.grade, s1.age, s1.section);

    cout << "Enter your name: ";
    cin >> s2.name;
    cout << "Enter your age: ";
    cin >> s2.age;
    cout << "Enter your grade: ";
    cin >> s2.grade;
    cout << "Enter your section: ";
    cin >> s2.section;

    s2.printData(s2.name, s2.grade, s2.age, s2.section);
}   