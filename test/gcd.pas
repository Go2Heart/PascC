
program example(input,output);
    var x,y:integer;
        c:array[1..2,5..6] of char;
    function gcd(a,b:integer):integer;
        begin 
            if b=0 then gcd:=a
            else gcd:=gcd(b, a mod b)
        end;
    function gcd1(a,b:integer):integer;
        begin 
            if b=0 then gcd:=a
            else gcd:=gcd(b, a mod b)
        end;
    begin
        read(x, y);
        write(gcd(x, y))
    end.