program test(input,output);  
const e=10;  
      f=20;  
var a: array[0..5,6..10,11..15] of integer;  
    b,c: integer;  
    d: char;  
begin  
    a[d,b>c,b+c]:=b;//表达式类型不为integer  
    b:=a[e-f, 6-3, 20];//下标越界 常量表达式也可以计算出结果  
    a[e+f, e*f, e/f]:=b;  
    b:=a[e mod f, e div f, e+f*e];  
end.  
