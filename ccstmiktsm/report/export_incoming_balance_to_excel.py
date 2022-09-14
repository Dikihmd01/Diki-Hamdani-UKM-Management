from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.ccstmiktsm.export_incoming_balance_excel'
    _inherit = 'report.report_xlsx.abstract'
    report_date = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, incoming_balance):
        sheet = workbook.add_worksheet('Daftar Surat Masuk')
        sheet.write(0, 0, str(self.report_date))
        sheet.write(1, 0, 'Kode')
        sheet.write(1, 1, 'Keterangan')
        sheet.write(1, 2, 'Tanggal')
        sheet.write(1, 3, 'Jumlah Nominal')
        sheet.write(1, 4, 'Periode')

        row = 2
        col = 0
        for obj in incoming_balance:
            col = 0
            sheet.write(row, col, obj.income_code)
            sheet.write(row, col + 1, obj.name)
            sheet.write(row, col + 2, str(obj.date_in))
            sheet.write(row, col + 3, obj.new_income)
            sheet.write(row, col + 4, obj.balance_id.name)


            row += 1