libname mydblib odbc dsn='SQLServerDSN' user='username' password='password';

proc sql;
    connect to odbc (dsn='SQLServerDSN' user='username' password='password');
    
    create table work.mydata.dbo as
    select * from connection to odbc
    (
        SELECT * FROM database.table1.dbo
        INNER JOIN database.table2.dbo
        ON database.table1.dbo.id = database.table2.dbo.id
    );
    
    disconnect from odbc;
quit;
