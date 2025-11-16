from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost, BlogCategory

def blog_list(request):
    """Display all published blog posts"""
    category_slug = request.GET.get('category')
    
    posts = BlogPost.objects.filter(is_published=True)
    
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        posts = posts.filter(category=category)
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = BlogCategory.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
    """Display single blog post"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    recent_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:5]
    
    context = {
        'post': post,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/blog_detail.html', context)

# CRUD Operations
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def blog_post_create(request):
    """Create a new blog post"""
    if request.method == 'POST':
        from .forms import BlogPostForm
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog:blog_detail', slug=post.slug)
    else:
        from .forms import BlogPostForm
        form = BlogPostForm()
    
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def blog_post_update(request, slug):
    """Update an existing blog post"""
    post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    
    if request.method == 'POST':
        from .forms import BlogPostForm
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog:blog_detail', slug=post.slug)
    else:
        from .forms import BlogPostForm
        form = BlogPostForm(instance=post)
    
    return render(request, 'blog/blog_form.html', {'form': form, 'post': post})

@login_required
def blog_post_delete(request, slug):
    """Delete a blog post"""
    post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog:blog_list')
    
    return render(request, 'blog/blog_confirm_delete.html', {'post': post})
