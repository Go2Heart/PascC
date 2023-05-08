program test(input,output);  
var a:array[1..6] of integer;  
    b:integer;  
begin  
    a:=1;//左值不带下标引用数组  
    b:=a;//右值不带下标引用数组  
end.  
