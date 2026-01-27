#include<iostream>
using namespace std;

void greet(){
    cout << "Good Morning\n";
}

void greetByName(string fname, string lname){
    cout << "Good Morning, " << fname << " " << lname << "!\n";
}

int main(){
    // function is a block of code which can be used to perform some task repeatedly
    // 3 stages of Function:
    // Function Declaration : Giving a name for the function
    // Function Definition : Setting some rules
    // Function Call : Calling the function
    // Parameters & Arguments:
    // Variables within a paranthesis while declaring a function is called Parameters
    // Variables within a paranthesis while calling a function is called Arguments
    greet(); 
    greet(); 
    greet(); 
    string fname1 = "Akshay";
    string lname1 = "Rao";
    string name2 = "Ajay";
    string name3 = "Jay";
    greetByName(fname1, lname1);
}