from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
from odoo.addons.base_vat.models import res_partner



class ResPartner(models.Model):
    _inherit = 'res.partner'

    ar_name = fields.Char(string="Name")
    ar_street = fields.Char(string="Street")
    ar_street2 = fields.Char(string="Strre2")
    ar_city = fields.Char(string="City")
    ar_zip = fields.Char(string="Zip")
    ar_state = fields.Char(string="State")
    ar_l10n_sa_edi_building_number = fields.Char(string="Building nu")
    ar_l10n_sa_edi_plot_identification = fields.Char(string="Identification no")
    ar_country = fields.Char(string="Country")
    ar_country_code = fields.Char(string="Country Code")


class AccountMove(models.Model):
    _inherit = 'account.move'


    qr_image = fields.Binary(string="QR Image")