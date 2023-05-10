program test(input,output);  
var a:integer;  
    b:real;  
    c:boolean;  
    d:char;  
function fib(i:integer):integer;  
begin  
    if i=0 then  
        fib:='a' //表达式类型为char，但是返回值类型为integer
    else  
    begin  
        if i=1 then  
            fib:=1 //正确
        else  
            fib:=fib(i-1)+fib(i-2); //正确
    end;  
end;  
begin  
    a:=a*2; //正确  
    a:=b; //左值类型为integer，右值类型为real，错误  
    b:=a; //左值类型为real, 右值类型为integer，正确  
    a:=a+b; //左值类型为integer，右值类型为real，错误  
    b:=a+b; //左值类型为real，右值类型为integer，正确  
    a:=c; //左值类型为integer，右值类型为boolean，错误  
    c:=a; //左值类型为boolean，右值类型为integer，错误  
    a:=d; //左值类型为integer，右值类型为char，错误  
    d:=a; //左值类型为char，右值类型为integer，错误  
    b:=c; //左值类型为real，右值类型为boolean，错误  
    c:=b; //左值类型为boolean，右值类型为real，错误  
    b:=d; //左值类型为real，右值类型为char，错误  
    d:=b; //左值类型为char，右值类型为real，错误  
    c:=d; //左值类型为boolean，右值类型为char，错误  
    d:=c; //左值类型为char，右值类型为boolean，错误  
end.  
