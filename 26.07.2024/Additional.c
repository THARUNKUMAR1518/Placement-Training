
#include<stdio.h>
int main()
{
    int n,i,sum=0;
    printf("Enter the number range to add even numbers :");
    scanf("%d",&n);
    for(i=0;i<=n;i++)
    {
    if(i%2==0)
    { 
      sum=sum+i;   
    }
    }
    printf("The Sum is %d",sum);
    return 0;
}


