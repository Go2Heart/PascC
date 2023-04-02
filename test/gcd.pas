
program example(input,output);
    const z=500;p=250;

    var x,y:integer;
        c:array[1..2,5..6] of char;
    function gcd(a,b:integer;var c,d:integer):integer;
        begin 
            if b=0 then gcd:=a
            else gcd:=gcd(b, a mod b)
        end;
    procedure gcd1(a,b:integer);
        begin 
            if b=0 then gcd:=a
            else gcd:=gcd(b, a mod b)
        end;
    begin
        read(x, y);
        write(gcd(x, y))
    end.