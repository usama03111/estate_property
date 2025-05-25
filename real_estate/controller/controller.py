from odoo import http, _
from odoo.http import request
from collections import OrderedDict
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.portal.controllers import portal
from odoo.osv.expression import OR


class RealEstate(http.Controller):

    def _get_search_domain(self, search_in, search):
        domain = []
        if search_in == 'home':
            domain = ['|', ('name', 'ilike', search), ('description', 'ilike', search)]
        elif search_in == 'all':
            domain = ['|', ('name', 'ilike', search), ('description', 'ilike', search)]
        return domain


    @http.route("/realestate/", auth="public", website=True)
    def display_estate_property(self, sortby=None, filterby=None, search=None, search_in='all', **kw):
        searchbar_sortings = {
            'date': {'label': _('Date Availability'), 'order': 'date_availability asc'},
            'name': {'label': _('Name'), 'order': 'name'},
        }
        if not sortby:
            sortby = 'date'
            print(" not order", sortby)
        order = searchbar_sortings[sortby]['order']
        print("order", order)

        searchbar_filters = {'all': {'label': _('All Homes'), 'domain': []},
                             'apartment': {'label': _('Apartment'),
                                           'domain': [("property_type_id.name", '=', "Appartment xml")]},
                             'accepted': {'label': _('Accepted'),
                                          'domain': [("state", "=", "accepted")]}, }
        if not filterby:
            filterby = 'all'
        domain = searchbar_filters[filterby]['domain']
        if search and search_in:
            domain+= self._get_search_domain(search_in , search)

        searchbar_inputs = {
            'all': {'input': 'all', 'label': _('Search in All'), 'order': 1},
            'homes': {'input': 'home', 'label': _('Search in Homes'), 'order': 1}}

        propertys = http.request.env['estate.property'].search(domain, order=order)

        return http.request.render("real_estate.portal_my_estate_property",
                                   {"propertys": propertys,
                                    "page_name": "estate_property",
                                    'searchbar_sortings': searchbar_sortings,
                                    'sortby': sortby,
                                    'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
                                    'filterby': filterby,
                                    'search_in': search_in,
                                    'search': search,
                                    'searchbar_inputs': searchbar_inputs,
                                    'default_url': "/realestate/", })

    @http.route("/realestate/property/<model('estate.property'):name>/", auth="public", website=True)
    def display_estate_property_detail(self, name):
        return http.request.render("real_estate.estate_property_detail",
                                   {"name": name,
                                    "page_name": "estate_property_detail",})




class RealEstatePortal(CustomerPortal):
    # def _prepare_home_portal_values(self, counters):
    #     values = super(RealEstatePortal, self)._prepare_home_portal_values(counters)
    #     property_count = http.request.env['estate.property'].search_count([])
    #     values.update({
    #         "count": property_count,
    #     })
    #     return values

    def _prepare_home_portal_values(self, counters):
        values = super(RealEstatePortal, self)._prepare_home_portal_values(counters)
        if 'realestate_count' in counters:  # Match the key used in template
            values['realestate_count'] = http.request.env['estate.property'].sudo().search_count([])
        return values