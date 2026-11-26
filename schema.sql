-- DecodeLabs Project 3
-- SQL Data Analysis
-- Database: SQLite

CREATE TABLE IF NOT EXISTS orders (
    OrderID TEXT PRIMARY KEY,
    Date TEXT,
    CustomerID TEXT,
    Product TEXT,
    Quantity INTEGER,
    UnitPrice REAL,
    ShippingAddress TEXT,
    PaymentMethod TEXT,
    OrderStatus TEXT,
    TrackingNumber TEXT,
    ItemsInCart INTEGER,
    CouponCode TEXT,
    ReferralSource TEXT,
    TotalPrice REAL
);
