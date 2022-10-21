%{
    #include "ejemplo.tab.h"
    #include <math.h>
%}


%%
[0-9]+ { printf("int\n"); yylval.entero = atoi(yytext); return ENTERO; }
[0-9]*\.[0-9]+ { printf("decimal\n");  yylval.real = atof(yytext); return flo;}
[Mm][Oo][dD] {printf("Modulo\n"); return MOD;}
"(" {return parentD;}
")" {return parentI;}
"," {return COMA;}
"/" {return DIV;}
"+" {printf("Operacion\n"); return SUMA;}
"-" {return RES;}
"*" {return MULTI;}
\n {printf("Salto de linea\n"); return EOL;}
. {}
%%
yywrap(){}

