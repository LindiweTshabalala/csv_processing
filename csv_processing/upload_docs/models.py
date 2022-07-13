from django.db import models

class Document(models.Model):
    doc_text = models.CharField(max_length=200)

    def __str__(self):
        return self.doc_text

