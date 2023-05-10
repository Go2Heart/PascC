program test(input,output);
const m = 100;
var a,b,c:integer;
    d,e,f:real;
    g,h,i:char;
    j,k,l:boolean;

function fun:real;
begin
    fun:=1;
end;
 
begin
    j:=a>=b; //正确
    j:=d>e; //正确
    j:=g<=h; //正确
    j:=j<k; //正确
    j:=a<>d; //正确，隐式类型转换
    j:=a=m; //正确
    j:=a=fun; //正确，隐式类型转换
    j:=a=g; //错误，a和g类型不匹配
    k:=a>=j; //错误，a和j类型不匹配
    k:=d>g; //错误，d和g类型不匹配
    k:=d<=j; //错误，d和j类型不匹配
    k:=g<j; //错误，g和j类型不匹配
end.
