
from rest_framework.filters import BaseFilterBackend


class CommonFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_fields = getattr(view, 'filter_fields', [])
        kw = {}
        for k, v in request.query_params.items():
            if k not in filter_fields or not v.strip():
                continue
            kw[k.strip()] = v.strip()
        return queryset.filter(**kw)


class SortFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        sorted = getattr(view, 'sort_by', [])
        sort_fields = getattr(view, 'sort_fields', [])
        args = []
        for field in request.query_params.get('sort_by', '').split(','):
            field = field.strip()
            if not field:
                continue
            if sort_fields and field.rstrip('-') not in sort_fields:
                continue
            args.append(field)
        return queryset.order_by(*args)

