from django.db import models

class PurchaseLot(models.Model):
    date_of_purchase = models.DateField()
    lot_identifier = models.CharField(max_length=200)
    venue_of_purchase = models.CharField(max_length=200)
    venue_transaction_number = models.CharField(max_length=200)
    original_source = models.CharField(max_length=200)
    purchase_type = models.CharField(max_length=200)
    main_category = models.CharField(max_length=200)
    short_description = models.TextField()
    units_received = models.IntegerField()
    subtotal_cost = models.DecimalField(max_digits=10, decimal_places=2)
    fees_on_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_inbound = models.DecimalField(max_digits=10, decimal_places=2)
    other_cost = models.DecimalField(max_digits=10, decimal_places=2)
    discounts = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    link_to_webpage = models.URLField()
    # Remaining fields will be updated with methods or signals as we fetch data from APIs and update Items

class Item(models.Model):
    purchase_lot = models.ForeignKey(PurchaseLot, on_delete=models.CASCADE)
    sku_identifier = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    units_received = models.IntegerField()
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    # Remaining fields will be updated with methods or signals as we fetch data from APIs and update LineItems

class Order(models.Model):
    order_date = models.DateTimeField()
    order_venue = models.CharField(max_length=200)
    order_number = models.CharField(max_length=200)
    subtotal_sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_handling_charged = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid_by_buyer = models.DecimalField(max_digits=10, decimal_places=2)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    # net_revenue will be calculated as (total_paid_by_buyer - fees - shipping_cost)

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    line_item_number = models.CharField(max_length=200)
    quantity = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_handling_charged = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid_by_buyer = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    # shipping_cost will be calculated and updated programmatically

class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    line_item = models.ForeignKey(LineItem, on_delete=models.CASCADE, null=True, blank=True)
    transaction_date = models.DateTimeField()
    transaction_number = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    transaction_type = models.CharField(max_length=200)
    transaction_value = models.DecimalField(max_digits=10, decimal_places=2)
    booking_entry = models.CharField(max_length=200)
