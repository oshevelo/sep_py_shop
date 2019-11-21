from rest_framework import serializers

from apps.catalog.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = ('id', 'category_name', 'top_category', 'sub_category')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['sub_category'] = CategorySerializer(many=True)

        return fields

    def create(self, validated_data):
        sub_categories_data = validated_data.pop('sub_category')
        category = Category.objects.create(**validated_data)
        for sub_category_data in sub_categories_data:
            # How to solve error Error in formatting: RecursionError: maximum recursion depth exceeded
            # create() got multiple values for keyword argument 'top_category'
            Category.objects.create(top_category=category, **sub_category_data)
        return category
