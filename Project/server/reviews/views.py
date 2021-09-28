from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Review
from .forms import ReviewForm, CommentForm

from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden


@login_required
@require_POST
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()      
            return redirect('movies:movie_detail', movie.pk)

    else:
        form = ReviewForm()
    context = {
        'form': form,
        'title': movie.title,
        'movie': movie,
    }
    return render(request, 'community/create.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def review_list(request):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()      
            return redirect('movies:movie_detail', movie.pk)

    else:
        form = ReviewForm()
    context = {
        'form': form,
        'title': movie.title,
        'movie': movie,
    }
    return render(request, 'community/create.html', context)


    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@login_required
@require_GET
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user.is_authenticated:
        if request.user == review.user:
            review.delete()
            return redirect('community:index')
    return redirect('community:detail', review.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('community:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
    else:
        # return redirect('community:index')
        return HttpResponseForbidden()
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'community/update.html', context)


@require_POST
def review_score(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def review_keyword(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        # return HttpResponseForbidden()
    return redirect('community:detail', review_pk)



@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            liked = False
        else:
            review.like_users.add(user)
            liked = True

        liked_status = {
            'liked': liked,
            'likeCount': review.like_users.count()
        }
        return JsonResponse(liked_status)
    return HttpResponse(status=401)