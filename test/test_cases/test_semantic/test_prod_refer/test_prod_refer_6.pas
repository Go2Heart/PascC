program test(input,output);  
var a,b:integer;  
procedure pro(var c:integer;d:char);  
begin  
    writeln(c);  
    writeln(d);  
end;  
begin  
    pro; //缺少实参  
    pro(a); //缺少实参  
    pro(a,'y'); //正确  
    pro(a,b); //第二个实参类型不匹配  
end.  
