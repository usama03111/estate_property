from odoo import http
from odoo.http import request
from odoo.addons.project.controllers.portal import CustomerPortal

class ProjectCustomPortal(CustomerPortal):


    def _get_my_tasks_searchbar_filters(self, project_domain=None, task_domain=None):
        searchbar_filters = super()._get_my_tasks_searchbar_filters(project_domain,task_domain)

        # extends filterby criteria with project_task_type has a relation field with project.project "stage_id" field the customer has access to
        stage_ids= request.env['project.task.type'].search([("user_id",'=',False)])
        for stage in stage_ids:
            searchbar_filters.update({
                str(stage.id): {'label': stage.name, 'domain': [('stage_id', '=', stage.id)]}
            })

        return searchbar_filters
