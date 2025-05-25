
from odoo import  api , fields , models

class EstateProperty(models.AbstractModel):
    _name = "report.real_estate.report_property_detail"

    def _get_report_values(self, docids, data=None):
        domain = []
        name = data.get('get_data').get("name")
        # from_date = data.get('get_data').get("from_date")
        # date_to = data.get('get_data').get("date_to")

        if name:
            domain += [('name', '=', name[1])]

        user_id = self.env['estate.property'].search(domain)
        property_data = []

        for house in user_id:
            vals = {
                'name': house.name,
                'property_type': house.property_type_id.name,
                'best_offer': house.best_offer,
                'selling_price': house.selling_price,
                'date_availability': house.date_availability,
            }
            property_data.append(vals)
        for offer in house.offer_ids:
            property_data.append({
                'partner_name': offer.partner_id.name,
                'offer_price': offer.price,
                'offer_status': offer.status,
            })
        print("property_data", property_data)
        return {
            'doc_ids': docids,
            'doc_model': 'estate.property',
            'data': data,
            'property_data': property_data,

        }
