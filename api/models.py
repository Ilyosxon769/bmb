from django.db import models


class ImportExcel(models.Model):
    fexcel=models.FileField(upload_to='excel/%Y/%m/%d')
    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.fexcel.storage, self.fexcel.path
        # Delete the model before the file
        super(ImportExcel, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)
