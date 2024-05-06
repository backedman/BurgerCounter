# The Ultimate Burger App Leaderboard for CMSC388J Spring 2024

## Description of Your Final Project Idea:
The final project is basically just a leaderboard of users counting how many burgers they ate, as well as the total amount of calories in the burger. The project contains login, registration, burger ordering (through forms), as well as the ability to change your password. Users can submit a burger order form to increase their burger count and calories.

## Functionality Available Only to Logged-In Users:
- Only logged-in users can access the home screen where they can see their own burger count, their own calorie count, as well as a button to order another burger.
- Logged-in users are also the only ones who can access the account page to change their password.
- In the header, login/registration buttons are replaced with Account/Logout.
- Home page redirects to leaderboard for non-logged-in users.

## Forms:
1. **RegistrationForm**: Takes in username, email, password (and confirm password) fields to create an account on MongoDB.
2. **LoginForm**: Takes in username, password to log into/authenticate user.
3. **BurgerForm**: Takes in Buns, Lettuce, Tomato, and Patties from user to calculate calories using CalorieNinja.
4. **UpdatePasswordForm**: Takes in current password and new password (and confirmation) to update the current user's password.

## Routes/Blueprints:
- **Users**:
  - **index**: Home page to list the amount of burgers the user has, as well as calories.
  - **leaderboard**: Lists the users and their burgers and calories in sorted order (sorted by burgers).
  - **burger**: Page with the form to order more burgers (described above).
- **Authentication**:
  - **login**: Page to login using LoginForm (described above).
  - **registration**: Page to register using RegistrationForm (described above).
  - **account**: Page to change the password of the user using UpdatePasswordForm (described above).
  - **logout**: Logs the user out.

## Data Storage in MongoDB:
The username, email, password (hashed), burger count, and calories will be stored and retrieved from MongoDB.

## Python Package/API:
I used the CalorieNinja API to count the calories for each burger. It affects the user experience by having real-time calorie updates on the new burgers they add. If burger meat is suddenly fewer calories, the new burgers will automatically and instantaneously reflect that even if I stop maintaining the website.
