program RecordExample;

type
  TStudent = record
    Name: string;
    Age: integer;
    GPA: real;
  end;

var
  Student1: TStudent;
  Student2: TStudent;

begin
  Student1.Name := 'Alice';
  Student1.Age := 20;
  Student1.GPA := 3.8;

  Student2.Name := 'Bob';
  Student2.Age := 22;
  Student2.GPA := 3.5;

  writeln('Student 1:');
  writeln('Name: ', Student1.Name);
  writeln('Age: ', Student1.Age);
  writeln('GPA: ', Student1.GPA:4:2);

  writeln('Student 2:');
  writeln('Name: ', Student2.Name);
  writeln('Age: ', Student2.Age);
  writeln('GPA: ', Student2.GPA:4:2);

end.