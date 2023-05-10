program test(input,output);  
var a,b:integer;  
    c:char;  
    e:real;  
    f:array[1..5] of integer;  
function fun:real;  
begin  
    exit(f[1]); //正确，integer到real的隐式类型转换  
    exit(a); //正确，integer到real的隐式类型转换  
    exit(c); //错误，定义的返回值类型为real，而返回值表达式的类型为char  
    exit(e); //正确，返回值类型一直  
    exit; //错误，缺少返回值表达式  
    exit(a,b); //错误，返回值表达式多余  
end;  
procedure pro;  
begin  
    exit(1); //错误，返回值表达式多余  
    exit; //正确，过程不需要返回值  
end;  
begin  
    exit(1); //错误  
    exit; //正确，主程序不需要返回值  
end.  
