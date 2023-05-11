program fibnacci(input,output);
    var fib:array[0..105] of integer;
        i,x,n,m:integer;
    begin
        read(n); read(m);
        fib[1] := 1; fib[2] := 1; 
        for i:=2 to n do
        begin
            fib[i] := fib[i-1] + fib[i-2];
        end;
        for i:=1 to m do
        begin
            read(x);
            write(fib[x]);
        end;
    end.
