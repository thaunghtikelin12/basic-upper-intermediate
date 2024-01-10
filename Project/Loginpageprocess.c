 #include "stdio.h"
int menu();
int Login();
int Register();
int regcount=0;
int total;

struct Data{
    char i_useremail[20];
    char i_username[20];
    char i_userpassword[20];
    int i_userID[10];

};
struct Data Db[10];
int main (){
    
        int menuNo=menu();
        if(menuNo==1){
            Login();
        }
        else if(menuNo==2){
            Register();
        }
        else if(menuNo==3){
            return 0;
        }
        return menu();
}
int menu(){
    int a;
    printf("Enter 1 for Log in \n"
           "Enter 2 for Register \n"
           "Enter 3 for Exit :\n");
    scanf ("%d",&a);
    return a;
}
int check(char first[20],char second[20]);
int Login(){
    char l_useremail[20];
    char l_userpassword[20];
    printf("Enter your email :");
    scanf(" %[^\n]",&l_useremail);
    printf("Enter your password :");
    scanf(" %[^\n]",&l_userpassword);
    check(l_useremail,l_userpassword);
}
int check(char first[20],char second[20]){
    int i;
    int j;
    int fir=0;
    int sec=0;

    for(i=0;i<20;i++){
        if(first[i]=='\0'){
            break;
        } else{fir++;}
    }
    for(i=0;i<20;i++){
        if(second[i]=='\0'){
            break;
        } else{sec++;}
    }
    for(i=0;i<regcount;i++){
        int k=0;
        for (j=0;j<20;j++){
            if (first[j] != '\0' && first[j]==Db[i].i_useremail[j] )
            {k++;}
        }
       printf("%d\n",k);
       printf("%d\n",fir);
       printf("%d\n",sec);
        if (k==fir){
            int Plogin=0;
            int m=0;
            for(j=0;j<20;j++){
               if (second[j]==Db[i].i_userpassword[j] && second[j] !='\0'){
                   m++;}
            }printf("%d",m);
            if(m==sec){
                printf("Your Log in is success\n");
            return main();}
        }else{
        printf("your email is fail\n");
        return Login();}
    }
}
int Rmail(char Rfirst[20]);
int Stongpass(char Sfirst[20]);
int Register(){
    int Sp;
    int Rm;
    printf("Enter your Regsister Email :");
    scanf(" %[^\n]",&Db[regcount].i_useremail);
    Rm=Rmail(Db[regcount].i_useremail);
    if (Rm!=-1){
        return Register();
    }
    printf("Enter your confirm password :");
    scanf(" %[^\n]",&Db[regcount].i_userpassword);
    
    Sp = Stongpass(Db[regcount].i_userpassword);
    if(Sp!=-1){
        printf("Your password is week \nAt least one small letter\nAt least one Cap letter\nAtleast one specail letter");
        return Register();
    }
    printf("Enter your confirm ID :\n");
    scanf(" %d",&Db[regcount].i_userID);

    printf("Enter your confirm Name :");
    scanf(" %[^\n]",&Db[regcount].i_username);

    regcount++;

    // printf("your user name is %s\n",Db[regcount].i_useremail);
    // printf("your password is %s\n",Db[regcount].i_userpassword);
    return main();
}
int Rmail(char Rfirst[20]){
    int i;
    int j;
    int k=0;
    for(i=0;i<regcount;i++){
//        int j;
        for(j=0;j<20;j++){
            if (Rfirst[j]==Db[i].i_useremail[j]){
                k++;
            }if (k==20){
                printf("Yor Email is repeat\n");
                return Register();
            }
        }
    }printf("[1] Repeat Email function success\n");
    return -1;
}
int Stongpass(char Sfirst[20]){

    int inpas=0;
    int spechar=0;
    int Smachar=0;
    int Capchar=0;
    int i;
    for(i=0;i<20;i++){
        if('a'<=Sfirst[i] && Sfirst[i]<='z'){
            Smachar++;
        }
        if('A'<=Sfirst[i] && Sfirst[i]<='Z'){
            Capchar++;
        }if((33<=Sfirst[i] && Sfirst[i]<=47)|| (58<=Sfirst[i]  &&  Sfirst[i]<=64)||(91<= Sfirst[i] && Sfirst[i]<=96)||(123<=Sfirst[i] && Sfirst[i]<=126)){
            spechar++;
        }
    }
    inpas=spechar+Capchar+Smachar;
    if(inpas>6 && spechar>0 && Capchar>0 && Smachar>0){
        printf("[2]Your password is strong \n\n");
        return -1;
    }else{
        printf("%d",inpas);
        return 1;}
}






