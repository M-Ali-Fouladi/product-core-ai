from .base import BaseImporter


class MockImporter(BaseImporter):

    def import_product(self, url: str):

        return {
            "title": "iPhone 16 Pro 256GB",
            "brand": "Apple",
            "category": "Smartphones",
            "image": "https://example.com/iphone.jpg",
            "description": "Demo Product",
            "external_id": "iphone16pro",
            "price": 1199.99,
            "currency": "USD",
            "store": "mock",
            "url": url
        }
