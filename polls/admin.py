# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from . models import StudentApps, StudentReg, StaffReg, Department

admin.site.register(StudentApps)
admin.site.register(StudentReg)
admin.site.register(StaffReg)
admin.site.register(Department)

