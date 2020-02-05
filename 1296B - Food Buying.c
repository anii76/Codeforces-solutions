//https://codeforces.com/contest/1296/problem/B

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int t,s,i,x;
    scanf("%d", &t);
    for(x = 1; x<=t; x++){
        scanf("%d",&s);
        i = 0;
        while ((s-10*i)/10 >0){
            s++;
            i++;
        }
        printf("%d\n",s);
    }
    return 0;
}
