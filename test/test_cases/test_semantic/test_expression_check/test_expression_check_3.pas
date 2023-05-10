program test(input,output);  
var a,b,c:integer;  
    d,e,f:real;  
    g,h,i:char;  
    j,k,l:boolean;  
begin  
    a:=b+c; //正确  
    d:=d+e; //正确  
    a:=b+f; //错误，左值为integer，右值为real  
    d:=e+c; //正确  
  
    a:=b/c; //正确  
    d:=d/e; //正确  
    a:=b/f; //错误，左值为integer，右值为real  
    d:=e/c; //正确  
  
    a:=g-h; //错误，g和h均为char  
    d:=j-k; //错误，j和k均为boolean  
    a:=b-g; //错误，g为char  
    d:=c-j; //错误，j为boolean  
    a:=d-g; //错误，a为int，d为real，g为char  
    d:=d-l; //错误，l为boolean  
    a:=g-k; //错误，a为integer，g为char，k为boolean  
      
    a:=g*h; //错误，g和h均为char  
    d:=j*k; //错误，j和k均为boolean  
    a:=b*g; //错误，g为char  
    d:=c*j; //错误，j为boolean  
    a:=d*g; //错误，a为int，d为real，g为char  
    d:=d*l; //错误，l为boolean  
    a:=g*k; //错误，a为integer，g为char，k为boolean  
  
    a:=-b; //正确  
    d:=-b; //正确  
    a:=-d; //错误，a为integer，d为real  
    d:=-d; //正确  
    a:=-g; //错误，a为integer，g为char  
    d:=-g; //错误，d为real，g为char  
    a:=-j; //错误，a为integer，j为boolean  
    d:=-j; //错误，d为real，j为boolean  
end.  
