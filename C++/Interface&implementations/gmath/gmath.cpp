#include <cmath>
#include "gmath.h"
extern const double PI = 3.1415926;
double sinDegrees(double angle){
    return sin(toRadians(angle));
}
double cosDegrees(double angle){
    return cos(toRadians(angle));
}
double toDegrees(double radians){
    return radians * 180 / PI;
}
double toRadians(double degrees){
    return degrees * PI / 180;
}