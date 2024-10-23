from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage
from PIL import Image, ImageFilter

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            processed_image = apply_filters(uploaded_image.image.path)
            uploaded_image.processed_image = processed_image
            uploaded_image.save()
            return render(request, 'display_image.html', {'image': uploaded_image})
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def apply_filters(image_path):
    scales = ['L', 'RGB', 'CMYK']
    for scale in scales:
        img = Image.open(image_path).convert(scale)
        processed_path = 'path/to/save/processed_image_'+scale+'.jpg'
        img.save(processed_path)
    return processed_path
