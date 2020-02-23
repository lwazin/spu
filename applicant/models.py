from django.db import models

# Create your models here.


class Applicant(models.Model):

    # 2. PERSONAL DETAILS
    gender = models.TextField(max_length=30)
    date_of_birth = models.DateField()

    # 3. CITIZENSHIP
    south_african = models.BooleanField(default=True)
    id_number = models.SlugField()

    # 4. PERSONAL INFORMATION
    population_group = models.SlugField()
    marital_status = models.SlugField()
    home_language = models.SlugField()
    religious_affiliation = models.SlugField()

    # 6. PERSONAL INFORMATION (Next Of Kin)
    nok_relationship = models.TextField(max_length=30)

    # 8. ACADEMIC HISTORY – SOUTH AFRICAN QUALIFICATIONS
    school = models.TextField(max_length=70)
    location = models.TextField(max_length=70)
    writing_loc = models.TextField(max_length=70, blank=True)
    exam_number = models.SlugField(blank=True)
    authority = models.TextField(max_length=50)

    # 9. INTERNATIONAL QUALIFICATIONS
    qualification_complete = models.BooleanField(blank=True)
    exam_month = models.SlugField(blank=True)


class StudyHistory(models.Model):

    # 10. PREVIOUS AND CURRENT TERTIARY EDUCATION STUDIES
    applicant = models.ForeignKey(
        Applicant, related_name='applicant', on_delete=models.CASCADE)
    study_programme = models.TextField(max_length=70)
    institution = models.TextField(max_length=70)
    student_number = models.SlugField()
    full_time = models.BooleanField(default=True)
    registration_date0 = models.DateField()
    registration_date1 = models.DateField()
    graduation_date = models.DateField()
    status = models.SlugField()


class Subject(models.Model):

    applicant = models.ForeignKey(
        Applicant, related_name='applicant', on_delete=models.CASCADE)
    subject = models.TextField(max_length=30, blank=True)


class Details(models.Model):

    applicant = models.ForeignKey(
        Applicant, related_name='applicant', on_delete=models.CASCADE)

    detail_type = models.SlugField()

    title = models.TextField(max_length=30)
    surname = models.TextField(max_length=30)
    full_names = models.TextField(max_length=30)

    street = models.TextField(max_length=70)
    city = models.TextField(max_length=70)
    province = models.TextField(max_length=70)
    country = models.TextField(max_length=70)
    code = models.SlugField()

    number_1 = models.SlugField()
    number_2 = models.SlugField(blank=True)
    number_3 = models.SlugField(blank=True)
    email = models.EmailField()


class Choice(models.Model):

    # 1. CHOICE OF STUDY PROGRAMME
    applicant = models.ForeignKey(
        Applicant, related_name='applicant', on_delete=models.CASCADE)
    choice = models.TextField(max_length=30)
    choice_order = models.IntegerField(default=0)


class SpecialNeed(models.Model):

    # 4. PERSONAL INFORMATION (Disability or Special Needs)
    applicant = models.ForeignKey(
        Applicant, related_name='applicant', on_delete=models.CASCADE)
    special_need = models.TextField(max_length=30)


class Sport(models.Model):

    # 4. PERSONAL INFORMATION (Sport Involvement)
    applicant = models.ForeignKey(
        Applicant, related_name='applicant', on_delete=models.CASCADE)
    sport = models.TextField(max_length=30)
    level = models.TextField(max_length=50)


class Document(models.Model):

    # 4. PERSONAL INFORMATION (Sport Involvement)
    applicant = models.ForeignKey(
        Applicant, related_name='applicant', on_delete=models.CASCADE)
    document_type = models.SlugField()
    document = models.ImageField(upload_to='documents')
