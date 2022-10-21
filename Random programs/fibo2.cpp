#include <stdio.h>

int main (){
	int n, fn, f1,f2;
	
	printf("\t n=");
	scanf("%d",&n);
	
	for(int i=0;i<n;i++ )
	{
		if(i==0){fn=1, f1=1, f2=1;
		}
		if(i==1){fn=1, f1=1, f2=1;
		}
	
	fn=f1+f2;
	
	f2=f1;
	f1=fn;
	}
	
	printf("\n\n n=%d \t fn=%d", n,fn);
	
return 0;}
