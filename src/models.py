# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class CarCharacteristic(models.Model):
    id_car_characteristic = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=42, blank=True, null=True)
    id_parent = models.CharField(max_length=2, blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.CharField(max_length=10, blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_characteristic'


class CarCharacteristicValue(models.Model):
    id_car_characteristic_value = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=109, blank=True, null=True)
    unit = models.CharField(max_length=15, blank=True, null=True)
    id_car_characteristic = models.SmallIntegerField(blank=True, null=True)
    id_car_modification = models.IntegerField(blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.CharField(max_length=10, blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_characteristic_value'


class CarEquipment(models.Model):
    id_car_equipment = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=28, blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.BigIntegerField(blank=True, null=True)
    id_car_modification = models.IntegerField(blank=True, null=True)
    price_min = models.CharField(max_length=7, blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_equipment'


class CarGeneration(models.Model):
    id_car_generation = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=28, blank=True, null=True)
    id_car_model = models.IntegerField(blank=True, null=True)
    year_begin = models.CharField(max_length=4, blank=True, null=True)
    year_end = models.CharField(max_length=4, blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.CharField(max_length=10, blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_generation'


class CarMark(models.Model):
    id_car_mark = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=8, blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.BigIntegerField(blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)
    name_rus = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_mark'


class CarModel(models.Model):
    id_car_model = models.IntegerField(blank=True, null=True)
    id_car_mark = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=13, blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.BigIntegerField(blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)
    name_rus = models.CharField(max_length=21, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_model'


class CarModification(models.Model):
    id_car_modification = models.IntegerField(blank=True, null=True)
    id_car_serie = models.IntegerField(blank=True, null=True)
    id_car_model = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=35, blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.CharField(max_length=10, blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_modification'


class CarOption(models.Model):
    id_car_option = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    id_parent = models.SmallIntegerField(blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.BigIntegerField(blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_option'


class CarOptionValue(models.Model):
    id_car_option_value = models.IntegerField(blank=True, null=True)
    is_base = models.SmallIntegerField(blank=True, null=True)
    id_car_option = models.IntegerField(blank=True, null=True)
    id_car_equipment = models.IntegerField(blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.BigIntegerField(blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_option_value'


class CarSerie(models.Model):
    id_car_serie = models.IntegerField(blank=True, null=True)
    id_car_model = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    date_create = models.BigIntegerField(blank=True, null=True)
    date_update = models.CharField(max_length=10, blank=True, null=True)
    id_car_generation = models.IntegerField(blank=True, null=True)
    id_car_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_serie'


class CarType(models.Model):
    id_car_type = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_car_type'


class AccountsBusinessaccount(models.Model):
    id = models.UUIDField(primary_key=True)
    tariff_plan = models.IntegerField()
    deadline = models.DateTimeField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    video = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField('AccountsUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_businessaccount'


class AccountsBusinessaccountimages(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=100)
    main = models.ForeignKey(AccountsBusinessaccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_businessaccountimages'


class AccountsColors(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'accounts_colors'


class AccountsColorsTranslation(models.Model):
    language_code = models.CharField(max_length=15)
    name = models.CharField()
    color = models.CharField(max_length=25)
    dark_color = models.CharField(primary_key=True, max_length=25)
    master = models.ForeignKey(AccountsColors, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_colors_translation'
        unique_together = (('language_code', 'master'),)


class AccountsPlans(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.BigIntegerField()
    duration = models.IntegerField()
    cashback = models.CharField()

    class Meta:
        managed = False
        db_table = 'accounts_plans'


class AccountsPlansTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    description = models.TextField()
    master = models.ForeignKey(AccountsPlans, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_plans_translation'
        unique_together = (('language_code', 'master'),)


class AccountsTariff(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.BigIntegerField()
    period = models.CharField()

    class Meta:
        managed = False
        db_table = 'accounts_tariff'


class AccountsTariffPlans(models.Model):
    id = models.BigAutoField(primary_key=True)
    tariff = models.ForeignKey(AccountsTariff, models.DO_NOTHING)
    plans = models.ForeignKey(AccountsPlans, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_tariff_plans'
        unique_together = (('tariff', 'plans'),)


class AccountsTariffTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    description = models.TextField()
    master = models.ForeignKey(AccountsTariff, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_tariff_translation'
        unique_together = (('language_code', 'master'),)


class AccountsUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    is_staff = models.BooleanField()
    date_joined = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=150)
    balance = models.IntegerField()
    code = models.IntegerField(blank=True, null=True)
    field_avatar = models.CharField(db_column='_avatar', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    is_active = models.BooleanField()
    mkg_id = models.CharField(max_length=99999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AccountsUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_groups'
        unique_together = (('user', 'group'),)


class AccountsUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class CarCharacteristicValue(models.Model):
    id_car_characteristic = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'car_characteristic_value'


class CarsCarcharacteristic(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING, blank=True, null=True)
    id_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_carcharacteristic'


class CarsCarcharacteristicvalue(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=255)
    unit = models.CharField(max_length=255, blank=True, null=True)
    id_car_characteristic = models.ForeignKey(CarsCarcharacteristic, models.DO_NOTHING, blank=True, null=True)
    id_car_modification = models.ForeignKey('CarsCarmodification', models.DO_NOTHING, blank=True, null=True)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_carcharacteristicvalue'


class CarsCarcolors(models.Model):
    id = models.CharField(primary_key=True, max_length=25)
    name = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_carcolors'


class CarsCarequipment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price_min = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    id_car_modification = models.ForeignKey('CarsCarmodification', models.DO_NOTHING)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_carequipment'


class CarsCargeneration(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=100, blank=True, null=True)
    year_begin = models.CharField(max_length=255, blank=True, null=True)
    year_end = models.CharField(max_length=255, blank=True, null=True)
    id_car_model = models.ForeignKey('CarsCarmodel', models.DO_NOTHING)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_cargeneration'


class CarsCarmark(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=100, blank=True, null=True)
    name_rus = models.CharField(max_length=255)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_carmark'


class CarsCarmodel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    name_rus = models.CharField(max_length=255, blank=True, null=True)
    id_car_mark = models.ForeignKey(CarsCarmark, models.DO_NOTHING)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_carmodel'


class CarsCarmodification(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    id_car_model = models.ForeignKey(CarsCarmodel, models.DO_NOTHING, blank=True, null=True)
    id_car_serie = models.ForeignKey('CarsCarserie', models.DO_NOTHING)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_carmodification'


class CarsCaroption(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING, blank=True, null=True)
    id_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_caroption'


class CarsCaroptionvalue(models.Model):
    id = models.IntegerField(primary_key=True)
    is_base = models.SmallIntegerField()
    id_car_equipment = models.ForeignKey(CarsCarequipment, models.DO_NOTHING)
    id_car_option = models.ForeignKey(CarsCaroption, models.DO_NOTHING)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_caroptionvalue'


class CarsCarserie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    id_car_generation = models.ForeignKey(CarsCargeneration, models.DO_NOTHING)
    id_car_model = models.ForeignKey(CarsCarmodel, models.DO_NOTHING, blank=True, null=True)
    id_car_type = models.ForeignKey('CarsCartype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_carserie'


class CarsCartype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cars_cartype'


class CarsPermissionforfront(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cars_permissionforfront'


class CarsPostsCarprices(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.IntegerField()
    cars = models.ForeignKey('CarsPostsCarsposts', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_carprices'


class CarsPostsCarsposts(models.Model):
    id = models.UUIDField(primary_key=True)
    is_autoup = models.BooleanField()
    autoup_time = models.TimeField(blank=True, null=True)
    autoup_until = models.DateTimeField(blank=True, null=True)
    is_vip = models.BooleanField()
    vipped_until = models.DateTimeField(blank=True, null=True)
    is_premium = models.BooleanField()
    premium_until = models.DateTimeField(blank=True, null=True)
    premium_gradient = models.CharField(max_length=255, blank=True, null=True)
    premium_dark_gradient = models.CharField(max_length=255, blank=True, null=True)
    is_urgent = models.BooleanField()
    urgent_until = models.DateTimeField(blank=True, null=True)
    is_top = models.BooleanField()
    topped_until = models.DateTimeField(blank=True, null=True)
    featured = models.BooleanField(blank=True, null=True)
    ad_color = models.CharField(max_length=7, blank=True, null=True)
    ad_dark_color = models.CharField(max_length=7, blank=True, null=True)
    colored_until = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    mkg_id = models.CharField(max_length=99999, blank=True, null=True)
    mileage_unit = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video_url = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    horse_power = models.IntegerField()
    engine_volume = models.SmallIntegerField()
    mileage = models.IntegerField()
    serie = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    car_condition = models.ForeignKey('CarsPostsCondition', models.DO_NOTHING, blank=True, null=True)
    car_type = models.ForeignKey(CarsCartype, models.DO_NOTHING, blank=True, null=True)
    color = models.ForeignKey(CarsCarcolors, models.DO_NOTHING, blank=True, null=True)
    comment_allowed = models.ForeignKey('HouseCommentallowed', models.DO_NOTHING)
    currency = models.ForeignKey('HouseCurrency', models.DO_NOTHING)
    customs = models.ForeignKey('HousePossibility', models.DO_NOTHING, blank=True, null=True)
    exchange = models.ForeignKey('HouseExchange', models.DO_NOTHING)
    featured_option = models.ForeignKey('CarsPostsFeaturedoption', models.DO_NOTHING)
    fuel = models.ForeignKey('CarsPostsFuel', models.DO_NOTHING, blank=True, null=True)
    gear_box = models.ForeignKey('CarsPostsGearbox', models.DO_NOTHING, blank=True, null=True)
    installment = models.ForeignKey('HousePossibility', models.DO_NOTHING, related_name='carspostscarsposts_installment_set', blank=True, null=True)
    mark = models.ForeignKey(CarsCarmark, models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey(CarsCarmodel, models.DO_NOTHING, blank=True, null=True)
    registration_country = models.ForeignKey('CarsPostsRegistrationcountry', models.DO_NOTHING)
    steering_wheel = models.ForeignKey('CarsPostsSteeringwheel', models.DO_NOTHING, blank=True, null=True)
    transmission = models.ForeignKey('CarsPostsTransmission', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_posts_carsposts'


class CarsPostsCarspostsConfiguration(models.Model):
    id = models.BigAutoField(primary_key=True)
    carsposts = models.ForeignKey(CarsPostsCarsposts, models.DO_NOTHING)
    generaloptions = models.ForeignKey('CarsPostsGeneraloptions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_carsposts_configuration'
        unique_together = (('carsposts', 'generaloptions'),)


class CarsPostsCarspostsExterior(models.Model):
    id = models.BigAutoField(primary_key=True)
    carsposts = models.ForeignKey(CarsPostsCarsposts, models.DO_NOTHING)
    exterior = models.ForeignKey('CarsPostsExterior', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_carsposts_exterior'
        unique_together = (('carsposts', 'exterior'),)


class CarsPostsCarspostsInterior(models.Model):
    id = models.BigAutoField(primary_key=True)
    carsposts = models.ForeignKey(CarsPostsCarsposts, models.DO_NOTHING)
    interior = models.ForeignKey('CarsPostsInterior', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_carsposts_interior'
        unique_together = (('carsposts', 'interior'),)


class CarsPostsCarspostsLikes(models.Model):
    id = models.BigAutoField(primary_key=True)
    carsposts = models.ForeignKey(CarsPostsCarsposts, models.DO_NOTHING)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_carsposts_likes'
        unique_together = (('carsposts', 'user'),)


class CarsPostsCarspostsMedia(models.Model):
    id = models.BigAutoField(primary_key=True)
    carsposts = models.ForeignKey(CarsPostsCarsposts, models.DO_NOTHING)
    media = models.ForeignKey('CarsPostsMedia', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_carsposts_media'
        unique_together = (('carsposts', 'media'),)


class CarsPostsCarspostsOtherOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    carsposts = models.ForeignKey(CarsPostsCarsposts, models.DO_NOTHING)
    otheroptions = models.ForeignKey('CarsPostsOtheroptions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_carsposts_other_options'
        unique_together = (('carsposts', 'otheroptions'),)


class CarsPostsCarspostsSafety(models.Model):
    id = models.BigAutoField(primary_key=True)
    carsposts = models.ForeignKey(CarsPostsCarsposts, models.DO_NOTHING)
    safety = models.ForeignKey('CarsPostsSafety', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_carsposts_safety'
        unique_together = (('carsposts', 'safety'),)


class CarsPostsCondition(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_condition'


class CarsPostsExterior(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_exterior'


class CarsPostsFeaturedoption(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_featuredoption'


class CarsPostsFuel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_fuel'


class CarsPostsGearbox(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_gearbox'


class CarsPostsGeneraloptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_generaloptions'


class CarsPostsInterior(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_interior'


class CarsPostsMedia(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_media'


class CarsPostsOtheroptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_otheroptions'


class CarsPostsPictures(models.Model):
    id = models.BigAutoField(primary_key=True)
    pictures = models.CharField(max_length=100)
    cars = models.ForeignKey(CarsPostsCarsposts, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_pictures'


class CarsPostsRegion(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_region'


class CarsPostsRegistrationcountry(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_registrationcountry'


class CarsPostsSafety(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_safety'


class CarsPostsSteeringwheel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_steeringwheel'


class CarsPostsTowns(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    region = models.ForeignKey(CarsPostsRegion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cars_posts_towns'


class CarsPostsTransmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cars_posts_transmission'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HouseAccounttype(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_accounttype'


class HouseAccounttypeTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseAccounttype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_accounttype_translation'
        unique_together = (('language_code', 'master'),)


class HouseBalcony(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_balcony'


class HouseBalconyTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseBalcony, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_balcony_translation'
        unique_together = (('language_code', 'master'),)


class HouseBuilding(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    lon = models.FloatField()
    lat = models.FloatField()
    address = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=20, blank=True, null=True)
    crossing = models.CharField(max_length=255, blank=True, null=True)
    floors = models.IntegerField()
    ceiling_height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    storey = models.IntegerField(blank=True, null=True)
    about_complex = models.TextField(blank=True, null=True)
    media = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    completion_date = models.CharField(max_length=50, blank=True, null=True)
    finishing = models.BooleanField(blank=True, null=True)
    cadastre_number = models.CharField(max_length=50, blank=True, null=True)
    building_class = models.ForeignKey('HouseBuildingclass', models.DO_NOTHING, blank=True, null=True)
    district_id = models.ForeignKey('HouseDistrict', models.DO_NOTHING, blank=True, null=True)
    heating = models.ForeignKey('HouseHeating', models.DO_NOTHING, blank=True, null=True)
    material_id = models.ForeignKey('HouseBuildingtype', models.DO_NOTHING, blank=True, null=True)
    microdistrict_id = models.ForeignKey('HouseMicrodistrict', models.DO_NOTHING, blank=True, null=True)
    object_state = models.ForeignKey('HouseBuildingstate', models.DO_NOTHING, blank=True, null=True)
    region_id = models.ForeignKey('HouseRegion', models.DO_NOTHING, blank=True, null=True)
    serie = models.ForeignKey('HouseSerie', models.DO_NOTHING, blank=True, null=True)
    town_id = models.ForeignKey('HouseTown', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_building'


class HouseBuildingclass(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_buildingclass'


class HouseBuildingclassTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseBuildingclass, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_buildingclass_translation'
        unique_together = (('language_code', 'master'),)


class HouseBuildingimage(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    complex = models.ForeignKey(HouseBuilding, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_buildingimage'


class HouseBuildingprice(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.IntegerField()
    building = models.ForeignKey(HouseBuilding, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_buildingprice'


class HouseBuildingstate(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_buildingstate'


class HouseBuildingstateTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseBuildingstate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_buildingstate_translation'
        unique_together = (('language_code', 'master'),)


class HouseBuildingtype(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_buildingtype'


class HouseBuildingtypeTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseBuildingtype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_buildingtype_translation'
        unique_together = (('language_code', 'master'),)


class HouseCanalization(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_canalization'


class HouseCanalizationTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseCanalization, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_canalization_translation'
        unique_together = (('language_code', 'master'),)


class HouseCategory(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_category'


class HouseCategoryTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_category_translation'
        unique_together = (('language_code', 'master'),)


class HouseCommentallowed(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_commentallowed'


class HouseCommentallowedTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseCommentallowed, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_commentallowed_translation'
        unique_together = (('language_code', 'master'),)


class HouseCommercialtype(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_commercialtype'


class HouseCommercialtypeTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseCommercialtype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_commercialtype_translation'
        unique_together = (('language_code', 'master'),)


class HouseCondition(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_condition'


class HouseConditionTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseCondition, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_condition_translation'
        unique_together = (('language_code', 'master'),)


class HouseCurrency(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_currency'


class HouseCurrencyTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    sign = models.CharField(max_length=10)
    master = models.ForeignKey(HouseCurrency, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_currency_translation'
        unique_together = (('language_code', 'master'),)


class HouseDistrict(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    town = models.ForeignKey('HouseTown', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_district'


class HouseDocument(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_document'


class HouseDocumentTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    master = models.ForeignKey(HouseDocument, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_document_translation'
        unique_together = (('language_code', 'master'),)


class HouseDoor(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_door'


class HouseDoorTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseDoor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_door_translation'
        unique_together = (('language_code', 'master'),)


class HouseElectricity(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_electricity'


class HouseElectricityTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseElectricity, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_electricity_translation'
        unique_together = (('language_code', 'master'),)


class HouseExchange(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_exchange'


class HouseExchangeTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseExchange, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_exchange_translation'
        unique_together = (('language_code', 'master'),)


class HouseFinishing(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_finishing'


class HouseFinishingTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseFinishing, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_finishing_translation'
        unique_together = (('language_code', 'master'),)


class HouseFlatoptions(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_flatoptions'


class HouseFlatoptionsTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseFlatoptions, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_flatoptions_translation'
        unique_together = (('language_code', 'master'),)


class HouseFloor(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_floor'


class HouseFloorTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseFloor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_floor_translation'
        unique_together = (('language_code', 'master'),)


class HouseFlooring(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_flooring'


class HouseFlooringTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseFlooring, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_flooring_translation'
        unique_together = (('language_code', 'master'),)


class HouseFurniture(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_furniture'


class HouseFurnitureTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseFurniture, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_furniture_translation'
        unique_together = (('language_code', 'master'),)


class HouseGas(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_gas'


class HouseGasTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseGas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_gas_translation'
        unique_together = (('language_code', 'master'),)


class HouseHeating(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_heating'


class HouseHeatingTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseHeating, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_heating_translation'
        unique_together = (('language_code', 'master'),)


class HouseInstallment(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_installment'


class HouseInstallmentTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseInstallment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_installment_translation'
        unique_together = (('language_code', 'master'),)


class HouseInternet(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_internet'


class HouseInternetTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseInternet, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_internet_translation'
        unique_together = (('language_code', 'master'),)


class HouseIrrigation(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_irrigation'


class HouseIrrigationTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseIrrigation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_irrigation_translation'
        unique_together = (('language_code', 'master'),)


class HouseLandamenities(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_landamenities'


class HouseLandamenitiesTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseLandamenities, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_landamenities_translation'
        unique_together = (('language_code', 'master'),)


class HouseLandlocation(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_landlocation'


class HouseLandlocationTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseLandlocation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_landlocation_translation'
        unique_together = (('language_code', 'master'),)


class HouseLandoptions(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_landoptions'


class HouseLandoptionsTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseLandoptions, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_landoptions_translation'
        unique_together = (('language_code', 'master'),)


class HouseMaterial(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_material'


class HouseMaterialTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseMaterial, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_material_translation'
        unique_together = (('language_code', 'master'),)


class HouseMicrodistrict(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    district = models.ForeignKey(HouseDistrict, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_microdistrict'


class HouseOptions(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_options'


class HouseOptionsTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseOptions, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_options_translation'
        unique_together = (('language_code', 'master'),)


class HouseParking(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_parking'


class HouseParkingTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseParking, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_parking_translation'
        unique_together = (('language_code', 'master'),)


class HouseParkingtype(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_parkingtype'


class HouseParkingtypeTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseParkingtype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_parkingtype_translation'
        unique_together = (('language_code', 'master'),)


class HousePhone(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_phone'


class HousePhoneTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HousePhone, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_phone_translation'
        unique_together = (('language_code', 'master'),)


class HousePhones(models.Model):
    id = models.BigAutoField(primary_key=True)
    phones = models.TextField()  # This field type is a guess.
    property = models.ForeignKey('HouseProperty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_phones'


class HousePictures(models.Model):
    id = models.BigAutoField(primary_key=True)
    pictures = models.CharField(max_length=100)
    property = models.ForeignKey('HouseProperty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_pictures'


class HousePossibility(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_possibility'


class HousePossibilityTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    master = models.ForeignKey(HousePossibility, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_possibility_translation'
        unique_together = (('language_code', 'master'),)


class HousePrice(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.IntegerField()
    m2_price = models.IntegerField()
    property = models.ForeignKey('HouseProperty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_price'


class HousePricetype(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_pricetype'


class HousePricetypeTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=10)
    master = models.ForeignKey(HousePricetype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_pricetype_translation'
        unique_together = (('language_code', 'master'),)


class HouseProperty(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_autoup = models.BooleanField()
    autoup_time = models.TimeField(blank=True, null=True)
    autoup_until = models.DateTimeField(blank=True, null=True)
    is_vip = models.BooleanField()
    vipped_until = models.DateTimeField(blank=True, null=True)
    is_premium = models.BooleanField()
    premium_until = models.DateTimeField(blank=True, null=True)
    premium_gradient = models.CharField(max_length=255, blank=True, null=True)
    premium_dark_gradient = models.CharField(max_length=255, blank=True, null=True)
    is_urgent = models.BooleanField()
    urgent_until = models.DateTimeField(blank=True, null=True)
    is_top = models.BooleanField()
    topped_until = models.DateTimeField(blank=True, null=True)
    featured = models.BooleanField(blank=True, null=True)
    ad_color = models.CharField(max_length=7, blank=True, null=True)
    ad_dark_color = models.CharField(max_length=7, blank=True, null=True)
    colored_until = models.DateTimeField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    land_square = models.IntegerField(blank=True, null=True)
    living_square = models.IntegerField(blank=True, null=True)
    kitchen_square = models.IntegerField(blank=True, null=True)
    ceiling_height = models.FloatField(blank=True, null=True)
    square = models.IntegerField(blank=True, null=True)
    cadastre_number = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=100, blank=True, null=True)
    crossing = models.CharField(max_length=100, blank=True, null=True)
    point = models.PointField(blank=True, null=True)
    youtube_url = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    views = models.IntegerField()
    active_post = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    upped_at = models.DateTimeField(blank=True, null=True)
    balkony = models.ForeignKey(HouseBalcony, models.DO_NOTHING, blank=True, null=True)
    building_type = models.ForeignKey(HouseBuildingtype, models.DO_NOTHING, blank=True, null=True)
    business_account = models.ForeignKey(AccountsBusinessaccount, models.DO_NOTHING, blank=True, null=True)
    canalization = models.ForeignKey(HouseCanalization, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(HouseCategory, models.DO_NOTHING)
    comment_allowed = models.ForeignKey(HouseCommentallowed, models.DO_NOTHING, blank=True, null=True)
    commercial_type = models.ForeignKey(HouseCommercialtype, models.DO_NOTHING, blank=True, null=True)
    complex_id = models.ForeignKey(HouseBuilding, models.DO_NOTHING, blank=True, null=True)
    condition = models.ForeignKey(HouseCondition, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(HouseCurrency, models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(HouseDistrict, models.DO_NOTHING, blank=True, null=True)
    door = models.ForeignKey(HouseDoor, models.DO_NOTHING, blank=True, null=True)
    electricity = models.ForeignKey(HouseElectricity, models.DO_NOTHING, blank=True, null=True)
    exchange = models.ForeignKey(HouseExchange, models.DO_NOTHING, blank=True, null=True)
    floor = models.ForeignKey(HouseFloor, models.DO_NOTHING, blank=True, null=True)
    flooring = models.ForeignKey(HouseFlooring, models.DO_NOTHING, blank=True, null=True)
    floors = models.ForeignKey(HouseFloor, models.DO_NOTHING, related_name='houseproperty_floors_set', blank=True, null=True)
    furniture = models.ForeignKey(HouseFurniture, models.DO_NOTHING, blank=True, null=True)
    gas = models.ForeignKey(HouseGas, models.DO_NOTHING, blank=True, null=True)
    heating = models.ForeignKey(HouseHeating, models.DO_NOTHING, blank=True, null=True)
    installment = models.ForeignKey(HousePossibility, models.DO_NOTHING, blank=True, null=True)
    internet = models.ForeignKey(HouseInternet, models.DO_NOTHING, blank=True, null=True)
    irrigation = models.ForeignKey(HouseIrrigation, models.DO_NOTHING, blank=True, null=True)
    land_location = models.ForeignKey(HouseLandlocation, models.DO_NOTHING, blank=True, null=True)
    material = models.ForeignKey(HouseMaterial, models.DO_NOTHING, blank=True, null=True)
    microdistrict = models.ForeignKey(HouseMicrodistrict, models.DO_NOTHING, blank=True, null=True)
    mortgage = models.ForeignKey(HousePossibility, models.DO_NOTHING, related_name='houseproperty_mortgage_set', blank=True, null=True)
    owner_type = models.ForeignKey(HouseAccounttype, models.DO_NOTHING)
    parking = models.ForeignKey(HouseParking, models.DO_NOTHING, blank=True, null=True)
    parking_type = models.ForeignKey(HouseParkingtype, models.DO_NOTHING, blank=True, null=True)
    phone_info = models.ForeignKey(HousePhone, models.DO_NOTHING, blank=True, null=True)
    price_for = models.ForeignKey(HousePricetype, models.DO_NOTHING)
    region = models.ForeignKey('HouseRegion', models.DO_NOTHING, blank=True, null=True)
    rental_term = models.ForeignKey('HouseRentalterm', models.DO_NOTHING, blank=True, null=True)
    room_location = models.ForeignKey('HouseRoomlocation', models.DO_NOTHING, blank=True, null=True)
    rooms = models.ForeignKey('HouseRooms', models.DO_NOTHING, blank=True, null=True)
    serie = models.ForeignKey('HouseSerie', models.DO_NOTHING, blank=True, null=True)
    toilet = models.ForeignKey('HouseToilet', models.DO_NOTHING, blank=True, null=True)
    town = models.ForeignKey('HouseTown', models.DO_NOTHING, blank=True, null=True)
    type_id = models.ForeignKey('HouseType', models.DO_NOTHING)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    water = models.ForeignKey('HouseWater', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_property'


class HousePropertyDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(HouseProperty, models.DO_NOTHING)
    document = models.ForeignKey(HouseDocument, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_property_documents'
        unique_together = (('property', 'document'),)


class HousePropertyFlatOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(HouseProperty, models.DO_NOTHING)
    flatoptions = models.ForeignKey(HouseFlatoptions, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_property_flat_options'
        unique_together = (('property', 'flatoptions'),)


class HousePropertyLandAmenities(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(HouseProperty, models.DO_NOTHING)
    landamenities = models.ForeignKey(HouseLandamenities, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_property_land_amenities'
        unique_together = (('property', 'landamenities'),)


class HousePropertyLandOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(HouseProperty, models.DO_NOTHING)
    landoptions = models.ForeignKey(HouseLandoptions, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_property_land_options'
        unique_together = (('property', 'landoptions'),)


class HousePropertyOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(HouseProperty, models.DO_NOTHING)
    options = models.ForeignKey(HouseOptions, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_property_options'
        unique_together = (('property', 'options'),)


class HousePropertyRoomOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(HouseProperty, models.DO_NOTHING)
    roomoption = models.ForeignKey('HouseRoomoption', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_property_room_options'
        unique_together = (('property', 'roomoption'),)


class HousePropertySafety(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(HouseProperty, models.DO_NOTHING)
    safety = models.ForeignKey('HouseSafety', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_property_safety'
        unique_together = (('property', 'safety'),)


class HouseRegion(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    map = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'house_region'


class HouseRentalterm(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_rentalterm'


class HouseRentaltermTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseRentalterm, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_rentalterm_translation'
        unique_together = (('language_code', 'master'),)


class HouseRoomlocation(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_roomlocation'


class HouseRoomlocationTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseRoomlocation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_roomlocation_translation'
        unique_together = (('language_code', 'master'),)


class HouseRoomoption(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_roomoption'


class HouseRoomoptionTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseRoomoption, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_roomoption_translation'
        unique_together = (('language_code', 'master'),)


class HouseRooms(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_rooms'


class HouseRoomsTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseRooms, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_rooms_translation'
        unique_together = (('language_code', 'master'),)


class HouseSafety(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_safety'


class HouseSafetyTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseSafety, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_safety_translation'
        unique_together = (('language_code', 'master'),)


class HouseSerie(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_serie'


class HouseSerieTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseSerie, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_serie_translation'
        unique_together = (('language_code', 'master'),)


class HouseToilet(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_toilet'


class HouseToiletTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseToilet, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_toilet_translation'
        unique_together = (('language_code', 'master'),)


class HouseTown(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    map = models.CharField(max_length=50)
    region = models.ForeignKey(HouseRegion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'house_town'


class HouseType(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_type'


class HouseTypeTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    master = models.ForeignKey(HouseType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_type_translation'
        unique_together = (('language_code', 'master'),)


class HouseWater(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'house_water'


class HouseWaterTranslation(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    master = models.ForeignKey(HouseWater, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_water_translation'
        unique_together = (('language_code', 'master'),)


class MainComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=100)
    object_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_comments'


class MainReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    object_id = models.CharField(max_length=200)
    rating = models.IntegerField()
    comment = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_review'


class TariffsAutoup(models.Model):
    id = models.UUIDField(primary_key=True)
    days = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tariffs_autoup'


class TariffsHighlight(models.Model):
    id = models.UUIDField(primary_key=True)
    days = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tariffs_highlight'


class TariffsTop(models.Model):
    id = models.UUIDField(primary_key=True)
    days = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tariffs_top'


class TariffsUrgent(models.Model):
    id = models.UUIDField(primary_key=True)
    days = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tariffs_urgent'


class ThumbnailKvstore(models.Model):
    key = models.CharField(primary_key=True, max_length=200)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'thumbnail_kvstore'


class TransactionsTransaction(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions_transaction'
