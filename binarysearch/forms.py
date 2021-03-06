from django.db.models import Q
from simple_search import BaseSearchForm
from myapp.models import MyModel, MyCategory


class MyModelSearchForm(BaseSearchForm):
    class Meta:
        base_qs = MyModel.objects
        search_fields = ('^name', 'description', 'specifications', '=id') 

        # assumes a fulltext index has been defined on the fields
        # 'name,description,specifications,id'
        fulltext_indexes = (
            ('name', 2), # name matches are weighted higher
            ('name,description,specifications,id', 1),
        )

    """ 
    A custom addition - the absence of a prepare_category method means
    the query will search for an exact match on this field.
    """
    category = forms.ModelChoiceField(
        queryset = MyCategory.objects.all(),
        required = False
    )

    """ 
    This field creates a custom query addition via the prepare_start_date
    method.
    """
    start_date = forms.DateField(
        required = False,
        input_formats = ('%Y-%m-%d',),
    )
    def prepare_start_date(self):
        if self.cleaned_data['start_date']:
            return Q(creation_date__gte=self.cleaned_data['start_date'])
        else:
            return "