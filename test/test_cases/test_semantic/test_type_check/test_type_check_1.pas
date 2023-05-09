program test(input,output);
var a,b:integer;  
    c:boolean;  
    d:real;  
    e:char;  
begin  
    a:=1;  
    {repeat
        begin
            writeln(a);
            a:=a+1
        end
    until a+b; //条件表达式类型错误
    while e do //条件表达式类型错误  
        begin  
            writeln(a);  
            a:=a+1  
        end;  }
    if c=d then //条件表达式类型错误  
        begin  
            a:=a+1;  
            writeln(a)  
        end  
    else  
        begin  
            a:=a+10;  
            writeln(a)  
        end;  
end.  
