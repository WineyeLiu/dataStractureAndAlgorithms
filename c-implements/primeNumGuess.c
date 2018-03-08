#include <stdio.h>
#include <math.h>

int isPrime(int n)
{
    int res = 1;
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



int main()  
{
    /*
    int firstP = 0, secondP = 0;
    int N = 20;
    int flag = 1;
    while ()
    */
    int max;
    scanf("%d", &max);
    int a[max/2];
    int index = 0;
    for (int i = 1; i <= max; i++)
    {
        if (isPrime(i) == 1)
        {
            a[index] = i;
            index ++;
        }
    }
    /* for (int j = 0; j < index; j++)
    {
        printf("%d\n", a[j]);
    } */
    //printf("isPrime? %d", isPrime(4));
    
    int ct = 0;
    for (int i = 0; i < index - 1; i++)
    {
        if (a[i+1] - a[i] == 2)
        {
            ct++;
        }
    }
    printf("%d", ct);
    return 0;
}