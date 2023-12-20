

How to test this API:

Does the web application use Django to serve static HTML content?
Look at: http://127.0.0.1:8000/restaurant/

Are the menu and table booking APIs implemented?
Look at:
http://127.0.0.1:8000/restaurant/menu/     Shows list of menu items
http://127.0.0.1:8000/restaurant/menu/2/    Shows menu for given id
http://127.0.0.1:8000/restaurant/booking/ Returns url for table bookings
http://localhost:8000/restaurant/booking/tables/    Shows list of table bookings

Is the application set up with user registration and authentication?
Look at:
http://127.0.0.1:8000/auth/users/   Shows the list of registered users
http://127.0.0.1:8000/auth/users/me/    Shows the currently logged in user info
http://127.0.0.1:8000/auth/token/login/     Allows you to get the user's token by entering username and password
http://127.0.0.1:8000/auth/token/logout/    Logs current user out
http://127.0.0.1:8000/restaurant/api-token-auth/    Allows you to get the user token


