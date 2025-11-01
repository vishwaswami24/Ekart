 /* Code for changing active link on clicking */

// Function to display current date and time
const datetimeDisplayElement = document.getElementById("datetime-display");

// Create a new Date object
const currentDateTime = new Date();

// Extract the date and time components
const date = currentDateTime.toDateString();
const time = currentDateTime.toLocaleTimeString();

// Display the date and time in the span element
datetimeDisplayElement.textContent = `Current Date: ${date} | Current Time: ${time}`;

// Function to update cart count
function updateCartCount() {
    fetch('/api/cart-count/')
        .then(response => response.json())
        .then(data => {
            const cartCountElement = document.getElementById('cart-count');
            if (cartCountElement) {
                cartCountElement.textContent = data.count;
                if (data.count > 0) {
                    cartCountElement.style.display = 'inline';
                } else {
                    cartCountElement.style.display = 'none';
                }
            }
        })
        .catch(error => {
            console.error('Error fetching cart count:', error);
        });
}

// Update cart count on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
});

// Update cart count after adding to cart
document.addEventListener('click', function(e) {
    if (e.target && e.target.closest('a[href*="/addcart/"]')) {
        // Update cart count immediately
        setTimeout(updateCartCount, 1000);
    }
});

// Update cart count after removing from cart
document.addEventListener('click', function(e) {
    if (e.target && e.target.closest('a[href*="/removecart/"]')) {
        // Update cart count immediately
        setTimeout(updateCartCount, 1000);
    }
});

// Update cart count after updating quantity
document.addEventListener('click', function(e) {
    if (e.target && e.target.closest('a[href*="/updateqty/"]')) {
        // Update cart count immediately
        setTimeout(updateCartCount, 1000);
    }
});

// Update cart count when adding items to cart
function addToCart(productId) {
    fetch(`/addcart/${productId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (response.ok) {
            updateCartCount();
        }
    })
    .catch(error => {
        console.error('Error adding to cart:', error);
    });
}

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
 