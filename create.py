from connect_db import Database


def create_table():

    category_table = """
        CREATE TABLE category(category_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_update DATE,
            create_date TIMESTAMP DEFAULT now()); """

    product_table = """
        CREATE TABLE product(product_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            category_id INT REFERENCES category(category_id),
            create_date TIMESTAMP DEFAULT now()); """

    color_table = """
        CREATE TABLE color(color_id SERIAL PRIMARY KEY,
            name VARCHAR(50));  """

    product_detail_table = """
        CREATE TABLE product_detail(product_detail_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            description TEXT,
            price NUMERIC,
            color_id INT REFERENCES color(color_id),
            count INT,
            product_id INT REFERENCES product(product_id),
            rating FLOAT,
            create_date TIMESTAMP DEFAULT now());  """

    country_table = """
        CREATE TABLE country(country_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            create_date TIMESTAMP DEFAULT now());  """

    city_table = """
            CREATE TABLE city(city_id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                country_id INT REFERENCES country(country_id),
                create_date TIMESTAMP DEFAULT now());  """

    address_table = """
            CREATE TABLE address(address_id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                city_id INT REFERENCES city(city_id),
                create_date TIMESTAMP DEFAULT now());  """

    customer_table = """
        CREATE TABLE customer(customer_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            password VARCHAR(20),
            email VARCHAR(20),
            birth_date DATE,
            address_id INT REFERENCES address(address_id),
            create_date TIMESTAMP DEFAULT now());  """

    official_detail_table = """
        CREATE TABLE official_detail(official_detail_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES product(product_id),
            customer_id INT REFERENCES customer(customer_id),
            create_date TIMESTAMP DEFAULT now());  """

    payment_status_table = """
        CREATE TABLE payment_status(payment_status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now());  """

    payment_type_table = """
        CREATE TABLE payment_type(payment_type_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now());  """

    payment_table = """
        CREATE TABLE payment(payment_id SERIAL PRIMARY KEY,
            official_detail_id INT REFERENCES official_detail(official_detail_id),
            amount FLOAT,
            payment_status_id INT REFERENCES payment_status(payment_status_id),
            payment_type_id INT REFERENCES payment_type(payment_type_id),
            create_date TIMESTAMP DEFAULT now());  """

    store_table = """
            CREATE TABLE store(store_id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                address_id INT REFERENCES address(address_id),
                create_date TIMESTAMP DEFAULT now());  """

    data = {
        "category_table": category_table,
        "product_table": product_table,
        "color_table": color_table,
        "product_detail_table": product_detail_table,
        "country_table:": country_table,
        "city_table": city_table,
        "address_table": address_table,
        "customer_table": customer_table,
        "official_detail_table": official_detail_table,
        "payment_status_table": payment_status_table,
        "payment_type_table": payment_type_table,
        "payment_table": payment_table,
        "store_table": store_table
    }

    for i in data:
        print(f"{i}: {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()
