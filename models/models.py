# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import io
import base64

class exoplanet(models.Model):
    _name = 'exoplanet.planets'
    _description = 'exoplanet.exoplanet'

    koi_name = fields.Char(string="Koi Name")
    koi_disposition = fields.Char(string="Koi Disposition")
    koi_insol = fields.Char(string="Koi Insol")
    koi_prad = fields.Char(string="Koi Prad")

    #name = fields.Char(string='Descripción')
    #unit_price = fields.Char(string='Precio unitario')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class UploadFile(models.TransientModel):
    _name = 'exoplanet_upload_file'

    upload_file = fields.Binary(string='Upload file', required=True)
    file_name = fields.Char(string='File name')

    def import_file(self):
        if self.file_name:
            if '.csv' not in self.file_name:
                raise exceptions.ValidationError('El archivo debe ser un CSV')
            file = self.read_file_from_binary(self.upload_file)
            lines = file.split('\n')
            for line in lines:
                elements = line.split(',')
                if len(elements) > 1:
                    self.env['exoplanet.planets'].create({
                        #'koi_name': elements[1],
                        #'koi_disposition': elements[3],
                        #'koi_insol': elements[31],
                        #'koi_prad': elements[25],
                        'koi_name': elements[0],
                        'koi_disposition': elements[1],
                        'koi_insol': elements[2],
                        'koi_prad': elements[3],
                    })

    def read_file_from_binary(self, file):
        try:
            with io.BytesIO(base64.b64decode(file)) as f:
                f.seek(0)
                return f.read().decode('UTF-8')
        except Exception as e:
            print(str(e))
            raise e