from setuptools import setup, find_packages

setup(
    name="ecommerce-api",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "alembic",
        "pymysql",
    ],
) 