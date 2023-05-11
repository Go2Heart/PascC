program test(input,output);  
const output=5; //常量与主程序参数同名  
var rea:integer; //变量与库程序同名
    test:char; //变量与主程序名同名  
    input:real; //变量与主程序参数同名  
    writ:array[1..5] of integer; //数组名与库程序名同名
  
function writel:integer; //函数名与库程序同名
begin  
  
end;


function test:integer; //函数名与主程序名同名
begin
  
end;  
  
procedure test; //过程名与主程序名同名  
begin  
  
end;  
  
function input:integer; //函数名与主程序参数同名  
begin  
  
end;  
  
procedure output; //过程名与主程序参数同名  
begin  
  
end;    
procedure pro(var test:integer;writ:real;input:char);//参数与主程序名、库程序名、主程序参数名同名
const writel=5; //常量与库程序同名
var output:integer; //变量与主程序参数同名  
begin  
  
end;  
  
begin  
  
end.  
