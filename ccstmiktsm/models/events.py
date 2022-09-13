from odoo import api, fields, models


class Events(models.Model):
    _name = 'ccstmiktsm.event'
    _description = 'Acara'

    DIVISION_OPTIONS = [
        ('SE', 'Software Engineer'),
        ('PD', 'Product Design'),
        ('BA', 'Business Analyst'),
        ('ccpasif', 'CC Pasif'),
        ('external', 'External'),
    ]

    STATE_OPTIONS = [
        ('diajukan', 'Diajukan'),
        ('diterima', 'Diterima'),
        ('dijadwalkan', 'Dijadwalkan'),
        ('selesai', 'Selesai'),
        ('dibatalkan', 'Dibatalkan'),
    ]

    name = fields.Char(string='Nama Kegiatan')
    event_code = fields.Char(
        string='Kode Kegiatan',
        readonly=True,
        copy=False,
        required=True,
        default='New'
    )
    event_type_id = fields.Many2one(
        comodel_name='ccstmiktsm.eventtype',
        string='Jenis Kegiatan',
        required=True
    )
    state = fields.Selection(
        string='Status',
        selection=STATE_OPTIONS,
        default='diajukan'
    )
    
    speaker = fields.Char(
        string='Pemateri',
        required=True
    )
    division_of_speaker = fields.Selection(
        string='Asal pemateri',
        selection=DIVISION_OPTIONS,
        required=True
    )
    event_date = fields.Date(
        string='Tanggal',
        default=fields.Datetime.now()
    )
    place = fields.Char(string='Tempat')
    
    @api.model
    def create(self, vals):
        if vals.get('event_code', 'New') == 'New':
            vals['event_code'] = self.env['ir.sequence'].next_by_code(
                'ccstmiktsm.event' or 'New')

        result = super(Events, self).create(vals)
        return result
    
    def action_proposed(self):
        self.write({
            'state': 'diajukan'
        })
    
    def action_approved(self):
        self.write({
            'state': 'diterima'
        })
    
    def action_scheduled(self):
        self.write({
            'state': 'dijadwalkan'
        })
    
    def action_done(self):
        self.write({
            'state': 'selesai'
        })
    
    def action_canceled(self):
        self.write({
            'state': 'dibatalkan'
        })
