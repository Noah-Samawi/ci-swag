from django.views import View

# Create your views here.
class CheckoutView(View):
    template_name = 'checkout/checkout.html'

     
    def get(self, request, *args, **kwargs):  

        return render(request, self.template_name)


   