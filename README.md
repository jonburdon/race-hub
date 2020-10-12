[insert logo image here]

# Rachub


### [Deployed Project on Heroku](https://race-hub.herokuapp.com/)

[Deployed Project on Heroku](#developer-aims) | [Deployed Project on Heroku](#credits)

## [Developer Aims](#developer-aims)

## UX


## User Stories


## UI Structure

## Visual Layout

## Features

## Technologies Used

## Information Architecture


User Stories
As a user, I want to be able to navigate the site with ease to find what I'm looking for without any hassle.
As a user, I wish to see information about where the meat is sourced form so that I can order with confidence.
As a user, I want the menu to be easily accessible with easy navigation so I can put together my order with ease.
As a user, I want to be able to view and modify my order before completing it so that I can last minute changes before committing my payment details.
As a user, I want to be able to pay securely so that I don't have to concern myself with unfulfilled orders or being wrongfully charged for an order.
As a user, I want to be able to store my details and previous orders to speed up the completion of future orders.
Site Owner Stories
As a user, I want to offer a visually striking site so that shoppers will have confidence in my business' quality.
As a user, I want an admin interface so that I modify site content when the menu changes.
As a user, I want to be able to view a history of all orders on the site so that I can track the performance of the business over time.

## Deployment

## Local Development

## Testing

## [Credits](#credits)


### Nice to have
- dropdowns open on hover (desktop)



## Navigation
Used advice from https://stackoverflow.com/questions/29752882/cant-scroll-within-mobile-drop-down-nav/29753214 to make mobile mega dropdowns scroll on mobile devices
Refactored code, based on: https://codepen.io/JakubHonisek/pen/xXaYqg
Code for mobile view buttons refacroted from Code Institute tutorial



## Home Page App

- Pillow installed to handle image field


## Events App
- Inspiration for Bootstrap cards taken from: https://codepen.io/aminulhchy/pen/RVeJMZ

## Known Issues
- Remove item from cart removes all entries for this event, not the single athlete.

### Testing

Navigation elements from https://codepen.io/skywalkapps/pen/VeNzwG were found to be incompatible with Bootstrap 4.

### References and Acknowledgements:
Responsive Bootstrap Mega Menu: https://codepen.io/JakubHonisek/pen/xXaYqg

#### Stripe

Card number for testing with authentication (triggers popup with overlay)
4000 0025 0000 3155

## Deployment

### NB need bulk data import using fixtures for news sets of results, clubs etc:
NB: Fixtures have not been used to upload bulk product data so import of results data etc.

NB: Heroku login ipaddress mismatch error: Use `heroku login -i` to login from terminal rather than opening browser

NB: eu-west-2 for London in django settings.

During Deployment an error was found in the requirements.txt file due to a typo. This was fixed and the deployment process was then successful.

During Deployment a typo was found in Procfile. NB race_hub is the name of the application. race-hub is used in AWS and also as the project name in Heroku.

NB When logging in to deployed app for the first time, to verify email address... this may not appear. Try logging in to front end. This will cause allauth to create the email address in the back end. It can then be verified.

Bug found during deployment. Image urls were incorrectly coded and did not include {{ MEDIA_URL }} path.


### Credits:

- icons licensed and used from https://uxwing.com/
- logos created by the author using Boxy SVG for macos