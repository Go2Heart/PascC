program test(input,output);//斐波那契数列，递归调用，错误的程序  
var a:integer;  
function fib(i:integer):integer;  
begin  
    if i=0 then  
        fib:=1  
    else  
    begin  
        if i=1 then  
            fib:=1  
        else  
            fib:=fib(i-1)+fib;//缺少实参  
    end;  
end;  
begin  
    writeln(fib(5));  
end.  
