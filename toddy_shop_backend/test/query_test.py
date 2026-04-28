from django.conf import settings
from django.db import connection, reset_queries

settings.DEBUG = True
reset_queries()

from shops.models import ToddyShop
from shops.serializers import ToddyShopListSerializer

shops = list(
    ToddyShop.objects.select_related("place__district", "category", "status", "owner__role").prefetch_related(
        "facilities", "hygiene_tags"
    )
)
data = ToddyShopListSerializer(shops, many=True).data

print(f"\nTotal queries fired: {len(connection.queries)}")
for i, q in enumerate(connection.queries):
    print(f"{i+1}. {q['sql'][:150]}")
