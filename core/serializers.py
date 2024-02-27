from rest_framework import serializers
from .models import District,Rooms,Price,Market,Company



class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')

class DistrictDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ('id', 'name', 'description')



class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('id', 'name','countrooms','repair','square')

class RoomsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rooms
        fields = ('id', 'name','repair', 'floors','wallmaterial','yearofconstraction')



class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'name','mbank')

class PriceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ('id', 'name','currency', 'company')



class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'name')

class MarketDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Market
        fields = ('id', 'name', 'descriptions','distance')



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name','description')

class CompanyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'portfolio','history')

