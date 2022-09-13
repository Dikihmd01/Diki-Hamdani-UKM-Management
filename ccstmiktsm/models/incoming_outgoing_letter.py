from odoo import api, fields, models


class IncomingLetter(models.Model):
    _name = 'ccstmiktsm.incomingletter'
    _description = 'Surat Masuk'

    UKM_OPTIONS = [
        ('LFM', 'LFM'),
        ('Homeband', 'Homebans'),
        ('Mapalas', 'Mapalas'),
        ('FDK', 'FDK'),
        ('BEM', 'BEM'),
        ('Padus', 'Padus'),
        ('MB', 'Marching Band')
    ]

    STATE_OPTIONS = [
        ('draft', 'Draft'),
        ('terkirim', 'Terkirim'),
        ('selesai', 'Selesai'),
        ('dibatalkan', 'Dibatalkan'),
    ]

    name = fields.Char(string='Judul Surat')
    incoming_code = fields.Char(
        string='Kode Surat Masuk',
        readonly=True,
        copy=False,
        required=True,
        default='New'
    )
    letter_from = fields.Selection(
        string='Dari',
        selection=UKM_OPTIONS
    )
    sender_name = fields.Char(string='Nama Pengirim')
    date_incoming = fields.Date(
        string='Tanggal',
        default=fields.Datetime.now()
    )
    received_by = fields.Char(
        string='Nama Penerima',
        required=True
    )
    state = fields.Selection(
        string='State', 
        selection=STATE_OPTIONS,
        required=True,
        readonly=True,
        default='draft')
    archive = fields.Binary(string='Arsip')
    file_name = fields.Char(string='Nama File')
    

    @api.model
    def create(self, vals):
        if vals.get('incoming_code', 'New') == 'New':
            vals['incoming_code'] = self.env['ir.sequence'].next_by_code(
                'ccstmiktsm.incomingletter' or 'New'
            )

        result = super(IncomingLetter, self).create(vals)
        return result
    
    def action_draft(self):
        self.write({
            'state': 'draft'
        })
    
    def action_sent(self):
        self.write({
            'state': 'terkirim'
        })
    
    def action_done(self):
        self.write({
            'state': 'selesai'
        })
    
    def action_canceled(self):
        self.write({
            'state': 'dibatalkan'
        })
    

class OutcomingLetter(models.Model):
    _name = 'ccstmiktsm.outcomingletter'
    _description = 'Surat Keluar'

    
    UKM_OPTIONS = [
        ('LFM', 'LFM'),
        ('Homeband', 'Homebans'),
        ('Mapalas', 'Mapalas'),
        ('FDK', 'FDK'),
        ('BEM', 'BEM'),
        ('Padus', 'Padus'),
        ('MB', 'Marching Band')
    ]

    STATE_OPTIONS = [
        ('draft', 'Draft'),
        ('terkirim', 'Terkirim'),
        ('selesai', 'Selesai'),
        ('dibatalkan', 'Dibatalkan'),
    ]

    name = fields.Char(string='Judul Surat')
    outcoming_code = fields.Char(
        string='Kode Surat Keluar',
        readonly=True,
        copy=False,
        required=True,
        default='New'
    )
    destination = fields.Selection(
        string='Tujuan',
        selection=UKM_OPTIONS
    )
    sender_name = fields.Char(string='Nama Pengirim')
    date_outcoming= fields.Date(
        string='Tanggal',
        default=fields.Datetime.now()
    )
    received_by = fields.Char(
        string='Nama Penerima',
        required=True
    )
    state = fields.Selection(
        string='State', 
        selection=STATE_OPTIONS,
        required=True,
        readonly=True,
        default='draft')
    archive = fields.Binary(string='Arsip')
    file_name = fields.Char(string='Nama File')
    

    @api.model
    def create(self, vals):
        if vals.get('outcoming_code', 'New') == 'New':
            vals['outcoming_code'] = self.env['ir.sequence'].next_by_code(
                'ccstmiktsm.outcomingletter' or 'New'
            )

        result = super(OutcomingLetter, self).create(vals)
        return result
    
    def action_draft(self):
        self.write({
            'state': 'draft'
        })
    
    def action_sent(self):
        self.write({
            'state': 'terkirim'
        })

    def action_done(self):
        self.write({
            'state': 'selesai'
        })
    
    def action_canceled(self):
        self.write({
            'state': 'dibatalkan'
        })
