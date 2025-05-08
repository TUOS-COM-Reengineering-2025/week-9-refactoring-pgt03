class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def calculate_total_with_tax(self, purchases):
        total = 0
        for item in purchases:
            if item['price'] > self.tax_threshold:
                taxed_price = item['price'] * (1 + self.tax_rate)
                total += taxed_price
            else:
                total += item['price']
        return total

    def is_eligible_for_discount(self, total):
        return total > self.discount_threshold

    def is_potential_discount_customer(self, total):
        return 300 < total <= self.discount_threshold

    def generate_report(self):
        for name, purchases in self.customers.items():
            total = self.calculate_total_with_tax(purchases)
            print(name)
            if self.is_eligible_for_discount(total):
                print("Eligible for discount")
            elif self.is_potential_discount_customer(total):
                print("Potential future discount customer")
            else:
                print("No discount")

            if total > 1000:
                print("VIP Customer!")
            elif total > 800:
                print("Priority Customer")

    def calculate_shipping_fee(self, purchases):
        return calculate_shipping_fee_with_condition(
            purchases, lambda p: p.get('weight', 0) > 20, 50, 20
        )


def calculate_shipping_fee_with_condition(purchases, condition, fee_if_true, fee_if_false):
    for purchase in purchases:
        if condition(purchase):
            return fee_if_true
    return fee_if_false


def calculate_shipping_fee_for_heavy_items(purchases):
    return calculate_shipping_fee_with_condition(
        purchases, lambda p: p.get('weight', 0) > 20, 50, 20
    )


def calculate_shipping_fee_for_fragile_items(purchases):
    return calculate_shipping_fee_with_condition(
        purchases, lambda p: p.get('fragile', False), 60, 25
    )
