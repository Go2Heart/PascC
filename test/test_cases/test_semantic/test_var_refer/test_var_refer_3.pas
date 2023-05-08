program test(input,output);   
var a:integer;  
procedure pro;  
begin  
    pro:=a; //在子过程的定义中错误地引用了该子过程名  
    a:=pro; //在子过程的定义中错误地引用了该子过程名  
end;  
begin  
    pro;  
end.  
