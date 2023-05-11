program test(input,output);  
const h=5;  
var d:array[1..5] of integer;  
    e,f,g:integer;  
function fun(var a,b,c:integer):integer;//检查a,b,c是否已经从小到大排序
begin  
    if a<=b then
        if b<=c then  
            fun:=1;
    fun:=0
end;  
  
procedure pro(var a:integer;b:integer);  
var c:integer;  
begin  
    writeln(fun(a,b,c)); //正确  
end;  
begin  
    writeln(fun(d[1],d[2],d[3]));//正确
    writeln(fun(h,e,f)); //第一个参数是常量标识符，不能作为引用参数对应的形参  
    writeln(fun(d,e,f)); //第一个参数是数组名，不能作为引用参数对应的形参
    writeln(fun(e+f,e,f)); //第一个参数是复杂表达式，不能作为引用参数对应的形参  
    writeln(fun(e,e>f,f)); //第二个参数是复杂表达式，不能作为引用参数对应的形参
    writeln(fun(e,f,1)); //第三个参数是常量，不能作为引用参数对应的形参
end.  
