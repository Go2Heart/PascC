program test(input,output);  
var a:integer;  
    b:array[0..5] of integer;  
function fun:integer;  
begin  
    fun:=1;  
    a:=fun[1]; //错把函数名当数组  
    fun[1]:=a; //错把函数名当数组  
end;  
procedure pro;  
begin  
    a:=pro[1]; //错把过程名当数组  
    pro[1]:=a; //错把过程名当数组  
    writeln('y');  
end;  
procedure pro2(var d:integer;e:char);  
begin  
    a:=d[1]; //错把引用参数当数组  
    a:=e[1]; //错把传值参数当数组  
    a:=pro2[1]; //错把过程名当数组  
    d[1]:=a; //错把引用参数当数组  
    e[1]:=a; //错把传值参数当数组  
    pro2[1]:=a; //错把过程名当数组  
end;  
begin  
    a:=test[1]; //错把主程序名当数组  
    a:=input[1]; //错把主程序参数当数组  
    a:=fun[1]; //错把函数名当数组  
    a:=pro[1]; //错把过程名当数组  
    a:=b[1]; //正确的数组引用  
    test[1]:=a; //错把主程序名当数组  
    output[1]:=a; //错把主程序参数当数组  
    fun[1]:=a; //错把函数名当数组  
    pro[1]:=a; //错把过程名当数组  
    b[1]:=a; //正确的数组引用  
end.  
