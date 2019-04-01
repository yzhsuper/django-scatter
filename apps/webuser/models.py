# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _


class WebUser(AbstractBaseUser, PermissionsMixin):

    email = models.CharField(max_length=128, unique=True, help_text='邮箱', null=True, blank=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = WebUserManager()

    class Meta:
        swappable = "AUTH_USER_MODEL"
        db_table = 'web_user'
