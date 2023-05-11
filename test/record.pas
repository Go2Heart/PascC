program RecordExample;
const 
  c = 2;

type
  IIII = INTEGER;
  INT = IIII;
  int_array = array[1..10] of integer;

  TStudent = record
  Name: string;
    Age: IIII;
    GPA: real;
  end;

  TCourse = record
  Name: string;
  Code: string;
    Credit: int_array;
  end;

  TEnrollment = record
    Student:  TStudent;
    Course: array [1..2] of TCourse;
    Grade: INT;
  end;

  

var
  Enrollment: TEnrollment;
  arr: array[1..10] of integer;
  i, j, temp: integer;

begin
  Enrollment.Student.Age := 20;
  Enrollment.Student.GPA := 3.5;
  Enrollment.Course[2].Credit[2] := 3;
  Enrollment.Grade := 85;

  writeln('Grade: ', Enrollment.Grade);

  writeln('Enter 10 numbers:');
  i:=1;
  while i<=10 do
  BEGIN
      readln(arr[i]);
      i := i+1;
  END;

repeat 
  i:=i-1;
until i=0;
  for i := 1 to 9 do
    for j := i + 1 to 10 do
      if arr[i] > arr[j] then begin
        temp := arr[i];
        arr[i] := arr[j];
        arr[j] := temp;
      end;

  writeln('Sorted array:');
  for i := 1 to 10 do
    write(arr[i], ' ');
end.
