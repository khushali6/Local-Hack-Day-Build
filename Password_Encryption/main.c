#include<stdio.h>
int main(){
    char pass[100], c;
    int i;
    printf("Enter Your Password : ");
    gets(pass);
    for(i = 0; pass[i] != '\0';++i)
    {c = pass[i];
    if(c >= 'a' && c <= 'z'){
        c = c + 3;
        
        if(c > 'z')
        {c = c -'z' + 'a' -1;
        }
        pass[i] = c;
        
    }
    else if(c >= 'A' && c <= 'Z')
    {c = c + 3;
    if(c > 'Z')
    {c = c -'Z' + 'A' -1;
        
    }
    pass[i] = c;
        
    }}
    printf("Password after Encryption: %s\n", pass);return 0;}