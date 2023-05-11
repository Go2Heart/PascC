program test(input,output);
const a=3;
      b=1.0;
      c='c';
var d,e,f:integer;
    g,h,i:real;
    j,k,l:char;
    m,n,o:boolean;
function fun(a:integer):integer;
begin
    {exit(a+1);}
    fun:=1;
end;
begin
    d:=5; e:=10;
    g:=0.25; h:=0.5;
    j:='a'; k:='b';

    f:= d mod (e div fun(d)); //涉及mod、div和函数调用的复杂表达式
    writeln(f); //类型为integer

    g:= --d + e / d * ( - b); //涉及加减乘除、取相反数、加括号的复杂表达式
    writeln(g); //类型为real

    o:= ( ( f mod e ) <> d ) or ( a > b); //涉及<>、or的复杂表达式
    writeln(o); //类型为boolean

    m:= not not ( ( d + e ) = f ); //涉及取非、=的复杂表达式
    writeln(m); //类型为boolean

    n:= ( g * e < f ) and ( (f mod e) >= d ); //涉及and、<、>=、mode的复杂表达式
    writeln(n); //类型为boolean

    writeln( j <= c); //比较char的大小关系

    writeln( m > n); //比较boolean的大小关系
end.
