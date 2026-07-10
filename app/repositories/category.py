class CategoryRepository(BaseRepository):
        
        def get_by_name(self, name: str):
              return (self.db.query(Category).filter(Category.name == name).first())

        def create(self, name: str, slug: str):
            category = Category(name=name,slug=slug)
            self.db.add(category)
            return category
        def get_by_slug(self, slug: str):
            return (self.db.query(Category).filter(Category.slug == slug).first())    
