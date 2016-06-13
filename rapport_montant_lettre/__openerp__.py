# -*- encoding: utf-8 -*-

{
    'name': 'Factures-Commandes avec le montant en lettres en Francais(qweb)',
    'version': '1.0',
    'depends': ['account'],
    "author" : "Othmane GHANDI, OSI Soft",
    "website" : "http://www.odoo.gotodoo.com",
    'description': "Ce module permet de  convertir le montant des factures et des Bons de commande  en lettres (en Francais) dans le rapport pdf",
    'category': 'Generic Modules/Accounting',
    'depends' : [
                    'account','sale',
                ],
    'data' : [
              'views/report_invoice.xml',
              'views/report_saleorder.xml',
              'report.xml',
               ],
     
  
    'application': True,
    'installable': True

}


