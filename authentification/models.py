from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models  # Use gis models for geographic fields
from django.utils.translation import gettext_lazy as _  # For translations if needed

class Alert(models.Model):
    TYPES = [
        ('flood', _('خطر الفيضانات')),
        ('climatic', _('خطر مناخي')),
        ('animal_health', _('مخاطر مرتبطة بصحة الحيوان والنبات')),
        ('human_health', _('مخاطر مرتبطة بصحة الإنسان')),
        ('gatherings', _('الأماكن التي يحتمل أن تتأثر بالتجمعات البشرية الهامة')),
        ('forest_fire', _('حرائق الغابات')),
        ('pollution', _('خطر تلوث')),
        ('earthquake', _('الزلزال والمخاطر الجيولوجية')),
        ('nuclear', _('أخطار الاشعاعات النووية')),
        ('industrial', _('أخطار صناعية وطاقوية')),
        ('other', _('مخاطر أخرى')),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    alert_type = models.CharField(max_length=50, choices=TYPES)
    address = models.CharField(max_length=255)  
    alert_image = models.ImageField(upload_to='alert_images/', blank=True, null=True)
    location = models.PointField(geography=True, srid=4326, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert: {self.alert_type} by {self.user.username} at {self.location}"