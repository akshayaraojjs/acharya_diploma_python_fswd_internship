#include<iostream>
using namespace std;

class BankAccount{
    // Private Member which cannot be accessed out of the Class
    private:
    string AcNo;
    int balance = 0;

    // Public Members
    public:
    string name, address, bank, branch;

    // Setter is a method or function used to assign the value for Private Members
    // Getter is a method or function used to fetch or get the value from Private Members

    // Setter
    void createAccount(string Name, string Loc){
        string acNum = "12345678910";
        acNum = AcNo;

        cout << "Account created for " << Name << ", and the A/C Number is as follows: " << acNum << endl;
    }

    void Deposit(int amount){
        balance = balance + amount;

        cout << "Rs." << amount << "/- has been deposited, Updated Balance: " << balance << endl;
    }
    
    void Withdraw(string acNum, int amount){
        balance = balance - amount;
        
        cout << "Rs." << amount << "/- has been withdrawn, Updated Balance: " << balance << endl;
    }

    // Getter
    void checkBalance(string acNum){
        cout << "Account Balance: Rs." << balance << "/-" << endl;
    }
};

int main(){
    BankAccount p1, p2;

    string AccountNum;
    int Amount;

    // We can't access the private member outside of the class, we can use the setter or getter methods to access the values
    // p2.balance;
    p1.name = "Akshay Rao";
    p1.address = "Chikkabanavara";
    p1.bank = "SBI";
    p1.branch = "Chikkabanavara";

    p1.createAccount(p1.name, p1.address);

    p1.Deposit(2000);
    p1.Deposit(5000);
    cout << "Enter your A/C Number:";
    cin >> AccountNum;
    p1.checkBalance(AccountNum);

    p1.Withdraw(AccountNum, 3000);

    p1.checkBalance(AccountNum);

    cout << "Enter the following details for creating the Bank Account: \n";
    cout << "Enter your name:";
    cin >> p2.name;
    cout << "Enter your address:";
    cin >> p2.address;
    cout << "Enter your bank name:";
    cin >> p2.bank;
    cout << "Enter your branch address:";
    cin >> p2.address;
    p2.createAccount(p2.name, p2.address);
    cout << "Enter the amount to be deposited: ";
    cin >> Amount;
    p2.Deposit(Amount);
    cout << "Enter the A/C Number to check the balance: ";
    cin >> AccountNum;
    p2.checkBalance(AccountNum);
    cout << "Enter the amount to be withdrawn: ";
    cin >> Amount;
    p2.Withdraw(AccountNum, Amount);
    cout << "Enter the A/C Number to check the balance: ";
    cin >> AccountNum;
    p2.checkBalance(AccountNum);
}