"""Products app tests"""

from django.test import TestCase
from django.urls import reverse

from .models import Product, Category

class ProductsPageTests(TestCase):
    '''
    Test case class for verifying the functionality of the products page.
    '''
    def test_all_products_page(self):
        '''
        Test if all products page can be accessed
        and it returns the correct template
        '''
        response = self.client.get(reverse('products'))
        self.assertTemplateUsed(response, 'products/products.html')


class ProductsDetailPageTests(TestCase):
    '''
    Test case class for verifying the functionality of the product detail page.
    '''

    @classmethod
    def setUpTestData(cls):
        ''' Create test product'''
        cls.category = Category.objects.create(name='Fiction')
        cls.product = Product.objects.create(
            name="Test Name",
            id=10292021102495812,
            description='Test description',
            sale=10,
            price=20.00,
            image_url='https://testimage.com',
            image= "beanie.jpg",
            rating=4.5

        )

    def test_product_detail_page(self):
        '''
        Test if all products page can be accessed
        and it returns the correct template
        '''
        response = self.client.get(reverse('product_detail',
                                kwargs={'product_id': self.product.id}))
        self.assertTemplateUsed(response, 'products/product_detail.html')
