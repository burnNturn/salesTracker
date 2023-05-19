
from django.test import TestCase
from .models import Item
from amazon_api import sp_api
from ebay_api import api

class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Item.objects.create(name='Test Item', sku_identifier='A103-111', cost_per_unit=9.99)

    def test_name_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('sku_identifier').verbose_name
        self.assertEqual(field_label, 'sku_identifier')

    def test_price_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('cost_per_unit').verbose_name
        self.assertEqual(field_label, 'cost_per_unit')

class AmazonAPITest(TestCase):
    def setUp(self):
        self.api = AmazonAPI()

    def test_get_order(self):
        # Note: You would replace 'test_order_id' with a real order ID for testing
        order = self.api.get_order('test_order_id')
        self.assertEqual(order['status'], 'SUCCESS')
        self.assertIsNotNone(order['data'])

    def test_get_order_not_found(self):
        order = self.api.get_order('nonexistent_order_id')
        self.assertEqual(order['status'], 'ERROR')
        self.assertEqual(order['message'], 'Order not found')

class EbayAPITest(TestCase):
    def setUp(self):
        self.api = EbayAPI()

    def test_get_listing(self):
        # Note: You would replace 'test_listing_id' with a real listing ID for testing
        listing = self.api.get_listing('test_listing_id')
        self.assertEqual(listing['status'], 'SUCCESS')
        self.assertIsNotNone(listing['data'])

    def test_get_listing_not_found(self):
        listing = self.api.get_listing('nonexistent_listing_id')
        self.assertEqual(listing['status'], 'ERROR')
        self.assertEqual(listing['message'], 'Listing not found')

