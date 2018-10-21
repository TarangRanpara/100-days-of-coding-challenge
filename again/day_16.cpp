#include <iostream>

using namespace std;

int main()
{
    int n = 0;
    cout<<"enter n:";   cin>>n;
    string str[n];

    //user input
    for(int i=0;i<n;i++)
        cin>>str[i];

    //naive approach
    for(int i=0; i<n-1; i++){

        //comparing with each next element
        for(int j=i+1; j<n; j++){
            if(str[i] > str[j]){

                string temp = str[i];
                str[i] = str[j];
                str[j] = temp;
            }
        }
    }

    //displaying result
    for(int i=0;i<n;i++)
        cout<<str[i]<<endl;

    return 0;
}
