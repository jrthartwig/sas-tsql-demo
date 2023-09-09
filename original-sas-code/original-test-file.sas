libname mydblib odbc dsn='SQLServerDSN' user='username' password='password';

proc sql;
    connect to odbc (dsn='SQLServerDSN' user='username' password='password');
    
    create table work.mydata as
    select * from connection to odbc
    (
        SELECT * FROM database.table1
        INNER JOIN database.table2
        ON database.table1.id = database.table2.id
    );
    
    disconnect from odbc;
quit;
