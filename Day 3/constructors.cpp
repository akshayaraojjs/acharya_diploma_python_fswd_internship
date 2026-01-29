#include<iostream>
using namespace std;

class Hotel{
    // akshay rao - Lower Case
    // AKSHAY RAO- Upper Case
    // Akshay Rao- Title Case
    // akshayRao- Camel Case
    // AkshayRao- Pascal Case
    // akshay_rao- Snake Case
    private:
    string wifiName, password, roomNum;

    public:
    string Cname, Cmobile, Caadhar;
    int numOfDays, Amount;

    // Default Constructor
    Hotel(){
        Cname = "Guest";
        Cmobile = "N/A";
        Caadhar = "N/A";
        numOfDays = 0;
    }
    
    void printCustomerDetails(){
        cout << "Customer Details are as follows: \n";
        cout << "Customer Name: " << Cname << endl;
        cout << "Customer Phone Number: " << Cmobile << endl;
        cout << "Customer Aadhaar Number: " << Caadhar << endl;
    }

    void bookRoom(string name, string phone, string govt, int days){
        Amount = days * 250;

        cout << "Total amount for " << days << " of stay in our Hotel costs Rs." << Amount << "/-" << endl;  

        roomNum = "A105";

        cout << "Thank You for the payment! Your Room No: " << roomNum << ". Enjoy your stay!" << endl;
    }

    // setter
    void wifiEnquiry(string name, string rNum){
        string wifiSSID = "Ashoka";
        string wifiPassword = "Ashoka@123";

        wifiName = wifiSSID;
        password = wifiPassword;

        cout << "Wifi Details for the Customer: \n";
        cout << "Wifi Name: " << wifiName << endl;
        cout << "Wifi Password: " << password << endl;
    }

    void giveWifiDetails(){
        string ssid = "Guest";
        string pass = "Guest@123";

        wifiName = ssid;
        password = pass;

        cout << "Wifi Details for the Guest User: \n";
        cout << "Wifi Name: " << wifiName << endl;
        cout << "Wifi Password: " << password << endl;
        cout << "Wifi can be used freely for 30mins!" << endl;
    }

    // Constructor is a special type of method
    // Constructor is having the same name as that of Class
    // Constructor is used to assign the initial values for the data members
    // Constructor will be called automatically when the object is created
    // Constructor doesn't return any value
    // Types of Constructors: Default, Parametersized, Constructor Overloading
};

int main(){
    Hotel cust1, cust2;
    cust1.printCustomerDetails();
    cust1.giveWifiDetails();

    cust2.Cname = "Akshay Rao";
    cust2.Cmobile = "9852487544";
    cust2.Caadhar = "985248754412";

    cust2.printCustomerDetails();

    cust2.bookRoom(cust2.Cname, cust2.Cmobile, cust2.Caadhar, 5);

    cust2.wifiEnquiry(cust2.Cname, "A103");
}