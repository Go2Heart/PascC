program test(input,output);  
const test=1; //已定义为主程序名  
      input=2; //已定义为主程序参数  
      d=d; //右值未定义  
      a=test; //右值非常量  
      b=a; //右值未定义  
      c=3; //正确  
      a=b; //右值未定义  
      c=c; //已定义为常量  
  
function fun(var a:integer;b:char):integer;  
const fun=-5; //已定义为当前所在函数名  
      a=-10; //已定义为当前所在函数的引用参数  
      b=a; //已定义为当前所在函数的传值参数  
begin  
  
end;  
  
procedure pro(var a:integer;b:char);  
const fun=3; //正确  
      pro=-6; //已定义为当前所在过程名  
      a=fun; //左值已定义为当前所在过程的引用参数  
      b=pro; //左值已定义为当前所在过程的传值参数  
      c=fun; //正确  
begin  
  
end;  
  
begin  
      
end.  
