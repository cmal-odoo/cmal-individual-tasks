from odoo import models, api
from datetime import date

class HrEmployee(models.Model):
    #_name = 'birthday.handler'
    _inherit = 'hr.employee'

    @api.model
    def send_birthday_email(self, employee_id):
        email_template = self.env.ref('birthday_automation.birthday_email_template')
        email_template.send_mail(employee_id)

    @api.model
    def _cron_birthday_handler(self):
        
        # Get current date
        # Get filtered list of employees with a birthday on the current date
        # Loop through each and send an email wishing a happy birthday

        today = date.today()
        employees = self.search([])
        birthday_employees = employees.filtered(lambda r: r.birthday and r.birthday.day == today.day and r.birthday.month == today.month)

        for birthday_employee in birthday_employees:
            self.send_birthday_email(self, birthday_employee.id)

