from django import forms
from .models import Note 
class NoteForm(forms.ModelForm):    
    class Meta:        
        model = Note        
        fields = ["title", "text", "is_done"]        
        widgets = {            
            "text": forms.Textarea(attrs={"rows": 5}),        
            }
