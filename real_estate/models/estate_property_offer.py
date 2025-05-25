
from  dateutil import relativedelta

from odoo import api, fields, models , _
from odoo.exceptions import UserError
from odoo.exceptions import  ValidationError
class EstateOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offers made for real estates"

    price = fields.Float()
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        copy=False,
    )
    partner_id = fields.Many2one("res.partner",)
    property_id = fields.Many2one("estate.property" , invisible=True)
    property_offer_id = fields.Many2one("estate.property.type", invisible=True)
    type_id = fields.Many2one(related='property_id.property_type_id' , store=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    @api.depends('validity')
    def _compute_date_deadline(self):
        for property in self:
            property.date_deadline = fields.date.today() + relativedelta.relativedelta(days=property.validity)

    def _inverse_date_deadline(self):
        for property in self:
            property.validity = (property.date_deadline - fields.Date.today()).days


    def action_accept(self):
        self.ensure_one()
        if 'accepted' in self.property_id.offer_ids.mapped('status'): #this is because it returns the list if ids
            raise  UserError(_('The offer is already accepted'))
        self._check_constraint()
        self.status = 'accepted'
        self.property_id.selling_price = self.price


    def action_refuse(self):
        self.status = 'refused'

    # @api.constrains('selling_price')
    def _check_constraint(self):
        for estate in self:
            if estate.property_id.expected_price > estate.price:
                raise ValidationError(_("Sorry The offer can't be accepted because your accepted offer price is less than expected price"))