# فروشگاه آنلاین FastAPI

این یک API کامل برای فروشگاه آنلاین با استفاده از FastAPI و MySQL است.

## ویژگی‌ها

- احراز هویت و مجوزدهی کاربران (JWT)
- مدیریت محصولات
- مدیریت دسته‌بندی‌ها
- سبد خرید
- سیستم سفارش و پرداخت
- پروفایل کاربری
- مستندات Swagger خودکار

## پیش‌نیازها

- Python 3.8+
- MySQL
- pip (مدیر بسته Python)

## نصب و راه‌اندازی

1. کلون کردن مخزن:
```bash
git clone <repository-url>
cd ecommerce-fastapi
```

2. ایجاد محیط مجازی و فعال‌سازی آن:
```bash
python -m venv venv
source venv/bin/activate  # در لینوکس/مک
# یا
.\venv\Scripts\activate  # در ویندوز
```

3. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

4. تنظیم فایل `.env`:
```
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/ecommerce_db
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. ایجاد پایگاه داده MySQL:
```sql
CREATE DATABASE ecommerce_db;
```

6. اجرای برنامه:
```bash
uvicorn main:app --reload
```

## مستندات API

پس از اجرای برنامه، می‌توانید به مستندات Swagger در آدرس زیر دسترسی پیدا کنید:
```
http://localhost:8000/docs
```

## نقش‌های کاربری

- **مدیر (ADMIN)**: دسترسی کامل به تمام عملیات‌ها
- **مشتری (CUSTOMER)**: دسترسی محدود به عملیات‌های مربوط به خود

## مسیرهای API

### احراز هویت
- `POST /api/v1/auth/register`: ثبت‌نام کاربر جدید
- `POST /api/v1/auth/login`: ورود کاربر

### کاربران
- `GET /api/v1/users/me`: دریافت اطلاعات کاربر فعلی
- `GET /api/v1/users`: لیست تمام کاربران (فقط مدیر)
- `GET /api/v1/users/{user_id}`: دریافت اطلاعات یک کاربر خاص

### محصولات
- `POST /api/v1/products`: ایجاد محصول جدید (فقط مدیر)
- `GET /api/v1/products`: لیست محصولات
- `GET /api/v1/products/{product_id}`: دریافت اطلاعات یک محصول
- `PUT /api/v1/products/{product_id}`: به‌روزرسانی محصول (فقط مدیر)
- `DELETE /api/v1/products/{product_id}`: حذف محصول (فقط مدیر)

### دسته‌بندی‌ها
- `POST /api/v1/categories`: ایجاد دسته‌بندی جدید (فقط مدیر)
- `GET /api/v1/categories`: لیست دسته‌بندی‌ها
- `GET /api/v1/categories/{category_id}`: دریافت اطلاعات یک دسته‌بندی
- `PUT /api/v1/categories/{category_id}`: به‌روزرسانی دسته‌بندی (فقط مدیر)
- `DELETE /api/v1/categories/{category_id}`: حذف دسته‌بندی (فقط مدیر)

### سبد خرید
- `POST /api/v1/cart/items`: افزودن محصول به سبد خرید
- `GET /api/v1/cart/items`: دریافت محتویات سبد خرید
- `PUT /api/v1/cart/items/{item_id}`: به‌روزرسانی تعداد محصول در سبد خرید
- `DELETE /api/v1/cart/items/{item_id}`: حذف محصول از سبد خرید

### سفارش‌ها
- `POST /api/v1/orders`: ثبت سفارش جدید
- `GET /api/v1/orders`: لیست سفارش‌ها
- `GET /api/v1/orders/{order_id}`: دریافت اطلاعات یک سفارش
- `PUT /api/v1/orders/{order_id}/status`: به‌روزرسانی وضعیت سفارش (فقط مدیر)

## امنیت

- استفاده از JWT برای احراز هویت
- رمزنگاری پسورد با bcrypt
- کنترل دسترسی مبتنی بر نقش
- اعتبارسنجی داده‌ها با Pydantic

## مجوز

MIT 