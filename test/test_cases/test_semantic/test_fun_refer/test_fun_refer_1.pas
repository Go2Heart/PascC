program test(input,output);//斐波那契数列，递归调用，正确的程序  
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
            fib:=fib(i-1)+fib(i-2);  
    end;  
end;  
begin  
    writeln(fib(5));  
end.  
