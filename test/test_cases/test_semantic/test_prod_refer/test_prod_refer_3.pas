program test(input,output);  
var a,b:integer;  
    c:char;  
    e:real;  
    f:array[1..5] of integer;  
function fun:integer;  
begin  
    fun:=1;  
end;  
procedure pro(var d:integer;h:char);  
var i:real;  
    j:boolean;  
begin  
    read(d,h,i,j); //正确  
    read(a,c,e,f[1]); //正确  
    read(f); //错误，数组名不能作为read的参数
    read(a+b); //错误，复杂表达式不能作为read的参数
    read(test); //错误，主程序名不能作为read的参数  
    read(input); //错误，主程序参数不能作为read的参数  
    read(pro); //错误，过程名不能作为read的参数  
    read(fun); //错误，函数名不能作为read的参数  
end;  
begin  
    read(pro); //错误，过程名不能作为read的参数  
    read(fun); //错误，函数名不能作为read的参数  
    read(f); //错误，数组名不能作为read的参数  
    read(a,b,c,e,f[1]); //正确  
end.  
