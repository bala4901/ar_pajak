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


from osv import fields, osv


class jenis_setor_pajak(osv.osv):
    _name = 'pajak.jenis_setor_pajak'
    _description = 'Jenis Setor Pajak'
    
    def default_active(self, cr, uid, context={}):
    	return True

    _columns = {
							'name' : fields.char(string='Jenis Setor Pajak', size=100, required=True),					
							'code' : fields.char(string='Kode', size=30, required=True),
                            'akun_pajak_id' : fields.many2one(string='Akun Pajak', obj='pajak.akun_pajak', required=True),
							'active' : fields.boolean(string='Active'),
							'description' : fields.text(string='Description'),
    						}
    						
    _defaults = {
							'active' : default_active,
    						}


jenis_setor_pajak()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
	




