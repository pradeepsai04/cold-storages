from django import forms
from .models import dest

class destform(forms.ModelForm):
    class Meta:
        model=dest
        fields=("OWNER_NAME","COST","UPLOAD_HOUSE_IMAGE","UPLOAD_HOUSE_IMAGE2","UPLOAD_HOUSE_IMAGE3","ADDRESS","ADDRESS_URL","ENTER_LOCATION","AREA","STATE")
