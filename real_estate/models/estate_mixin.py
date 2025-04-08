from pkg_resources import require

from odoo import fields, models

class EstateMixin(models.Model):
    _name = "estate.mixin"
    _description = 'Estate Mixin'

    """Prototype inherit is used to remove the code reusability so we inherit these inside the
    # estate_tag model """

    name = fields.Char(required = True)
