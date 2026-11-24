def product_info(pid, name, quantity, price):
    return (f"Product ID: {pid}\n"
            f"Product Name: {name}\n"
            f"Quantity: {quantity}\n"
            f"Price: Rs.{price:.2f}")

# Example
print(product_info(pid, "name", quantity, price))
