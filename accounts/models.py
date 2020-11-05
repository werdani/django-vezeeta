from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify


# Create your models here.
TYPE_OF_PERSON=(
    ("M","Male"),
    ("F","Female"),
)

class Profile(models.Model):
    DOCTOR_IN={
        ("جلديه","جلديه"),
        ("اسنان","اسنان"),
        ("نفسي","نفسي"), 
        ("اطفال حديثي الولاده","اطفال حديثي الولاده"),
        ("مخ واعصاب","مخ واعصاب"),
        ("عظام","عظام"),
        ("نساء وتوليد","نساء وتوليد"),
        ("انف واذن وحنجره","انف واذن وحنجره"),
        ("قلب واعويه دمويه","قلب واعويه دمويه"),
        ("امراض دم","امراض دم"),
        ("اورام","اورام"),
        ("باطنه","باطنه"),
        ("تخسيس وتغذيه","تخسيس وتغذيه"),
        ("جراحه اطفال","جراحه اطفال"),
        ("جراحه اورام","جراحه اورام"),
        ("جراحه اوعيه دمويه","جراحه اوعيه دمويه"),
        ("جراحه تجميل","جراحه تجميل"),
        ("جراحه سمنه مناطير","جراحه سمنه مناطير"),
               
    }
    user = models.OneToOneField(User,verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الاسم :"), max_length=50)
    surname = models.CharField(_("اللقب :"), max_length=50)
    subtitle = models.CharField(_("نبذه عنك :"), max_length=50)
    address = models.CharField(_("المحافظه :"), max_length=50)
    address_detail = models.CharField(_("العنوان بالتفصيل :"), max_length=150)
    phone_number = models.CharField(_("الهاتف :"), max_length=50)
    working_hours = models.CharField(_("عدد ساعات العمل :"), max_length=50)
    wating_time = models.CharField(_("مده الانتظار :"), max_length=50,blank=True, null=True)
    who_i = models.TextField(_("من انا :"))
    price = models.IntegerField(_("سعر الكشف :"),blank=True,null=True) 
    facbook = models.CharField( max_length=50,blank=True,null=True)
    twitter = models.CharField(max_length=50,blank=True,null=True)
    google = models.CharField(max_length=50,blank=True,null=True)
    join_new = models.DateTimeField(_("وقت الانضمام :"),auto_now_add=True,blank=True,null=True)
    type_preson = models.CharField(_("النوع :"),choices = TYPE_OF_PERSON ,max_length=50)
    doctor = models.CharField(_("دكتور ؟"),choices= DOCTOR_IN, max_length=50,blank=True, null=True)
    image = models.ImageField(_("الصوره الشخصيه :"), upload_to='profile',blank=True, null=True)
    specialist_doctor = models.CharField(_("متخصص في :"), max_length=50,blank=True, null=True)
    slug = models.SlugField(_("slug"),blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
       
        super(Profile, self).save(*args, **kwargs) # Call the real save() method
    

    
    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return '%s' %(self.user.username)

def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)
    