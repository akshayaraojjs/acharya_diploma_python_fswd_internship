#include<iostream>
using namespace std;

class Car{
    public:
    // Data Members
    string model, type;
    int launch_year;
    float mileage;

    // Member Functions
    void startCar(string m){
        cout << m << " car started!" << endl;
    }

    void driveCar(string m, string t){
        cout << m << " car started moving which consumes " << t << " as the fuel for moving" << endl;
    }

    void checkMileage(float m){
        cout << "The car is giving the mileage of " << m << " kmpl" << endl;
    }
};

int main(){
    Car c1, c2; // c1 & c2 are the objects of Car Class
    c1.model = "Toyato Innova";
    c1.type = "Diesel";
    c1.launch_year = 2025;
    c1.mileage = 23.5;

    c1.startCar(c1.model);
    c1.driveCar(c1.model, c1.type);
    c1.checkMileage(c1.mileage);

    cout << "Enter the details of Car 2: \n";
    cout << "Enter the Car Model Name: ";
    cin >> c2.model;
    cout << "Enter the Car Fuel Type: ";
    cin >> c2.type;
    cout << "Enter the Car Launch Year: ";
    cin >> c2.launch_year;
    cout << "Enter the Car Mileage: ";
    cin >> c2.mileage;

    c2.startCar(c2.model);
    c2.driveCar(c2.model, c2.type);
    c2.checkMileage(c2.mileage);
}