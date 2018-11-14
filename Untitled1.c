#include<stdio.h>
//#include<fstream.h>
int main()
{
    char n0='a',n1='a',n2='a',n3='a';
    freopen("demofile.txt","r",stdin);
    freopen("addout.txt","w",stdout);
    while(1){
            n0=n1;
            n1=n2;
    n2=n3;

    scanf("%c",&n3);
    if((n3=='{'&&n2=='{'))
        {
            while(1)
        {
            n0=n1;
            n1=n2;
            n2=n3;
            scanf("%c",&n3);
            //printf("%c %c %c",n1,n2,n3);
            if((n3=='}'&&n2=='}'))break;
        }
        }
    if(n0='<'&&n1=='r'&&n2=='e'&&n3=='f'){
        while(1)
        {
            n0=n1;
            n1=n2;
            n2=n3;
            scanf("%c",&n3);
            //printf("%c %c %c",n1,n2,n3);
            if(n0=='/'&&n1=='r'&&n2=='e'&&n3=='f')break;
        }
    }
    if(n0='q'&&n1=='u'&&n2=='o'&&n3=='t'){
        while(1)
        {
            n0=n1;
            n1=n2;
            n2=n3;
            scanf("%c",&n3);
            //printf("%c %c %c",n1,n2,n3);
            if(n0=='q'&&n1=='u'&&n2=='o'&&n3=='t')break;
        }
    }

    if(n0=='<'&&n1=='!'&&n2=='-'&&n3=='-'){
        while(1)
        {
            n0=n1;
            n1=n2;
            n2=n3;
            scanf("%c",&n3);
            //printf("%c %c %c",n1,n2,n3);
            if(n1=='-'&&n2=='-'&&n3=='>')break;
        }
    }
    printf("%c",n3);
    }
   // printf("%d",n2);
}

