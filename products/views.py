from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


# Create your views here.


def all_products(request):
    """ A view for all products,sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                            request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
         
            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            products = products.filter(queries)
       
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_single(request, product_id):
    """ view showing  individual product """

    product = get_object_or_404(Product, pk=product_id)
    review_id = get_object_or_404(Product, pk=product_id)
    review = Review.objects.filter(product=review_id)
    form = ReviewForm()

    context = {
        'product': product,
        'review': review,
        'form': form,
        'reviews': review,
    }

    return render(request, 'products/product_single.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_single', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully updated product!')
        else:
            messages.error(request, 'Failed to update product. Try again.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """
    A view to allow the user to add a review to a product
    """
    print('review view')
    if request.user.is_authenticated:
        if request.method == 'POST':

            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                product = Product.objects.get(pk=product_id)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, 'Your review was successful')
                return redirect(reverse('product_single', args=[product.id]))
            else:
                messages.error(request, 'Failed to add your review')
        else:
            form = ReviewForm()
            print(form)

        context = {
            'form': form,
            }
        return redirect(reverse('product_single', args=[product_id]), context)
    

@login_required
def edit_review(request, review_id):
    """ Edit a review  """

    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
        else:
            messages.error(request, 'Failed to update review. Try again.')
    else:
        form = ReviewForm(instance=review)

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'review': review,
        'edit': True,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete review """

    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.user:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('products'))
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('products'))
