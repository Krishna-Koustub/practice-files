#include<stdio.h>
intmain ()
{
    intnum,rev=0,temp,rem;
    printf("please enter the number \n");
    scanf("%d",&num);
    temp=num;
    while (temp!=0)
    {
        rem=temp%10;
        temp=temp / 10;
        rev = rev*10 + rem;
    }
    printf("the reverse number is :%d\n",rev);
    if (num==rev)
    {
        printf("it is a palindrome \n");
    }
    else
    {
        printf("it is not a palindrome \n");
    }
}
