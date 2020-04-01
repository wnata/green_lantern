from typing import List
import json

def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    dict = {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    try:
        con.autocommit = True
        cursor = con.cursor()
        sql = f"""
        INSERT INTO customers(customername, contactname, address, city, postalcode, country) 
        VALUES('{dict.get('customer_name')}', 
                '{dict.get('contactname')}',
                '{dict.get('address')}',
                '{dict.get('city')}',
                '{dict.get('postalcode')}',
                '{dict.get('country')}'
                );
        """
        cursor.execute(sql)
        con.commit()
    except:
        raise Exception



def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    try:
        cursor = cur
        sql = """
        select * from customers;
        """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    try:
        cursor = cur
        sql = """
        select * from customers
        where country = 'Germany';
        """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """

    try:
        con.autocommit = True
        cursor = con.cursor()
        sql = f"""
        update customers
        set customername = 'Johnny Depp'
        where customername in (select customername from customers limit 1);
        """
        cursor.execute(sql)
        con.commit()
        sql = f"""select * from customers"""
        cursor.execute(sql)
        records = cursor.fetchall()
        con.commit()
    except:
        raise Exception
    return records


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    try:
        con.autocommit = True
        cursor = con.cursor()
        sql = f"""
        DELETE FROM customers
        WHERE CustomerID in (select CustomerID from customers order by CustomerID desc limit 1);
        """
        cursor.execute(sql)
        con.commit()
    except:
        raise Exception


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    try:
        cursor = cur
        sql = f"""
        select country from suppliers;
        """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    try:
        cursor = cur
        sql = f"""
        select country from suppliers order by country desc;
        """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    try:
        cursor = cur
        sql = f"""
        select city
            ,count(city) AS "qty" 
        from customers
        group by city
        order by "qty" desc;
        """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    try:
        cursor = cur
        sql = f"""
        select count(country) AS "count" 
            ,country
        from customers
        group by country
        having count(country) > 10;
        """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    try:
        cursor = cur
        sql = f"""
        select *
        from customers
        limit 10;
        """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    try:
        cursor = cur
        sql = f"""
        select *
        from customers
        Offset 11 Rows;
        """
        cursor.execute(sql)
        records = cursor.fetchall()
        # j_ar = json.dumps(records)
        # print(j_ar)
    except:
        raise Exception

    return records


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    try:
        cursor = cur
        sql = f"""
        select supplierid, suppliername, contactname, city, country
        from suppliers
        where country in ('USA', 'UK', 'Japan');
        """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    try:
        cursor = cur
        sql = f"""
           select p.productname
           from products p
                join suppliers s on s.supplierid = p.supplierid
           where s.country='Sweden';
           """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    try:
        cursor = cur
        sql = f"""
           select p.productid,
                p.productname,
                p.unit,
                p.price,
                s.country,
                s.city,
                s.suppliername
           from products p
                join suppliers s on s.supplierid = p.supplierid;
           """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    try:
        cursor = cur
        sql = f"""
           select c.customername,
            c.contactname,
            c.country,
            o.orderid
        from orders o
            join customers c on c.CustomerID=o.CustomerID
           """
        cursor.execute(sql)
        records = cursor.fetchall()
    except:
        raise Exception

    return records


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    try:
        cursor = cur
        sql = f"""
           select c.customername,
                c.address,
                c.country as "customercountry",
                s.country as "suppliercountry",
                s.supplierName
        from customers c 
            full join suppliers s on c.country=s.country
            order by c.country, s.country;
           """

        cursor.execute(sql)
        records = cursor.fetchall()
        len(records)
    except:
        raise Exception

    return records