# cmal - JaniClean: Automation for Employee's Birthday Template
[Link](https://www.odoo.com/web#id=3361698&cids=3&menu_id=4720&action=4665&active_id=3361672&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Research automated actions in Odoo backend. Found [ir.cron](https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/models/ir_cron.py) and studied how it's used
- [X] Research email handling in Odoo backend
- [X] Create email template that gets employee name and birthday and creates the email
- [X] Set up automation that checks every day if the current day matches an employee's birth day and month
- [X] Create email automation for detected birthdays
- [ ] Test emails

## Issues/Blocking Points
- [X] Sending emails via Odoo in a testing environment
- [X] Lack of automated action documentation
- [X] Unable to debug cron once module installed - nothing happens, no clear way to debug

## Topics I need clarification on
- [X] Automation/cron
- [X] Email sending code
      
## Interns who helped me
- N/A

## Interns I helped
- N/A
