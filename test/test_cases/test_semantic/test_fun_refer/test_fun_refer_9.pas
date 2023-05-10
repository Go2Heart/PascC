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
    writeln(fun(d,e,f)); //d为integer类型，引用参数必须保证类型强一致，所以第一个实参表达式报错  
end.  
