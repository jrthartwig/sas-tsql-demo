libname mydblib odbc dsn='SQLServerDSN' user='username' password='password';

proc sql;
    connect to odbc (dsn='SQLServerDSN' user='username' password='password');
    
    create table work.mydata as
    select * from connection to odbc
    (
        SELECT * FROM database.schema.table1
        INNER JOIN database.schema.table2
        ON database.schema.table1.id = database.schema.table2.id
    );
    
    disconnect from odbc;
quit;
