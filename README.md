ALX_BE_CapstoneProject: BeautySite 🛍️
Project Overview

BeautySite is a full-featured e-commerce platform specializing in beauty and cosmetic products, built as the capstone project for the ALX Backend Engineering program. This Django-based web application provides users with a seamless shopping experience for skincare, makeup, and beauty accessories.
Project Name & Branding

Name: BeautySite
Concept: A warm, approachable e-commerce platform that makes beauty shopping feel personal and curated.
Core Features

    ✅ User authentication and profile management

    ✅ Product catalog with categories (skincare, makeup, haircare, etc.)

    ✅ Advanced search and filtering

    ✅ Shopping cart with real-time updates

    ✅ Secure checkout process

    ✅ Order tracking and history

    ✅ Product reviews and ratings

    ✅ Admin dashboard for inventory management

Enhanced Features

    🎯 Personalized product recommendations

    📝 Beauty quiz for product matching

    💝 Wishlist functionality

    🎁 Gift basket creation

    ⭐ Loyalty rewards program

    📱 Responsive design for all devices

Technology Stack
Backend

    Framework: Django

    Database: PostgreSQL

    API: Django REST Framework

    Authentication: JWT tokens

    Payment Processing: Stripe API integration

Frontend

    Templating: Django Templates

    Styling: CSS

    JavaScript: Javascript

Deployment(current considerations, yet to be updated with valid information)

    Platform: Render / AWS / Heroku

    Containerization: Docker

    CI/CD: GitHub Actions

Database Schema
Key Models

    User & Profile - Extended user model with beauty preferences

    Product & Category - Hierarchical product organization

    Cart & CartItem - Shopping session management

    Order & OrderItem - Transaction processing

    Review & Rating - Customer feedback system

    Wishlist - Saved items for future purchase

Relationships

    User ↔ Profile (One-to-One)

    User ↔ Cart (One-to-One)

    User → Orders (One-to-Many)

    Category → Products (One-to-Many)

    Product → Reviews (One-to-Many)

    Cart → CartItems (One-to-Many)

API Endpoints
Authentication

    POST /api/auth/register/ - User registration

    POST /api/auth/login/ - User login

    POST /api/auth/token/refresh/ - Token refresh

    GET /api/auth/profile/ - User profile

Products

    GET /api/products/ - List all products

    GET /api/products/{id}/ - Product details

    GET /api/products/search/ - Search products

    GET /api/products/categories/ - List categories

Cart & Checkout

    GET /api/cart/ - View cart

    POST /api/cart/add/ - Add to cart

    PUT /api/cart/update/{id}/ - Update quantity

    DELETE /api/cart/remove/{id}/ - Remove item

    POST /api/orders/create/ - Create order

Reviews

    GET /api/reviews/product/{id}/ - Product reviews

    POST /api/reviews/ - Create review

    PUT /api/reviews/{id}/ - Update review

Project Structure
text

beautybasket/
├── apps/
│   ├── users/           # Authentication & profiles
│   ├── products/        # Product catalog
│   ├── cart/           # Shopping cart
│   ├── orders/         # Order processing
│   ├── reviews/        # Ratings & reviews
│   └── wishlist/       # Wishlist functionality
├── static/
│   ├── css/            # Custom styles
│   ├── js/             # JavaScript files
│   └── images/         # Product & UI images
├── templates/          # Django templates
├── media/              # User uploads
└── config/             # Project configuration

Installation & Setup
Prerequisites

    Python 3.9+

    PostgreSQL 12+

    pip package manager

Local Development

    Clone the repository:

bash

git clone https://github.com/yourusername/Alx_BE_CapstoneProject.git
cd Alx_BE_CapstoneProject

    Create and activate virtual environment:

bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install dependencies:

bash

pip install -r requirements.txt

    Configure environment variables:

bash

cp .env.example .env
# Edit .env with your database credentials

    Set up database:

bash

python manage.py migrate
python manage.py createsuperuser

    Run development server:

bash

python manage.py runserver

Development Timeline
Phase 1: Idea & Planning

    - Choose a project idea and begin planning

Phase 2: Design Database Schema & Define API Endpoints

    - Create an ERD diagram using tools

Phase 3: Start Building (current)

    - Project setup and commence development

Phase 4: Continue working on the project

    - Project feature refinements and functionality improvements

Phase 5: Polish & Submit

    Polish, test, finalize project and submit.

Future Enhancements

    Mobile Application - React Native app for iOS/Android

    AI Recommendations - Machine learning for personalized suggestions

    AR Try-On - Virtual makeup try-on feature

    Subscription Boxes - Monthly beauty box service

    Social Features - User profiles and sharing

    Multi-vendor Support - Marketplace for multiple sellers

Contributing

This is a capstone project for ALX Backend Engineering program. While primarily an individual project, feedback and suggestions are welcome through issue reports.
License

This project is created for educational purposes as part of the ALX Backend Engineering program.
Acknowledgments (Current Acknowledgments, will be properly updated on submission day)

    ALX Backend Web Development Program
    Mathimu Ngobeni
    developer.mozilla.org
    django-rest-framework.org
    turing.com


About

Project Developer: Kamohelo Tshabalala
ALX Program: Backend Web Development Capstone Project
Repository: Alx_BE_CapstoneProject

This project demonstrates comprehensive backend engineering skills including Django development, database design, API creation, and full-stack web application deployment.
