# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################

import re
from openerp import netsvc
from openerp.osv import osv, fields

class shipyard(osv.osv):
    """Shipyard"""
    
    _name = 'nautical.shipyard'
    _description = 'Shipyard'

    _columns = {
        'name': fields.char(string='Name', required=True),
    }

    _defaults = {
    }


    _constraints = [
    ]




shipyard()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
