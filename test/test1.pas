program sort(input, output);
var a : array[0..10] of integer;
x : integer;
procedure readarray;
    var i : integer;
    begin
        for i:=1 to 9 do read(a[i])
    end;
procedure exchange (i,j:integer);
    begin
        x:=a[i]; a[i]:=a[j]; a[j]:=x
    end;
begin
readarray;
end.
{program example(input, output);
var x, y: integer;
function gcd(a, b: integer): 
integer;
begin 
if b=0 then gcd:=a
else gcd:=gcd(b, a mod b)
end;
begin
read(x, y);
write(gcd(x, y))
end.}