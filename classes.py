from datetime import datetime
from connect_db import Database


class Base:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table} ORDER BY {table}_id"
        return Database.connect(query, "select")

    @staticmethod
    def update_id(table, column_name, old_data, new_data):
        query = f"UPDATE {table} SET {column_name} = {new_data} WHERE {column_name} = {old_data}"
        return Database.connect(query, "update")

    @staticmethod
    def update(table, column_name, old_data, new_data):
        query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(table, data):
        query = f"DELETE FROM {table} WHERE {table}_id = {data}"
        return Database.connect(query, "delete")

    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = '{data}'"
        return Database.connect(query, "delete")


class Category(Base):
    def __init__(self, name, last_updated):
        self.name = name
        self.last_updated = f"{datetime.now()}"
        self.table_name = "category"

    def insert(self):
        query = f"INSERT INTO {self.table_name}(name, last_update) VALUES('{self.name}', '{self.last_updated}')"
        return Database.connect(query, "insert")


class Product(Base):
    def __init__(self, product_name, category_id):
        self.product_name = product_name
        self.category_id = category_id
        self.table_name = "product"

    def insert(self):
        query = f"INSERT INTO product(name, category_id) VALUES('{self.product_name}', {self.category_id})"
        return Database.connect(query, "insert")


class Color(Base):
    def __init__(self, name):
        self.name = name
        self.table_name = "color"

    def insert(self):
        query = f"INSERT INTO color(name) VALUES('{self.name}')"
        return Database.connect(query, "insert")


class ProductDetail(Base):
    def __init__(self, name, description, price, color_id, count, product_id, rating):
        self.name = name
        self.description = description
        self.price = price
        self.color_id = color_id
        self.count = count
        self.product_id = product_id
        self.rating = rating
        self.table_name = "product_detail"

    def insert(self):
        query = f"""
        INSERT INTO product_detail(name, description, price, count, color_id, product_id, rating) 
        VALUES('{self.name}', '{self.description}', {self.price}, {self.color_id}, {self.count}, {self.product_id}, {self.rating})"""
        return Database.connect(query, "insert")


class Country(Base):
    def __init__(self, name):
        self.name = name
        self.table_name = "country"

    def insert(self):
        query = f"""INSERT INTO country(name) VALUES('{self.name}')"""
        return Database.connect(query, "insert")


class City(Base):
    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id
        self.table_name = "city"

    def insert(self):
        query = f"""INSERT INTO city(name, country_id) VALUES('{self.name}', {self.country_id})"""
        return Database.connect(query, "insert")


class Address(Base):
    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id
        self.table_name = "address"

    def insert(self):
        query = f"""INSERT INTO address(name, city_id) VALUES('{self.name}', {self.city_id})"""
        return Database.connect(query, "insert")


class Customer(Base):
    def __init__(self, first_name, last_name, password, email, birth_date, address_id):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.birth_date = birth_date
        self.address_id = address_id
        self.table_name = "customer"

    def insert(self):
        query = f"""
        INSERT INTO customer(first_name, last_name, password, email, birth_date, address_id) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.password}', '{self.email}', '{self.birth_date}', {self.address_id})"""
        return Database.connect(query, "insert")


class OfficialDetail(Base):
    def __init__(self, product_id, customer_id):
        self.product_id = product_id
        self.customer_id = customer_id
        self.table_name = "official_detail"

    def insert(self):
        query = f"""INSERT INTO official_detail(product_id, customer_id) VALUES({self.product_id}, {self.customer_id})"""
        return Database.connect(query, "insert")


class PaymentStatus(Base):
    def __init__(self, name):
        self.name = name
        self.table_name = "payment_status"

    def insert(self):
        query = f"""INSERT INTO payment_status(name) VALUES('{self.name}')"""
        return Database.connect(query, "insert")


class PaymentType(Base):
    def __init__(self, name):
        self.name = name
        self.table_name = "payment_type"

    def insert(self):
        query = f"""INSERT INTO payment_type(name) VALUES('{self.name}')"""
        return Database.connect(query, "insert")


class Payment(Base):
    def __init__(self, amount, official_detail_id, payment_status_id, payment_type_id):
        self.amount = amount
        self.official_detail_id = official_detail_id
        self.payment_status_id = payment_status_id
        self.payment_type_id = payment_type_id
        self.table_name = "payment"

    @staticmethod
    def full_select():
        query = """SELECT product.name, customer.first_name, customer.last_name, payment.amount,
            payment_status.name, payment_type.name FROM payment
        INNER JOIN official_detail
            ON official_detail.official_detail_id = payment.official_detail_id
             
        INNER JOIN product
            ON product.product_id = official_detail.product_id        
        
        INNER JOIN customer
            ON customer.customer_id = official_detail.customer_id
            
        INNER JOIN payment_status
            ON payment_status.payment_status_id = payment.payment_status_id
        
        INNER JOIN payment_type
            ON payment_type.payment_type_id = payment.payment_type_id
        """

        return Database.connect(query, "select")

    def insert(self):
        query = f"""INSERT INTO {self.table_name}(amount, official_detail_id, payment_status_id, payment_type_id) 
        VALUES({self.amount}, {self.official_detail_id}, {self.payment_status_id}, {self.payment_type_id});"""
        return Database.connect(query, "insert")


class Store(Base):
    def __init__(self, name, address_id):
        self.name = name
        self.address_id = address_id
        self.table_name = "store"

    def insert(self):
        query = f"""INSERT INTO store(name, address_id) VALUES('{self.name}', {self.address_id})"""
        return Database.connect(query, "insert")

