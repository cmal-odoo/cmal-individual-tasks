# cmal - Kinsman Enterprises : Hiding the cart and prices on website
[Link](https://www.odoo.com/web#id=3361704&cids=3&menu_id=4720&action=4665&active_id=3361672&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Setup eCommerce on testing DB to understand how prices and cart are displayed
- [ ] Found information on cart and price display at website_sale/views/templates.xml
- [ ] Created model 'models/website.py' that inherits from website and adds a boolean field to toggle price and cart visibility
- [ ] Created conditional templates in 'views/templates.xml' that use the boolean field to determine the visibility
- [ ] Created header inheritance in 'views/header.xml' to display a checkbox to toggle the boolean
- [ ] Created basic JavaScript in 'static/js/main.js' to handle logic for toggling the boolean
- [ ] Created a controller in 'controllers/kinsman_controllers.py' that is accessed by the JavaScript to toggle the boolean
- [ ] Integrated the JavaScript into the website by creating file 'views/assets.xml'

## Issues/Blocking Points
- [X] Difficulty understanding how to add something that appears on all websites created from any template
- [ ] First time using JavaScript in Odoo

## Topics I need clarification on
- [X] Topic #1
      
## Interns who helped me
- [tetragram] - [# minutes helped] - [What they helped on]

## Interns I helped
- [tetragram] - [# minutes helped]
