<p align="center"> 
<img src="https://github.com/cfaulkner985/poster-king/blob/master/static/img/poster-king-logo.png">
</p>

# ReadMe

Link to view the website - https://poster-king.herokuapp.com/

I am creating an e-commerce website for selling posters and will be called Poster King.  The website will be a site where users can browse through different posters and will be able to purchase them. The website will be sports posters at the start but I have the option down the line to add different categories.

The website will have a login page which will then bring them to the main shopping page where they will be able to browse through all the products or select from different categories. Once a user adds their product to the basket then they will be able to purchase them entering in delivery and payment details. The user will also be able to see what they have purchased in the past where it will be linked to their username. If the customer currently does not have an account then they will be able to create one. When they create an account, they will also be able to change email, password and other details related to their account.

# UX
This website is based for people of all ages who like collecting sports posters. There is a big demand for posters for people to frame and to put up on theirs walls.

The posters on the site will be for combat sports fans so I will have a variation of UFC, WWE and Boxing posters as there is a big fan base for all 3 sports which I am also a fan of.

# User Stories
## Customer
### Products
*	I want to see all the product to see your full range so I may purchase one or many.
*	I want to be able to see an induvial product and see what details are shown about that product.
*	I want to be able to see how much my total is so I can see how much I am spending on the posters.
*	I want to be able to see the different categories and be able to sort through them without having to see all the products.
*	I want to be able to search for a specific product to see if it is on the site.

### Purchasing
*	Once I have selected the items I want to buy and added them to the basket I want to see them in the basket.
*	I want to be able to be able to change the items in my basket e.g. change quantity of an item.
*	I want to be able to enter my payment details for the products as quickly and as easily as possible.
*	I want to be sure that my payment information is secure before confirming the payment details on the site.
*	I want a confirmation of my order on the site before confirming just to double check that I have not made any mistakes.
*	I then want an email confirmation so I know that you have received the order and are processing it.

## User
*	I want to be able to easily create an account and be able to see the profile that I have created.
*	I want to be able to login easily to see my account and be able to logout easily when I am finished with my account.
*	I want to be able to recover my password in case I forget and am able to change if I wish to do so.
*	I want to able to easily access my account so I can see my details, order history etc.
*	I want to receive an email confirmation once I have registered to let me know that I created the account successfully.

# Wireframe Mockups

# Features
Every page features a top responsive navigation bar with the logo in the top left, search bar in the middle and links to 'My Account' and shopping car on the top right. The 'My Account' will have a dropdown option for the user to either sign in or register. When signed in they the options will change to profile and log out. Each page has a footer with copyright information.

Below the top navigation bar is a navigation bar which the user can use to navigate through different categories on the site. It has four different categories and when the user clicks on the one of the four options they will have more options via a dropdown menu.

## Home page
The home page has a main heading at the top of the page just below the navigation bar welcoming them to the site. Below this heading there are slider images of different rooms with the poster displayed in them. The user can click between them by clicking on the left side or right side of the images. The idea of this is to give the user an idea of what the poster would look like in a room setting.

Below this a button which when click will bring the user to the all products page wheere they will see all the products for sale on the site. 

## Posters page
The poster page has a heading at the top to make the user aware of what page they are currently on.

Below the heading the user will be able to see how many posters are currently displayed on the page. Beside it there is a sort by dropdown where the user can sort the posters by 8 fifferent views which will help the user navigate the poster better.

The posters page is laid out in columns of thumbnail images of the posters which are 4 wide for desktop view, 1 columns wide for mobile devices, 2 or 3 columns wide for tablets.
Below the posters it displays name of poster, price, category it belongs to and rating it has been given.

#### This page will be the same for all posters page in whatever category the user selects

Every page - except the home page - features its own hero image at the top, detailing a drawing or painting by the artist, or in the case of the about page, a photo of the artist in her studio. The purpose of the hero image is to grab attention and give a positive emotional response to the user.

## Posters detail page
The poster page detail features an image of the poster which is increased to a larger image so user can see it in more detail. To the right of the image are the details relating to the poster. On the top is the name of the poster, below that is the price of the poster, below that is the category is which the poster belongs to and below that is the rating of the poster. Below this is a description of the event in which the poster belongs to. It details date, location, matches relating to the poster.

It also has a quantity selector which allows the user to go up and down in quantity depending on how many the user wants. The minus sign will decrease the quantity and the plus sign will increase the quantity.

The page has 2 buttons at the bottom. The first one is keep shopping button which will bring the user back to the products page so they can search for more posters. The second button is the add to cart button which when pressed will bring the poster the user want to the shopping cart. They will get a notification it has been added to the cart and the cart value will increase.

## Shopping Cart page
The shopping cart page has a heading at the top to make the user aware they are on the correct page.

The shopping cart features the product info of the products that are currently in the shopping cart. It has the image of the poster which has the name and ID of the poster to the right of it. It also shows the price, quantity and sub total of the poster.

This is also where the user can change there mind about the quantity of the posters they want to purchase. Below th quantity selector the user has the option to either update the quantity or remove the poster completely from there shopping basket.

#### This is the same layout for every poster that is in the shopping cart

Below this the the prices which will have the total value of the cart and the delivery cost below that. Then this will be added together to give the user the grand total. If the user spend £50 or more then they will get free delivery but if they have spent less they will be informed on how much more they have to get free delivery.

The page has 2 buttons at the bottom. The first one is keep shopping button which will bring the user back to the products page so they can search for more posters. The second button is the secure checkout button which will bring the user to the checkout screen to complete the order.

When the user click on the shopping cart icon and there is nothing in the cart it will let the user know and has a button to bring the user back to the posters page

## Checkout page
The Checkout cart page has a heading at the top to make the user aware they are on the correct page.

The checkout page has 3 seperate forms for the user to fill out to the complete the order. The first form is the detals form where the user will enter in there full name and e-mail address. The second form is the delivery form where the user will fill out the following detais:
* Street Address 1
* Street Address 2 (If any)
* Town or City
* Country
* Postal Code (If any)
* Phone Number
* County or State (If any)

The third form is the payment where the usre will fill out there card details. If the user enters an incorrect card number they will be shown that they have entered an incorrect card number. But if the card number is correct they will be able to enter the details without any error notification.

To the right of the three forms os the order summary which be able to see the order they are about to purchase. It will display the image, name, quantity, sub total, order total, delivery and grand total.

The page has 2 buttons at the bottom. The first one is ajust cart button which will bring the user back to the shopping cart page to make any changes they want. The second button is the complete order button which will bring the user to the confirmation order page.

## Order Confirmation page
The Order Confirmation page has a heading at the top to thank the user for shopping on the site.

Below the heading the user will get a message to let them know the order has been confirmed and that they will recieve an e-mail confirmation. The confitmaion has an unique order number and the date and time of the sale. Below this is all the order details which has the details of the product, delivery and the billing information.

The page has a button on the botton of the page which is keep shopping and that will bring the user back to the products page.

## Sign Up page
The Sign Up page has a heading at the top to make the user aware they are on the correct page.

The Sign Up page has a link below the heading where the user can click to sign in if they already have an account. If not then they will have to fill out the form to create an account. They will first have to enter there e-mail and address twice and if they don't match they will get a notification and to go any further they will have to match. Then will then have to create a username whuch is unique to them and if it is already taken then they will have to come up with a new one. They will then have to create a password twice where they will both have to match or they wont be able to sign up. Theer is also validation on the password field so they will be informed if there password does not meet the criteria

The page has 2 buttons at the bottom. The first one is back to login button which will bring the user back to the login page. The second button is the sign up button which will bring the user to a page where they will be told that they have been sent an e-mail and to confirm the account they will have to follow the link in the e-mail.

## Login page
The Login page has a heading at the top to make the user aware they are on the correct page.

The Login page has a link below the heading where the user can click to sign up if they have not created an account yet. If they have an account then they will enter the username and password in the fields provided. Below this is a remember me tick box so if the user wants the computer they are using to remember there detail then they will click this box and if they dont or using a shared computer then they would leave it unticked.

The page has 2 buttons at the bottom. The first one is back to home button which will bring the user back to the home page. The second button is the sign in button which will sign the user in so they can shop under there own account.

## Password Reset page
The Password Reset page has a heading at the top to make the user aware they are on the correct page.

The Password Reset page has field where the user will type in there e-mail address so they can reset there password. If the user enters an incorrect e-mail adress then they will gert a notification letting them know that they must enter a valid e-mail address.

The page has 2 buttons at the bottom. The first one is back to login button which will bring the user back to the login page. The second button is the reset my password button button which will send the user a link to there e-mail address in which they can follow to reset there password.

## Existing Features


## Features to implement in the future


## Technologies Used
* I have used HTML, CSS and JavaScript programming languages.
* I used Gitpod (https://gitpod.io/) to build the website.
* I used Django as I want to create a python based web framework for this project.
* I used Django-Allauth (https://django-allauth.readthedocs.io/en/latest/installation.html) for the authentication system of the project and has the features I need for the site
* I used Django Crispy Forms to helps to manage the forms and able adjust forms properties in the backend.
* I used Django Countries which was used for the country field for user to be able to selct the contry they are from.
* I used Stripe to set up the payment methods for the site as customer can pay by card
STRIPE_SECRET_KEY = sk_test_51HWkmcDjRi8A10veALZ0pN026QXz2AxtnRJ1FIemsNcNCwAYeIYY0XTOGHbtJ5NoHgRlsK9DziT9Rl1YYrcUxVKP00EGniLvTF
STRIPE_PUBLIC_KEY = pk_test_51HWkmcDjRi8A10vetThFdSScrABqiauWU7ZeDjTRyzXv8OhiqEV0cnL5eHma6g4ju8hjrQe5laaU4VFn7oSk8aiX00jGHsgnYA
* I used Bootstrap for responsive simplistic layouts.
* I used Pillow to be able to use the image field for the products on the site.
* I used JQuery (https://jquery.com/) for the JavaScript in the website
* I used Font Awesome (https://fontawesome.com) to add the icons used in the site
* Block templates were used so I don’t have to repeat my code to save time
* I used autopep8 (https://github.com/hhatto/autopep8) to tidy up my python code

## Committing files to GitHub
When I make changes to each file I push them from GitHub from GitPod and below are the steps I do to do this. This is essential as to not losing any of the work I have done.
1.	On my GitPod project scroll down and click on the command prompt at the bottom.
2. Check status by typing in ‘git status’.
3.	Type ‘git add’ to add the files for staging.
4.	Type ‘git commit -m "Add all files" to commit the files.
5.	Type ‘git push’ to push the files to GitHub.

## Credits
Product images - https://www.wikipedia.org/ & https://www.pinterest.co.uk/

Product descptions - https://www.wikipedia.org/

Logo - Was created in Paint and https://www.font-generator.com/

Images for the slider - https://desenio.co.uk/ & 

Code Institte includeing the Boutique Ado project which helped me alot.

My mentor Rohit Sharma was a great help guided me through this project.




