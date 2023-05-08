program test(input,output);  
var d,e,f:integer;  
function fun(var a:real;b,c:real):integer;//a为引用参数, b和c为传值参数  
begin  
    if a<=b then  
        if b<=c then  
            fun:=1;  
    fun:=0  
end;  
  
begin  
    fun(d,e,f);//该PASCAL-S语言不支持函数的未引用调用  
end.  
