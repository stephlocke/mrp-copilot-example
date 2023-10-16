# app/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_on_hand = models.IntegerField(default=0)

class BillOfMaterials(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    component = models.ForeignKey(Product, related_name='components', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class WorkOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()
    delivery_date = models.DateField()

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class SalesOrder(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()
    delivery_date = models.DateField()

class Invoice(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_date = models.DateField()

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    hire_date = models.DateField()
    termination_date = models.DateField(blank=True, null=True)

class WorkCenter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

class Routing(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    work_center = models.ForeignKey(WorkCenter, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class ProductionOrder(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

class ProductionOrderLine(models.Model):
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class ProductionOrderWorkOrder(models.Model):
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE)
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)