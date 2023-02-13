from django.test import Client, TestCase
from rest_framework.renderers import JSONRenderer
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=80, inventory=100)
        Menu.objects.create(title="Kofte", price=120, inventory=70)
        Menu.objects.create(title="Kebab", price=100, inventory=90)

    def test_getall(self):
        menus = Menu.objects.all()
        serialized_menus = [MenuSerializer(menu).data for menu in menus]
        json_menus = JSONRenderer().render(serialized_menus)

        clnt = Client()
        response = clnt.get("/restaurant/menu/")
        response_data = response.content

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_menus, response_data)
