from fastapi import Form, File, UploadFile
from pydantic import BaseModel


# https://stackoverflow.com/a/60670614
"""
Schemas is a great approach to working with FastAPI applications with Jinga2 Templates. For example, expected input fields for a form can be stored in a 'schema'.
This can prevents large blocks of code when working with large input forms.
"""
# Author: Viraj Vaitha
## TO DO: Allow multiple images?

# Import Libaries

# 1. unsupervised learning examples app router contains input field for images and k clusters.


class SegmentationForm(BaseModel):
    k_cluster: int
   
    file: UploadFile

    @classmethod
    def as_form(
        cls,
        k_cluster: int = Form(...),
        file: UploadFile = File(...)
    ):
        return cls(
            k_cluster = k_cluster,
            file=file
        )