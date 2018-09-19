#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int n;
    cout<<"enter no of test cases:";    cin>>n;

    while((n--) > 0) {

        int len = 0;
        cout<<"enter length:";  cin>>len;

        string str;
        cout << "enter string:" << endl;    cin>>str;

        int counter = 0,i = 0;

        while(i<len){

            if(isdigit(str[i])){

                while(isdigit(str[i]))
                    i++;
                counter++;
                i++;
            }
            else
                i++;
        }
        cout<<counter;
    }
    return 0;
}
