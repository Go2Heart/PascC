program test(input,output);
var a,b:integer;
    c:char;
    f:array[1..5] of integer;
function fun:integer;
begin
    fun:=1;
end;
procedure pro2(var d:real; e:boolean);
begin
    d; //错把引用参数当成函数调用
    e; //错把传值参数当成函数调用
    pro2(d,e); //正确
end;
begin
    pro; //过程未定义
    pro2(a, a>b); //正确
    test; //将主程序名错当为过程调用
    input; //将主程序参数错当为过程调用
    a; //将integer变量错当成过程调用
    c; //将char变量错当成过程调用
    fun; //将函数错当成过程调用
    f; //将数组错当成过程调用
end.
