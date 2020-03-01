from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Personal(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    personal_name = models.CharField(max_length=64, blank=False)
    personal_surname = models.CharField(max_length=64, blank=False)
    personal_title = models.CharField(max_length=64, blank=False)
    personal_gender = models.CharField(max_length=64, blank=False)
    personal_population = models.CharField(max_length=64, blank=False)
    personal_marital = models.CharField(max_length=64, blank=False)
    personal_language = models.CharField(max_length=64, blank=False)
    personal_religion = models.CharField(max_length=64, blank=False)
    personal_disability = models.CharField(max_length=64, blank=False)
    personal_address = models.CharField(max_length=70, blank=False)
    personal_city = models.CharField(max_length=64, blank=False)
    personal_province = models.CharField(max_length=64, blank=False)
    personal_country = models.CharField(max_length=64, blank=False)
    personal_postal = models.CharField(max_length=64, blank=False)
    personal_mobile1 = models.CharField(max_length=20, blank=False)
    personal_mobile2 = models.CharField(max_length=20, blank=True)
    personal_citizenship = models.CharField(max_length=64, blank=False)
    personal_id = models.CharField(max_length=64, blank=False)
    personal_email = models.EmailField(blank=False)
    personal_date_of_birth = models.DateField(blank=False)


class NextOfKin(models.Model):

    applicant = models.ForeignKey(
        Personal, related_name='next_of_kin', on_delete=models.CASCADE, default=None)

    next_of_kin_relationship = models.CharField(max_length=64, blank=False)
    next_of_kin_title = models.CharField(max_length=64, blank=False)
    next_of_kin_surname = models.CharField(max_length=64, blank=False)
    next_of_kin_name = models.CharField(max_length=64, blank=False)
    next_of_kin_id = models.CharField(max_length=64, blank=False)
    next_of_kin_address = models.CharField(max_length=70, blank=False)
    next_of_kin_city = models.CharField(max_length=64, blank=False)
    next_of_kin_province = models.CharField(max_length=64, blank=False)
    next_of_kin_country = models.CharField(max_length=64, blank=False)
    next_of_kin_code = models.CharField(max_length=64, blank=False)
    next_of_kin_mobile1 = models.CharField(max_length=64, blank=False)
    next_of_kin_mobile2 = models.CharField(max_length=64, blank=True)
    next_of_kin_email = models.EmailField(blank=False)


class Fees(models.Model):

    applicant = models.ForeignKey(
        Personal, related_name='fees', on_delete=models.CASCADE, default=None)

    fees_title = models.CharField(max_length=64, blank=False)
    fees_surname = models.CharField(max_length=64, blank=False)
    fees_name = models.CharField(max_length=64, blank=False)
    fees_id = models.CharField(max_length=64, blank=False)
    fees_address = models.CharField(max_length=70, blank=False)
    fees_city = models.CharField(max_length=64, blank=False)
    fees_province = models.CharField(max_length=64, blank=False)
    fees_country = models.CharField(max_length=64, blank=False)
    fees_code = models.CharField(max_length=64, blank=False)
    fees_mobile1 = models.CharField(max_length=64, blank=False)
    fees_mobile2 = models.CharField(max_length=64, blank=True)
    fees_email = models.EmailField(blank=False)


class SouthAfricanQualifications(models.Model):

    applicant = models.ForeignKey(
        Personal, related_name='south_african_qualifications', on_delete=models.CASCADE, default=None)

    sa_qualification_school = models.CharField(max_length=64, blank=True)
    sa_qualification_city = models.CharField(max_length=64, blank=True)
    sa_qualification_write = models.CharField(max_length=64, blank=True)
    sa_qualification_exam = models.CharField(max_length=64, blank=True)
    sa_qualification_nsc1 = models.CharField(max_length=64, blank=True)
    sa_qualification_nsc2 = models.CharField(max_length=64, blank=True)
    sa_qualification_nsc3 = models.CharField(max_length=64, blank=True)
    sa_qualification_nsc4 = models.CharField(max_length=64, blank=True)
    sa_qualification_nsc5 = models.CharField(max_length=64, blank=True)
    sa_qualification_nsc6 = models.CharField(max_length=64, blank=True)
    sa_qualification_nsc7 = models.CharField(max_length=64, blank=True)
    sa_qualification_nsc8 = models.CharField(max_length=64, blank=True)
    sa_qualification_authority = models.CharField(max_length=64, blank=True)


class InternationalQualifications(models.Model):

    applicant = models.ForeignKey(
        Personal, related_name='international_qualifications', on_delete=models.CASCADE, default=None)

    int_qualification_complete = models.CharField(max_length=64, blank=True)
    int_qualification_month = models.CharField(max_length=64, blank=True)
    int_qualification_authority = models.CharField(max_length=64, blank=True)


class TertiaryEducationStudies(models.Model):

    applicant = models.ForeignKey(
        Personal, related_name='tertiary_education_studies', on_delete=models.CASCADE, default=None)

    current_study_programme = models.CharField(max_length=64, blank=True)
    current_institution = models.CharField(max_length=64, blank=True)
    current_student_number = models.CharField(max_length=64, blank=True)
    current_int_qualification_complete = models.CharField(
        max_length=64, blank=True)
    current_start_date = models.DateField()
    current_end_date = models.DateField()
    current_graduation_date = models.DateField()
    current_int_qualification_complete = models.DateField()

    current_study_programme2 = models.CharField(max_length=64, blank=True)
    current_institution2 = models.CharField(max_length=64, blank=True)
    current_student_number2 = models.CharField(max_length=64, blank=True)
    current_int_qualification_complete = models.CharField(
        max_length=64, blank=True)
    current_start_date2 = models.DateField()
    current_end_date2 = models.DateField()
    current_graduation_date2 = models.DateField()
    current_int_qualification_complete2 = models.DateField()
