program test(input,output);   
var a:integer;  
procedure pro;  
begin  
    a:=1;  
end;  
begin  
    a:=pro;//在子过程外错误地引用了子过程名  
    writeln(a);  
end.  
