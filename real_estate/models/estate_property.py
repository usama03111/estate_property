from email.policy import default
from typing import Dict, List

from dateutil.relativedelta import relativedelta
from pkg_resources import require
from reportlab.graphics.transform import inverse
<<<<<<< HEAD
from  datetime import date
=======

>>>>>>> 05b39e2e21064740b2093465314b30c8cdd717a6
from  odoo import api , models , fields , _
from odoo.exceptions import ValidationError
from odoo.tools.populate import compute


class RealEstate(models.Model):
    _name = 'estate.property'
    _description = 'test model'

    active = fields.Boolean(default=True , invisible=True)
    name = fields.Char(string='House' , required=True)
    state = fields.Selection(
        [
            ("new", "New"),
            ("received", "Offer Received"),
            ("accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ], required=True , copy=False , default='new',)

    def action_received(self):
        for rec in self:
            rec.state = 'new'

    def action_new(self):
        for rec in self:
            rec.state = 'received'

    def action_accepted(self):
        for rec in self:
            rec.state = 'accepted'

    def action_sold(self):
        for rec in self:
            rec.state = 'sold'

    def action_cancel(self):
        for rec in self:
            rec.state = 'canceled'

    postcode = fields.Char()

    def _default_date(self):
        return fields.Date.today()
    # Can either write the one line method in the field definition, or call a method ( )
    date_availability = fields.Date(default= _default_date)
    expected_price = fields.Float()

    selling_price = fields.Float()

    description = fields.Text()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ],)

    property_type_id = fields.Many2one('estate.property.type')
    offer_ids = fields.One2many('estate.property.offer','property_id')
    tag_ids = fields.Many2many('estate.property.tag')
    total_area = fields.Integer(compute='_compute_total_area')
    best_offer = fields.Float(compute='_compute_best_offer')

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for property in self:
            property.best_offer = max(property.offer_ids.mapped('price')) if property.offer_ids else 0


    @api.depends('living_area' , 'garden_area')
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area

    @api.onchange('garden')
    def _onchange_garden(self):
        for estate in self:
            if not estate.garden:
                estate.garden_area = 0

    @api.onchange('date_availability')
    def _onchange_date_availability(self):
        for estate in self:
<<<<<<< HEAD
            if estate.date_availability < date.today():
                return {
                    "warning":{"title":_("Invalid Date") , "message":_("Your date avalibility is not set today date")}
                }


    # @api.constrains('selling_price')
=======
            return {
                "warning":{"title":_("warning") , "message":_("this is onchange methode")}
            }

    @api.constrains('selling_price')
>>>>>>> 05b39e2e21064740b2093465314b30c8cdd717a6
    def _check_constraint(self):
        for estate in self:
            if estate.best_offer > estate.selling_price :
                raise ValidationError(_('The selling price is Less than best offer'))

<<<<<<< HEAD
=======

>>>>>>> 05b39e2e21064740b2093465314b30c8cdd717a6
