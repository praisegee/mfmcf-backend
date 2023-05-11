from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

User = get_user_model()
CAMPUS = [("oye", "Oye"), ("ikole", "Ikole")]
MARITAL_STATUS = [("single", "Single"), ("engaged", "Engaged"), ("married", "Married")]


class BirthdayCelebrant(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=100,
        help_text=_("Prefix the name with a title (Bro|Sis) e.g Bro PraiseGod."),
    )
    birthday = models.CharField(
        _("Date of birth"),
        max_length=20,
        help_text=_("Just the day and the month; in the formart `DD-MM`."),
    )
    picture = models.ImageField(_("Picture"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class SpotLight(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=100,
        help_text=_("Prefix the name with a title (Bro|Sis) e.g Bro PraiseGod."),
    )
    description = models.CharField(
        _("Description"),
        max_length=500,
        help_text=_("A short description of the person."),
    )
    birthday = models.CharField(
        _("Date of birth"),
        max_length=20,
        help_text=_("Just the day and the month; in the formart `DD-MM`."),
    )
    marital_status = models.CharField(
        _("Marital status"), max_length=10, choices=MARITAL_STATUS, default="Single"
    )
    hobby = models.CharField(_("Hobby"), max_length=50)
    campus = models.CharField(_("Campus"), max_length=10, choices=CAMPUS, default="Oye")
    faculty = models.CharField(_("Faculty"), max_length=50)
    department = models.CharField(_("Department"), max_length=50)
    picture = models.ImageField(_("Picture"))
    favorite_bible_verse = models.CharField(
        _("Favourite Bible verse"), max_length=20, help_text="e.g. 'Matt 15 v 12'"
    )
    favorite_quote = models.CharField(
        _("Favourite Quote"),
        max_length=225,
        help_text="Type 'None' if this field is not provided.",
    )
    phone_number = models.CharField(_("Phone number"), max_length=15)
    email = models.EmailField(_("Email"), max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("-created_at",)


class Executive(models.Model):
    fullname = models.CharField(_("Full name"), max_length=100)
    campus = models.CharField(_("Campus"), max_length=10, choices=CAMPUS, default="Oye")
    position = models.CharField(_("Position"), max_length=50, help_text="Office post")
    picture = models.ImageField(_("Picture"))
    facebook = models.URLField(_("Facebook profile link"))
    twitter = models.URLField(_("Twitter profile link"))
    linked_in = models.URLField(_("LinkedIn profile link"))
    instagram = models.URLField(_("Instagram profile link"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.fullname
