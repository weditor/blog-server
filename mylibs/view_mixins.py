
class PrivateQueryMixin:
    def get_queryset(self):
        queryset = super(PrivateQueryMixin, self).get_queryset()
        if not self.request.user or not self.request.user.is_authenticated:
            queryset = queryset.filter(is_private=False)
        return queryset

