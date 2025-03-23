from pkg_resources import require

from odoo import fields, models

class EstateOffer(models.Model):
    _name = "estate.property.tag"
    # _inherit = "estate.mixin"
    _description = "Tags Of Real Estate Model"
    _sql_constraints = [
        ("unique_tag_name","UNIQUE(name)","Tag name should be unique")
    ]

    name = fields.Char(required=True)
    color = fields.Integer()

