from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, users, products, categories, orders, cart

app = FastAPI(
    title="E-Commerce API",
    description="API for Online Shopping Application",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])
app.include_router(users.router, prefix="/api/v1", tags=["Users"])
app.include_router(products.router, prefix="/api/v1", tags=["Products"])
app.include_router(categories.router, prefix="/api/v1", tags=["Categories"])
app.include_router(orders.router, prefix="/api/v1", tags=["Orders"])
app.include_router(cart.router, prefix="/api/v1", tags=["Cart"])

@app.get("/")
async def root():
    return {"message": "Welcome to E-Commerce API"} 