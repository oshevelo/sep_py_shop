from apps.catalog.models import Category
from apps.products.models import Product
from rest_framework import serializers


class TopCategorySerializer(serializers.ModelSerializer):
    # make field not readonly allow access it during post request
    id = serializers.IntegerField()

    class Meta:
        model = Category

        fields = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = ['id', 'category_name', 'top_category', 'sub_category']

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['sub_category'] = CategorySerializer(many=True, allow_null=True)
        fields['top_category'] = TopCategorySerializer(required=False, allow_null=True)

        return fields

    def create(self, validated_data):
        # ? data not used why to pop
        validated_data.pop('sub_category')
        top_category = validated_data.pop('top_category')
        category = Category.objects.create(**validated_data)
        # Is this equivalent to but below does not work
        # category = super().create(**validated_data)
        if top_category:
            top_cat = Category.objects.get(pk=top_category['id'])
            category.top_category = top_cat
            category.save()
        return category


class CategoryProductSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'avaliable_count',
            'detail',
            'active',
            'created',
            'updated',
            'publication_date',
            'number_of_pages',
            'categories'
        )
