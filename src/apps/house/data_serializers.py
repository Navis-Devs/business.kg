from apps.house import data_models
from rest_framework import serializers


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Rooms
        fields = ['id', 'name']

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Options
        fields = ['id', 'name']
        
class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Water
        fields = ['id', 'name']
        
class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Electricity
        fields = ['id', 'name']

class CommentAllowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.CommentAllowed
        fields = ['id', 'name']
        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Material
        fields = ['id', 'name']

class FloorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Floor
        fields = ['id', 'name']

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Condition
        fields = ['id', 'name']        

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.AccountType
        fields = ['id', 'name']        

class HeatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Heating
        fields = ['id', 'name']        

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Region
        fields = '__all__'     

class TownsSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Town
        fields = '__all__'   

class PhoneInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Phone
        fields = ['id', 'name']      
   
class CanalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Canalization
        fields = ['id', 'name']
             
class InternetSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Internet
        fields = ['id', 'name']   

class ToiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Toilet
        fields = ['id', 'name']           

class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Gas
        fields = ['id', 'name']

class TypeBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.BuildingType
        fields = ['id', 'name']
    
class BalconySerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Balcony
        fields = ['id', 'name']

class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Door
        fields = ['id', 'name']

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Parking
        fields = ['id', 'name']

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Furniture
        fields = ['id', 'name']


class FlooringSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Flooring
        fields = ['id', 'name'] 
        
class SafetySerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Safety
        fields = ['id', 'name']

class FlatOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.FlatOptions
        fields = ['id', 'name']

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Exchange
        fields = ['id', 'name']

class PriceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.PriceType
        fields = ['id', 'name']

class FlatOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.FlatOptions
        fields = ['id', 'name']
        
class RoomLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.RoomLocation
        fields = ['id', 'name']
        
class FinishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Finishing
        fields = ['id', 'name']
        
class LandOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.LandOptions
        fields = ['id', 'name']  

class LandLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.LandLocation
        fields = ['id', 'name']
        
class FlooringSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Flooring
        fields = ['id', 'name']    
        
class RentalTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.RentalTerm
        fields = ['id', 'name']     
        
class IrrigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Irrigation
        fields = ['id', 'name']

        
class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Serie
        fields = ['id', 'name']
   
   
class LandAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.LandAmenities
        fields = ['id', 'name']
             
class RoomOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.RoomOption
        fields = ['id', 'name']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Currency
        fields = ['id', 'name', 'sign']

class ParkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.ParkingType
        fields = ['id', 'name']
        
class PosibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Possibility
        fields = ['id', 'name']
        
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Type
        fields = ['id', 'name']
        
class CommercialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.CommercialType
        fields = ['id', 'name']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Category
        fields = ['id', 'name']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Document
        fields = ['id', 'name']         
                
class MicroDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.MicroDistrict
        fields = '__all__'  

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.Town
        fields = '__all__'  

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_models.District
        fields = ['id', 'name', 'slug', 'status', 'latitude', 'longitude', 'zoom', 'town']   
        
class CombinedSerializer(serializers.Serializer):
    type = TypeSerializer(many=True)
    category = CategorySerializer(many=True)
    rooms = RoomsSerializer(many=True)
    material = MaterialSerializer(many=True)
    floors = FloorsSerializer(many=True)
    condition = ConditionSerializer(many=True)
    owner_type = OwnerSerializer(many=True)
    heating = HeatingSerializer(many=True)
    phone_info = PhoneInfoSerializer(many=True)
    internet = InternetSerializer(many=True)
    commercial_type = CommercialTypeSerializer(many=True)
    toilet = ToiletSerializer(many=True)
    gas = GasSerializer(many=True)
    balcony = BalconySerializer(many=True)
    door = DoorSerializer(many=True)
    parking = ParkingSerializer(many=True)
    parking_type = ParkingTypeSerializer(many=True)
    furniture = FurnitureSerializer(many=True) 
    flooring = FlooringSerializer(many=True)
    safety = SafetySerializer(many=True)
    flat_options = FlatOptionsSerializer(many=True)
    exchange = ExchangeSerializer(many=True)
    price_type = PriceTypeSerializer(many=True)
    currency = CurrencySerializer(many=True)
    possibility = PosibilitySerializer(many=True)
    document = DocumentSerializer(many=True)
    building_type = TypeBuildingSerializer(many=True)
    comment_allowed = CommentAllowedSerializer(many=True)
    irrigation = IrrigationSerializer(many=True)  
    land_options = LandOptionsSerializer(many=True)  
    land_location = LandLocationSerializer(many=True)  
    room_location = RoomLocationSerializer(many=True)
    rental_term = RentalTermSerializer(many=True) 
    serie = SerieSerializer(many=True)
    land_amenities = LandAmenitiesSerializer(many=True)  
    room_option = RoomOptionSerializer(many=True) 
    water = WaterSerializer(many=True)
    electricity = ElectricitySerializer(many=True)
    options = OptionsSerializer(many=True)
    rental_term = RentalTermSerializer(many=True)
    finishing = FinishingSerializer(many=True)
    canalization = CanalizationSerializer(many=True)
    region = RegionsSerializer(many=True)
    district = DistrictSerializer(many=True)
    microdistrict = MicroDistrictSerializer(many=True)
    town = TownSerializer(many=True)