from odoo import api, fields, models


class EventTypes(models.Model):
    _name = 'ccstmiktsm.eventtype'
    _description = 'Jenis Kegiatan'

    name = fields.Char(string='Jenis Kegiatan')
    event_type_code = fields.Char(string='Kode Jenis Kegiatan',
                                readonly=True,
                                copy=False,
                                required=True,
                                default='New')
    description = fields.Char(string='Deskripsi Kegiatan')
    event_ids = fields.One2many(comodel_name='ccstmiktsm.event',
                                inverse_name='event_type_id',
                                string='Kegiatan')
    

    @api.model
    def create(self, vals):
        if vals.get('event_type_code', 'New') == 'New':
            vals['event_type_code'] = self.env['ir.sequence'].next_by_code(
                'ccstmiktsm.eventtype' or 'New'
            )

        result = super(EventTypes, self).create(vals)
        return result
    
