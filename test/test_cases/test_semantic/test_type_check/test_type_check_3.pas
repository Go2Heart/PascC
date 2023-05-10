program test(input,output);  
var a,b:integer;  
    c:char;  
  
function fun:integer;  
begin  
    for fun:=1 to 3 do //错把函数名当循环变量  
        writeln('y')
end;  
  
procedure pro(var d:integer;e:char);  
begin  
    for pro:=1 to 3 do //错把过程名当循环变量  
        writeln(a*b);  
    for d:=1 to 3 do //正确  
        writeln(a/b);  
    for e:=1 to 3 do //错把char变量当循环变量  
        writeln(a mod b);
    for fun:=1 to 3 do //错把函数名当循环变量  
        writeln(a div b)  
end;  
  
begin  
    for test:= 1 to 3 do //错把程序名当循环变量  
        writeln(a);  
    for input:=1 to 3 do //错把主程序参数当循环变量  
        writeln(b);  
    for c:=1 to 3 do //错把char变量当循环变量  
        writeln(c);  
    for fun:=1 to 3 do //错把函数名当循环变量  
        writeln(a+b);  
    for pro:=1 to 3 do //错把过程名当循环变量  
        writlen(a-b);  
    for d:=1 to 3 do //循环变量未定义  
        writeln(a*b)  
end.  
