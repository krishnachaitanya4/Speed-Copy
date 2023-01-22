from django.conf import settings
from shop.models import Products
class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session.get[settings.CART_SESSION_ID]=[]
        self.cart = cart
    
    def add(self,products,pages,quantity,p_file,color,sides):
        product_id = str(products.id)
        pro = {
            product_id:{
                'pages':pages,
                'quantity':quantity,
                'file':p_file,
                'color':color,
                'sides':sides
            }
        }
        cart.append(pro)

        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_its = self.cart.keys()