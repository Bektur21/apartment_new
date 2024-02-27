from django.contrib import admin
from .models import District, Rooms, Price, Market, Company

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    search_fields = ('name',)

@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('countofrooms', 'repair', 'company', 'furniture', 'square', 'floors', 'wallmaterial', 'heating', 'yearofconstraction', 'additionally')
    list_display_links = ('company', 'countofrooms', 'repair', 'square', 'furniture', 'floors')
    search_fields = ('company', 'countofrooms', 'repair', 'square')
    list_filter = ('repair', 'furniture', 'floors', 'heating')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'currency', 'mbank', 'company')
    list_display_links = ('price', 'company', )
    search_fields = ('company',)
    list_filter = ('currency', 'mbank')

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions', 'distance')
    list_display_links = ('name', 'distance')
    search_fields = ('name',)
    list_filter = ('distance',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'history', 'portfolio', 'descriptions')
    list_display_links = ('name', 'descriptions', 'portfolio', )
    search_fields = ('name', 'portfolio', )
    list_filter = ('portfolio',)
    