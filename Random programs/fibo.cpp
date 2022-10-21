#include <stdio.h>

int memo[500];
int calc[500];
int n;

int fibo(int n){
	if(n==0){return 1;
	}
	if(n==1){return 1;
	}
	if(calc[n]==1){return memo[n];
	}
	
	memo[n]= fibo(n-1) + fibo(n-2) ;
	calc[n]=1;
	
return memo[n];}


int main(){
	int fn;
	
		printf("\n n=");
		scanf("%d",&n);
		for(int i=0; i<=n;i++){calc[i]=0;
		}
		
		fn=fibo(n-1)+fibo(n-2);
		
		printf("\n %d \t %d",n, fn);
		
return 0;}
