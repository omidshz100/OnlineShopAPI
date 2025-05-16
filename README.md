# FastAPI Online Store

This is a full-featured API for an online store using FastAPI and MySQL.

## Features

* User authentication and authorization (JWT)
* Product management
* Category management
* Shopping cart
* Order and payment system
* User profile
* Automatic Swagger documentation

## Prerequisites

* Python 3.8+
* MySQL
* pip (Python package manager)

## Installation & Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd ecommerce-fastapi
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# or
.\venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the `.env` file:

```
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/ecommerce_db
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Create the MySQL database:

```sql
CREATE DATABASE ecommerce_db;
```

6. Run the application:

```bash
uvicorn main:app --reload
```

## API Documentation

Once the app is running, you can access the Swagger documentation at:

```
http://localhost:8000/docs
```

## User Roles

* **Admin**: Full access to all operations
* **Customer**: Limited access to personal operations only

## API Endpoints

### Authentication

* `POST /api/v1/auth/register`: Register a new user
* `POST /api/v1/auth/login`: User login

### Users

* `GET /api/v1/users/me`: Get current user information
* `GET /api/v1/users`: List all users (admin only)
* `GET /api/v1/users/{user_id}`: Get information of a specific user

### Products

* `POST /api/v1/products`: Create a new product (admin only)
* `GET /api/v1/products`: List products
* `GET /api/v1/products/{product_id}`: Get product details
* `PUT /api/v1/products/{product_id}`: Update product (admin only)
* `DELETE /api/v1/products/{product_id}`: Delete product (admin only)

### Categories

* `POST /api/v1/categories`: Create a new category (admin only)
* `GET /api/v1/categories`: List categories
* `GET /api/v1/categories/{category_id}`: Get category details
* `PUT /api/v1/categories/{category_id}`: Update category (admin only)
* `DELETE /api/v1/categories/{category_id}`: Delete category (admin only)

### Cart

* `POST /api/v1/cart/items`: Add product to cart
* `GET /api/v1/cart/items`: Get cart contents
* `PUT /api/v1/cart/items/{item_id}`: Update quantity of an item in cart
* `DELETE /api/v1/cart/items/{item_id}`: Remove item from cart

### Orders

* `POST /api/v1/orders`: Place a new order
* `GET /api/v1/orders`: List orders
* `GET /api/v1/orders/{order_id}`: Get order details
* `PUT /api/v1/orders/{order_id}/status`: Update order status (admin only)

## Security

* JWT-based authentication
* Password hashing with bcrypt
* Role-based access control
* Data validation with Pydantic

## License

MIT
