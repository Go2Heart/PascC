program test(input,output); //在子函数外出现对函数名的左值引用  
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
    fib:=a; //在子函数外出现对函数名的左值引用
end.  
