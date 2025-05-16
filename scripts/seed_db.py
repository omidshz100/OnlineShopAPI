import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal, engine
from app.models import Base, User, Category, Product, UserRole
from app.utils.security import get_password_hash

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # Create admin user
        admin = User(
            email="admin@example.com",
            hashed_password=get_password_hash("admin123"),
            full_name="Admin User",
            role=UserRole.ADMIN
        )
        db.add(admin)

        # Create test customer
        customer = User(
            email="customer@example.com",
            hashed_password=get_password_hash("customer123"),
            full_name="Test Customer",
            role=UserRole.CUSTOMER
        )
        db.add(customer)

        # Create categories
        electronics = Category(
            name="Electronics",
            description="Electronic devices and accessories"
        )
        clothing = Category(
            name="Clothing",
            description="Fashion items and accessories"
        )
        books = Category(
            name="Books",
            description="Books and publications"
        )
        db.add_all([electronics, clothing, books])
        db.commit()

        # Create products
        products = [
            Product(
                name="Smartphone",
                description="Latest model smartphone with advanced features",
                price=999.99,
                stock=50,
                category_id=electronics.id
            ),
            Product(
                name="Laptop",
                description="High-performance laptop for professionals",
                price=1499.99,
                stock=30,
                category_id=electronics.id
            ),
            Product(
                name="T-Shirt",
                description="Cotton t-shirt with modern design",
                price=29.99,
                stock=100,
                category_id=clothing.id
            ),
            Product(
                name="Jeans",
                description="Classic blue jeans",
                price=79.99,
                stock=75,
                category_id=clothing.id
            ),
            Product(
                name="Python Programming",
                description="Comprehensive guide to Python programming",
                price=49.99,
                stock=200,
                category_id=books.id
            ),
            Product(
                name="Web Development",
                description="Modern web development techniques",
                price=59.99,
                stock=150,
                category_id=books.id
            )
        ]
        db.add_all(products)
        db.commit()

        print("Database seeded successfully!")

    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database() 