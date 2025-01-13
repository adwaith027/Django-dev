from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse
from .forms import ProfileForm

def create_profile(request):
    form=ProfileForm()
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return HttpResponse('file type you uploaded is not supported')
            user_pr.save()
            return HttpResponse('file uploaded successfully')
    context = {"form": form,}
    return render(request, 'createfileupload.html', context)