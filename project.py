from classes import (Category, Product, Color, ProductDetail, Country, City,
                     Address, Customer, OfficialDetail,
                     PaymentStatus, PaymentType, Payment, Store)


def category_table():
    services = input("""
        Services:
            1. SELECT
            2. INSERT
            3. UPDATE
            4. DELETE
            0. Back
            >>> """)

    if services == "1":     # SELECT
        if len(Category.select("category")) == 0:
            print("Data not yet exist!")

        else:
            for i in Category.select("category"):
                print(f"""
                    ID: {i[0]},
                    Name: {i[1]},
                    Last Updated: {i[2]},
                    Create Date: {i[3]}
                """)

        return category_table()

    elif services == "2":  # INSERT
        name = input("Name: ")
        last_updated = input("Last Updated: ")
        category = Category(name, last_updated)
        print(category.insert())
        return category_table()

    elif services == "3":  # UPDATE
        print("Update Category:")
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(Category.update_id(int(old_data), int(new_data)))
        else:
            print(Category.update(column_name.lower(), old_data, new_data))

        return category_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(Category.delete_id("category", value))
        else:
            print(Category.delete("category", column_name, value))
        return category_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return category_table()


def product_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(Product.select("product")) == 0:
            print("Data not yet exist!")

        else:
            for i in Product.select("product"):
                print(f"""
                        ID: {i[0]},
                        Product Name: {i[1]},
                        Category ID: {i[2]},
                        Create Date: {i[3]}
                    """)

        return product_table()

    elif services == "2":  # INSERT
        product_name = input("Product Name: ")
        category_id = int(input("Category ID: "))
        product = Product(product_name, category_id)
        print(product.insert())
        return product_table()

    elif services == "3":  # UPDATE
        print("Update :")
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id" or column_name.lower() == "category id":
            print(Product.update_id(int(old_data), int(new_data)))
        else:
            print(Product.update(column_name.lower(), old_data, new_data))

        return product_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(Product.delete_id("product", value))
        else:
            print(Product.delete("product", column_name, value))
        return product_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return product_table()


def color_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(Color.select("color")) == 0:
            print("Data not yet exist!")

        else:
            for i in Color.select("color"):
                print(f"""
                        ID: {i[0]},
                        Color: {i[1]},
                    """)

        return color_table()

    elif services == "2":  # INSERT
        color_name = input("Color Name: ")
        name = Color(color_name)
        print(name.insert())
        return color_table()

    elif services == "3":  # UPDATE
        print("Update :")
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(Color.update_id(int(old_data), int(new_data)))
        else:
            print(Color.update(column_name.lower(), old_data, new_data))

        return color_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(Color.delete_id("color", value))
        else:
            print(Color.delete("color", column_name, value))
        return color_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return color_table()


def product_detail_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(ProductDetail.select("product_detail")) == 0:
            print("Data not yet exist!")

        else:
            for i in ProductDetail.select("product_detail"):
                print(f"""
                        ID: {i[0]},
                        Name: {i[1]},
                        Description: {i[2]},
                        Price: {i[3]},
                        Count: {i[4]},
                        Color ID: {i[5]},
                        Product ID: {i[6]},
                        Rating: {i[7]},
                        Create Date: {i[8]},
                    """)

        return product_detail_table()

    elif services == "2":  # INSERT
        product_detail_1 = input("Product Detail Name: ")
        product_detail_2 = input("Description: ")
        product_detail_3 = float(input("Price: "))
        product_detail_4 = int(input("Count: "))
        product_detail_5 = int(input("Color ID: "))
        product_detail_6 = int(input("Product ID: "))
        product_detail_7 = float(input("Rating: "))
        name = ProductDetail(product_detail_1, product_detail_2, product_detail_3, product_detail_4, product_detail_5, product_detail_6, product_detail_7)
        print(name.insert())
        return product_detail_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(ProductDetail.update_id(int(old_data), int(new_data)))
        else:
            print(ProductDetail.update(column_name.lower(), old_data, new_data))

        return product_detail_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(ProductDetail.delete_id("product_detail", value))
        else:
            print(ProductDetail.delete("product_detail", column_name, value))
        return product_detail_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return product_detail_table()


def country_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(Country.select("country")) == 0:
            print("Data not yet exist!")

        else:
            for i in Country.select("country"):
                print(f"""
                        ID: {i[0]},
                        Name: {i[1]},
                        Create date: {i[2]},
                    """)

        return country_table()

    elif services == "2":  # INSERT
        country_name = input("Country Name: ")
        name = Country(country_name)
        print(name.insert())
        return country_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(Country.update_id(int(old_data), int(new_data)))
        else:
            print(Country.update(column_name.lower(), old_data, new_data))

        return country_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(Country.delete_id("country", value))
        else:
            print(Country.delete("country", column_name, value))
        return country_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return country_table()


def city_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(City.select("city")) == 0:
            print("Data not yet exist!")

        else:
            for i in City.select("city"):
                print(f"""
                        ID: {i[0]},
                        Name: {i[1]},
                        Country ID: {i[2]},
                        Create date: {i[3]},
                    """)

        return city_table()

    elif services == "2":  # INSERT
        city_name = input("City Name: ")
        country_id = int(input("Country ID: "))
        name = City(city_name, country_id)
        print(name.insert())
        return city_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(City.update_id(int(old_data), int(new_data)))
        else:
            print(City.update(column_name.lower(), old_data, new_data))

        return city_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(City.delete_id("city", value))
        else:
            print(City.delete("city", column_name, value))
        return city_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return city_table()


def address_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(Address.select("address")) == 0:
            print("Data not yet exist!")

        else:
            for i in Address.select("address"):
                print(f"""
                        ID: {i[0]},
                        Name: {i[1]},
                        City ID: {i[2]},
                        Create date: {i[3]},
                    """)

        return address_table()

    elif services == "2":  # INSERT
        address_name = input("Address: ")
        city_id = int(input("City ID: "))
        name = Address(address_name, city_id)
        print(name.insert())
        return address_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(Address.update_id(int(old_data), int(new_data)))
        else:
            print(Address.update(column_name.lower(), old_data, new_data))

        return address_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(Address.delete_id("address", value))
        else:
            print(Address.delete("address", column_name, value))
        return address_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return address_table()


def customer_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(Customer.select("customer")) == 0:
            print("Data not yet exist!")

        else:
            for i in Customer.select("customer"):
                print(f"""
                        ID: {i[0]},
                        First Name: {i[1]},
                        Last Name: {i[2]},
                        Password: {i[3]},
                        Email: {i[4]},
                        Birth Date: {i[5]},
                        Address ID: {i[6]},
                        Create Date: {i[7]},
                    """)

        return customer_table()

    elif services == "2":  # INSERT
        customer_1 = input("First Name: ")
        customer_2 = input("Last Name: ")
        customer_3 = input("Password: ")
        customer_4 = input("Email: ")
        customer_5 = input("Birth Date: ")
        customer_6 = int(input("Address ID: "))
        name = Customer(customer_1, customer_2, customer_3, customer_4, customer_5, customer_6)
        print(name.insert())
        return customer_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(Customer.update_id(int(old_data), int(new_data)))
        else:
            print(Customer.update(column_name.lower(), old_data, new_data))

        return customer_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(Customer.delete_id("customer", value))
        else:
            print(Customer.delete("customer", column_name, value))
        return customer_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return customer_table()


def official_detail_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(OfficialDetail.select("official_detail")) == 0:
            print("Data not yet exist!")

        else:
            for i in OfficialDetail.select("official_detail"):
                print(f"""
                        ID: {i[0]},
                        Product ID: {i[1]},
                        Customer ID: {i[2]},
                        Create Date: {i[3]}
                    """)

        return official_detail_table()

    elif services == "2":  # INSERT
        official_detail_1 = int(input("Product ID: "))
        official_detail_2 = int(input("Customer ID: "))
        name = OfficialDetail(official_detail_1, official_detail_2)
        print(name.insert())
        return official_detail_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(OfficialDetail.update_id(int(old_data), int(new_data)))
        else:
            print(OfficialDetail.update(column_name.lower(), old_data, new_data))

        return official_detail_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(OfficialDetail.delete_id("official_detail", value))
        else:
            print(OfficialDetail.delete("official_detail", column_name, value))
        return official_detail_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return official_detail_table()


def payment_status_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(PaymentStatus.select("payment_status")) == 0:
            print("Data not yet exist!")

        else:
            for i in PaymentStatus.select("payment_status"):
                print(f"""
                        ID: {i[0]},
                        Name: {i[1]},
                        Create Date: {i[2]}
                    """)

        return payment_status_table()

    elif services == "2":  # INSERT
        payment_status_1 = input("Name: ")
        name = PaymentStatus(payment_status_1)
        print(name.insert())
        return payment_status_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(PaymentStatus.update_id(int(old_data), int(new_data)))
        else:
            print(PaymentStatus.update(column_name.lower(), old_data, new_data))

        return payment_status_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(PaymentStatus.delete_id("payment_status", value))
        else:
            print(PaymentStatus.delete("payment_status", column_name, value))
        return payment_status_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return payment_status_table()


def payment_type_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(PaymentType.select("payment_type")) == 0:
            print("Data not yet exist!")

        else:
            for i in PaymentType.select("payment_type"):
                print(f"""
                        ID: {i[0]},
                        Name: {i[1]},
                        Create Date: {i[2]}
                    """)

        return payment_type_table()

    elif services == "2":  # INSERT
        payment_type_1 = input("Name: ")
        name = PaymentType(payment_type_1)
        print(name.insert())
        return payment_type_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(PaymentType.update_id(int(old_data), int(new_data)))
        else:
            print(PaymentType.update(column_name.lower(), old_data, new_data))

        return payment_type_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(PaymentType.delete_id("payment_type", value))
        else:
            print(PaymentType.delete("payment_type", column_name, value))
        return payment_type_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return payment_type_table()


def payment_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(Payment.select("payment")) == 0:
            print("Data not yet exist!")

        else:
            for i in Payment.full_select():
                print(f"""
                        ID: {i[0]},
                        Amount: {i[1]},
                        Official Detail ID: {i[2]},
                        Payment Status ID: {i[3]},
                        Payment Type ID: {i[4]},
                        Create Date: {i[5]},
                    """)

        return payment_table()

    elif services == "2":  # INSERT
        amount = int(input("Amount: "))
        official_detail_id = int(input("official_detail_id: "))
        payment_status_id = int(input("payment_status_id: "))
        payment_type_id = int(input("payment_type_id: "))
        payment = Payment(amount, official_detail_id, payment_status_id, payment_type_id)
        print(payment.insert())
        return payment_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(Payment.update_id(int(old_data), int(new_data)))
        else:
            print(Payment.update(column_name.lower(), old_data, new_data))

        return payment_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(Payment.delete_id("payment", value))
        else:
            print(Payment.delete("payment", column_name, value))
        return payment_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return payment_table()


def store_table():
    services = input("""
            Services:
                1. SELECT
                2. INSERT
                3. UPDATE
                4. DELETE
                0. Back
                >>> """)

    if services == "1":  # SELECT
        if len(Store.select("store")) == 0:
            print("Data not yet exist!")

        else:
            for i in Store.select("store"):
                print(f"""
                        ID: {i[0]},
                        Name: {i[1]},
                        Address ID: {i[2]},
                        Create Date: {i[3]}
                    """)

        return store_table()

    elif services == "2":  # INSERT
        store_1 = input("Name: ")
        store_2 = int(input("Address ID: "))
        name = Store(store_1, store_2)
        print(name.insert())
        return store_table()

    elif services == "3":  # UPDATE
        column_name = input("Column Name: ")
        old_data = input("Old Data: ")
        new_data = input("New Data: ")
        if column_name.lower() == "id":
            print(Store.update_id(int(old_data), int(new_data)))
        else:
            print(Store.update(column_name.lower(), old_data, new_data))

        return store_table()

    elif services == "4":
        print("Delete ")
        column_name = input("Column Name: ")
        value = input("Data: ")
        if column_name == "id":
            print(Store.delete_id("store", value))
        else:
            print(Store.delete("store", column_name, value))
        return store_table()

    elif services == "0":
        return main()

    else:
        print("Error!")
        return store_table()


def main():
    tables = input("""
        Tables:
            1. Category
            2. Product
            3. Color
            4. Product Detail
            5. Country
            6. City
            7. Address
            8. Customer
            9. Official Detail
            10. Payment Status
            11. Payment Type
            12. Payment
            13. Store
            >>> """)

    if tables == "1":
        return category_table()

    elif tables == "2":
        return product_table()

    elif tables == "3":
        return color_table()

    elif tables == "4":
        return product_detail_table()

    elif tables == "5":
        return country_table()

    elif tables == "6":
        return city_table()

    elif tables == "7":
        return address_table()

    elif tables == "8":
        return customer_table()

    elif tables == "9":
        return official_detail_table()

    elif tables == "10":
        return payment_status_table()

    elif tables == "11":
        return payment_type_table()

    elif tables == "12":
        return payment_table()

    elif tables == "13":
        return store_table()

    else:
        print("Error!")
        return main()


if __name__ == "__main__":
    main()
