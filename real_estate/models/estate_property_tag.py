from pkg_resources import require

<<<<<<< HEAD
from odoo import fields, models , api
=======
from odoo import fields, models
>>>>>>> 05b39e2e21064740b2093465314b30c8cdd717a6

class EstateOffer(models.Model):
    _name = "estate.property.tag"
    # _inherit = "estate.mixin"
    _description = "Tags Of Real Estate Model"
    _sql_constraints = [
        ("unique_tag_name","UNIQUE(name)","Tag name should be unique")
    ]

    name = fields.Char(required=True)
    color = fields.Integer()

