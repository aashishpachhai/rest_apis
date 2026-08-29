import django_filters
from employee.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(field_name='name',lookup_expr='iexact')
    address=django_filters.CharFilter(field_name='address',lookup_expr='icontains')
    id=django_filters.RangeFilter(field_name='id') # works only with the  field int field
    min_emp_id=django_filters.CharFilter(method='get_Range', label='Min Employee ID')
    max_emp_id=django_filters.CharFilter(method='get_Range',label='Max Employee Id')
    class Meta:
        model=Employee
        fields=['name','address','id','min_emp_id','max_emp_id']

    def get_Range(self,queryset,name,value):
        if name=='min_emp_id':
            return queryset.filter(emp_id__gte=value)
        elif name=='max_emp_id':
            return queryset.filter(emp_id__lte=value)
        else:
            return queryset