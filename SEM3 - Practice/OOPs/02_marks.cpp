/*
Write a C++ Program to create a class Marks which contain marks of 3 Subject. Create necessary function for class should be defining outside the class. 
Create another class sports which contain the score. Create necessary function this class which will define outside the class. 
Create another class for result which public inherit from marks and sports. 
Calculate Result based on marks or score.
*/

#include<iostream>
#include<cstring>

using namespace std;

class Marks {
    public:
    int math, science, art;

    public:
    int take_marks();
};

int Marks::take_marks() {

    cout << "Enter the marks of Maths : ";
    cin >> math;

    cout << "Enter the marks of Science : ";
    cin >> science;

    cout << "Enter the marks of Art : ";
    cin >> art;

    return (math+science+art);
}

class Sports {
    public:
    int score;

    public:
    int take_score();
};

int Sports::take_score() {
    cout << "Enter the Score : ";
    cin >> score;
    return score;
}

class Result: public Marks, public Sports {
    public:
    int total_result;
    
    public:
    void display_result();
};

void Result::display_result() {
    total_result = take_marks() + take_score();
    cout << "Result : " <<  total_result;
}

int main() {
    Result r1;
    r1.display_result();
    return 0;
}