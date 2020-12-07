#include <iostream> 
#include <float.h> 
#include <stdlib.h> 
#include <math.h> 
using namespace std; 
  
// A structure to represent a Point in 2D plane 
struct Point 
{ 
    int x, y; 
}; 
  
  
/* Following two functions are needed for library function qsort(). 
   Refer: http://www.cplusplus.com/reference/clibrary/cstdlib/qsort/ */
  
// Needed to sort array of points according to X coordinate 
int compareX(const void* a, const void* b) 
{ 
    Point *p1 = (Point *)a,  *p2 = (Point *)b; 
    return (p1->x - p2->x); 
} 
// Needed to sort array of points according to Y coordinate 
int compareY(const void* a, const void* b) 
{ 
    Point *p1 = (Point *)a,   *p2 = (Point *)b; 
    return (p1->y - p2->y); 
} 
  
// A utility function to find the distance between two points 
float dist(Point p1, Point p2) 
{ 
    return sqrt( (p1.x - p2.x)*(p1.x - p2.x) + 
                 (p1.y - p2.y)*(p1.y - p2.y) 
               ); 
} 
  
// A Brute Force method to return the smallest distance between two points 
// in P[] of size n 
float bruteForce(Point P[], int n) 
{ 
    float min = FLT_MAX; 
    for (int i = 0; i < n; ++i) 
        for (int j = i+1; j < n; ++j) 
            if (dist(P[i], P[j]) < min) 
                min = dist(P[i], P[j]); 
    return min; 
} 
  
// A utility function to find a minimum of two float values 
float min(float x, float y) 
{ 
 return (x < y)? x : y; 
} 
  
  
// A utility function to find the distance between the closest points of 
// strip of a given size. All points in strip[] are sorted according to 
// y coordinate. They all have an upper bound on minimum distance as d. 
// Note that this method seems to be a O(n^2) method, but it's a O(n) 
// method as the inner loop runs at most 6 times 
float stripClosest(Point strip[], int size, float d) 
{ 
    float min = d;  // Initialize the minimum distance as d 
  
    // Pick all points one by one and try the next points till the difference 
    // between y coordinates is smaller than d. 
    // This is a proven fact that this loop runs at most 6 times 
    for (int i = 0; i < size; ++i) 
        for (int j = i+1; j < size && (strip[j].y - strip[i].y) < min; ++j) 
            if (dist(strip[i],strip[j]) < min) 
                min = dist(strip[i], strip[j]); 
  
    return min; 
} 
  