import csv

def csv_to_sql(csv_file, sql_file, table_name):
    # Open CSV file for reading
    with open(csv_file, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Read headers

        # Open SQL file for writing
        with open(sql_file, 'w') as sqlfile:
            # Iterate over rows in CSV
            for row in csvreader:
                # Generate INSERT statement
                sql_insert = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(map(quote_value, row))});\n"
                sqlfile.write(sql_insert)

def quote_value(value):
    # Helper function to quote SQL values (strings)
    return f"'{value}'"

# Example usage
csv_file = 'E:\Data Analyst Projects\PowerBi\PIZZA SALES\pizza_sales.csv'
sql_file = 'pizza_sales.sql'
table_name = 'pizza_sale'

csv_to_sql(csv_file, sql_file, table_name)
