from django.contrib import admin
# from .models import related models


# Register your models here.
from django.contrib import admin
from .models import CarMake, CarModel

# Register CarMake model
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display these fields in the list view
    search_fields = ('name',)  # Enable searching by name in the admin

admin.site.register(CarMake, CarMakeAdmin)

# Register CarModel model
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'dealer_id', 'type', 'year')  # Display these fields in the list view
    list_filter = ('type', 'year')  # Enable filtering by type and year in the admin
    search_fields = ('name', 'car_make__name')  # Enable searching by name and car make name in the admin

admin.site.register(CarModel, CarModelAdmin)


# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline
from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline to manage CarModel and CarMake together
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

# Register CarMake model
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Include CarModelInline to manage CarModel on the same page
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(CarMake, CarMakeAdmin)

# Register CarModel model
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'dealer_id', 'type', 'year')
    list_filter = ('type', 'year')
    search_fields = ('name', 'car_make__name')

admin.site.register(CarModel, CarModelAdmin)


# Register models here
