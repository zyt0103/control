from django.contrib import admin
from .models import DemodModel, DemodType, DemodResult

@admin.register(DemodModel)
class DemodModelAdmin(admin.ModelAdmin):
    list_display = (
        "signal_id",
        "demod_type_id",
        "demod_prob_fact",
        "demod_prob_theory",
        "create_datetime",
        "deleted",
        "deleted_at"
    )


@admin.register(DemodType)
class DemodTypeAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "demod_type_id",
        "demod_type_name",
        "ant_num",
        "protocol",
        "sync_type",
        "create_datetime",
        "deleted",
        "deleted_at"
    )


@admin.register(DemodResult)
class DemodResultAdmin(admin.ModelAdmin):
    list_display = (
        "signal_id",
        "demod_type_id",
        "signal_demoded",
        "create_datetime",
        "deleted",
        "deleted_at"
    )