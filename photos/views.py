
from django.shortcuts import render
from .models import Image,Location,Category
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=='POST':
        category = request.POST.get("imagesearch")
        print(category.lower())
        category_id=Category.search_by_category(category.lower())
        searched_images = Image.search_by_category(category_id)
        message = f"{category}"
        print(searched_images)
        return render(request, 'all-photos/search_results.html', {"message": message, "images": searched_images})
    else:
       images = Image.objects.all()
       locations = Location.get_locations()
       print(locations)
    return render(request, 'all-photos/index.html', {'images': images[::-1], 'locations': locations})
  

def image_location(request,location_name):
    images = Image.filter_by_location(location_name)
    print(images)
    return render(request, 'all-photos/locations.html',{'location_images': images})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'all-photos/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'all-photos/search_results.html', {"message": message})