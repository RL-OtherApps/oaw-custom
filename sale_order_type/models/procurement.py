# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015-2016 Rooms For (Hong Kong) Limited T/A OSCG
#    <https://www.odoo-asia.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp import models, fields, api
from openerp import SUPERUSER_ID


class ProcurementOrder(models.Model):
    _inherit = "procurement.order"


    @api.model
    def _update_so_line(self, res):
        purchase_line_id = res[self.ids[0]]
        sale_line_id = self.move_dest_id.procurement_id.sale_line_id.id
        self.env['sale.order.line'].browse([sale_line_id])[0].sudo(SUPERUSER_ID).write({'purchase_line_id': purchase_line_id})


    @api.multi
    def make_po(self):
        res = super(ProcurementOrder, self).make_po()
        self._update_so_line(res)
        return res
