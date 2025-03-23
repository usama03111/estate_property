from email.policy import default

from  odoo import models , api , fields , _
from odoo.tools.populate import compute


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'test'
    _order = "sequence desc"

    sequence = fields.Integer(default=1)
    name = fields.Char(string='Name')
    property_ids = fields.One2many('estate.property','property_type_id')
    offer_ids = fields.One2many('estate.property.offer' , 'property_offer_id')
    offer_count = fields.Integer(compute='_compute_offer_count')
    property_count = fields.Integer(compute='_compute_property_count')


    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for vals in vals_list:
            self.env["estate.property.tag"].create({
                "name": vals.get('name'),
            })
        return res

    def unlink(self):
        self.property_ids.state = "canceled"
        return super().unlink()

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for rec  in self:
            rec.offer_count = len(rec.offer_ids) if rec.offer_ids else 0

    @api.depends("property_ids")
    def _compute_property_count(self):
        for rec in self:
            rec.property_count = len(rec.property_ids) if rec.property_ids else 0


    def action_open_property_ids(self):
        return {
            "name":_("Related Properties"),
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "estate.property",
            "target": "current",
            "domain": [("property_type_id" , "=" , self.id)],
            "context": {"default_property_type_id": self.id}
        }