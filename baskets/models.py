from django.db import models
from django.utils.functional import cached_property

from users.models import User
from mainapp.models import Product
# Create your models here.
#
# class BasketQuerySet(models.QuerySet):
#
#     def delete(self,*args,**kwargs):
#         for item in self:
#             item.product.quantity +=item.quantity
#             item.product.save()
#         super(BasketQuerySet, self).delete()



class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return  f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_items_cached
        return sum(basket.sum() for basket in baskets)

    def total_quantity(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_items_cached
        return sum(basket.quantity for basket in baskets)

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    # def delete(self, using=None, keep_parents=False):
    #     self.product.quantity += self.quantity
    #     self.save()
    #     super(Basket, self).delete()
    #
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.get_item(int(self.pk))
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(Basket, self).save()

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity