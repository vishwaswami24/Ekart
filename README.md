# Vishwa E-cart

Vishwa E-cart is a Django-based e-commerce platform designed for selling electrical products such as fans, bulbs, and tubelights. It features user authentication, product browsing, shopping cart management, order placement, and secure payment processing via Razorpay.

## Features

- **User Authentication**: Registration, login, logout, and profile management.
- **Product Catalog**: Browse products categorized into Tubelight, Fan, and Bulb. Products from brands like Bajaj, Havells, and Philips.
- **Shopping Cart**: Add, update quantity, and remove items from the cart.
- **Order Management**: Place orders, view order details, and track order history.
- **Payment Integration**: Secure payments using Razorpay.
- **Email Notifications**: Automated emails for order confirmations.
- **Responsive Design**: Built with Bootstrap for mobile-friendly interface.

## Technologies Used

- **Backend**: Django (Python)
- **Database**: SQLite (default Django database)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Payment Gateway**: Razorpay
- **Email**: Django's built-in email system

## Installation

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd vishwa
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```
   python manage.py createsuperuser
   ```

6. **Run the server**:
   ```
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- Register a new account or login with existing credentials.
- Browse products on the homepage.
- Filter products by category or price range.
- View product details and add to cart.
- Manage cart items (update quantity, remove).
- Proceed to checkout and make payment via Razorpay.
- View order history in your profile.

## Project Structure

- `vishwa/`: Main Django project directory.
- `vapp/`: Django app containing models, views, and URLs.
- `templates/`: HTML templates.
- `static/`: CSS, JS, and image files.
- `media/`: Uploaded product images.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
