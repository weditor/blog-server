
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


