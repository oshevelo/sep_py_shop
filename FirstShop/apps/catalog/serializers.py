from rest_framework import serializers

from apps.catalog.models import Category


class TopCategorySerializer(serializers.ModelSerializer):
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
        # ? Created with 2 post requests 1 top 2 sub

        # ? Keep remove sub cat data ?
        print('22222222222222222222222---------------------------------------------------------')
        for k, v in validated_data:
            print(k, v)
        print(len(validated_data['top_category']))
        sub_categories_data = validated_data.pop('sub_category')
        top_category = validated_data.pop('top_category')
        category = Category.objects.create(**validated_data)
        # Is this equivalent to
        # category = super().create(**validated_data)

        if top_category:
            print('---------------------------------------------------------')
            print(top_category)
            # TBD ad id verification
            top_cat = Category.objects.get(top_category['id'])
            category.top_category = top_cat
            category.save()
        return category
