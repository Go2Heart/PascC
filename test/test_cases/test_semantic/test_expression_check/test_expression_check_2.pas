program test(input,output);  
var a,b,c:integer;  
    d,e,f:real;  
    g,h,i:char;  
    j,k,l:boolean;  
  
function fun1:integer;  
begin  
    fun1:=1;  
end;  
  
function fun2:boolean;  
begin  
    fun2:=2>1;  
end;  
  
begin  
    j:= not a; //a是integer而不是boolean  
    j:= not d; //d是real而不是boolean  
    j:= not g; //g是char而不是boolean  
    j:= not j; //正确  
    j:= not fun1; //fun1是integer而不是boolean  
    j:= not fun2; //正确  
    j:= j and k; //正确  
    j:= a and l; //a是integer而不是boolean  
    j:= g and h; //g是char而不是boolean，h是char而不是boolean  
    j:= j or k; //正确  
    j:= a or l; //a是integer而不是boolean  
    j:= g or h; //g是char而不是boolean，h是char而不是boolean  
    j:= ((a+b)>c) or k; //正确  
end.  
