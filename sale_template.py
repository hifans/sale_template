#-*- coding:utf-8 -*-
##############################################################################
#
#    Powered By Rainsoft(QingDao) Author:Kevin Kong 2014 (kfx2007@163.com)
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
#
##############################################################################

from openerp import fields,models,api,_

class sale_template(models.Model):
		_name='sale_template.template'

		name = fields.Char('name')
                products = fields.One2many('sale_template.line',"template_id")


class sale_template_line(models.Model):
		_name='sale_template.line'

                template_id = fields.Many2one('sale_template.template')
                product = fields.Many2one('product.product','Product')
                quantity = fields.Integer('Quantity')

class sale_order(models.Model):
    _inherit='sale.order'

    sale_template = fields.Many2one('sale_template.template','Sale Template')

    @api.one
    def btn_import(self):
        for product in self.sale_template.products:
            self.env['sale.order.line'].create({
                'order_id':self.id,
                'product_id':product.product.id,
                'product_uom_qty':product.quantity,
                })
            

		
