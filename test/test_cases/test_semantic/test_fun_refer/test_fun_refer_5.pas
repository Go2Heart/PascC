program test(input,output);  
const f=5;  
var a,b:integer;  
    c:array[1..5] of integer;  
procedure pro(var d:integer; e:char);  
begin  
    a:=d(1); //d是当前所在过程的引用参数而不是函数  
    a:=e(1); //e是当前所在过程的传值参数而不是函数  
    a:=f(5); //f是常量而不是函数  
end;  
  
begin  
    a:=fun(1); //fun未定义  
    a:=b(1); //b是普通变量而不是函数  
    a:=c(1); //c是数组而不是函数  
    a:=test(1); //test是主程序名而不是函数  
    a:=input(1); //input是主程序参数而不是函数  
    a:=pro(1); //pro是子过程名而不是函数  
end.  
