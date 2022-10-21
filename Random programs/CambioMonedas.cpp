#include <stdio.h>

int main(){
	 int cambio[4];		// tipos de monedas para cambio : {10, 5, 2, 1}
	 int dinero=0, n;
	
	printf("\n ingrese la cantidad a dar cambio: \n");
	scanf("%d",&dinero);
	
	if (dinero>=10){
		n=dinero/10;
		dinero= dinero%10;
		cambio[0]=n;
	}
	
	if (dinero>=5){
		n=dinero/5;
		dinero= dinero%5;
		cambio[1]=n;
	}
	
		if (dinero>=2){
		n=dinero/2;
		dinero= dinero%2;
		cambio[2]=n;
	}

	if (dinero>=1){
		n=dinero/1;
		dinero= dinero%1;
		cambio[3]=n;
	}

printf("\n\n El cambio seria en:");
printf("\n\t %d \tmonedas de 10",cambio[0]);
printf("\n\t %d \tmonedas de 5",cambio[1]);
printf("\n\t %d \tmonedas de 2",cambio[2]);
printf("\n\t %d \tmonedas de 1",cambio[3]);
return 0;}
