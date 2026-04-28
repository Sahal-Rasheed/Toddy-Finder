import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import Place, District, User, Status, ShopCategory
from shops.models import ToddyShop

district = District.objects.first()
place, _ = Place.objects.get_or_create(
    name="Alappuzha Town",
    defaults={"district": district, "address": "Alappuzha", "latitude": 9.4981, "longitude": 76.3388},
)
owner = User.objects.get(username="testowner")
status = Status.objects.get(name="Active")
category = ShopCategory.objects.first()
shop, created = ToddyShop.objects.get_or_create(
    name="Test Shop",
    defaults={"owner": owner, "status": status, "category": category, "place": place, "address": "Test Address"},
)
print(f"Shop {'created' if created else 'already exists'} — id: {shop.id}")
