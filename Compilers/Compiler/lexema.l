%{

    typedef struct dato
    {
        int tipo;
        int entero;
        double doble;
        char* string;
        char* id;
    }Dato;

    #include "prac.tab.h"
    #include <string.h>
    #include <stdio.h>
    #include <stdlib.h> 
    #include <stdbool.h>

    int largo(char* yytext);
%}


numeroInt [+-]?[0-9]+
numeroReal [+-]?[0-9]*["."][0-9]+
int "int"
string "string"
double "double"
show "show"
nameVar [a-zA-Z_]+[a-zA-z_0-9]*
blank [[:blank:]]
parentI "("
parentD ")"
COMA ","
DIV "/"
SUMA "+"
RES "-"
MULTI "*"
ASIG "="
MOD "%"
POW [Pp][Ow][Ww]
CadeValida \"(([^\"]|\\\")*[^\\])?\" 
endExp ";"
EOL \n 
%%

{int} {return INT;}
{double} {return DOUBLE;}
{string} {return STRING;}
[Pp][Oo][wW] {return POW;}
[Ii][Ff] {return SI;}
{show} {return SHOW;}
{numeroInt} {
        printf("Numero entero\n");
        yylval.dato.tipo=1;
        yylval.dato.entero=atoi(yytext);
        return DATO;
    }
{nameVar} {
        int i,j;
        char c = yytext[0];
        for(i=0;c!='\0';i++){
            c=yytext[i+1];
        }
        yylval.dato.id= malloc(i+1);
        for(j=0;j<i;j++){
            yylval.dato.id[j]=yytext[j];    
        }
        yylval.dato.id[i]='\0';
        return VARIABLE;
    }   
{numeroReal} {
        // printf("Numero decimal\n");
        yylval.dato.tipo=2;
        yylval.dato.doble=atof(yytext);
        return DATO;
        }
{CadeValida} {
        // printf("cadena valida\n");
        yylval.dato.tipo=3;
        int stringL= largo(yytext);
        yylval.dato.string = malloc(stringL);
        for(int i=0; i<stringL;i++){
            
            yylval.dato.string[i]= yytext[i+1];
        }
        return DATO;

    }
{endExp} {return yytext[0];} 
{EOL} {
    return EOL;} 
{ASIG} {return yytext[0];} 
"+" { return yytext[0];}
"%" { return yytext[0];}
")" { return yytext[0];}
"(" { return yytext[0];}
"," { return yytext[0];}
">" { return yytext[0];}


%%
yywrap(){}


int largo(char* yytext){
    int length=0;
    while(yytext[length]!='\0'){
     length++;
    }

        
    return length-2;
}