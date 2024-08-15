from django import forms

from fruitipedia.fruits.models import Fruit, Category


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {"name": forms.TextInput(attrs={"placeholder": "Category name", })}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ""


class CategoryCreateForm(CategoryBaseForm):
    pass


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Fruit name"}),
            "image": forms.URLInput(attrs={"placeholder": "Image url"}),
            "description": forms.TextInput(attrs={"placeholder": "Description"}),
            "nutrition": forms.NumberInput(attrs={"placeholder": "Nutrition"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ""


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(FruitBaseForm):
    pass

