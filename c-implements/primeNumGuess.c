#include <stdio.h>
#include <math.h>

int isPrime(int n)
{
    int res = 1
    for (int i = 2; i <= (int)sqrt(n); i++)
    {
        if(n%i == 0) 
        {
            res = 0;
            break;
        }
    }
    return res;
}


void main()  
{
    int firstP = 0, secondP = 0;
    int N = 20;
    int flag = 1;
    while ()
}