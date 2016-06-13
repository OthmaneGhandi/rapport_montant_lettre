# -*- encoding: utf-8 -*-


import convertion
from openerp import api
from openerp.osv import osv


class sale_order(osv.osv):
    
    _inherit = "sale.order"

    def print_quotation(self, cr, uid, ids, context=None):
        '''
        This function prints the sales order and mark it as sent, so that we can see more easily the next step of the workflow
        '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        self.signal_workflow(cr, uid, ids, 'quotation_sent')
        return self.pool['report'].get_action(cr, uid, ids, 'rapport_montant_lettre.report_saleorder', context=context)

    @api.multi
    @api.depends('amount_total')
    def get_amount_letter(self):
        amount = convertion.trad(self.amount_total,'DH')
        amount = amount + '  TTC'
        return amount

