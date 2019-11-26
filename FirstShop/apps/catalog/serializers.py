from rest_framework import serializers

from apps.catalog.models import Category


class TopCategorySerializer(serializers.ModelSerializer):
    # TBD How to add nested top categories ?

    class Meta:
        model = Category

        fields = ('id',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = ('id', 'category_name', 'top_category', 'sub_category')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['sub_category'] = CategorySerializer(many=True, allow_null=True)
        fields['top_category'] = TopCategorySerializer(required=False, allow_null=True)

        return fields

    def create(self, validated_data):
        # ? Keep remove sub cat data ?
        sub_categories_data = validated_data.pop('sub_category')
        top_category = validated_data.pop('top_category')
        category = Category.objects.create(**validated_data)
        # Is this equivalent to
        # category = super().create(**validated_data)
        if top_category:
            # TBD ad id verification
            top_cat = Category.objects.get(top_category['id'])
            category.top_category = top_cat
            category.save()
        # for sub_category_data in sub_categories_data:
        # How to solve error Error in formatting: RecursionError: maximum recursion depth exceeded
        # create() got multiple values for keyword argument 'top_category'
        # Category.objects.create(top_category=category, **sub_category_data)
        return category
