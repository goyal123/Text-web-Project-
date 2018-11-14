#include<stdio.h>
//#include<fstream.h>

int main()
{
    char n0='a',n1='a',n2='a',n3='a';
    char a[100001];int i=0;
    freopen("demofile.txt","r",stdin);
    freopen("addout1.txt","w",stdout);
    printf("asd");
    while(1){
            n0=n1;
            n1=n2;
    n2=n3;
    i=0;
    scanf("%c",&n3);
    if((n3=='{'))
        {
          a[i]=n3;

          //printf(" *%d %c* ",i,a[i]);
          i++;
           while(1)
        {
            n0=n1;
            n1=n2;
            n2=n3;
            //printf("%c",n3);
            scanf("%c",&n3);
            //printf(" *%d %c* ",i,n3);
            //printf("%d",n3);
            if(n3=='{'||n3=='}')a[i]=n3;
            if(a[i]=='}'&&a[i-1]=='{')
                i=i-1;
            //a[i]=n3;
            //printf("%c %c %c",n1,n2,n3);
           // if((n3=='}'))break;
           if(i==1)break;
            if(n3=='{'||n3=='}')i++;
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
