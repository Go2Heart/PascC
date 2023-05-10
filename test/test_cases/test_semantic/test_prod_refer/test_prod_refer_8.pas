program test(input,output);  
const h=5;  
var d:array[1..5] of integer;  
    e,f,g:integer;  
  
procedure pro(var a,b,c:integer);//检查a,b,c是否已经从小到大排序  
begin  
    if a<=b then  
        if b<=c then  
            writeln(1)  
        else  
            writeln(0)  
    else  
        writeln(0);  
end;  
  
begin  
    pro(d[1],d[2],d[3]); //正确  
    pro(h,e,f); //第一个参数是常量标识符，不能作为引用参数对应的形参  
    pro(d,e,f); //第一个参数是数组名，不能作为引用参数对应的形参  
    pro(e+f,e,f); //第一个参数是复杂表达式，不能作为引用参数对应的形参  
    pro(e,e>f,f); //第二个参数是复杂表达式，不能作为引用参数对应的形参  
    pro(e,f,1); //第三个参数是常量，不能作为引用参数对应的形参  
end.  
