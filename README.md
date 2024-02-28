# CI-Swag PP5

[(Developer: Darrach Barneveld)](https://github.com/DarrachBarneveld)

[Link to deployed site](https://ci-swag-e9f8de0bed4b.herokuapp.com/)

<hr>
CiSwag is an online merchandise store catering specifically to software developers. It also is an edu platform where users can enroll in extra online courses and subscribe to memberships. Built using Python, Django, HTML, CSS, JavaScript, Amazon S3 and Stripe.

![CI SWAG STORE PREVIEW](./documentation/images/features/homepage.png)

# Table Of Content

- [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Site Goals](#site-goals)
  - [Scope](#scope)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Database Schema](#database-schema)
  - [Models](#models)
  - [Fonts](#fonts)
  - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
    - [Overview](#overview)
    - [EPICS(Milestones)](#epics---milestones)
    - [User Stories Issues](#user-stories---issues)
    - [MoSCoW prioritisation](#moscow-prioritisation)
    - [GitHub Projects](#github-projectskanban)
    - [Late Design Changes](#late-design-changes)
- [Features](#features)
  - [Navigation Header](#navigation-header)
  - [Footer](#footer)
  - [Home Page](#home-page)
  - [Products Page](#products-page)
  - [Programs Page](#programs-page)
  - [Subscriptions Page](#subscriptions-page)
  - [Product Detail Page](#product-detail-page)
  - [Program Detail Page](#program-detail-page)
  - [Cart Page](#cart-page)
  - [Checkout Page](#checkout-page)
  - [Confirmation Page](#confirmation-page)
  - [Profile Page](#profile-page)
  - [My Courses Page](#my-courses-page)
  - [Privacy Policy Page](#privacy-policy-page)
  - [Sign In Page](#sign-in-page)
  - [Sign Up Page](#sign-up-page)
  - [Sign Out Page](#sign-out-page)
  - [Newsletter](#newsletter)
  - [Notification Messages](#notification-messages)
  - [Confirmation Modal](#confirmation-modal)
  - [Password Reset Page](#password-reset-page)
  - [Password Change Page](#password-change-page)
  - [Email Verification](#email-verification)
  - [Order Confirmation Email](#order-confirmation-email)
  - [Password Reset Email ](#password-reset-email)
  - [Error Pages](#error-pages)
  - [Future Features](#future-features)
- [Marketing](#marketing)
  - [Initial Plan](#initial-plan)
  - [Paid Business Plan](#paid-business-plan)
- [Search Engine Optimization SEO](#search-engine-optimization-seo)
- [Testing](#testing)
- [Bugs](#bugs)
- [Technologies and Languages](#technologies-and-languages)
  - [Languages](#languages-used)
  - [Python Modules](#python-modules-imported)
  - [Technologies and programs](#technologies-and-programs)
- [Deployment](#deployment)
  - [Pre Deployment](#pre-deployment)
    - [Stripe Setup](#stripe-setup)
    - [AWS Setup](#aws-setup)
  - [Deployment on Heroku](#deployment-on-heroku)
  - [Fork the Repository](#fork-the-repository)
  - [Clone the Repository](#clone-the-repository)
  - [Run the Repository Locally](#run-the-repository-locally)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)

## User Experience

### User Stories

1. As a developer I can setup a new Django project so that I can create the project's structure [#1](https://github.com/DarrachBarneveld/ci-swag/issues/1)
2. As a developer, I can perform an early deployment of the application to verify the functionality of the initial setup so that I can continue testing the application as it evolves during development. [#2](https://github.com/DarrachBarneveld/ci-swag/issues/2)
3. As a developer I can connect database, static/media storage and stripe payments so that data is accessible on deployment and payments are configured early [#3](https://github.com/DarrachBarneveld/ci-swag/issues/3)
4. As a developer I can choose a colour theme so that all pages have a consistent feel and style. [#4](https://github.com/DarrachBarneveld/ci-swag/issues/4)
5. As a developer I can layout wireframes so that I have a clear idea of the sites structure and theme. [#5](https://github.com/DarrachBarneveld/ci-swag/issues/5)
6. As a Developer, I want to ensure the styling and theme of the website are consistent with intuitive UI/UX so that users easily digest content and perform all actions with ease. [#6](https://github.com/DarrachBarneveld/ci-swag/issues/6)
7. As a User I can intuitively navigate through the website so that I can view all content with ease. [#7](https://github.com/DarrachBarneveld/ci-swag/issues/7)
8. As a user I want the website to be responsive so I can view it on multiple devices [#8](https://github.com/DarrachBarneveld/ci-swag/issues/8)
9. As a developer, I can plan out multiple apps that have clear separation of function so that a larger scale project can be broken down into smaller modules [#9](https://github.com/DarrachBarneveld/ci-swag/issues/9)
10. As a developer, I can create data model classes for products so that structure my data effectively develop relationships between each type [#10](https://github.com/DarrachBarneveld/ci-swag/issues/10)
11. As a developer, I can create data model classes for programs so that structure my data effectively develop relationships between each type [#11](https://github.com/DarrachBarneveld/ci-swag/issues/11)
12. As a developer, I can create data model classes for subscriptions so that structure my data effectively develop relationships between each type [#12](https://github.com/DarrachBarneveld/ci-swag/issues/12)
13. As a developer, I can create data model classes for profile so that structure my data effectively develop relationships between each type [#13](https://github.com/DarrachBarneveld/ci-swag/issues/13)
14. As a developer, I can create data model classes for orders so that structure my data effectively develop relationships between each type [#14](https://github.com/DarrachBarneveld/ci-swag/issues/14)
15. As a site owner, I can see all my models and data through an admin portal so I can effectively manage my data through CRUD requests [#15](https://github.com/DarrachBarneveld/ci-swag/issues/15)
16. As a User, I can create or login into my account so that I can retrieve my preexisting secure data [#16](https://github.com/DarrachBarneveld/ci-swag/issues/16)
17. As a User, I can log out so that I can secure my account from other users [#17](https://github.com/DarrachBarneveld/ci-swag/issues/17)
18. As a developer, I can create mock data so that the final application has products, programs and other required models immediately created [#18](https://github.com/DarrachBarneveld/ci-swag/issues/18)
19. As a developer, I can have a base template so that all other templates can inherit from it and keep consistant theming [#19](https://github.com/DarrachBarneveld/ci-swag/issues/19)
20. As a User, I can visit the home page so that I can get a understanding of what the website content is about and navigate through [#20](https://github.com/DarrachBarneveld/ci-swag/issues/20)
21. As a developer, I can create data model classes for categories so that structure my data effectively develop relationships between each type [#21](https://github.com/DarrachBarneveld/ci-swag/issues/21)
22. As a User, I can visit the product page so that I can view all products available to purchase [#22](https://github.com/DarrachBarneveld/ci-swag/issues/22)
23. As a User, I can see standardised product preview card, providing key information at a glance so I can quickly make a decision [#23](https://github.com/DarrachBarneveld/ci-swag/issues/23)
24. As a User, I can visit the product detail page so that I can get more information on the product and add it to my card [#24](https://github.com/DarrachBarneveld/ci-swag/issues/24)
25. As a User, I can use a search bar to narrow down search results so that I can quickly find products/programs tailored to me [#25](https://github.com/DarrachBarneveld/ci-swag/issues/25)
26. As a User, I can visit the program page so that I can view all program available to enroll in [#26](https://github.com/DarrachBarneveld/ci-swag/issues/26)
27. As a User, I can visit the program detail page so that I can get more information on the program and add it to my cart [#27](https://github.com/DarrachBarneveld/ci-swag/issues/27)
28. As a User, I can see standardised program preview card, providing key information at a glance so I can quickly make a decision [#28](https://github.com/DarrachBarneveld/ci-swag/issues/28)
29. As a User, I can add and remove items from my shopping cart so that I can manage my purchases easily and efficiently. [#29](https://github.com/DarrachBarneveld/ci-swag/issues/29)
30. As a User, I can view detailed information about items in my shopping cart on the cart detail page, so that I can review my items before proceeding to checkout. [#30](https://github.com/DarrachBarneveld/ci-swag/issues/30)
31. As a User, I can easily identify and interact with individual items in my shopping cart through standardised cart item cards, so that I can quickly review and manage my selections. [#31](https://github.com/DarrachBarneveld/ci-swag/issues/31)
32. As a User, I can receive notification messages whenever a CRUD (Create, Read, Update, Delete) action is taken, so that I am informed about the outcome of my actions and any relevant changes. [#32](https://github.com/DarrachBarneveld/ci-swag/issues/32)
33. As a User, I can visit the subscription page so that I can view all subscriptions available [#33](https://github.com/DarrachBarneveld/ci-swag/issues/33)
34. As a User, I can view a checkout page so that I can get a run down of items and my total charge [#34](https://github.com/DarrachBarneveld/ci-swag/issues/34)
35. As a developer, I can view and manage line items within orders to track my purchase accurately and efficiently. [#35](https://github.com/DarrachBarneveld/ci-swag/issues/35)
36. As a User, I can securely process my order based on the checkout so that I can buy products from the store [#36](https://github.com/DarrachBarneveld/ci-swag/issues/36)
37. As a Developer, I can securely complete my payment using Stripe integration with webhooks, ensuring that my transaction is protected and verified. [#37](https://github.com/DarrachBarneveld/ci-swag/issues/37)
38. As a User, I can get sales and member discounts so that I can get items at a better price [#40](https://github.com/DarrachBarneveld/ci-swag/issues/40)
39. As a User, I can remove my active membership so that I can opt out of payments [#41](https://github.com/DarrachBarneveld/ci-swag/issues/41)
40. As a User, I can visit a profile page so that I can view my personal details and update them [#42](https://github.com/DarrachBarneveld/ci-swag/issues/42)
41. As a User, I can view my past orders on the profile page so that I can track my purchase history and review previous transactions. [#43](https://github.com/DarrachBarneveld/ci-swag/issues/43)
42. As a User, I can view the order confirmation page to see the details of my recent order so that I can verify the items purchased and their prices. [#44](https://github.com/DarrachBarneveld/ci-swag/issues/44)
43. As a User, I can access a my courses page where I can view all the courses I have bought or enrolled in, so that I can easily track my learning progress and access course materials. [#45](https://github.com/DarrachBarneveld/ci-swag/issues/45)
44. As a User, I want to receive a confirmation email after registering for an account, so that I can verify my email address and activate my account. [#46](https://github.com/DarrachBarneveld/ci-swag/issues/46)
45. As a User, I can receive an order confirmation emails after successfully completing a purchase, so that I have a record of the transaction and can review the details of my order. [#47](https://github.com/DarrachBarneveld/ci-swag/issues/47)
46. As a User, I can see a loading spinner so that I know my actions were registered and a result in pending [#48](https://github.com/DarrachBarneveld/ci-swag/issues/48)
47. As a User, I can see my current membership level so that I know what discounts I can avail of [#49](https://github.com/DarrachBarneveld/ci-swag/issues/49)
48. As a User, I can access a short video on the program page if I am enrolled in a course, so that I can get a mock studying experience. [#50](https://github.com/DarrachBarneveld/ci-swag/issues/50)
49. As a User, I can discover related products and programs on the program page, so that I can explore additional resources or offerings that complement my current selection. [#51](https://github.com/DarrachBarneveld/ci-swag/issues/51)
50. As a User, I can discover related products and programs on the program page, so that I can explore additional resources or offerings that complement my current selection. [#51](https://github.com/DarrachBarneveld/ci-swag/issues/51)
51. As a User, I can see error pages (such as 400, 403, 404, 500) so that I am informed and guided appropriately when unexpected issues arise during my interaction with the website. [#54](https://github.com/DarrachBarneveld/ci-swag/issues/54)
52. As a User, I can access the Privacy Policy page so that I understand how my personal information is collected, used, and protected. [#62](https://github.com/DarrachBarneveld/ci-swag/issues/62)
53. As a User, I can sign up for the newslette so that I stay updated with the latest news and offerings. [#65](https://github.com/DarrachBarneveld/ci-swag/issues/65)
54. As a developer, I can ensure that all code is thoroughly documented with comments in a standardised format so that anyone reading the code can easily understand its purpose [#68](https://github.com/DarrachBarneveld/ci-swag/issues/68)
55. As a User, I can reset my password if I forget it, so that I can regain access to my account. [#69](https://github.com/DarrachBarneveld/ci-swag/issues/69)
56. As a User, I can delete my account so that my personal information and data are removed from the website. [#74](https://github.com/DarrachBarneveld/ci-swag/issues/74)

### Site Goals

1. Sell coding merchandise to cater to the coding community's needs and interests.
2. Offer subscription for discounts to incentivise repeat purchases and foster customer loyalty.
3. Provide short online courses allowing authenticated users to supplement their knowledge.
4. Encourage community engagement and interaction to build a strong coding community through newsletters and marketing pages.
5. Curate educational resources and content to support developers continuous learning and skill development needs.
6. Execute effective marketing and promotion strategies to attract and retain customers.

### Scope

The project combines an online store with an educational hub focusing on coding. Users can shop for coding-related merch and also access short courses to boost their coding skills/knowledge. CI-Swag aims for user-friendliness, accessibility, and enjoyment. It ensuring a smooth experience for both shoppers and learners. Members will also have access to rewards and course discounts to foster a wider community. The platform will encompass the following key features:

1. [EPIC - Initial Set Up:](https://github.com/DarrachBarneveld/ci-swag/milestone/1)

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.

2. [EPIC - UX Design Planning:](https://github.com/DarrachBarneveld/ci-swag/milestone/2)

- The website will be responsive, allowing users to access it on both desktop and mobile devices.
- The website will have a consistant theming throughout
- The websites navigation will be inituitve and allow multiple methods of accessing content

3. [EPIC - Data Modelling:](https://github.com/DarrachBarneveld/ci-swag/milestone/3)

- Developers can model the products, profiles, program, subscription and order model
- Models will each have a relationship to each other
- Fixtures will be used to prepopulate data for the store and dynamic content
- User profile/order models will be malleable and th only content subject to CRUD

4. [User Authentication:](https://github.com/DarrachBarneveld/ci-swag/milestone/4)

- Account registration is available for users, granting them full access to CISwag features.
- Once registered, users can log in to access their profiles, courses and subscriptions
- Non authenticated users can still purchase item/merch from the store

5. [EPIC - Site Layout:](https://github.com/DarrachBarneveld/ci-swag/milestone/5)

- Users navigate to their profile page to view and manage their account details, preferences, and order history.
- Users explore product pages to access detailed information about individual items, including descriptions, images, prices, and reviews.
- Users interact with the cart page to review and modify their selected items before proceeding to checkout.
- Users visit the checkout page to complete their purchases by providing shipping and payment details.
- Users browse program pages to discover and enroll in short online courses, accessing course descriptions, schedules, and enrollment options.
- Users engage with the order page to track the status of their orders, view shipping updates, and access order confirmation details.
- Users explore the home page to discover popular articles, featured products, and upcoming courses, providing a curated overview of available content.
- Users navigate category pages to explore articles, products, and courses grouped by relevant topics or themes, facilitating targeted browsing and discovery.

6. [EPIC - UI UX Styling:](https://github.com/DarrachBarneveld/ci-swag/milestone/6)

-Users can navigate intuitively through a visually appealing interface designed for emotional resonance and ease of use.

- Enhance user engagement with interactive elements and responsive design for seamless interactions across devices.
- Improve readability and focus with effective use of whitespace and clear visual hierarchy.
- Optimise performance to ensure fast loading times, enhancing overall user satisfaction and experience.

7. [EPIC - Cart And Checkout:](https://github.com/DarrachBarneveld/ci-swag/milestone/7)

- Users seamlessly add items to their cart and proceed to a user-friendly checkout process.
- Simplify checkout with a clear and concise process, guiding users through each step smoothly.
- Intergration of Stripe payment processing/webhooks for security of payments
- Order processing and storage within user models and database
- Administration access to view all orders that are logged in the database
- Handling of both authenticated on anonymous users payments and confirmations of orders

8. [EPIC - Bug Fixes:](https://github.com/DarrachBarneveld/ci-swag/milestone/8)

- All Errors in coding logic handled
- Documentation of bugs and solutions
- All unhandled errors listed with efforts to solve
- Defensive programming

9. [EPIC - Documentation:](https://github.com/DarrachBarneveld/ci-swag/milestone/9)

- Documentation of the development processes
- Planning and structure of the application as well as purpose
- Extensive testing and results of validation

10. [EPIC - Marketing and SEO](https://github.com/DarrachBarneveld/ci-swag/milestone/10)

- Marketing of website through email newsletter
- Planning of business model and strategies
- Online marketing through FB and Google business pages
- Inclusion of meta descriptions, keywords and semantic structure
- Necessary SEO files - robots, sitemap etc.

Benefits of key features and the EPIC Milestone Approach:

1. Guided Progress: Each issue is placed into a milestone and the tasks/open issues are tracked

2. Adaptability: This approach promotes flexibility as each issue is clearly linked to a broader scope

## Design

The primary design goal of the CI Swag was to focus clear categorisation of products, programs and memberships. The website must be clearly distinguisted from the ecommerce platform of products to the edu paid courses section.

The primary objective of our website design was to ensure an incredibly user-friendly and efficient navigation experience. This was achieved through an intutive filtering system of products, rendering of related items and a responsive and clean navigation menu. Links in various areas of pages also provide return navigation options.

I wanted clear seperation between authenticated users and non authenticated users. Users can access more content if authenticated and could view order history, enrolled programs and can update fields.

I wanted the design to be consistant though each page to have a unique feel to it. This was acheived through resuable component cards and a consistancy of colour, buttons, forms and other UI elements. I want the user to feel as if using the website was a fun and engaging experience as if browsing a shop in person.

This commitment to intuitive navigation and user-focused design principles remained at the forefront of project's development.

In order to enhance development style I researched different styling options via Bootstrap template examples and was greatly inspired by [StartBootstrap](https://startbootstrap.com/templates/ecommerce)

### Colour Scheme

The websites colour theme closly mimics Code Institutes colour theme. The use of orange, black, white and grey are the primary colours to help mimic the feel. Action components such as checkout, pay now or update forms are clearly distinguished with a bold blue or green colour, while all other less important/navigation buttons are consistant with the theme.

![Colour Scheme](./documentation/images/colour%20theme.png)

### Database Schema

![Database schema](./documentation/images/dbdiagram.png)

### Models

#### Allauth User Model

The User model is an integral component of Django Allauth, featuring pre-established fields as part of its standard configuration. Among these fields are username, email, name, password, and others. This model primarily serves the purpose of user authentication, which is why it is not recommended to make direct alterations to it. Furthermore, the User model is linked to the Profile model through a one-to-one relationship, facilitating the management of user-specific data and interactions.

#### Profile Model

Profile Model: The Profile Model provides a snapshot of each user's presence on the platform, encapsulating their user information, delivery information and order history. It is has a one to one relationship with the auth User Model.

#### Category Model

The Category Model categorises products and programs, ensuring users can easily discover relatable products/programs.

#### Product Model

The Product Model is one of the main models of the application and is closely similar to the program model. It includes image, price, name, description, sku, discounts, sale and rating.

#### Program Model

The program model contains all fields of the product model with extra field such as difficulty, videourl and length that are unique to it.

#### Module Model

The moduel model is linked closely to the program model. A module contains a tile and description and is linked to a program

#### Subscription Model

The subscription model is a model that holds information about a users membership. It has one to many relationship with a userprofile. A subscription contains discounts amounts on products and programs.

#### Order Model

The Order model contains information about a purchase. It contains lineitems of products. Products are based on a generic key type as they can be either products, programs or subscriptions. Its fields are date, lineitems, delivery, user and total cost.

#### OrderLine Item

The Order Line Item model is linked to the Order Model. Its fields are an FK to an order, the content_type, object_id, content_object, quantity, total, discount and item total.

### Fonts

The font used in this project is Segoe UI Roboto, which give a standard feel as mimiced in the CI website. <br>
![Font](./documentation/images/font-family.png)

### Wireframes

#### Desktop

<details><summary>Home</summary>
<img src="./documentation/images/wireframes/homepage.png">
</details>
<details><summary>Products</summary>
<img src="./documentation/images/wireframes/productpage.png">
</details>
<details><summary>Product Detail</summary>
<img src="./documentation/images/wireframes/productdetailpage.png">
</details>
<details><summary>Programs</summary>
<img src="./documentation/images/wireframes/programpage.png">
</details>
<details><summary>Program Detail</summary>
<img src="./documentation/images/wireframes/programdetailpage.png">
</details>
<details><summary>Subscription</summary>
<img src="./documentation/images/wireframes/subscriptionpage.png">
</details>
<details><summary>Cart</summary>
<img src="./documentation/images/wireframes/cartpage.png">
</details>
<details><summary>Checkout</summary>
<img src="./documentation/images/wireframes/checkoutpage.png">
</details>
<details><summary>Profile</summary>
<img src="./documentation/images/wireframes/profilepage.png">
</details>
<details><summary>Courses</summary>
<img src="./documentation/images/wireframes/mycoursespage.png">
</details>
<details><summary>Login/Register</summary>
<img src="./documentation/images/wireframes/loginregisterpage.png">
</details>
<details><summary>Thank You</summary>
<img src="./documentation/images/wireframes/thankyoupage.png">
</details>

#### Mobile

<details><summary>Home</summary>
<img src="./documentation/images/wireframes/homepagemobile.png">
</details>
<details><summary>Products</summary>
<img src="./documentation/images/wireframes/productpagemobile.png">
</details>
<details><summary>Product Detail</summary>
<img src="./documentation/images/wireframes/productdetailpagemobile.png">
</details>
<details><summary>Programs</summary>
<img src="./documentation/images/wireframes/programpagemobile.png">
</details>
<details><summary>Program Detail</summary>
<img src="./documentation/images/wireframes/programdetailpagemobile.png">
</details>
<details><summary>Subscription</summary>
<img src="./documentation/images/wireframes/subscriptionpagemobile.png">
</details>
<details><summary>Cart</summary>
<img src="./documentation/images/wireframes/cartpagemobile.png">
</details>
<details><summary>Checkout</summary>
<img src="./documentation/images/wireframes/checkoutpagemobile.png">
</details>
<details><summary>Profile</summary>
<img src="./documentation/images/wireframes/productdetailpagemobile.png">
</details>
<details><summary>Courses</summary>
<img src="./documentation/images/wireframes/mycoursespagemobile.png">
</details>

### Agile Methodology

#### Overview

This project adhered to agile principles, allowing for the meticulous planning of website features through the creation of user stories. Each story included specific acceptance criteria and tasks, facilitating clear objectives. Grouping these stories into EPIC milestones enabled a focused approach to addressing key elements of the site, ensuring necessary prerequisites were distinctly outlined for successful implementation.

#### EPICS - Milestones

In the Agile methodology framework, user stories are categorised into eight EPICs or Milestones. Moreover, an additional set of Milestones, referred to as Error Handling, was established specifically to address any errors encountered during testing, development, or optimisation of site elements with refined code or enhancements.

<details><summary>Milestones</summary>
<img src="./documentation/images/milestones.png">
</details>

#### User Stories - Issues

The user story issue format includes the user story, acceptance criteria, and tasks, detailing essential steps for issue resolution. Whenever feasible, commit messages are linked to their respective issues during development, ensuring the significance of each commit and visually tracking progress on project issues. Milestones, Kanban boards, and other Agile tools are employed to monitor these issues effectively.

<details><summary>User Story</summary>
<img src="./documentation/images/issues.png">
</details>

#### MoSCoW Prioritisation

The project utilised the "MoSCoW" technique to categorise and prioritise features and requirements effectively. "MoSCoW" represents "Must have, Should have, Could have, and Won't have," aiding in organising and prioritising features. This method guides the development process, ensuring that critical elements are addressed as a top priority.

<details><summary>MoSCoW</summary>
<img src="./documentation/images/moscow.png">
</details>

#### GitHub Projects/Kanban

The project implemented a simple Kanban Board structure, comprising columns like Todo, In Progress, and Done. This arrangement offered a well-organised method for monitoring task progress, facilitating visualising and managing the workflow during development. The GitHub project Kanban was linked to the repository for consistent reference.

<details><summary>Kanban</summary>
<img src="./documentation/images/kanban.png">
</details>

#### Late Design Changes

A key late design change was to alter the Phonenumber field within the Profile model. This was both linked to orders and user profiles. An issue was dealing with accessibiliy of the country selector phone number code and the entry of the number in a standardised format to the Order model. The result was removing this feature and instead prompting the user to fill in an international number with error context rendered.

## Features

### Navigation Header

The navigation bar is a consistent element across all pages, designed using Bootstrap and optimised for full responsiveness. The left is centered around navigation of content while the right hand side is related to user authentication. Authenticated users can also see create posts and view profile links while unauthenticated users only see a prompt to login/register.

The mobile version of the navbar has all the content rendered when a hamburger icon is clicked. When clicked a dropdown display is rendered showing all navigation links.

<details><summary>Navbar</summary>
<img src="./documentation/images/features/navbar.png">
</details>

<details><summary>Mobile</summary>
<img src="./documentation/images/features/navbarmobile.png">
</details>

### Footer

The footer contains all the contact informtion about the website as well as the copywrite of trademark. It links to the socials as well as developers contact email. The privacy policy is also linked here

<details><summary>Footer</summary>
<img src="./documentation/images/features/footer.png">
</details>

### Home Page

The homepage serves as the central hub of the site, providing visitors with an overview of its offerings, including featured products, testimonials, imagery, and marketing copy. It serves as a gateway to navigate the store sections through shop now navigation links, inviting users to explore further and discover more about the brand's offerings and value propositions. It uses the fold of the screen to showcase branding imagery.

<details><summary>Home</summary>
<img src="./documentation/images/features/homepage.png">
</details>

### Products Page

The products page showcases preview cards of various products, each accompanied by basic descriptions and images, offering users a quick overview of available items. A filtering system based on categories, prices, sales, and ratings, so users can refine their search to find desired products. Additionally, a search bar enables users to explore specific items, enhancing their browsing experience and allowing them to refine very specific requests.

<details><summary>Products</summary>
<img src="./documentation/images/features/productspage.png">
</details>

### Programs Page

Similar to the products page, the programs page presents preview cards of different educational programs, providing brief descriptions and images to offer users a glimpse into each program's content and offerings. Searchbar and filtering tools remain consistant with the products page

<details><summary>Programs</summary>
<img src="./documentation/images/features/programspage.png">
</details>

### Subscriptions Page

The subscription page displays available membership packages, presenting users with a clear overview of the various subscription options offered. Users can easily identify their current membership package, allowing for seamless management and potential upgrades or downgrades as needed. This page provides transparency and accessibility for users to make informed decisions regarding their subscription preferences.

<details><summary>Subscriptions</summary>
<img src="./documentation/images/features/subscriptions.png">
</details>

### Product Detail Page

The product detail page contains information about the selected product, including price, rating, sale status, and SKU. Featuring an image of the product, users can view it before making a purchase decision. Additionally, the page lists related products at the bottom, offering users additional options to explore. With the option to adjust the quantity and an "Add to Cart" button where users can update there cart with a product quantity.

<details><summary>Product Detail</summary>
<img src="./documentation/images/features/productdetail.png">
</details>

### Program Detail Page

The program detail page provides in-depth information about the selected program, including its name, duration, cost, and a breakdown of modules or sections covered. Users can gain an understanding of the program's content and structure before making a decision. Users must be authenticated before they can enroll in courses and users who have purchased the program, a related video is displayed, offering valuable insights or introductory content to enhance the learning experience.

In the future users will have videos relating to the courses and can track progress, however for the initial build there is just the dummy education video loaded.

<details><summary>Program Detail</summary>
<img src="./documentation/images/features/programdetail.png">
</details>

### Cart Page

The cart page displays a summary of the items currently in the user's cart, presenting essential information such as product details and quantities. Additionally, users can view the total cost of all items in their cart as well as any discounts to certain items. This page serves as a hub users to review and manage their selected items before proceeding to checkout.

<details><summary>Cart</summary>
<img src="./documentation/images/features/cartpage.png">
</details>

### Checkout Page

The checkout page streamlines the purchasing process, guiding users through the final steps of completing their orders. Users can review their selected items, input shipping and payment information. Users can add email changes and name changes for orders, but this will only affect a singler purpose. The checkout page provides order summary details, ensuring transparency regarding the total cost, including discounts and shipping fees. Stripe payment elements are used to handle the payment processing

<details><summary>Checkout</summary>
<img src="./documentation/images/features/checkoutpage.png">
</details>

### Confirmation Page

The thank you and order confirmation page serves as a final acknowledgment of the user's completed purchase, expressing gratitude for their patronage. It provides a summary of the order details, including items purchased, total cost, and shipping information. Additionally, users may receive confirmation numbers or order IDs for reference. This page also serves as the order history page so users can review all orders they have purchased.

<details><summary>Confirmation</summary>
<img src="./documentation/images/features/checkoutsuccess.png">
</details>

### Profile Page

The profile page is where users can easily update their user details such as name and username as well as and edit delivery information. Users can access a overview of their past orders, allowing them to track their purchase history and review previous transactions.

<details><summary>Profile</summary>
<img src="./documentation/images/features/profilepage.png">
</details>

### My Courses Page

The my courses page gives authenticated users quick access to view there total purchased courses. It shows a list of all program preview cards for courses that have been purchased in their order history.

<details><summary>Profile</summary>
<img src="./documentation/images/features/mycourses.png">
</details>

### Privacy Policy Page

This page indicates the legal text of the website and informs users of the privacy and policies as they will be submitting personal data to the website upon checkout. This page was created using a policy generator.

<details><summary>Privacy Policy Page</summary>
<img src="./documentation/images/features/privacypolicypage.png">
</details>

### Sign In page

This page comprises a form with fields for entering a username and password. Beneath the form is the sign up button which submits the form. Below the form is a redirect to the register page if the user does not have an account. Click the remember me checkbox to remain logged in as a session.

<details><summary>Sign In</summary>
<img src="./documentation/images/features/login.png">
</details>

### Sign Up page

It features a form with fields for inputting name, email, username, password, and password confirmation. Underneath the form, there is a link to log in for users with existing accounts, followed by the signup button. After signup, users receive a welcome email at the provided email address and are then directed to the home page.

<details><summary>Sign Up</summary>
<img src="./documentation/images/features/register.png">
</details>

### Sign out page

Upon clicking the "log out" link in the navigation, users are directed to a confirmation page. This page includes a cautionary message and two buttons: one for returning and one for logging out.

<details><summary>Sign Out</summary>
<img src="./documentation/images/features/logout.png">
</details>

### Newsletter

An area where users can input there email to sign up to a newsletter. Users dont have to be authenticated to signup to the newsletter

<details><summary>Newsletter</summary>
<img src="./documentation/images/features/newsletter.png">
</details>

### Notification Messages

Notification messages were user every time the user performs CRUD operation, sign in, and sign out.

<details><summary>Notifications</summary>
<img src="./documentation/images/features/notifications.png">
</details>

### Confirmation Modal

This modal appears whenever a users is performing a delete CRUD operation. It ensures the user must confirm their action before the permanent deletion of a subscription

<details><summary>Confirmation Modal</summary>
<img src="./documentation/images/features/confirmmodal.png">
</details>

### Password Reset Page

This page is for users that which to request a password reset verification link to an email

<details><summary>Password Reset Page</summary>
<img src="./documentation/images/features/passwordreset.png">
</details>

### Password Change Page

This page is for users that clicked the verification link in their email to change a password. Once password is updated they are redirected to sign in again

<details><summary>Password Change Page</summary>
<img src="./documentation/images/features/changepassword.png">
</details>

### Account Deletion

This Feature allows users to delete their accounts so that all there personal data can be removed from the website. This adheres to GDPR principles

<details><summary>Account Deletion</summary>
<img src="./documentation/images/features/accountdeletion.png">
</details>

### Email Verification

An email is sent to a users selected email address on sign up requesting the verification of that email

<details><summary>Email Verification</summary>
<img src="./documentation/images/features/emailverification.png">
</details>

### Order Confirmation Email

An email is sent to both authnetication and non authenticated users upon the completion of a successful purchase from the store

<details><summary>Order Confirmation Email</summary>
<img src="./documentation/images/features/orderconfirmationemail.png">
</details>

### Password Reset Email

The Email template sent to a users inbox when they used the forgot password reset feature

<details><summary>Password Reset Email</summary>
<img src="./documentation/images/features/passwordresetemail.png">
</details>

### Error Pages

Custom Error pages are rendered to show the user what went wrong with their request. These error pages allow the user to redirect to the home page.

An Example below is the 400 page

<details><summary>400</summary>
<img src="./documentation/images/features/errorpage.png">
</details>

## Future Features

### Product Review

Enable users to share their experiences and feedback by writing reviews for products they have purchased. This feature enhances transparency and assists other users in making informed purchase decisions.

### Updating Emails

Allow users to easily update their email addresses associated with their accounts. This feature ensures that users can maintain accurate up to date information for ordering.

### Course Tracker

Implement a tracker that monitors users' progress through online courses based on completed modules. This feature provides users with a visual representation of their learning journey, helping them stay motivated and track their advancement towards course completion.

## Marketing

The B2C (Business-to-Consumer) ecommerce model is adopted for CISwag as it is an online merchandise and edu platform platform catering to individual consumers looking to purchase a wide array of coding related products or enroll in supplementary education courses.

The main target audience will be software engineering students or existing developers.

CI Swag's marketing strategy will focus on online channels to boost traffic and engagement. There will be an initial setup as seen in this project followed by the hypothesis of a marketing strategy that can be used when payments/business accounts are installed.

### Initial Plan

Facebook will serve as the primary platform, with a dedicated business page promoting products and fostering customer interaction. Posts will be made on the business page as well as information pertaining to the website. A automated bot will be setup to answer FAQ questions.

Additionally, Mailchimp will be utilized for weekly newsletters, updating subscribers on new offerings, promotions, and site enhancements. Emails of users can then be input into FB, google and other online providers to build an audience list.

By combining social media outreach with targeted email marketing, CI Swag aims to effectively engage its audience, drive website traffic, and enhance brand visibility in the competitive ecommerce landscape.

![Facebook Banner](./documentation/images/fbbanner.png)
![Facebook Page](./documentation/images/fbpage.png)
![Facebook Banner](./documentation/images/fbfaq.png)
![Facebook Banner](./documentation/images/fbreply.png)
![Newsletter](./documentation/images/features/newsletter.png)

### Paid Business Plan

Hypthoesis of a marketing plan for paid business. This will be broken down into 3 keys online providers. This will required GDPR considerations as well as a verified business.

#### Facebook

1. Boosted posts on the business homepage to extend reach
2. Installation of FB pixel throughout the website to capture analytics - CTR - Add To Cart, Purchase
3. Targeted add campaigns based on audience demographics and LLA audience modelling

#### Instagram

1. Reels and Shorts created to showcase products and testimonials
2. Linked to FB pixel for tracking performance metrics

### Google

1. Creating a google business account and updating business directory
2. Google ads for targeting audiences with banner ads and promoted search results
3. Analytics for understanding traffic and audience
4. Installing pixel throughout the website for key metrics

## Search Engine Optimization SEO

1. Descriptive meta tags were added to the main template, including title, description and keywords.
2. A sitemap was generated using [xml-sitemaps](https://www.xml-sitemaps.com/) This was generated using the deployed website. The file is included in the root level of the project.
3. Robots.txt file was created at the root level of the project. This file tells the search engine crawlers which URLs they can access on the website.

Future creation of a Google business account will improve SEO performance and website ratings.

## Testing

In depth testing documentation can be found [here.](./TESTING.md)

## Bugs

Here is a list of all the major bugs encountered throughout development. Links to specific issues provide a more in depth analysis of how they were identified and resolved. This can also be found documented in [TESTING.md](./TESTING.md)

| Bug                                                                                            | Status |
| ---------------------------------------------------------------------------------------------- | ------ |
| [Bug: Negative Products #52](https://github.com/DarrachBarneveld/ci-swag/issues/52)            | Closed |
| [Bug: Adding Generic Items To Cart #59](https://github.com/DarrachBarneveld/ci-swag/issues/59) | Closed |
| [Bug: Checkout Form Error Context #60](https://github.com/DarrachBarneveld/ci-swag/issues/60)  | Closed |
| [Bug: PhoneNumber Order Widget #63](https://github.com/DarrachBarneveld/ci-swag/issues/63)     | Closed |
| [Bug: Stripe Autofill #66](https://github.com/DarrachBarneveld/ci-swag/issues/66)              | Closed |
| [Bug: Form Accessibiliy #67](https://github.com/DarrachBarneveld/ci-swag/issues/67)            | Closed |
| [Bug: Form Accessibiliy #67](https://github.com/DarrachBarneveld/ci-swag/issues/67)            | Closed |

## Technologies And Languages

### Languages Used

- HTML
- CSS
- JavaScript
- JQuery
- Bootstrap
- Python
- Django

### Python Modules Imported

[Django-allauth](https://pypi.org/project/django-allauth/) is a versatile authentication and account management package for Django, providing a comprehensive set of features for user registration, authentication, account management, and social account integration.

[Dj-database-url](https://pypi.org/project/dj-database-url/) is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.

[Gunicorn](https://pypi.org/project/gunicorn/) is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

[Psycopg2](https://pypi.org/project/psycopg2/) is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

[Django Crispy Forms](https://pypi.org/project/django-crispy-forms/) is a Django application that enhances the presentation and customization of Django forms, making it easier to create aesthetically pleasing and responsive forms for web applications.

[Boto3](https://pypi.org/project/boto3/) is the Amazon Web Services (AWS) SDK for Python. It allows to interact with AWS services, such as S3 storage for media/static files

[Pillow](https://pypi.org/project/pillow/) is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

[Django-phonenumber-field](https://pypi.org/project/django-phonenumber-field/) is a library to assist in verification of phonenumbers

[Django Storages](https://pypi.org/project/django-storages/) Django Storages simplifies file storage management in Django apps by offering custom backends.

[Django Embed Video](https://pypi.org/project/django-embed-video/) Django-embed-video is a Django app that simplifies embedding videos from various platforms, such as YouTube and Vimeo, into Django templates by providing template tags and model fields.

[Stripe](https://pypi.org/project/stripe/) Stripe is a payment processing platform that enables payments by offering a developer-friendly API and a range of customizable payment solutions.

### Technologies and programs

- [Bootstrap](https://getbootstrap.com/) was used to quickly layout the responsive structure of the website
- [JQuery](https://jquery.com/) was used to apply all javascript functionality in a more efficient manner
- [Chat-GPT](https://chat.openai.com/) was used to create all written content and copy of the website
- [VS Code](https://code.visualstudio.com/) was used to code the website locally
- [Balsamiq - Wireframe](https://balsamiq.com/wireframes/) was used to create quick and precise wireframes
- [Favicon Generator](https://favicon.io/favicon-converter/) was used to generate Favicon
- [Font Awesome](https://fontawesome.com/) was used for all icons on the website
- [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used for scoring the website during the testing phase
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Wave Accessibility Tool](https://wave.webaim.org/) was used during testing to check accessibility
- [WebAim Contrast Checker](https://webaim.org/resources/contrastchecker/) was used to ensure proper contrast guidelines where adhered to.
- [Pylance Validator](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) was used as a linter to enhance best practice in the Python code.
- [CI Python Pep8 Checker](https://pep8ci.herokuapp.com/) was used to validate the Python code.
- [Stripe](https://stripe.com/) was used to handle all payment processing
- [AWS](https://aws.amazon.com/) was used host all static and media files for the site.
- [Coolors.co](https://coolors.co/) was used to display the colour scheme.
- [Pixelied](https://pixelied.com/convert/png-converter/png-to-webp) was used to convert images into nextgen formats
- [DBDiagram](https://dbdiagram.io/) was used to visually create the database structure and schemas
- [PostGresSQl](https://www.postgresql.org/) was used in development to store the database information locally
- [ElephantSQL](https://www.elephantsql.com/) was the database hosting provider for the production app
- [Heroku](https://heroku.com/) was the hosting provider used.

## Deployment

### Pre Deployment

To ensure the application is deployed correctly on Heroku it is mandatory to update the requirements.txt. This is a list of requirements that the application needs in order to run.

- To create the list of requirements we use the command pip3 freeze > requirements.txt. This will ensure the file with the requirements is updated.
- Then commit and push the changes to GitHub.

! Before pushing code to GitHub ensure all credentials are in an env.py file, which is included in the .gitignore file. This tells Git not to track this file which will prevent it from being added to Github and the credentials being exposed.

### Stripe setup

- Log in to [Stripe](https://stripe.com/en-ie)
- Navigate to developers section (link located at the top right)
- Go to API keys tab and copy the values of PUBLIC_KEY and SECRET_KEY and add them to your env.py file
- Navigate to the Webhooks page from the tab in the menu at the top and click on add endpoint.
- This section requires a link to the deployed application. The link should look like this https://your_website.herokuapp.com/checkout/wh/
- Choose the events the webhook should recieve and add endpoint.
- When the application is deployed, run a test transaction to ensure the webhooks are working. The events chan be checked in the webhooks page.

### AWS setup

- Log in to [AWS](https://aws.amazon.com/)

1. Create a new S3 bucket:

- Choose the closest AWS region.
- Add unique bucket name.
- Under Object Ownership select ACLs enabled to allow access to the objects in the bucket.
- Under Block Public Access settings unselect block all public access as the application will need access to the objects in the bucket.
- Click on create bucket.

2. Edit bucket settings.

- Bucket properties
  - Open the bucket page.
  - Go to properties tab and scroll down to website hosting and click on edit.
  - Enable static website hosting
  - Under the Hosting type section ensure Host a static website is selected.
  - Add Index.html to index document field and error.html to error document field and click save.
- Bucket permissions

  - Navigate and Click on the "Permissions" tab.
  - Scroll down to the "CORS configuration" section and click edit.
  - Enter the following snippet into the text box and click on save changes.

  ```
  [
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
  ]
  ```

  - Scroll to bucket policy section and click edit. Take note of the bucket arn (Example: arn:aws:s3:::test-bucket)
  - Click on policy generator and set the following settings:

    1. Select Type of Policy - S3 Bucket Policy
    2. Effect Allow
    3. Principal \*
    4. AWS Service Amazon S3
    5. Actions: GetObject
    6. Amazon arn: your arn from the previous page

  - Click on add statement and then generate policy.Copy the policy
  - Paste the policy into the bucket policy editor.
  - Add "/\*" to the end of the resource key to allow access to all resources in this bucket.
  - Navigate and Click Save changes.
  - For the Access control list (ACL) section, click edit and enable List for Everyone (public access) and accept the warning box. If the edit button is disabled, you need to change the Object Ownership section above to ACLs enabled (refer to Create Bucket section above).

3. Identify and Access Management (IAM)

- Create User group
  - In the search bar, search for IAM.
  - On the IAM page select user groups in the menu on the left.
  - Click on create user group, add a name and click create group. The users and permission policies will be added later.
- Create Permissions policy for the user group

  - Go to Policies in the left-hand menu and click create policy
  - Click on actions and import policy.
  - Search for "AmazonS3FullAccess", select this policy, and click "Import".
  - Click "JSON" under "Policy Document" to see the imported policy
  - Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the default value of the resource key ("_") and replace it with the bucket ARN.
    Copy the bucket ARN a second time into the "Resource" section of the JSON snippet. This time, add "/_" to the end of the ARN to allow access to all resources in this bucket.

  ```
      {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "s3:*",
                  "s3-object-lambda:*"
              ],
              "Resource": [
                  "arn:aws:s3:::your-project",
                  "arn:aws:s3:::your-project/*"
              ]
          }
      ]
  }

  ```

  - On the next page add polcity name and description and click create policy.

- Attach Policy to User Group

  - Click on User Groups in the left-hand menu.
  - Click on the user group name created during the above step and select the permissions tab.
  - Click Attach Policy.
  - Search for the policy created during the above step, select it and click attach policy.

- Create User
  - Click on Users in the left-hand menu and click on add user.
  - Enter a User name .
  - Select Programmatic access and AWS Management Console access and click next.
  - Click on add user to group, select the user group created earlier and click create user.
  - Take note of the Access key ID and Secret access key as these will be needed to connect to the S3 bucket.
  - To save a copy of the credentials click Download .csv

### Deployment on Heroku

- To deploy the project on Heroku, first create an account.
- Once logged in, create a new app by clicking on the create app button
- Pick a unique name for the app, select a region, and click Create App.
- On the next page select the settings tab and scroll down to Config Vars. If there are any files that should be hidden like credentials and API keys they should be added here. In this project, there are credentials that need to be protected. This project requires credentials added for:

        1. Django's secret key
        2. Database Credentials
        3. AWS access key
        3. AWS secret key
        4. Email host password.
        5. Stripe public key
        6. stripe secret key
        7. Stripe wh secret

- Scroll down to Buildpacks. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python
- From the tab above select the deploy section.
- The deployment method for this project is GitHub. Once selected, confirm that we want to connect to GitHub, search for the repository name, and click connect to connect the Heroku app to our GitHub code.
- Scroll further down to the deploy section where automatic deploys can be enabled, which means that the app will update every time code is pushed to GitHub. Click deploy and wait for the app to be built. Once this is done, a message should appear letting us know that the app was successfully deployed with a view button to see the app.

### Fork the Repository

1. Navigate to the [repository](https://github.com/Dayana-N/Book-Heaven-PP5)
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description
4. Choose to copy only the main branch or all branches to the new fork.
5. Click Create a Fork. A repository should appear in your GitHub

### Clone the Repository

1. Navigate to the [repository](https://github.com/Dayana-N/Book-Heaven-PP5)
2. Click on the Code button on top of the repository and copy the link.
3. Open Git Bash and change the working directory to the location where you want the cloned directory.
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.

### Run The Repository Locally

1. Go to the GitHub repository
2. Locate the green Code button above the list of files and click it
3. From the dropdown menu select download Zip.
4. Download and open the zip file to run in an editor
5. Create an env.py file and input the environment variables
6. Ensure [PostgreSQL](https://www.postgresql.org/) is install on your computer and ports are open
7. Create a virtual environment for installing the python modules in the pip file.
8. Run python3 makemigrations, migrate and runserver

## Credits

### Content

Additionaly copy for the website was prompted with use of [ChatGPT](https://chat.openai.com/)
For Readme/Testing templates inspiration and guidance from [BookHeaven](https://github.com/Dayana-N/Book-Heaven-PP5/blob/main/README.md)

### Media

All Media images on this website were created using [Leondardo AI](https://leonardo.ai/)
[Hero Image](https://www.linkedin.com/posts/melinda-zhang-2020_the-weekend-ended-with-a-blast-our-activity-6975486245997056001-W-_I/)

### Code

- Boutique Ado CI Walkthrough was used for the base of this project
- [Content Type Framework](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/)
- [Bootstrap Templates](https://startbootstrap.com/templates/ecommerce)
- [Local Stripe Webhook Testing](https://www.youtube.com/watch?v=q33qN2zz4E4&t=453s)
- [Basic Automated Tests](https://learndjango.com/tutorials/django-testing-tutorial)

### Acknowledgements

I would personally like to thank all people who underwent testing for this website. The critial feedback was instrumental in providing a good user experience, finding edge case errors and generally keeping me motivated to improve the website. John Paul Larkin, Megan ODonohoe, Juan Boccia, Izabella Lopes, Gary Donlan, Alan Bushell and Dayana.
