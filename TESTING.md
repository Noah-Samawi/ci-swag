Go back to [README.md](/README.md)

# Testing

- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#JavaScript)
  - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [User Story Testing](#user-story-testing)
- [Stripe](#stripe)

## Code Validation

### HTML

### CSS

## JavaScript

## Python

## Responsiveness

## Browser Compatibility

## Lighthouse

## Manual Testing

## Manual Testing

### Site Navigation

| Element                  | Action      | Expected Result                                         | Pass/Fail         |
| ------------------------ | ----------- | ------------------------------------------------------- | ----------------- |
| Logo                     | Click       | Redirect to Home page                                   | <mark>Pass</mark> |
| Swag Button              | Click       | Render a dropdown menu of all product categories        | <mark>Pass</mark> |
| Swag Dropdown Link       | Click       | Redirect to selected product category page              | <mark>Pass</mark> |
| Courses Button           | Click       | Render a dropdown menu of all program categories        | <mark>Pass</mark> |
| Courses Dropdown Link    | Click       | Redirect to selected program category page              | <mark>Pass</mark> |
| Subscription Link        | Click       | Redirect to subscription page                           | <mark>Pass</mark> |
| Profile Button           | Click       | Render a dropdown menu of all profile sections          | <mark>Pass</mark> |
| Profile Dropdown         | Click       | Redirect to selected page                               | <mark>Pass</mark> |
| Profile Dropdown Link    | Click       | Redirect to selected page                               | <mark>Pass</mark> |
| Profile Dropdown Auth    | Click       | Render logout, profile and my courses links             | <mark>Pass</mark> |
| Profile Dropdown NonAuth | Click       | Render login and register links                         | <mark>Pass</mark> |
| Cart Icon Link           | Click       | Redirect to cart page                                   | <mark>Pass</mark> |
| Hamburger Menu           | Click       | Render a dropdown menu of all links                     | <mark>Pass</mark> |
| Footer Socials           | Click       | Redirect in a new tab to all respective media platforms | <mark>Pass</mark> |
| Privacy and Policy Link  | Click       | Redirect to privacy policy page                         | <mark>Pass</mark> |
| About Page               | Click       | Redirect to about page                                  | <mark>Pass</mark> |
| Footer Email             | Click       | Open up an email provider with developer email attached | <mark>Pass</mark> |
| Register Link            | Display     | Render for non authenticated users                      | <mark>Pass</mark> |
| Log in Link              | Display     | Render for non authenticated users                      | <mark>Pass</mark> |
| Log out Link             | Display     | Render only if user is authenticated                    | <mark>Pass</mark> |
| Profile Link             | Display     | Render only if user is authenticated                    | <mark>Pass</mark> |
| Nav Link                 | Hover/Focus | Darken colour of text                                   | <mark>Pass</mark> |
| Footer Socials           | Hover/Focus | Provide background colour feedback change               | <mark>Pass</mark> |

### Home Page

| Element            | Action | Expected Result                           | Pass/Fail         |
| ------------------ | ------ | ----------------------------------------- | ----------------- |
| Shop Now Button    | Click  | Redirect to selected product page         | <mark>Pass</mark> |
| Buy Courses Button | Click  | Redirect to selected programs page        | <mark>Pass</mark> |
| Carousel Arrow     | Click  | Navigate to next slide based on direction | <mark>Pass</mark> |
| Carousel Button    | Click  | Navigate to next slide based on number    | <mark>Pass</mark> |
| Membership Link    | Click  | Redirect to Subscription page             | <mark>Pass</mark> |

### Product Page

| Element                 | Action      | Expected Result                                                 | Pass/Fail         |
| ----------------------- | ----------- | --------------------------------------------------------------- | ----------------- |
| Category Widgets        | Click       | Redirect to selected product category page                      | <mark>Pass</mark> |
| Filter By Price Button  | Click       | Filter queried products based on price                          | <mark>Pass</mark> |
| Filter By Rating Button | Click       | Filter queried products based on rating                         | <mark>Pass</mark> |
| Filter By Sale Button   | Click       | Filter queried products based on sale                           | <mark>Pass</mark> |
| Filter Direction        | Display     | Filter direction displayed via an arrow                         | <mark>Pass</mark> |
| Current Category        | Display     | Current displayed category is shown in the header               | <mark>Pass</mark> |
| Search Bar              | Search      | Filter products based on query to category, name or description | <mark>Pass</mark> |
| Product Cards           | Display     | All filtered Product Cards Rendered in grid layout              | <mark>Pass</mark> |
| Product Card Button     | Click       | Redirect to product detail page                                 | <mark>Pass</mark> |
| Product Card Button     | Hover/Focus | Background darkens, text lightens                               | <mark>Pass</mark> |
| Filter Button           | Hover/Focus | Background darkens                                              | <mark>Pass</mark> |
| Search Icon             | Hover/Focus | Background darkens                                              | <mark>Pass</mark> |
| Category Widgets        | Hover/Focus | Background turns orange, text turns white                       | <mark>Pass</mark> |

### Program Page

| Element                 | Action      | Expected Result                                                 | Pass/Fail         |
| ----------------------- | ----------- | --------------------------------------------------------------- | ----------------- |
| Category Widgets        | Click       | Redirect to selected program category page                      | <mark>Pass</mark> |
| Filter By Price Button  | Click       | Filter queried programs based on price                          | <mark>Pass</mark> |
| Filter By Rating Button | Click       | Filter queried programs based on rating                         | <mark>Pass</mark> |
| Filter By Sale Button   | Click       | Filter queried programs based on sale                           | <mark>Pass</mark> |
| Filter Direction        | Display     | Filter direction displayed via an arrow                         | <mark>Pass</mark> |
| Current Category        | Display     | Current displayed category is shown in the header               | <mark>Pass</mark> |
| Search Bar              | Search      | Filter programs based on query to category, name or description | <mark>Pass</mark> |
| Program Cards           | Display     | All filtered program Cards Rendered in grid layout              | <mark>Pass</mark> |
| Program Card            | Click       | Redirect to program detail page                                 | <mark>Pass</mark> |
| Product Card            | Hover/Focus | Border outline turns blue, cursor is a pointer                  | <mark>Pass</mark> |
| Filter Button           | Hover/Focus | Background darkens                                              | <mark>Pass</mark> |
| Search Icon             | Hover/Focus | Background darkens                                              | <mark>Pass</mark> |
| Category Widgets        | Hover/Focus | Background turns orange, text turns white                       | <mark>Pass</mark> |

### Product Detail Page

| Element             | Action      | Expected Result                                                  | Pass/Fail         |
| ------------------- | ----------- | ---------------------------------------------------------------- | ----------------- |
| Quantity Input      | Input       | Updates the total amount of desired product - no negative values | <mark>Pass</mark> |
| Add to Cart Button  | Click       | Total quantity of item added to cart                             | <mark>Pass</mark> |
| Add to Cart Button  | Click       | Notification appears upon outcome of adding to cart              | <mark>Pass</mark> |
| Back Link           | Click       | Redirects back to the products page                              | <mark>Pass</mark> |
| Paginator           | Click       | All navigations buttons redirect to correct paginated results    | <mark>Pass</mark> |
| View Product Button | Click       | Redirect to related product detail page                          | <mark>Pass</mark> |
| Related Products    | Display     | Display product cards of 4 related items with pagination         | <mark>Pass</mark> |
| Back Link           | Hover/Focus | Text darkens                                                     | <mark>Pass</mark> |
| Add to Cart Button  | Hover/Focus | Background darkens, text lightens                                | <mark>Pass</mark> |
| View Product Button | Hover/Focus | Background darkens, text lightens                                | <mark>Pass</mark> |
| Paginator Button    | Hover/Focus | Background darkens                                               | <mark>Pass</mark> |

### Program Detail Page

| Element                  | Action      | Expected Result                                                | Pass/Fail         |
| ------------------------ | ----------- | -------------------------------------------------------------- | ----------------- |
| Enroll Button            | Click       | Adds course to cart                                            | <mark>Pass</mark> |
| Remove from Cart Button  | Click       | Removes course from cart                                       | <mark>Pass</mark> |
| Login to Enroll          | Click       | Redirects to login page                                        | <mark>Pass</mark> |
| Enrolled Button          | Click       | Button is disabled if already enrolled                         | <mark>Pass</mark> |
| Add / Remove Cart Button | Click       | Notification appears upon outcome of adding/removing from cart | <mark>Pass</mark> |
| Module Accordion         | Click       | Display hidden text and rotate arrow                           | <mark>Pass</mark> |
| Back Link                | Click       | Redirects back to the programs page                            | <mark>Pass</mark> |
| Paginator                | Click       | All navigations buttons redirect to correct paginated results  | <mark>Pass</mark> |
| View Product Button      | Click       | Redirect to related program detail page                        | <mark>Pass</mark> |
| Related Products         | Display     | Display program cards of 4 related items with pagination       | <mark>Pass</mark> |
| Video                    | Display     | Display Video if course is purchased in orders                 | <mark>Pass</mark> |
| Enrolled Button          | Display     | Display Enrolled grey button if course is purchased            | <mark>Pass</mark> |
| Back Link                | Hover/Focus | Text darkens                                                   | <mark>Pass</mark> |
| Add to Cart Button       | Hover/Focus | Background darkens, text lightens                              | <mark>Pass</mark> |
| Remove from Cart Button  | Hover/Focus | Background darkens, text lightens                              | <mark>Pass</mark> |
| Login to Enroll          | Hover/Focus | Background darkens, text lightens                              | <mark>Pass</mark> |
| Paginator Button         | Hover/Focus | Background darkens                                             | <mark>Pass</mark> |

### Subscription Page

| Element                     | Action      | Expected Result                                                | Pass/Fail         |
| --------------------------- | ----------- | -------------------------------------------------------------- | ----------------- |
| Subscribe Button            | Click       | Adds subscription to cart                                      | <mark>Pass</mark> |
| Subscribe Button            | Click       | If subscription is already in cart it is replaced              | <mark>Pass</mark> |
| Remove Subscription Button  | Click       | A confirmation modal is displayed                              | <mark>Pass</mark> |
| Remove Subscription Confirm | Click       | Current active subscription is removed                         | <mark>Pass</mark> |
| Add / Remove Cart Button    | Click       | Notification appears upon outcome of adding/removing from cart | <mark>Pass</mark> |
| Non authenticated users     | Visit       | Redirected to Login page                                       | <mark>Pass</mark> |
| Remove Subscription Button  | Display     | If already subscribed remove button rendered and card is grey  | <mark>Pass</mark> |
| Subscription status         | Display     | Current subscription noticed in subheading                     | <mark>Pass</mark> |
| Subscribe Button            | Hover/Focus | Text darkens, border darkens                                   | <mark>Pass</mark> |

### Cart Page

| Element                     | Action      | Expected Result                                                | Pass/Fail         |
| --------------------------- | ----------- | -------------------------------------------------------------- | ----------------- |
| Update Cart Button          | Click       | Updates the quantity of product by desired amount              | <mark>Pass</mark> |
| Remove from Cart Button     | Click       | Removes all quantity of selected item from cart                | <mark>Pass</mark> |
| Remove Subscription Button  | Click       | A confirmation modal is displayed                              | <mark>Pass</mark> |
| Remove Subscription Confirm | Click       | Current active subscription is removed                         | <mark>Pass</mark> |
| Add / Remove Cart Button    | Click       | Notification appears upon outcome of adding/removing from cart | <mark>Pass</mark> |
| Checkout Button             | Click       | Redirects to checkout page                                     | <mark>Pass</mark> |
| Continue Shopping Link      | Click       | Redirects to products page                                     | <mark>Pass</mark> |
| Update Cart Button          | Display     | Only available for products                                    | <mark>Pass</mark> |
| Discounts                   | Display     | All added discounts are displayed (sale, membership)           | <mark>Pass</mark> |
| Total Cost                  | Display     | Total cost is accurately displayed with breakdown              | <mark>Pass</mark> |
| Update Cart Button          | Hover/Focus | Background darkens, text darkens                               | <mark>Pass</mark> |
| Remove from cart Button     | Hover/Focus | Background darkens, text darkens                               | <mark>Pass</mark> |
| Checkout Button             | Hover/Focus | Background darkens                                             | <mark>Pass</mark> |
| Continue Shopping Link      | Hover/Focus | Text darkens                                                   | <mark>Pass</mark> |

### Checkout Page

| Element                    | Action      | Expected Result                                            | Pass/Fail         |
| -------------------------- | ----------- | ---------------------------------------------------------- | ----------------- |
| Checkout Form              | Submit      | Checkout form submit user and delivery data to stripe      | <mark>Pass</mark> |
| Checkout Form              | Submit      | Stripe payment intent, charge and succeeded occurs         | <mark>Pass</mark> |
| Checkout Form              | Submit      | Non valid form returns context of errors                   | <mark>Pass</mark> |
| Checkout Form              | Submit      | Successful order redirects to checkout success page        | <mark>Pass</mark> |
| Checkout Form              | Submit      | Stripe webhooks are logged via stripe listeners            | <mark>Pass</mark> |
| Checkout Form Save Details | Submit      | Authenticated users details are saved if button is checked | <mark>Pass</mark> |
| Stripe Payment Element     | Submit      | Stripe payment element renders error context if not valid  | <mark>Pass</mark> |
| Pay Now Button             | Click       | Submits user/delivery/payment information                  | <mark>Pass</mark> |
| Continue Shopping Link     | Click       | Redirects to products page                                 | <mark>Pass</mark> |
| Remove from Cart Button    | Click       | Removes all quantity of selected item from cart            | <mark>Pass</mark> |
| Loading Spinner            | Display     | A loading spinner is displayed when await payment results  | <mark>Pass</mark> |
| Cart Items                 | Display     | All Cart items are displayed with a price breakdown        | <mark>Pass</mark> |
| Total Cost                 | Display     | The total cost is accounted for for a price breakdown      | <mark>Pass</mark> |
| Pay Now Button             | Hover/Focus | Background darkens                                         | <mark>Pass</mark> |
| Checkout Form Save Details | Checked     | Background darkens                                         | <mark>Pass</mark> |

### Checkout Success/ Past Order Page

| Element       | Action  | Expected Result                                                     | Pass/Fail         |
| ------------- | ------- | ------------------------------------------------------------------- | ----------------- |
| Checkout Form | Display | Checkout form rendered all Order information, price, user, delivery | <mark>Pass</mark> |
| Checkout Form | Display | Total cost breakdown is displayed for the user                      | <mark>Pass</mark> |
| Notification  | Display | A Notification appears highlighting the successful order number     | <mark>Pass</mark> |

### Profile Page

| Element                | Action      | Expected Result                                                  | Pass/Fail         |
| ---------------------- | ----------- | ---------------------------------------------------------------- | ----------------- |
| User Form              | Submit      | A valid user form updates the users first/last name and username | <mark>Pass</mark> |
| User Form              | Submit      | Non valid form returns the context of the error                  | <mark>Pass</mark> |
| User Notification      | Submit      | A Notification appears highlighting outcome of form submission   | <mark>Pass</mark> |
| Delivery Form          | Submit      | A valid form updates the user delivery information               | <mark>Pass</mark> |
| Delivery Form          | Submit      | Non valid form returns the context of the error                  | <mark>Pass</mark> |
| Delivery Notification  | Submit      | A Notification appears highlighting outcome of form submission   | <mark>Pass</mark> |
| Checkout Form          | Display     | Total cost breakdown is displayed for the user                   | <mark>Pass</mark> |
| Update Profile Button  | Click       | Submits the user form                                            | <mark>Pass</mark> |
| Update Delivery Button | Click       | Submits the user profile form for delivery information           | <mark>Pass</mark> |
| Past Order Link        | Click       | Redirects the user to the checkout success page / past order     | <mark>Pass</mark> |
| Past Orders            | Display     | Renders all authenticated users past orders                      | <mark>Pass</mark> |
| Update Profile Button  | Hover/Focus | Background darkens                                               | <mark>Pass</mark> |
| Update Delivery Button | Hover/Focus | Background darkens                                               | <mark>Pass</mark> |
| Past Order             | Hover/Focus | Text darkens                                                     | <mark>Pass</mark> |

### My Courses Page

| Element                | Action      | Expected Result                                    | Pass/Fail         |
| ---------------------- | ----------- | -------------------------------------------------- | ----------------- |
| Program Cards          | Display     | All enrolled program Cards Rendered in grid layout | <mark>Pass</mark> |
| Explore Courses Button | Click       | Redirect to programs page                          | <mark>Pass</mark> |
| Explore Courses Button | Display     | No Courses associated with user                    | <mark>Pass</mark> |
| Program Card           | Click       | Redirect to program detail page                    | <mark>Pass</mark> |
| Product Card           | Hover/Focus | Border outline turns blue, cursor is a pointer     | <mark>Pass</mark> |
| Explore Courses Button | Click       | Background darkens                                 | <mark>Pass</mark> |

### Sign Up Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Page          | Authentication | Authenticated users redirected to Home page | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Redirected to Home page                     | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Sign up in Notification received            | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Context rendered to UI                | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Notification received                 | <mark>Pass</mark> |
| Login Link    | Click          | Redirect to Login Page                      | <mark>Pass</mark> |
| Form Button   | Hover/Focus    | Darken Background                           | <mark>Pass</mark> |
| Login Link    | Hover/Focus    | Darken Text                                 | <mark>Pass</mark> |

### Sign In Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Page          | Authentication | Authenticated users redirected to Home page | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Redirected to Home page                     | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Sign up in Notification received            | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Context rendered to UI                | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Notification received                 | <mark>Pass</mark> |
| Register Link | Click          | Redirect to Sign In Page                    | <mark>Pass</mark> |
| Form Button   | Hover/Focus    | Darken Background                           | <mark>Pass</mark> |
| Register Link | Hover/Focus    | Darken Text                                 | <mark>Pass</mark> |

### Log Out Page

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Page          | Authentication | Un-authenticated users redirected to Home page | <mark>Pass</mark> |
| Logout Button | Click          | User session is Logged out                     | <mark>Pass</mark> |
| Logout Button | Click          | Redirected to Home page                        | <mark>Pass</mark> |
| Form Button   | Hover/Focus    | Darken Background                              | <mark>Pass</mark> |

## Automated testing

Automated testing was conducted to verify the accuracy of the page responses and templates. However, due to time constraints, there was no opportunity for further elaboration or expansion. Future features include full automated test coverage.

## User Story Testing

| User Story                                                                                                                                                                                             | Screenshot                                                                                                           | Result           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------- |
| As a developer I can setup a new Django project so that I can create the project's structure                                                                                                           | The project was set up successfully                                                                                  | <mark>PASS<mark> |
| As a developer, I can perform an early deployment of the application to verify the functionality of the initial setup so that I can continue testing the application as it evolves during development. | The application was deployed after the initial set up to confirm everything is working as expected                   | <mark>PASS<mark> |
| As a developer I can connect database, static/media storage and stripe payments so that data is accessible on deployment and payments are configured early                                             | The application was linked to AWS, Stripe And Elephant SQL. All required services are linked                         | <mark>PASS<mark> |
| As a developer I can choose a colour theme so that all pages have a consistent feel and style.                                                                                                         | A colour theme was selected for the website                                                                          | <mark>PASS<mark> |
| As a developer I can layout wireframes so that I have a clear idea of the sites structure and theme                                                                                                    | Wireframes created and referenced throughout site layout                                                             | <mark>PASS<mark> |
| As a User I can intuitively navigate through the website so that I can view all content with ease.                                                                                                     | Main navigation bar constructed and links to all relevant pages                                                      | <mark>PASS<mark> |
| As a Developer, I want to ensure the styling and theme of the website are consistent with intuitive UI/UX so that users easily digest content and perform all actions with ease.                       | All elements across all pages are responsive to multiple devices and screensizes                                     | <mark>PASS<mark> |
| As a developer, I can plan out multiple apps that have clear separation of function so that a larger scale project can be broken down into smaller modules                                             | Main application seperated into modular apps for clear functional seperation                                         | <mark>PASS<mark> |
| As a developer, I can create data model classes for products so that structure my data effectively develop relationships between each type                                                             | Product Model clearly structured with effective relationships                                                        | <mark>PASS<mark> |
| As a developer, I can create data model classes for programs so that structure my data effectively develop relationships between each type                                                             | Program Model clearly structured with effective relationships                                                        | <mark>PASS<mark> |
| As a developer, I can create data model classes for subscriptions so that structure my data effectively develop relationships between each type                                                        | Subscription Model clearly structured with effective relationships                                                   | <mark>PASS<mark> |
| As a developer, I can create data model classes for profile so that structure my data effectively develop relationships between each type                                                              | Profile Model clearly structured with effective relationships                                                        | <mark>PASS<mark> |
| As a developer, I can create data model classes for orders so that structure my data effectively develop relationships between each type                                                               | Order Model clearly structured with effective relationships                                                          | <mark>PASS<mark> |
| As a site owner, I can see all my models and data through an admin portal so I can effectively manage my data through CRUD requests                                                                    | Administration classes all registered with full CRUD capabilities                                                    | <mark>PASS<mark> |
| As a User, I can create or login into my account so that I can retrieve my preexisting secure data                                                                                                     | Non authenticated users can register and login through explicit forms                                                | <mark>PASS<mark> |
| As a User, I can log out so that I can secure my account from other users                                                                                                                              | Authenticated users can log out of their session                                                                     | <mark>PASS<mark> |
| As a developer, I can create mock data so that the final application has products, programs and other required models immediately created                                                              | Fixture files and json files created to quickly populate mock data                                                   | <mark>PASS<mark> |
| As a developer, I can have a base template so that all other templates can inherit from it and keep consistant theming                                                                                 | Base template designed, contains relevant links and scripts and is the root inheritance for all subsequent templates | <mark>PASS<mark> |
| As a User, I can visit the home page so that I can get a understanding of what the website content is about and navigate through                                                                       | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a developer, I can create data model classes for categories so that structure my data effectively develop relationships between each type                                                           | Category Model clearly structured with effective relationships                                                       | <mark>PASS<mark> |
| As a User, I can visit the product page so that I can view all products available to purchase                                                                                                          | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can see standardised product preview card, providing key information at a glance so I can quickly make a decision                                                                         | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can visit the product detail page so that I can get more information on the product and add it to my card                                                                                 | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can use a search bar to narrow down search results so that I can quickly find products/programs tailored to me                                                                            | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can visit the program page so that I can view all program available to enroll in                                                                                                          | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can visit the program detail page so that I can get more information on the program and add it to my cart in                                                                              | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can see standardised program preview card, providing key information at a glance so I can quickly make a decision                                                                         | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can add and remove items from my shopping cart so that I can manage my purchases easily and efficiently.                                                                                  | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can view detailed information about items in my shopping cart on the cart detail page, so that I can review my items before proceeding to checkout.                                       | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can easily identify and interact with individual items in my shopping cart through standardised cart item cards, so that I can quickly review and manage my selections.                   | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can receive notification messages whenever a CRUD (Create, Read, Update, Delete) action is taken, so that I am informed about the outcome of my actions and any relevant changes.         | <mark>PASS<mark>                                                                                                     |
| As a User, I can visit the subscription page so that I can view all subscriptions available                                                                                                            | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can view a checkout page so that I can get a run down of items and my total charge                                                                                                        | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a developer, I can view and manage line items within orders to track my purchase accurately and efficiently.                                                                                        | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can securely process my order based on the checkout so that I can buy products from the store                                                                                             | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a Developer, I can securely complete my payment using Stripe integration with webhooks, ensuring that my transaction is protected and verified.                                                     | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can get sales and member discounts so that I can get items at a better price                                                                                                              | Home page exists as the root url, shows relevant data                                                                | <mark>PASS<mark> |
| As a User, I can remove my active membership so that I can opt out of payments                                                                                                                         | <mark>PASS<mark>                                                                                                     |
| As a User, I can visit a profile page so that I can view my personal details and update them                                                                                                           | <mark>PASS<mark>                                                                                                     |
| As a User, I can view my past orders on the profile page so that I can track my purchase history and review previous transactions.                                                                     | <mark>PASS<mark>                                                                                                     |
| As a User, I can view the order confirmation page to see the details of my recent order so that I can verify the items purchased and their prices.                                                     | <mark>PASS<mark>                                                                                                     |
| As a User, I can access a my courses page where I can view all the courses I have bought or enrolled in, so that I can easily track my learning progress and access course materials.                  | <mark>PASS<mark>                                                                                                     |
| As a User, I want to receive a confirmation email after registering for an account, so that I can verify my email address and activate my account.                                                     | <mark>PASS<mark>                                                                                                     |
| As a User, I can receive an order confirmation emails after successfully completing a purchase, so that I have a record of the transaction and can review the details of my order.                     | <mark>PASS<mark>                                                                                                     |
| As a User, I can see a loading spinner so that I know my actions were registered and a result in pending                                                                                               | <mark>PASS<mark>                                                                                                     |
| As a User, I can see my current membership level so that I know what discounts I can avail of                                                                                                          | <mark>PASS<mark>                                                                                                     |
| As a User, I can discover related products and programs on the program page, so that I can explore additional resources or offerings that complement my current selection.                             | <mark>PASS<mark>                                                                                                     |
| As a User, I can see error pages (such as 400, 403, 404, 500) so that I am informed and guided appropriately when unexpected issues arise during my interaction with the website.                      | <mark>PASS<mark>                                                                                                     |
| As a User, I can see error pages (such as 400, 403, 404, 500) so that I am informed and guided appropriately when unexpected issues arise during my interaction with the website.                      | <mark>PASS<mark>                                                                                                     |

## Stripe
