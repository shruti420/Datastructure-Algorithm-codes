#include <iostream>
using namespace std; 
long long gcd(long long int a, long long int b){        
    if(b==0)
        return a;
    return gcd(b,a%b);
}

long long lcm(long long a,long long b){     
    if(a>b)
        return (a/gcd(a,b))*b;
    else
        return (b/gcd(a,b))*a;    
} 

int main()
{
    long long int a ,b ;
    cin>>a>>b;
    cout<<lcm(a,b)<<endl;        
    return 0;
}