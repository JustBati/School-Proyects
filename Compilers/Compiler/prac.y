%{
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct nodo{
    int id;
    char* name;
    char* value;
    int type;
    struct nodo *next;
}Nodo;

typedef struct dato{
    int tipo;
    int entero;
    double doble;
    char* string;
    char* id;
}Dato;

typedef struct cola{
    Nodo* primero;
    Nodo* ultimo;
    int tamanio;
}Cola;

void formar(char *name,char *value,int type);
void mostrar();
void modificar(char *name, char *value, int type);
int buscar(char *name);
struct nodo consulta(char *name);
char * potencia(char * str,int pot);

Cola *new;

int length(char* p);
char * conCat(char *c1, char * c2);
%}

/*Declaraciones de bison*/
%union 
{
    int entero;
    double real;
    char* cadena;
    struct dato dato;
}

%token EOL
%token <entero> ENTERO
%token <real> flo
%token <dato> VARIABLE
%token <dato> DATO

%token SI 
%token DIV 
%token MULTI 
%token MOD
%token SUMA 
%token RES 
%token parentD 
%token parentI 
%token COMA 
%token INT
%token DOUBLE
%token STRING
%token POW
%token SHOW

%type <dato> exp




%left '+' '-'
%left '*' '/' '%' POW

/* Gramaticas*/
%%


input: 
        | input line
;

line:   EOL
        |   exp EOL  {
            if($1.tipo==1){
                //printf("\tresultado:  %d\n", $1.entero); 
            }else if($1.tipo==2){
                //printf("\tresultado:  %f\n", $1.doble); 
            }else if($1.tipo==3){
                //printf("\tresultado:  %s\n", $1.string); 
            }
        }
        |   SHOW  {mostrar();}
;

exp:    DATO { $$ = $1; }
       | VARIABLE {
                        struct nodo aux;
                        aux.name= malloc(255);
                        aux.value= malloc(255);
                        aux= consulta($1.id);
                        if(aux.type==1){
                            $$.tipo=aux.type;
                            if(aux.value!=NULL){
                                $$.entero= atoi(aux.value);
                            }
                        }
		                if(aux.type==2){
		                	$$.tipo=aux.type;
		                	$$.doble=atof(aux.value);
		                }
		                if(aux.type==3){
		                	$$.tipo=aux.type;
		                	$$.string=aux.value;
		                }
		                if(aux.type==4){
		                	printf("ERROR: Variable no declarada\n");
		                }
        }
        | INT VARIABLE ';'{
                        if(buscar($2.id)==0){
                            formar($2.id,NULL,1);
                            $$.tipo=1;
                        }else{
                            printf("La variable ya existe\n");
                        }
                            $$.entero=0;
        }
        | DOUBLE VARIABLE ';'{
                        if(buscar($2.id)==0){
                            formar($2.id,NULL,2);
                            $$.tipo=2;
                        }else{
                            printf("La variable ya existe\n");
                        }
                            $$.doble=0;
        }
        | STRING VARIABLE ';'{
                        if(buscar($2.id)==0){
                            formar($2.id,NULL,3);
                            $$.tipo=3;
                        }else{
                            printf("La variable ya existe\n");
                        }
                            $$.string=NULL;
        }
        |INT VARIABLE '=' exp ';' { 
                        char *s= malloc(sizeof(char) * 128);
                        if(buscar($2.id)==0){
                            if($4.tipo==1 || $4.tipo==2){
                                if($4.tipo==2){
                                    int var= $4.doble;
                                    snprintf(s,sizeof(s),"%d",var);
                                    $$.entero=$4.doble;
                                }else{
                                    snprintf(s,sizeof(s),"%d",$4.entero);
                                    $$.entero=$4.entero;
                                }
                                formar($2.id,s,1);
                                $$.tipo=1;
                            }else{
                                printf("Tipo incompatible\n");
                            }         
                        }else{
                            printf("La variable ya existe\n");
                            $$.entero=0;
                        }
        }
        | DOUBLE VARIABLE '=' exp ';' {
                        char *s = malloc(sizeof(char)*128);
                        if(buscar($2.id)==0){
                            if($4.tipo==1 || $4.tipo==2){
                                 if($4.tipo==2){
                                    snprintf(s,sizeof(s),"%.3f",$4.doble);
                                    $$.doble=$4.doble;
                                }else{
                                    double var=$4.doble;
                                    snprintf(s,sizeof(s),"%.3f",var);
                                    $$.doble=$4.doble;
                                }
                                formar($2.id,s,2);
                                $$.tipo=2;
                            }else{
                                printf("Tipo incompatible\n");
                            }
                        }else{
                            printf("La variable ya existe\n");
                            $$.doble=0;
                        }
        }
        | STRING VARIABLE '=' exp ';' {
                        char *s = malloc(sizeof(char)*128);
                        if(buscar($2.id)==0){
                            if($4.tipo==3){
                                formar($2.id,$4.string,$4.tipo);
                                $$.tipo=3;
                                $$.string= $4.string;    
                            }else{
                                printf("Tipo incompatible\n");
                            }
                        }else{
                            printf("La variable ya existe\n");
                            $$.string=NULL;
                        }
        }
        | VARIABLE '=' exp ';' {
                        if(buscar($1.id)==0){
                            printf("Variable no encontrada\n");
                        }else{
                            if($3.tipo==1){
                                char *s =malloc(sizeof(int));
                                snprintf(s,sizeof(s),"%d",$3.entero);
                                modificar($1.id,s,$3.tipo);
                            }
                            if($3.tipo==2){
                                char *s =malloc(sizeof(double));
                                snprintf(s,sizeof(s),"%.4f",$3.doble);
                                modificar($1.id,s,$3.tipo);
                            }
                            if($3.tipo==3){
                                modificar($1.id,$3.string,$3.tipo);
                            }
                            printf("Variable modificada\n");
                        }
        }
        | exp '+' exp {
                if($1.tipo==1 && $3.tipo==1){
                    $$.tipo=1;
                    $$.entero= $1.entero + $3.entero;
                }
                else if($1.tipo==1 && $3.tipo==2){
                    $$.tipo=2;
                    $$.doble= $1.entero + $3.doble;
                }
                else if($1.tipo==2 && $3.tipo==1){
                    $$.tipo=2;
                    $$.doble= $1.doble + $3.entero;
                }
                else if($1.tipo==2 && $3.tipo==2){
                    $$.tipo=2;
                    $$.doble= $1.doble + $3.doble;
                }
                else if($1.tipo==3 && $3.tipo==3){
                    $$.tipo=3;
                    $$.string= conCat($1.string,$3.string);
                
                }else{
                    printf("Tipos incompatibles");
                }
        }
        |exp '-' exp {
            if($1.tipo==1 && $3.tipo==1){
                    $$.tipo=1;
                    $$.entero= $1.entero - $3.entero;
                }
                else if($1.tipo==1 && $3.tipo==2){
                    $$.tipo=2;
                    $$.doble= $1.entero - $3.doble;
                }
                else if($1.tipo==2 && $3.tipo==1){
                    $$.tipo=2;
                    $$.doble= $1.doble - $3.entero;
                }
                else if($1.tipo==2 && $3.tipo==2){
                    $$.tipo=2;
                    $$.doble= $1.doble - $3.doble;
                }
                else{
                    printf("Tipos incompatibles");
                }
        }
        |exp '*' exp {
                if($1.tipo==1 && $3.tipo==1){
                    $$.tipo=1;
                    $$.entero= $1.entero * $3.entero;
                }
                else if($1.tipo==1 && $3.tipo==2){
                    $$.tipo=2;
                    $$.doble= $1.entero * $3.doble;
                }
                else if($1.tipo==2 && $3.tipo==1){
                    $$.tipo=2;
                    $$.doble= $1.doble * $3.entero;
                }
                else if($1.tipo==2 && $3.tipo==2){
                    $$.tipo=2;
                    $$.doble= $1.doble * $3.doble;
                }
                else{
                    printf("Tipos incompatibles");
                }
        }
        |exp '/' exp {
                if($1.tipo==1 && $3.tipo==1 && $3.entero!=0){
                    $$.tipo=1;
                    $$.entero= $1.entero / $3.entero;
                }
                else if($1.tipo==1 && $3.tipo==2&& $3.doble!=0){
                    $$.tipo=2;
                    $$.doble= $1.entero / $3.doble;
                }
                else if($1.tipo==2 && $3.tipo==1&& $3.entero!=0){
                    $$.tipo=2;
                    $$.doble= $1.doble / $3.entero;
                }
                else if($1.tipo==2 && $3.tipo==2&& $3.doble!=0){
                    $$.tipo=2;
                    $$.doble= $1.doble / $3.doble;
                }
                else{
                    printf("Tipos incompatibles");
                }
        }
        |exp '%' exp {
                if($1.tipo==1 && $3.tipo==1){
                    $$.tipo=1;
                    $$.entero=fmod($1.entero , $3.entero);
                }
                else if($1.tipo==1 && $3.tipo==2){
                    $$.tipo=2;
                    $$.doble= fmod($1.entero , $3.doble);
                }
                else if($1.tipo==2 && $3.tipo==1){
                    $$.tipo=2;
                    $$.doble= fmod($1.doble , $3.entero);
                }
                else if($1.tipo==2 && $3.tipo==2){
                    $$.tipo=2;
                    $$.doble= fmod($1.doble , $3.doble);
                }
                else{
                    printf("Tipos incompatibles");
                }
        }
        |POW '(' exp ',' exp ')' {
            if($3.tipo==1 && $5.tipo==1){
                    $$.tipo=1;
                    $$.entero= pow($3.entero , $5.entero );
                }
                else if($3.tipo==1 && $5.tipo==2){
                    $$.tipo=2;
                    $$.doble= pow($3.entero , $5.doble);
                }
                else if($3.tipo==2 && $5.tipo==1){
                    $$.tipo=2;
                    $$.doble= pow($3.doble , $5.entero);
                }
                else if($3.tipo==2 && $5.tipo==2){
                    $$.tipo=2;
                    $$.doble= pow($3.doble , $5.doble);
                }

                else if($3.tipo==3 && $5.tipo==1){
                    $$.tipo=3;
                    $$.string= potencia($3.string,$5.entero);
                }else{
                    printf("Tipos incompatibles");
                }
        }
        |SI '(' exp '>' exp ')' ';'{
            if($3.tipo==1 && $5.tipo==1){
                    if($3.entero > $5.entero){
                  printf("True \n");

                    }else{
                  printf("False \n");
                    }                  
                }
                else if($3.tipo==1 && $5.tipo==2){
                   if($3.entero > $5.doble){
                  printf("True \n");

                    }else{
                  printf("False \n");
                    }
                }
                else if($3.tipo==2 && $5.tipo==1){
                   if($3.doble > $5.entero){
                  printf("True \n");

                    }else{
                  printf("False \n");
                    }
                }
                else if($3.tipo==2 && $5.tipo==2){
                   if($3.doble > $5.doble){
                  printf("True \n");

                    }else{
                  printf("False \n");
                    }
                  
                }
                else{
               printf("Tipos incompatibles");
                    
                }
        }

;





%%

int main(){
    new=(Cola*)malloc(sizeof(Cola));
    new->tamanio=0;
    new->primero=NULL;
    new->ultimo=NULL;
    yyparse();

    return 0;
}

yyerror(char * s){
    printf("error: %s\n", s);
    return 0;
}

int length(char* p) {
    int count = 0;
    while (*p != '\0') {
        count++;
        p++;
    }
    return count;
}

char * conCat(char *c1, char *c2){
	int  i;
	char *u;
	int j;
	i = j = 0;
	size_t t1 =  length(c1);
	size_t t3 =  length(c2);
	size_t sum = t1 + t3;
	u = (char*)malloc(sum + 1);
	 for(i = 0; i < t1; i++)
	 	if(c1[i] != '"')
	 		u[j++] = c1[i];

	 for(i = 0; i < t3; i++)
	 	if(c2[i] != '"')
	 		u[j++] = c2[i];


	 u[j] = '\0';
	 return u;
}

void formar(char *name,char *value,int type){
    if(new->tamanio==0){
        Nodo* n;
        n=(Nodo*)malloc(sizeof(Nodo));
        n->id= new->tamanio;  
        n->name=malloc(sizeof(char) * 128);
        n->value=malloc(sizeof(char) * 128);
        n->name=name;
        n->value= value;
        n->type= type;
        n->next=NULL;
        new->primero=n;
        new->ultimo=n;
        new->tamanio++;
        printf("variable agregada\n");
    }else{
        Nodo* n;
        n=(Nodo*)malloc(sizeof(Nodo));
        n->id= new->tamanio+1;  
        n->name=malloc(sizeof(char) * 128);
        n->value=malloc(sizeof(char) * 128);
        new->ultimo->next=n;
        n->name= name;
        n->value= value;
        n->type= type;
        n->next=NULL;
        new->ultimo=n;
        new->tamanio++;
        printf("variable agregada.\n");
    }
}

void mostrar(){
    struct nodo *control;
    control = NULL;
    if(new->primero==NULL && new->ultimo==NULL){

    }else
    {
            printf("Simbolos:\n");
            control= new->primero;
            do{
                printf("Id: %d || nombre: %s || valor: %s || tipo: %d\n",control->id,control->name, control->value, control->type);
                control=control->next;
            }while(control);
            printf("\n");
    }
}

int buscar(char *name){
    struct nodo *control;
    int encontrado=0;
    control = NULL;

    if(new->primero== NULL && new->ultimo==NULL){\
    }else{
        control= new->primero;
        do{
            if(0==strcmp(control->name,name)){
                
                    encontrado=1;
                    return encontrado;
                
            }
            control=control->next;
        }while(control);
        printf("\n");
    }
    return encontrado;
}

void modificar(char *name, char *value, int type){
    struct nodo *control;
    control= NULL;
    if(new->primero==NULL && new->ultimo==NULL){

    }else{
        control= new->primero;
        do{
            if(0==strcmp(control->name,name)){
                if(control->type==type||(type==2&&control->type==1)||(type==1&&control->type==2)){
                    control->value=value;
                }else{
                    printf("Tipos incompatibles\n");
                }
            }
            control= control->next;
        }while(control);
    }
}

struct nodo consulta(char *name){
    struct nodo *control;
    struct nodo aux;
    aux.name = malloc(255);
    aux.value = malloc(255);
    control=NULL;

    if(new->primero==NULL && new->ultimo==NULL){

    }else{
        control= new-> primero;
        do{
            if(0==strcmp(control->name,name)){
                aux=*control;
                return aux;
            }
            control= control->next;
        }while(control);
        printf("\n");

    }
    aux.type=4;
    return aux;
}

char * potencia(char * str,int pot){
	
	char * ptr = 0;
	int ptrSize = 0;
	int  l;
    for(int i;str[i]!='\0';i++){l=i;}
	for(int i = 0; i < pot; i++){
		ptrSize += l;
		ptr = (char*)realloc(ptr,ptrSize);
		ptr = strdup(conCat(ptr,str));
	}
	ptr[ptrSize] = '\0';
    
    return ptr;
}