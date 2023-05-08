program test(input,output);  
var a,b,c:integer;  
    d,e,f:real;  
    g,h,i:char;  
    j,k,l:boolean;  
begin  
    a:= a div b; //正确  
    a:= a div d; //d为real  
    a:= a div g; //g为char  
    a:= a div j; //j为boolean  
    a:= d div g; //d为real，g为char  
    a:= d div j; //d为real，j为boolean  
    a:= g div j; //g为char，j为boolean  
  
    a:= a mod b; //正确  
    a:= a mod d; //d为real  
    a:= a mod g; //g为char  
    a:= a mod j; //j为boolean  
    a:= d mod g; //d为real，g为char  
    a:= d mod j; //d为real，j为boolean  
    a:= g mod j; //g为char，j为boolean  
end.  
