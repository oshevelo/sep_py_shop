from rest_framework import serializers

from apps.catalog.models import Category


class CategorySerializer(serializers.ModelSerializer):
    # TBD How to add nested top categories ?
    class Meta:
        model = Category

        fields = ('id', 'category_name', 'top_category', 'sub_category')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['sub_category'] = CategorySerializer(many=True)

        return fields
