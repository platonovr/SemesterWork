from django.contrib import admin

# Register your models here.
from EventApp.models import Event, Place, UserProfile, Type, Rating, Comment, Debt
from JobApp.models import Task, Bill, Goal, Fact


admin.site.register(Event)
admin.site.register(Place)
admin.site.register(UserProfile)
admin.site.register(Type)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Debt)

admin.site.register(Task)
admin.site.register(Bill)
admin.site.register(Goal)
admin.site.register(Fact)