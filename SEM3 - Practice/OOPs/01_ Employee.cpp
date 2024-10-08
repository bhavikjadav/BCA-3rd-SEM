/*
Write a C++ Program to create a class Employee in which declare the members Empno, Name, Salary, Designation. Create a necessary function for taking the input of 5 employees and display the name of employee which designation is manager.
*/

#include<iostream>
#include<cstring>

using namespace std;

class Employee {
    public:
    int emp_no;
    char name[20];
    double salary;
    char designation[10];

    public:
    void take_input() {
        std::cout << "Enter the EMP No: ";
        std::cin >> emp_no;
       
        std::cout << "Enter the Name : ";
        std::cin >> name;
       
        std::cout << "Enter the Salary : ";
        std::cin >> salary;
       
        std::cout << "Enter the Designation : ";
        std::cin >> designation;
    }

    void display_output() {
        std::cout << "Emp No : " << emp_no << endl;
        std::cout << "Emp Name : " << name << endl;
        std::cout << "Emp Salary : " << salary << endl;
        std::cout << "Emp Designation : " << designation << endl;
    }
};

int main() {

    Employee e1[10];
    int i,n;
    char cmp[10] = "manager";

    std::cout << "How many entries you want ? ";
    std::cin >> n;

    for (i = 0; i < n; i++) {
        e1[i].take_input();
    }

    for (i = 0; i <= n; i++) {
        if (strcmp(e1[i].designation, cmp) == 0) {
            e1[i].display_output();
        }
    }

    return 0;
}