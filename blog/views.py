from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Category, Tag, Comment
from .forms import CommentForm  # Assuming you have a CommentForm defined

def home(request):
    posts = Post.objects.filter(status=Post.PUBLISHED).order_by('-created_at')
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, slug):
    # Get the post by slug and ensure it's published
    post = get_object_or_404(Post, slug=slug, status=Post.PUBLISHED)
    
    # Increment views count
    post.views += 1
    post.save()

    # Fetch related posts and approved comments
    related_posts = post.get_related_posts()
    # comments = post.comments.filter(approved=True)
    comments = post.comments.all()  # Get all comments (not just approved)


    # Handling comment submission via POST request
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Associate comment with post
            comment.author = request.user  # Associate comment with the logged-in user
            # comment.approved = True  # Automatically approve the comment
            comment.save()  # Save the comment
            print(f"New Comment: {comment.content}, Approved: {comment.approved}")
            return redirect('post_detail', slug=post.slug)  # Redirect to post detail after successful comment submission
    else:
        form = CommentForm()  # Initialize an empty form for GET request

    # Pass context to the template
    context = {
        'post': post,
        'related_posts': related_posts,
        'comments': comments,
        'form': form,  # Pass the form to the template
    }
    
    return render(request, 'blog/post_detail.html', context)

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.PUBLISHED).order_by('-created_at')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category_posts.html', context)

def tag_posts(request, name):
    tag = get_object_or_404(Tag, name=name)
    posts = tag.posts.filter(status=Post.PUBLISHED).order_by('-created_at')
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/tag_posts.html', context)

@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return JsonResponse({'likes_count': post.like_count()})

@login_required
def dislike_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
    return JsonResponse({'dislikes_count': post.dislike_count()})
