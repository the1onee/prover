import profile

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
# Create your models her
from django.db.models.signals import post_save



class Profile(models.Model):
    user=models.OneToOneField(User,verbose_name=_('user'),on_delete=models.CASCADE)
    name=models.CharField(_("nae:"),max_length=50)

    kghsf = models.IntegerField(_("سعر كشفيه:"), null=True)

    timeour = models.IntegerField(_("مده الانتظار:"),null=True  )
    timemany = models.IntegerField(_("عدد ساعات العمل :"),null=True  )
    salr = models.IntegerField(_("سعر المكالمه :"),null=True  )
    tkhss = models.CharField(_("التخصص :"), max_length=50,null=True )
    adress = models.CharField(_("adress :"), max_length=50, null=True)





    who_i = models.TextField(_("how"), max_length=50)
    price = models.IntegerField(_("are"),blank=True,null=True)
    imge= models.ImageField(("img"),upload_to='profile',blank=True,null=True)

    slug = models.SlugField(_("slug"), blank=True, null=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)




    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


    def __str__(self):
        return self.name



def create_profile(sender, **kwargs):

    if kwargs["created"]:

        Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


