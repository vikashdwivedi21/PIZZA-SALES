import psycopg2


hostname =  'localhost'
database = 'PIZZA SALES'
username = 'postgres'
pwd = 'vks881576' 
port_id = 5432
conn = None,
cur = None

sql_file = 'E:\Data Analyst Projects\PowerBi\PIZZA SALES\pizza_sales.sql'


try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id,
    

    )

    cur = conn.cursor()

#     script =    '''CREATE TABLE Pizza_Sale (
#     pizza_id INT NOT NULL,
#     order_id INT NOT NULL,
#     pizza_name_id VARCHAR(255) NOT NULL,
#     quantity INT NOT NULL,
#     order_date DATE NOT NULL,
#     order_time TIME NOT NULL,
#     unit_price FLOAT NOT NULL,
#     total_price FLOAT NOT NULL,
#     pizza_size VARCHAR(255) NOT NULL,
#     pizza_category VARCHAR(255) NOT NULL,
#     pizza_ingredients TEXT NOT NULL,
#     pizza_name VARCHAR(255) NOT NULL,
#     PRIMARY KEY (pizza_id, order_id)
# );


#     '''

   
#     # '''
#     cur.execute(script)

    #Read SQL statment from file
    with open(sql_file, 'r') as file:
        sql_commands = file.read().split(';')

    ## Execute each command 
    for command in sql_commands:
        if command.strip() != "":
            cur.execute(command)


    
    ## Commit the transaction 
    conn.commit()
    print("SQL commands executed sucessfully")

    


except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

    







