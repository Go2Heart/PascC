program test(input,output); //函数调用缺少实参(非递归)  
var a:integer;  
    d:char;  
function fun(b:integer;c:boolean):char;  
begin  
    if c then  
    begin  
        writeln(b);  
        fun:='y'  
    end  
    else  
    begin  
        fun:='n';  
    end;  
end;  
begin  
    d:=fun; //函数调用缺少实参(非递归)  
end.  
