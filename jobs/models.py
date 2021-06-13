from django.db import models
from user.models import CustomUser


class MtoJobCategories(models.Model):
    name = models.CharField(max_length=20, help_text="eg data entry")

    def __str__(self):
        return f"{self.name}"


class MicroTasks(models.Model):
    name = models.CharField(max_length=100, help_text="JO Name")
    category = models.ForeignKey(MtoJobCategories, on_delete=models.CASCADE, help_text="job category")
    target_date = models.DateField()
    description = models.TextField(help_text="Job Description")
    sample = models.FileField(upload_to='samples/%Y/%m/', default="samples/default.pdf", help_text="upload Job Sample")
    instructions = models.FileField(upload_to='samples/%Y/%m/', default="samples/default.pdf",
                                    help_text="Upload Job Instructions")
    quantity = models.IntegerField(help_text="Quantity of the Job")
    people_required = models.IntegerField(help_text="Number of people required ")
    skills = models.TextField()
    cost = models.IntegerField(help_text="Job Cost in AED")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class EvaluationStatus(models.Model):
    description = models.ForeignKey(MicroTasks, on_delete=models.CASCADE)


class MTOJobs(models.Model):
    job_id = models.ForeignKey(MicroTasks, on_delete=models.CASCADE)
    assigned_to_mto_id = models.IntegerField(help_text="primary key of the assigned mto from mto table")
    due_date = models.DateField()
    assigned_date = models.DateField()
    fees = models.FloatField()
    rating = models.IntegerField(help_text="Rating/Evaluation")
    payment_status = models.IntegerField(help_text="Mto payment status id")
    completed_date = models.DateField(help_text="Completed Date")
    output_path = models.FileField(upload_to='output/%Y/%m/', default="output/default.pdf",
                                   help_text="path of submitted job")
    evaluation_status = models.ForeignKey(EvaluationStatus, on_delete=models.CASCADE)


class MtoRoles(models.Model):
    role_description = models.CharField(max_length=50, help_text="eg assignees, admins, developers, evaluators")


class MtoAdminUsers(CustomUser):
    name = models.CharField(max_length=100)
    varal_role_id = models.ForeignKey(MtoRoles, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'MTO Admin User'
        verbose_name_plural = 'MTO Admin Users'
