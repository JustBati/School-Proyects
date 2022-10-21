    %{
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
%}

/*Declaraciones de bison*/
%union 
{
    int entero;
    double real;
}

%token EOL
%token <entero> ENTERO
%token <real> flo
%token MOD
%token SUMA 
%token RES 
%token DIV 
%token MULTI 
%token parentD 
%token parentI 
%token COMA 

%type <entero> exp
%type <real> expf



%left "+" "-"
%left "/" "*" MOD

/* Gramaticas*/
%%


input: 
        | input line
;

line:   exp EOL  {printf("\tresultado:  %d\n", $1); }
    |   expf EOL  {printf("\tresultado:  %f\n", $1); }
    |   EOL;

exp:    ENTERO { $$ = $1; }    
    | exp SUMA exp      { $$ = $1 + $3;    }          
    | RES exp      { $$ = -$2;    }          
    | exp RES exp       { $$ = $1 - $3;    }
    | exp MULTI exp       { $$ = $1 * $3;    }
    | exp DIV exp       { if($3==0){
                            yyerror("Error en el denominador\n");
                            }else{
                                $$ = $1 / $3;
                            }
      }
    | MOD parentD exp COMA exp parentI       { $$ = $3 % $5; }
;

expf: flo { $$ = (double)$1;}
    | expf SUMA expf      { $$ = $1 + $3;    }          
    | exp SUMA expf      { $$ = $1 + $3;    }          
    | expf SUMA exp      { $$ = $1 + $3;    }          
    | RES expf      { $$ = -$2;    }          
    | expf RES expf       { $$ = $1 - $3;    }
    | expf RES exp       { $$ = $1 - $3;    }
    | exp RES expf       { $$ = $1 - $3;    }
    | expf MULTI expf       { $$ = $1 * $3;    }
    | expf MULTI exp       { $$ = $1 * $3;    }
    | exp MULTI expf       { $$ = $1 * $3;    }
    | expf DIV exp       { if($3==0.0){
                            yyerror("Error en el denominador\n");
                            }else{
                                $$ = $1 / $3;
                            }
      } 
    | exp DIV expf       { if($3==0.0){
                            yyerror("Error en el denominador\n");
                            }else{
                                $$ = $1 / $3;
                            }
      } 
    | MOD parentD expf COMA expf parentI      { $$ = fmod($3, $5); }
    | MOD parentD expf COMA exp parentI     { $$ = fmod($3, $5); }
    | MOD parentD exp COMA expf parentI     { $$ = fmod($3, $5); }
;


%%

int main(){
    yyparse();

    return 0;
}

yyerror(char * s){
    printf("error: %s\n", s);
    return 0;
}