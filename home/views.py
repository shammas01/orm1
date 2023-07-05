from django.shortcuts import render


# Create your views here.


#04-07-2023 orm quarys
from django.db.models import Count,Sum,Avg,Max,Q,F,Func
import random
from . models import Hero,Category,Chapter,People,CategoryHero,Course,Instructor,Student,StudentProfile
from django.db.models.functions import Lower






qs=Student.objects.filter(email__startswith='s') 
qs=StudentProfile.objects.values('first_name').annotate(count=Count('first_name')).filter(count=1)
queryset = Student.objects.filter(Q(first_name__startswith='R') | Q(last_name__startswith='D'))
duplicates = Student.objects.values('first_name').annotate(name_count=Count('first_name')).filter(name_count__gt=1)
qs=Student.objects.all().aggregate(Avg('id'))
qs=Student.objects.all().aggregate(Sum('id'))
max_id = Student.objects.all().aggregate(max_id=Max("id"))['max_id']
pk = random.randint(1, max_id)
qs=Hero.objects.annotate(like_zeus=Func(F('name'), function='levenshtein', template="%(function)s(%(expressions)s, 'Zeus')"))
qs=Category.objects.bulk_create([Category(category_name="jeep"),Category(category_name="scooty"),Category(category_name="flight")])
qs=Student.objects.all().order_by('date_joined', '-last_login')
qs=Student.objects.all().order_by(Lower('username')).values_list('username', flat=True)


# signals are raised by Django during object creation or update
# pre_init,
# post_init,
# pre_save,
# post_save,
# pre_delete,
# post_delete