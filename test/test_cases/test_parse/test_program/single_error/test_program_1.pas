program test(input,output);  
var b:real;  
    c:array[1..5,6..10] of integer;  
function fun(d,e:integer):integer;  
begin  
    fun:=d+e;  
end;  
begin  
    c[3,8]:=fun(3,8);  
end.  
b:=c[1,6];  
