# E-commerce Order Processing System
# BUG REPORT: App crashes when processing orders with discount codes

class OrderProcessor:
    
    def __init__(self):
        self.orders = []
        self.discount_codes = {
            "SAVE10": 0.10,
            "SAVE20": 0.20,
            "BLACKFRIDAY": 0.50
        }
    
    def calculate_total(self, items, discount_code=None):
        # Calculate subtotal
        subtotal = sum(item["price"] * item["quantity"] for item in items)
        
        # Apply discount
        discount = self.discount_codes[discount_code]
        total = subtotal - (subtotal * discount)
        
        return total
    
    def process_order(self, customer_name, items, discount_code=None):
        total = self.calculate_total(items, discount_code)
        
        order = {
            "customer": customer_name,
            "items": items,
            "total": total,
            "discount_code": discount_code
        }
        
        self.orders.append(order)
        return order

# This crashes the entire app
processor = OrderProcessor()
order = processor.process_order(
    "John Doe",
    [
        {"name": "Laptop", "price": 999.99, "quantity": 1},
        {"name": "Mouse", "price": 29.99, "quantity": 2}
    ],
    discount_code=None  # No discount code — but app crashes!
)
print(f"Order processed: {order}")
