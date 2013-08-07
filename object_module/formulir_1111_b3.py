# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp.osv import fields, osv, orm
import openerp.addons.decimal_precision as dp
from openerp import netsvc
from openerp import pooler
from datetime import datetime

class formulir_1111_b3(osv.osv):
	_name = 'pajak.formulir_1111_b3'
	_description = 'Formulir  1111 B3'
	_inherit = ['mail.thread']
	
	def default_state(self, cr, uid, context={}):
		return 'draft'
		
	def default_name(self, cr, uid, context={}):
		return '/'
		
	def default_created_time(self, cr, uid, context={}):
		#TODO: Ticket #5
		return False
		
	def default_created_user_id(self, cr, uid, context={}):
		#TODO: Ticket #6
		return False

	
			
	
	_columns = 	{
								'name' : fields.char(string='# SPT', size=30, required=True, readonly=True),

                                

								'state' : fields.selection([('draft','Draft'),('confirm','Waiting For Approval'),('approve','Ready To Process'),('done','Done'),('cancel','Cancel')], 'Status', readonly=True),
								'created_time' : fields.datetime(string='Created Time', readonly=True),
								'created_user_id' : fields.many2one(string='Created By', obj='res.users', readonly=True),
								'confirmed_time' : fields.datetime(string='Confirmed Time', readonly=True),
								'confirmed_user_id' : fields.many2one(string='Confirmed By', obj='res.users', readonly=True),						
								'approved_time' : fields.datetime(string='Approved Time', readonly=True),
								'approved_user_id' : fields.many2one(string='Approved By', obj='res.users', readonly=True),		
								'processed_time' : fields.datetime(string='Processed Time', readonly=True),
								'processed_user_id' : fields.many2one(string='Process By', obj='res.users', readonly=True),				
								'cancelled_time' : fields.datetime(string='Processed Time', readonly=True),
								'cancelled_user_id' : fields.many2one(string='Process By', obj='res.users', readonly=True),																								
								'cancelled_reason' : fields.text(string='Cancelled Reason', readonly=True),
								}	
				
	_defaults =	{
							'name' : default_name,
							'state' : default_state,
							'created_time' : default_created_time,
							'created_user_id' : default_created_user_id,
							}

	def workflow_action_confirm(self, cr, uid, ids, context={}):
		for id in ids:
			self.write(cr, uid, [id], {'state' : 'confirm'})
		return True

	def workflow_action_approve(self, cr, uid, ids, context={}):
		for id in ids:
			self.write(cr, uid, [id], {'state' : 'approve'})
		return True			
		
	def workflow_action_done(self, cr, uid, ids, context={}):
		for id in ids:
			self.write(cr, uid, [id], {'state' : 'done'})
		return True		
		
	def workflow_action_cancel(self, cr, uid, ids, context={}):
		for id in ids:
			self.write(cr, uid, [id], {'state' : 'cancel'})
		return True		
		


		
	def button_action_set_to_draft(self, cr, uid, ids, context={}):
		for id in ids:
			if not self.delete_workflow_instance(self, cr, uid, id):
				return False

			if not self.create_workflow_instance(self, cr, uid, id):
				return False
				
		return True

		
        def button_action_cancel(self, cr, uid, ids, context={}):
                wkf_service = netsvc.LocalService('workflow')
                for id in ids:
                                if not self.delete_workflow_instance(self, cr, uid, id):
                                        return False

                                if not self.create_workflow_instance(self, cr, uid, id):
                                        return False

                                wkf_service.trg_validate(uid, 'pajak.formulir_1111_b3', id, 'button_cancel', cr)

                return True

        def log_audit_trail(self, cr, uid, id, event):
                #TODO: Ticket #12
                return True

        def delete_workflow_instance(self, cr, uid, id):
                #TODO: Ticket #13
                return True

        def create_workflow_instance(self, cr, uid, id):
                #TODO: Ticket #14
                return True

		
		

formulir_1111_b3()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: