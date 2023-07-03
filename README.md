# cmal - Sencentric, Inc. : Limit available Products in Shop based on O-2-Many Field on Contact Form
[Link](https://www.odoo.com/web#id=3361708&cids=3&menu_id=4720&action=4665&active_id=3361672&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Created new controller 'controllers/main.py' that inherits from website_sale. This controller checks if a user has portal access before allowing them to view the shop.
- [X] Inherited from res.partner model in 'models/res_partner.py' and added One2many field to store the user's visible products
- [X] Inherited the contact view in 'views/res_partner_views.xml' and added the One2many field to the view
- [ ] 

## Issues/Blocking Points
- [X] Struggling to make inherited fields actually show up in the contact view
- [X] Getting error "AttributeError: 'super' object has no attribute 'shop'" when trying to create the shop hiding functionality

## Topics I need clarification on
- [X] View Inheritance
- [X] Controller Inheritance
      
## Interns who helped me
N/A

## Interns I helped
- abar - 1min
- Helped with wrong view type displaying
