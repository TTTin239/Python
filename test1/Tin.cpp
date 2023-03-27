#include <iostream>
using namespace std;
int main()
{
    int n,lon;
    cin>>n;
    if(n<10&&n>=0){
        lon=9;
    }
    else if(n<100&&n>=10){
        for(int i=10;i<(9-(n/10))*10;i+=10){
            if((n+i)%3==0&&(n+i)>lon){
                lon=n+i;
            }
        }
        for(int j=1;j<9-(n%10);j++){
            if((n+j)%3==0&&(n+j)>lon){
                lon=n+j;
            }
        }
    }
    else if(n<1000&&n>=100){
        for(int i=100;i<(9-(n/100))*100;i+=100){
            if((n+i)%3==0&&(n+i)>lon){
                lon=n+i;
            }
        }
        for(int i=10;i<(9-(n/10))*10;i+=10){
            if((n+i)%3==0&&(n+i)>lon){
                lon=n+i;
            }
        }
        for(int j=1;j<9-(n%10);j++){
            if((n+j)%3==0&&(n+j)>lon){
                lon=n+j;
            }
        }
    }
    cout<<lon;
    //samon247
    return 0;
}

