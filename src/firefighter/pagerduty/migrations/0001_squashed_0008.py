# Generated by Django 4.1.9 on 2023-05-11 18:16

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("incidents", "0006_alter_user_slack_id"),
        ("incidents", "0022_alter_user_name"),
        ("incidents", "0001_initial"),
        ("incidents", "0005_alter_incidentupdate_communication_lead"),
    ]

    operations = [
        migrations.CreateModel(
            name="PagerDutyService",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                (
                    "status",
                    models.CharField(
                        help_text="The current state of the Service. Valid statuses are:\n<ul>\n<li><code>active</code>: The service is enabled and has no open incidents. This is the only status a service can be created with.</li>\n<li><code>warning</code>: The service is enabled and has one or more acknowledged incidents.</li>\n<li><code>critical</code>: The service is enabled and has one or more triggered incidents.</li>\n<li><code>maintenance</code>: The service is under maintenance, no new incidents will be triggered during maintenance mode.</li>\n<li><code>disabled</code>: The service is disabled and will not have any new triggered incidents.</li>\n</ul>",
                        max_length=16,
                    ),
                ),
                (
                    "summary",
                    models.CharField(
                        help_text="A short-form, PD server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier. ",
                        max_length=256,
                    ),
                ),
                (
                    "api_url",
                    models.URLField(
                        help_text="The API show URL at which the object is accessible. Corresponds to PagerDuty API field `self`",
                        max_length=256,
                    ),
                ),
                (
                    "web_url",
                    models.URLField(
                        help_text="A URL at which the entity is uniquely displayed in the Web app. Corresponds to PagerDuty API field `html_url`",
                        max_length=256,
                    ),
                ),
                (
                    "pagerduty_id",
                    models.CharField(
                        db_index=True,
                        default=None,
                        help_text="PagerDuty ID for the service.",
                        max_length=64,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ignore",
                    models.BooleanField(
                        default=False,
                        help_text="Ignore this service. Ignored services can't be triggered, and are hidden ins most places.",
                    ),
                ),
            ],
            options={
                "verbose_name": "PagerDuty service",
                "verbose_name_plural": "PagerDuty services",
            },
        ),
        migrations.CreateModel(
            name="PagerDutyIncident",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="A succinct description of the nature, symptoms, cause, or effect of the incident.",
                        max_length=256,
                    ),
                ),
                (
                    "summary",
                    models.CharField(
                        help_text="A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.",
                        max_length=256,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        help_text="The current status of the incident. Allowed values: triggered, acknowledged, resolved",
                        max_length=16,
                    ),
                ),
                (
                    "urgency",
                    models.CharField(
                        help_text="The urgency of the incident. Allowed values: high, low",
                        max_length=8,
                    ),
                ),
                (
                    "details",
                    models.CharField(
                        help_text="Additional incident details. Corresponds to PagerDuty API field `body.details`",
                        max_length=4000,
                    ),
                ),
                (
                    "api_url",
                    models.URLField(
                        help_text="The API show URL at which the object is accessible. Corresponds to PagerDuty API field `self`",
                        max_length=256,
                    ),
                ),
                (
                    "web_url",
                    models.URLField(
                        help_text="A URL at which the entity is uniquely displayed in the Web app. Corresponds to PagerDuty API field `html_url`",
                        max_length=256,
                    ),
                ),
                (
                    "incident_key",
                    models.CharField(
                        help_text="A string which identifies the incident. Sending subsequent requests referencing the same service and with the same incident_key will result in those requests being rejected if an open incident matches that incident_key.",
                        max_length=128,
                        unique=True,
                    ),
                ),
                (
                    "incident_number",
                    models.IntegerField(
                        help_text="The number of the incident. This is unique across your account."
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "incident",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pagerduty_incident_set",
                        to="incidents.incident",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="pagerduty.pagerdutyservice",
                    ),
                ),
            ],
            options={
                "verbose_name": "PagerDuty incident",
                "verbose_name_plural": "PagerDuty incidents",
            },
        ),
        migrations.CreateModel(
            name="PagerDutyTeam",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "pagerduty_id",
                    models.CharField(db_index=True, max_length=128, unique=True),
                ),
                (
                    "pagerduty_api_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                (
                    "pagerduty_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "PagerDuty team",
                "verbose_name_plural": "PagerDuty teams",
            },
        ),
        migrations.CreateModel(
            name="PagerDutyEscalationPolicy",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "pagerduty_id",
                    models.CharField(db_index=True, max_length=128, unique=True),
                ),
                ("name", models.CharField(max_length=128, unique=True)),
                ("summary", models.CharField(blank=True, max_length=128, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=1024, null=True),
                ),
                (
                    "pagerduty_api_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                (
                    "pagerduty_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                (
                    "teams",
                    models.ManyToManyField(
                        blank=True,
                        related_name="pagerduty_escalation_policy_set",
                        to="pagerduty.pagerdutyteam",
                    ),
                ),
            ],
            options={
                "verbose_name": "PagerDuty escalation policy",
                "verbose_name_plural": "PagerDuty escalation policies",
            },
        ),
        migrations.CreateModel(
            name="PagerDutyUser",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "pagerduty_id",
                    models.CharField(db_index=True, max_length=128, unique=True),
                ),
                (
                    "pagerduty_api_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                (
                    "pagerduty_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, default="", max_length=128),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pagerduty_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "teams",
                    models.ManyToManyField(
                        blank=True,
                        related_name="pagerduty_user_set",
                        to="pagerduty.pagerdutyteam",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                "verbose_name": "PagerDuty user",
                "verbose_name_plural": "PagerDuty users",
            },
        ),
        migrations.CreateModel(
            name="PagerDutySchedule",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "pagerduty_id",
                    models.CharField(db_index=True, max_length=128, unique=True),
                ),
                ("summary", models.CharField(blank=True, max_length=128, null=True)),
                (
                    "pagerduty_api_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                (
                    "pagerduty_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                (
                    "escalation_policies",
                    models.ManyToManyField(
                        blank=True,
                        related_name="pagerduty_schedule_set",
                        to="pagerduty.pagerdutyescalationpolicy",
                    ),
                ),
                (
                    "teams",
                    models.ManyToManyField(
                        blank=True,
                        related_name="pagerduty_schedule_set",
                        to="pagerduty.pagerdutyteam",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="pagerduty_schedule_set",
                        to="pagerduty.pagerdutyuser",
                    ),
                ),
            ],
            options={
                "verbose_name": "PagerDuty schedule",
                "verbose_name_plural": "PagerDuty schedules",
            },
        ),
        migrations.CreateModel(
            name="PagerDutyOncall",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "escalation_level",
                    models.IntegerField(
                        help_text="The escalation level for the on-call."
                    ),
                ),
                (
                    "start",
                    models.DateTimeField(
                        blank=True,
                        help_text="The start of the on-call. If null, the on-call is a permanent user on-call.",
                        null=True,
                    ),
                ),
                (
                    "end",
                    models.DateTimeField(
                        blank=True,
                        help_text="The end of the on-call. If null, the user does not go off-call.",
                        null=True,
                    ),
                ),
                (
                    "escalation_policy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="oncall_set",
                        to="pagerduty.pagerdutyescalationpolicy",
                    ),
                ),
                (
                    "pagerduty_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="oncall_set",
                        to="pagerduty.pagerdutyuser",
                    ),
                ),
                (
                    "schedule",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="oncall_set",
                        to="pagerduty.pagerdutyschedule",
                    ),
                ),
            ],
            options={
                "verbose_name": "PagerDuty on-call",
                "verbose_name_plural": "PagerDuty on-calls",
            },
        ),
        migrations.AddField(
            model_name="pagerdutyservice",
            name="escalation_policy",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pagerduty.pagerdutyescalationpolicy",
            ),
        ),
    ]
