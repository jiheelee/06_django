from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.

def main(request):
    movies = Movie.objects.all()
    return render(request, "movie/list.html",{'movies':movies})
    
def create(request):
    if request.method == "POST":
        #사용자가 작성한 데이터를 보내는 작업
        title = request.POST.get("title")
        audience = request.POST.get("audience")
        genre = request.POST.get("genre")
        score = request.POST.get("score")
        poster_url = request.POST.get("poster_url")
        description = request.POST.get("description")
        
        Movie.objects.create(title=title,audience=audience,genre=genre,score=score,poster_url=poster_url,description=description)
        return redirect('movies:main')
    else: #GET
        pass
        #사용자가 데이터를 작성할 html을 보여줌
    return render(request,"movie/new.html")
def detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request,"movie/detail.html",{"movie":movie})
    
def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "post":
        title = request.POST.get("title")
        audience = request.POST.get("audience")
        genre = request.POST.get("genre")
        score = request.POST.get("score")
        poster_url = request.POST.get("poster_url")
        description = request.POST.get("description")
        
        movie.title = title
        movie.audience = audience
        movie.genre = genre
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description
        
        movie.save()
        
        return redirect("movie:detail", id)
    else:
        pass
    return render(request, 'movie/update.html', {'movie':movie})
    
def delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    
    return redirect("movie:list")
        