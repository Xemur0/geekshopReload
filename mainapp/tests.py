from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from mainapp.models import ProductCategory, Product


class TestMainSmokeTest(TestCase):
    status_code_success = 200

    def setUp(self) -> None:
        category = ProductCategory.objects.create(name='Test')
        Product.objects.create(category=category, name='product_test', price=100)

        self.client = Client()

    def test_products_pages(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

    def test_products_product(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/detail/{product_item.pk}/')
            self.assertEqual(response.status_code, self.status_code_success)

    def test_products_basket(self):
        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 302)

    def tearDown(self) -> None:
        pass


class ProductsTestCase(TestCase):
   def setUp(self):
       category = ProductCategory.objects.create(name="стулья")
       self.product_1 = Product.objects.create(name="стул 1",
                                          category=category,
                                          price = 1999.5,
                                          quantity=150)

       self.product_2 = Product.objects.create(name="стул 2",
                                          category=category,
                                          price=2998.1,
                                          quantity=125,
                                          is_active=False)

       self.product_3 = Product.objects.create(name="стул 3",
                                          category=category,
                                          price=998.1,
                                          quantity=115)

   def test_product_get(self):
       product_1 = Product.objects.get(name="стул 1")
       product_2 = Product.objects.get(name="стул 2")
       self.assertEqual(product_1, self.product_1)
       self.assertEqual(product_2, self.product_2)

   def test_product_print(self):
       product_1 = Product.objects.get(name="стул 1")
       product_2 = Product.objects.get(name="стул 2")
       self.assertEqual(str(product_1), 'стул 1 | стулья')
       self.assertEqual(str(product_2), 'стул 2 | стулья')

