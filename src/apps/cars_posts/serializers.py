from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import CarsPosts, Media, Exterior, Interior, Security, GeneralOptions, Pictures

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class ExteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exterior
        fields = '__all__'

class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = '__all__'

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = '__all__'

class GeneralOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralOptions
        fields = '__all__'


# class PicturesListSerializer(serializers.ModelSerializer):
#     pictures = VersatileImageFieldSerializer(
#         sizes=[
#             ('medium_size', 'crop__400x400')
#         ]
#     )
#
#     class Meta:
#         model = Pictures
#         fields = ['pictures', ]
#
#
# class PicturesDetailSerializer(serializers.ModelSerializer):
#     pictures = VersatileImageFieldSerializer(
#         sizes=[
#             ('full_size', 'url'),
#         ]
#     )
#
#     class Meta:
#         model = Pictures
#         fields = ['pictures', ]


class CarsPostsSerializer(serializers.ModelSerializer):
    # read only
    car_type_name = serializers.CharField(source="car_type.name", read_only=True)
    mark_name = serializers.CharField(source="mark.name", read_only=True)
    model_name = serializers.CharField(source="model.name", read_only=True)
    serie_name = serializers.CharField(source="serie.name", read_only=True)
    modification_name = serializers.CharField(source="modification.name", read_only=True)

    # additional
    likes = serializers.IntegerField(source="likes.count", read_only=True)

    # nested
    exterior = ExteriorSerializer()
    interior = InteriorSerializer()
    media = MediaSerializer()
    security = SecuritySerializer()
    options = GeneralOptionsSerializer()

    class Meta:
        model = CarsPosts
        fields = (
            "id",
            "user",
            "car_type",
            "car_type_name",
            "mark",
            "mark_name",
            "model",
            "model_name",
            "year",
            "serie",
            "serie_name",
            "engine",
            "drive",
            "transmission",
            "modification",
            "modification_name",
            "steering_wheel",
            "video_url",
            "color",
            "condition",
            "mileage",
            "mileage_unit",
            "description",
            "availability",
            "customs_cleared",
            "registration",
            "other",
            "price",
            "currency",
            "exchange_possibility",
            "installment",
            "likes",

            # nested one to one
            "exterior",
            "interior",
            "media",
            "security",
            "options",
        )

    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        super().__init__(*args, **kwargs)

        if not context.get('is_detail', False):
            allowed_fields = ('id', 'user', 'mark_name',
                              'model_name', 'price', 'price_unit',
                              'year', 'modification_name', 'engine',
                              'serie_name', 'transmission', 'steering_wheel',
                              'mileage', 'mileage_unit',
                              )
            for field_name in list(self.fields):
                if field_name not in allowed_fields:
                    self.fields.pop(field_name)


    def create(self, validated_data):
        exterior_data = validated_data.pop('exterior')
        interior_data = validated_data.pop('interior')
        media_data = validated_data.pop('media')
        security_data = validated_data.pop('security')
        options_data = validated_data.pop('options')

        exterior = Exterior.objects.create(**exterior_data)
        interior = Interior.objects.create(**interior_data)
        media = Media.objects.create(**media_data)
        security = Security.objects.create(**security_data)
        options = GeneralOptions.objects.create(**options_data)

        car_post = CarsPosts.objects.create(
            **validated_data,
            exterior=exterior,
            interior=interior,
            media=media,
            security=security,
            options=options
        )

        return car_post

    def update(self, instance, validated_data):
        exterior_data = validated_data.pop('exterior', None)
        interior_data = validated_data.pop('interior', None)
        media_data = validated_data.pop('media', None)
        security_data = validated_data.pop('security', None)
        options_data = validated_data.pop('options', None)

        if exterior_data:
            for attr, value in exterior_data.items():
                setattr(instance.exterior, attr, value)
            instance.exterior.save()

        if interior_data:
            for attr, value in interior_data.items():
                setattr(instance.interior, attr, value)
            instance.interior.save()

        if media_data:
            for attr, value in media_data.items():
                setattr(instance.media, attr, value)
            instance.media.save()

        if security_data:
            for attr, value in security_data.items():
                setattr(instance.security, attr, value)
            instance.security.save()

        if options_data:
            for attr, value in options_data.items():
                setattr(instance.options, attr, value)
            instance.options.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance