import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skyeng_test_task.settings")
import django

django.setup()
from faker import Faker
from core.models import *
from model_bakery.recipe import Recipe, foreign_key

fake = Faker()

for _ in range(100):
    product = Recipe(
        Product,
        name=fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None),
        category=fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None),
        is_active=True,
        price=100
    )
    product.make()
    order = Recipe(
        Order,
        created_at=fake.future_datetime(end_date="+30d", tzinfo=None),
    )
    order.make()
    order_product = Recipe(
        OrderProduct,
        order=foreign_key(order),
        product=foreign_key(product),
        quantity=100,
    )
    order_product.make()
