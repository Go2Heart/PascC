program test(input,output);  
var a,b,c:integer;  
    d:array[1..5] of integer;  
  
function fun:integer;  
begin  
  
end;  
  
procedure pro(a,b,c:integer);  
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
    pro(a,b,c); //正确  
    pro(test,b,c); //test是主程序名  
    pro(input,b,c); //input是主程序参数  
    pro(fun,b,c); //正确  
    pro(v,b,c); //v未定义  
    pro(1,b,c); //正确  
    pro(d[1],b,c); //正确  
end.  
