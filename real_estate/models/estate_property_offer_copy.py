from pkg_resources import require

from odoo import fields, models

class EstateOffer(models.Model):
    _inherit = "estate.property.offer"


    account_move_id = fields.Many2one('account.move')

