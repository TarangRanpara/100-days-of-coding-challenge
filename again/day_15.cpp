#include <iostream>

using namespace std;

int get_sum(int n){
    int sum = 0;

    for(int i=1;i<n;i++)
        if(n%i == 0)
            sum += i;


    return sum;
}

int main()
{
    int n1,n2;
    cout<<"enter number pair:"<<endl;      cin>>n1>>n2;

    if(get_sum(n1) == n2 && get_sum(n2) == n1)
        cout<<n1<<" & "<<n2<<" are amicable numbers.";
    else
        cout<<n1<<" & "<<n2<<" are not amicable numbers.";

    return 0;
}
