program test(input,output);   
function fun(a,b,c:real):integer;//检查a，b，c是否已经为从小到大排序  
begin  
    if a<=b then  
        if b<=c then  
            fun:=1;  
    fun:=0  
end;  
begin  
    writeln(fun); //参数缺失  
    writeln(fun(1)); //参数缺失  
    writeln(fun(1,'a')); //参数缺失  
    writeln(fun(1,2,3)); //正确  
    writeln(fun('a',1.1,3)); //参数类型不一致  
end.  
