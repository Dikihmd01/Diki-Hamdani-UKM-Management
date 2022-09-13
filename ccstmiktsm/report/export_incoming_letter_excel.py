from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.ccstmiktsm.export_incoming_excel'
    _inherit = 'report.report_xlsx.abstract'
    report_date = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, incoming_letters):
        sheet = workbook.add_worksheet('Daftar Surat Masuk')
        sheet.write(0, 0, str(self.report_date))
        sheet.write(1, 0, 'Kode')
        sheet.write(1, 1, 'Keterangan')
        sheet.write(1, 2, 'Nama Organisasi')
        sheet.write(1, 3, 'Nama Pengirim')
        sheet.write(1, 4, 'Tanggal')
        sheet.write(1, 5, 'Nama Penerima')
        sheet.write(1, 6, 'Status')

        row = 2
        col = 0
        for obj in incoming_letters:
            col = 0
            sheet.write(row, col, obj.incoming_code)
            sheet.write(row, col + 1, obj.name)
            sheet.write(row, col + 2, obj.letter_from)
            sheet.write(row, col + 3, obj.sender_name)
            sheet.write(row, col + 4, obj.date_incoming)
            sheet.write(row, col + 5, obj.received_by)
            sheet.write(row, col + 6, obj.state)

            row += 1