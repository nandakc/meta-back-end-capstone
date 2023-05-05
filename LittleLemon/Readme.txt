Here are the details for my project for the given review criteria:

• Does the web application use Django to serve static HTML content?
Open http://127.0.0.1:8000/restaurant/ in a browser.
Open LittleLemon\templates\index.html in a text editor to see {% load static %} is used.

• Has the learner committed the project to a Git repository?
Git repo can be accessed at: https://github.com/nandakc/meta-back-end-capstone

• Does the application connect the backend to a MySQL database?
See the DATABASES definition in settings.py file.
NOTE: Please update the USER/PASSWORD to match your MySQL set-up for testing.

• Are the menu and table booking APIs implemented?
Open http://127.0.0.1:8000/restaurant/menu/ in a browser or Insomnia to see the Menu items.
NOTE: Everyone can view the menu items, but only authenticated users can add, edit or delete menu item(s).

Open http://127.0.0.1:8000/restaurant/booking/tables in a browser or Insomnia to see the Booking items.
NOTE: Everyone can create a booking, but only authenticated users can see, edit or delete a booking.

• Is the application set up with user registration and authentication?
Registration: Open http://127.0.0.1:8000/auth/users/ in a browser or Insomnia.
Authentication is implemented by allowing only an authenticated user to see/edit/delete booking or add/edit/delete menu items.

• Does the application contain unit tests?
LittleLemon\LittleLemon\tests folder has unit tests for Models and Views.

• Can the API be tested with the Insomnia REST client?
Described in the previous steps.
