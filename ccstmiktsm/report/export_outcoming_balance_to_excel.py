from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.ccstmiktsm.export_outcoming_balance_excel'
    _inherit = 'report.report_xlsx.abstract'
    report_date = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, outcoming_balance):
        sheet = workbook.add_worksheet('Daftar Pengeluaran')
        sheet.write(0, 0, str(self.report_date))
        sheet.write(1, 0, 'Kode')
        sheet.write(1, 1, 'Keterangan')
        sheet.write(1, 2, 'Tanggal')
        sheet.write(1, 3, 'Jumlah Nominal')
        sheet.write(1, 4, 'Periode')

        row = 2
        col = 0
        for obj in outcoming_balance:
            col = 0
            sheet.write(row, col, obj.outcome_code)
            sheet.write(row, col + 1, obj.name)
            sheet.write(row, col + 2, str(obj.date_out))
            sheet.write(row, col + 3, obj.new_outcome)
            sheet.write(row, col + 4, obj.balance_id.name)


            row += 1