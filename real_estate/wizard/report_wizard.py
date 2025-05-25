
from  odoo import  api  , fields , models

class PropertyReportWizard(models.TransientModel):
    _name = "property.report.wizard"
    _description = "these report is for to print the property data"

    name = fields.Many2one('estate.property' , string="House Name" , domain=[('state' , '=' , 'sold')])
    # from_date = fields.Date(string="From Date")
    # to_date = fields.Date(string="To Date")
    def print_property_report(self):
        data={
            "get_data":self.read()[0],

        }
        return self.env.ref('real_estate.report_estate_property_action').report_action(self , data=data)