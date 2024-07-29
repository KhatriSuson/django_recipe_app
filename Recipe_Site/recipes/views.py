from django.shortcuts import render, redirect, get_object_or_404
from recipes.models import Recipe
from recipes.froms import RecipeForm

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "list.html", {'recipes':recipes})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
        
    else:
        form = RecipeForm()
    return render(request, 'form.html', {'form':form})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "detail.html", {'recipe': recipe})

def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'form.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, "delete.html", {'recipe':recipe})


