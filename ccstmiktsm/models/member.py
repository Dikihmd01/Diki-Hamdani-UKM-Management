from email.policy import default
from odoo import api, fields, models


class Member(models.Model):
    _inherit = 'res.partner'
    _description = 'Anggota'

    DIVISION_OPTIONS = [
        ('SE', 'Software Engineer'),
        ('PD', 'Product Design'),
        ('BA', 'Business Analyst'),
    ]

    MAJOR_OPTIONS = [
        ('s1teknik_informatika', 'S1 - Teknik Informatika'),
        ('d3teknik_informatika', 'D3 - Teknik Informatika'),
        ('d3tkj', 'D3 - TKJ'),
    ]

    npm = fields.Char(string='NPM')
    major = fields.Selection(
        string='Jurusan',
        selection=MAJOR_OPTIONS,
        default='s1teknik_informatika'
    )
    division = fields.Selection(
        string='Divisi',
        selection=DIVISION_OPTIONS,
        default='SE'
    )
    state = fields.Selection(
        string='Status',
        selection=[
            ('aktif', 'Aktif'),
            ('pasif', 'Pasif'),
            ('keluar', 'keluar')
        ],
        default='aktif',
        required=True
    )
    batch = fields.Char(string='Angkatan')

