#include<iostream>
using namespace std;

bool prost(int n){
    for(int i = 2;i<= n;i++){
        if(n%i == 0){
            return false;
        }
    }
    return true;
}
int main(){
    int n;
    cin>>n;
    if(prost(n)){
        cout<<n;
    }
    else cout<<"Nije prost";
    return 0;
}
