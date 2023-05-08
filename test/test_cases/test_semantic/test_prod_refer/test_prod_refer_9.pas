program test(input,output);  
var d,e,f:integer;  
procedure pro(var a:real;b,c:real);//a为引用参数, b和c为传值参数  
begin  
    if a<=b then  
        if b<=c then  
            writeln(1)  
        else  
            writeln(0)  
    else  
        writeln(0);  
end;  
  
begin  
    pro(d,e,f); //d为integer类型，引用参数必须保证类型强一致，所以第一个实参表达式报错  
end.  
