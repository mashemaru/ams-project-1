from django.db import models


class user(models.Model):
    user_email = models.EmailField()
    user_password = models.CharField(max_length=60)
    user_givenName = models.CharField(max_length=60)
    user_middleInitial = models.CharField(max_length=60)
    user_surname = models.CharField(max_length=60)
    user_type = models.CharField(max_length=60)


class accrediting_body(models.Model):
    accrediting_body = models.CharField(max_length=60)


class files(models.Model):
    file_name = models.CharField(max_length=60)
    file_type = models.CharField(max_length=30)
    file_document = models.FileField(max_length=250)


class team(models.Model):
    team_name = models.CharField(max_length=60)


class degree_program(models.Model):
    program_code = models.CharField(max_length=60)
    program_name = models.CharField(max_length=60)
    program_est = models.CharField(max_length=60)
    program_grads = models.CharField(max_length=60)


class document_outline(models.Model):
    accrediting_body_id = models.ForeignKey(accrediting_body, default='1', on_delete=models.CASCADE)
    document_name = models.CharField(max_length=120)


class document_outline_item(models.Model):
    document_outline_id = models.ForeignKey(document_outline, default='1', on_delete=models.CASCADE)
    parent_document_outline_item_id = models.ForeignKey('self', on_delete=models.CASCADE)
    item_title = models.CharField(max_length=60)
    item_type = models.CharField(max_length=60)


class ongoing_accreditation(models.Model):
    accrediting_id = models.ForeignKey(accrediting_body, default='1', on_delete=models.CASCADE)
    degree_program_id = models.ForeignKey(degree_program, default='1', on_delete=models.CASCADE)
    teams_id = models.ForeignKey(team, default='1', on_delete=models.CASCADE)
    document_id = models.ForeignKey(document_outline, default='1', on_delete=models.CASCADE)


class completed_accreditation(models.Model):
    accrediting_id = models.ForeignKey(accrediting_body, default='1', on_delete=models.CASCADE)
    degree_program_id = models.ForeignKey(degree_program, default='1', on_delete=models.CASCADE)
    teams_id = models.ForeignKey(team, default='1', on_delete=models.CASCADE)
    document_id = models.ForeignKey(document_outline, default='1', on_delete=models.CASCADE)
    completed_result = models.CharField(max_length=60)
    completed_year = models.CharField(max_length=60)


class chapter_team(models.Model):
    accrediting_id = models.ForeignKey(accrediting_body, default='1', on_delete=models.CASCADE)
    teams_id = models.ForeignKey(team, default='1', on_delete=models.CASCADE)
    document_id = models.ForeignKey(document_outline, default='1', on_delete=models.CASCADE)
    document_outline_item_id = models.ForeignKey(document_outline_item, default='1', on_delete=models.CASCADE)


class user_teams(models.Model):
    accrediting_id = models.ForeignKey(accrediting_body, default='1', on_delete=models.CASCADE)
    teams_id = models.ForeignKey(team, default='1', on_delete=models.CASCADE)
    user_id = models.ForeignKey(user, default='1', on_delete=models.CASCADE)


class prev_accreditation(models.Model):
    degree_program_id = models.ForeignKey(degree_program, default='1', on_delete=models.CASCADE)
    accreditation_agency = models.CharField(max_length=60)
    accreditation_result = models.CharField(max_length=60)
    accreditation_year = models.CharField(max_length=60)

# Create your models here.
