from django.db import models
class Note(models.Model):    
    title = models.CharField("Заголовок", max_length=200)    
    text = models.TextField("Текст", blank=True)    
    is_done = models.BooleanField("Выполнено", default=False)    
    created_at = models.DateTimeField("Создано", auto_now_add=True)    
    updated_at = models.DateTimeField("Изменено", auto_now=True)
    class Meta:        
        ordering = ["-created_at"]        
        verbose_name = "Заметка"        
        verbose_name_plural = "Заметки"
         
    def __str__(self):        
     return self.title
