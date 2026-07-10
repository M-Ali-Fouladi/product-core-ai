from app.importers.factory import ImportFactory

importer = ImportFactory.get_importer("mock")

product = importer.import_product(
    "https://mock.com/product/1"
)

print(product)
