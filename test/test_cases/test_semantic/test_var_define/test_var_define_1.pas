program test(input,output);  
var test,input:integer; //test已定义为主程序名，input已定义为主程序参数  
    a:real; //正确  
    b:boolean; //正确  
    c:array[1..5] of integer; //正确  
    a:char; //a已定义为变量  
    c:real; //c已定义为数组  
  
function fun(var a:integer;b:char):integer;  
var fun:integer; //fun已定义为当前所在的函数名  
    a:real; //a已定义为当前所在函数的引用参数  
    b:boolean; //b已定义为当前所在函数的传值参数  
begin  
  
end;  
  
procedure pro(var a:integer;b:char);  
var fun:integer; //正确  
    pro:char; //pro已定义为当前所在的过程名  
    a:real; //a已定义为当前所在过程的引用参数  
    b:boolean; //b已定义为当前所在过程的传值参数  
begin  
  
end;  
  
begin  
      
end.  
