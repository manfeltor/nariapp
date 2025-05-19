import datetime
from django.utils.text import slugify

def plant_image_upload_path(instance, filename):
    today = datetime.date.today().strftime("%Y%m%d")
    code = instance.code or "unknown"
    ext = filename.split('.')[-1].lower()
    return f"images/plants/{code}-{today}.{ext}"
