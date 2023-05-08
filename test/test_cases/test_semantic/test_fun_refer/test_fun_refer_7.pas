program test(input,output);  
var a,b,c:integer;  
    d:array[1..5] of integer;  
  
procedure pro;  
begin  
  
end;  
  
function fun(a,b,c:integer):integer;//检查a，b，c是否已经为从小到大排序  
begin  
    if a<=b then  
        if b<=c then  
            fun:=1;  
    fun:=0  
end;  
begin  
    writeln(fun(a,b,c)); //正确  
    writeln(fun(test,b,c)); //test是主程序名  
    writeln(fun(input,b,c)); //input是主程序参数  
    writeln(fun(pro,b,c)); //pro是子过程明  
    writeln(fun(v,b,c)); //v未定义  
    writeln(fun(1,b,c)); //正确  
    writeln(fun(d[1],b,c)); //正确  
end.  
