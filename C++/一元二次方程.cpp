#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

// prototypes
void getCoefficients(double &a, double &b, double &c);
void solve(double a, double b, double c, double &x1, double &x2);
void printRoots(double x1, double x2);
void error(string msg);

// main program
int main()
{
    double a, b, c, r1, r2;
    getCoefficients(a, b, c);
    solve(a, b, c, r1, r2);
    printRoots(r1, r2);
    return 0;
}

// definitons
void getCoefficients(double &a, double &b, double &c)
{
    cout << "Enter coefficients: " << endl;
    cout << "a:";
    cin >> a;
    cout << "b:";
    cin >> b;
    cout << "c:";
    cin >> c;
}

void solve(double a, double b, double c, double &x1, double &x2)
{
    if (a == 0)
        error("The coefficient of a must be nonzero.");
    double disc = b * b - 4 * a * c;
    if (disc < 0)
        error("This equation has no real roots.");
    double sqrtDisc = sqrt(disc);
    x1 = (-b + sqrtDisc) / (2 * a);
    x2 = (-b - sqrtDisc) / (2 * a);
}

void prinRoots(double x1, double x2)
{
    if (x1 == x2)
    {
        cout << "There is a double root at " << x1 << endl;
    }
    else
    {
        cout << "The roots are " << x1 << "and" << x2;
    }
}

void error(string msg)
{
    cerr << msg << endl;
    exit(EXIT_FAILURE);
}