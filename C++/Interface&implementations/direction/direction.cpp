//This file implements the direction.h interface
#include <string>
#include "direction.h"

using namespace std;

Direction leftFrom(Direction dir){
    return Direction((dir + 3) % 4);
}
Direction rightFrom(Direction dir){
    return Direction((dir + 1) % 4);
}

string directionToString(Direction dir){
    switch (dir)
    {
    case North:
        return "north";
    case East:
        return "east";
    case West:
        return "west";
    case South:
        return "south";
        break;
    default:
        return "????";
    }
}