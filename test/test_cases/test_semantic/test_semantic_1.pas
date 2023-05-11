program proc(input,output);//主程序名、主程序参数和库程序同名
const m=10;
var a,x,y:integer;  
    b:real;  
    c:char;  
    d:boolean;  
    e:array[1..5] of integer;  
function fun1:integer;//报函数没有返回语句的警告  
begin  
    v:=a;//v未定义  
end;  
  
function fun2:integer;  
begin  
    fun2:=1;  
    fun2:=e[6];//数组下标越界  
    fun2;//函数不能作为一条单独的语句  
    a:=fun2[1];//错把函数名当做数组  
end;  
  
procedure pro1(a:integer;b:real);  
var c:real;    
    d:integer;  
begin   
    c:=a+b;//integer可以隐式转换为real  
    d:=a+b;//real不能隐式转换为integer  
end;  
  
procedure pro2(var a:real;b:integer);  
begin   
    {exit(a+b);//过程没有返回值  }
end;  
  
begin  
    a:=1;  
    m:=a;//常量赋值语句右值不为常量  
    b:=2;  
    c:=3;//赋值语句左右类型不匹配  
    d:=a>b;//d为false  
    if a then b:=b+1;//if条件表达式不为boolean  
    repeat a:=a+c until not d;//a:=a+c语句左右类型不匹配  
    for b:=10 to 1 do e(a,a);//循环变量不可以是real；错把数组名当做函数  
    while a<10 do a:=a+1;  
    x:=pro1(x,y);//pro1为过程，没有返回值  
    x:=1;  
    y:=2;  
    pro1(x,y);//传值参数支持integer到real的隐式转换  
    pro2(x,y);//pro2的第一个参数为传引用，integer无法隐式转换为real  
    pro1(x+y);//pro1有两个参数  
    pro1(x+y,x+y);//传值参数支持复合表达式  
    pro2(x+y);//pro2有两个参数  
    pro2(x+y,x+y);//pro2第一个参数为引用参数，只能是变量或者数组元素，不能是复杂表达式  
end.  
