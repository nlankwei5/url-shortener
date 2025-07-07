from django.db import models


class urlShortener(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-time_created"]
    
    def __str__(self):
        return f"{self.original_url} to {self.short_url}"
    
    
