

Following are the API URL

http://127.0.0.1:8000/restaurant/   Serves static content
http://127.0.0.1:8000/restaurant/menu/     Shows list of menu items
http://127.0.0.1:8000/restaurant/menu/2/    Shows menu for given id
http://127.0.0.1:8000/restaurant/booking/ Returns url for table bookings
http://localhost:8000/restaurant/booking/tables/    Shows list of table bookings


Djoser:
http://127.0.0.1:8000/auth/users/   Shows the list of registered users
http://127.0.0.1:8000/auth/users/me/    Shows the currently logged in user info


Djoser TOKEN:
http://127.0.0.1:8000/auth/token/login/     Allows you to get the user's token by entering username and password
http://127.0.0.1:8000/auth/token/logout/    Logs current user out
http://127.0.0.1:8000/restaurant/api-token-auth/    Allows you to get the user token


