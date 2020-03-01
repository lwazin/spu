from django.shortcuts import render
from django.contrib.auth import (
    login as auth_login,  authenticate, logout as _logout)
import random
import string

from .models import Personal, NextOfKin, Fees, SouthAfricanQualifications, InternationalQualifications, User, TertiaryEducationStudies

# Create your views here.


def applicant(request):

    def ran_gen(size=6, chars=string.ascii_letters):
        x = ''.join(random.choice(chars) for x in range(size))
        return x

    if request.method == 'POST':

        # Create User Using personal_id

        temp_User = User()

        temp_User.username = request.POST["personal_id"]
        temp_User.password = ran_gen()
        temp_User.first_name = request.POST["personal_name"]
        temp_User.last_name = request.POST["personal_surname"]
        temp_User.email = request.POST["personal_email"]

        temp_User.save()

        auth_login(request, temp_User)
        print('You are logged in!')

        # Personal Variables

        temp_Personal = Personal()
        temp_Personal.user = request.user

        temp_Personal.personal_name = request.POST["personal_name"]
        temp_Personal.personal_surname = request.POST["personal_surname"]
        temp_Personal.personal_title = request.POST["personal_title"]
        temp_Personal.personal_gender = request.POST["personal_gender"]
        temp_Personal.personal_date_of_birth = request.POST["personal_date_of_birth"]
        temp_Personal.personal_population = request.POST["personal_population"]
        temp_Personal.personal_marital = request.POST["personal_marital"]
        temp_Personal.personal_language = request.POST["personal_language"]
        temp_Personal.personal_religion = request.POST["personal_religion"]
        temp_Personal.personal_disability = request.POST["personal_disability"]
        temp_Personal.personal_address = request.POST["personal_address"]
        temp_Personal.personal_city = request.POST["personal_city"]
        temp_Personal.personal_province = request.POST["personal_province"]
        temp_Personal.personal_country = request.POST["personal_country"]
        temp_Personal.personal_postal = request.POST["personal_postal"]
        temp_Personal.personal_mobile1 = request.POST["personal_mobile1"]
        temp_Personal.personal_mobile2 = request.POST["personal_mobile2"]
        temp_Personal.personal_email = request.POST["personal_email"]
        temp_Personal.personal_citizenship = request.POST["personal_citizenship"]
        temp_Personal.personal_id = request.POST["personal_id"]

        temp_Personal.save()

        # Next Of Kin Variables

        temp_NextOfKin = NextOfKin()
        temp_NextOfKin.applicant = temp_Personal

        temp_NextOfKin.next_of_kin_relationship = request.POST['next_of_kin_relationship']
        temp_NextOfKin.next_of_kin_title = request.POST['next_of_kin_title']
        temp_NextOfKin.next_of_kin_surname = request.POST['next_of_kin_surname']
        temp_NextOfKin.next_of_kin_name = request.POST['next_of_kin_name']
        temp_NextOfKin.next_of_kin_id = request.POST['next_of_kin_id']
        temp_NextOfKin.next_of_kin_address = request.POST['next_of_kin_address']
        temp_NextOfKin.next_of_kin_city = request.POST['next_of_kin_city']
        temp_NextOfKin.next_of_kin_province = request.POST['next_of_kin_province']
        temp_NextOfKin.next_of_kin_country = request.POST['next_of_kin_country']
        temp_NextOfKin.next_of_kin_code = request.POST['next_of_kin_code']
        temp_NextOfKin.next_of_kin_mobile1 = request.POST['next_of_kin_mobile1']
        temp_NextOfKin.next_of_kin_mobile2 = request.POST['next_of_kin_mobile2']
        temp_NextOfKin.next_of_kin_email = request.POST['next_of_kin_email']

        temp_NextOfKin.save()

        # Liable For Settlement Of Fees

        temp_Fees = Fees()
        temp_Fees.applicant = temp_Personal

        temp_Fees.fees_title = request.POST['fees_title']
        temp_Fees.fees_surname = request.POST['fees_surname']
        temp_Fees.fees_name = request.POST['fees_name']
        temp_Fees.fees_id = request.POST['fees_id']
        temp_Fees.fees_address = request.POST['fees_address']
        temp_Fees.fees_city = request.POST['fees_city']
        temp_Fees.fees_province = request.POST['fees_province']
        temp_Fees.fees_country = request.POST['fees_country']
        temp_Fees.fees_code = request.POST['fees_code']
        temp_Fees.fees_mobile1 = request.POST['fees_mobile1']
        temp_Fees.fees_mobile2 = request.POST['fees_mobile2']
        temp_Fees.fees_email = request.POST['fees_email']

        temp_Fees.save()

        # South African Qualifications

        temp_SouthAfricanQualifications = SouthAfricanQualifications()
        temp_SouthAfricanQualifications.applicant = temp_Personal

        temp_SouthAfricanQualifications.sa_qualification_school = request.POST[
            'sa_qualification_school']
        temp_SouthAfricanQualifications.sa_qualification_city = request.POST[
            'sa_qualification_city']
        temp_SouthAfricanQualifications.sa_qualification_write = request.POST[
            'sa_qualification_write']
        temp_SouthAfricanQualifications.sa_qualification_exam = request.POST[
            'sa_qualification_exam']
        temp_SouthAfricanQualifications.sa_qualification_nsc1 = request.POST[
            'sa_qualification_nsc1']
        temp_SouthAfricanQualifications.sa_qualification_nsc2 = request.POST[
            'sa_qualification_nsc2']
        temp_SouthAfricanQualifications.sa_qualification_nsc3 = request.POST[
            'sa_qualification_nsc3']
        temp_SouthAfricanQualifications.sa_qualification_nsc4 = request.POST[
            'sa_qualification_nsc4']
        temp_SouthAfricanQualifications.sa_qualification_nsc5 = request.POST[
            'sa_qualification_nsc5']
        temp_SouthAfricanQualifications.sa_qualification_nsc6 = request.POST[
            'sa_qualification_nsc6']
        temp_SouthAfricanQualifications.sa_qualification_nsc7 = request.POST[
            'sa_qualification_nsc7']
        temp_SouthAfricanQualifications.sa_qualification_nsc8 = request.POST[
            'sa_qualification_nsc8']
        temp_SouthAfricanQualifications.sa_qualification_authority = request.POST[
            'sa_qualification_authority']

        temp_SouthAfricanQualifications.save()

        # International Qualifications

        temp_InternationalQualifications = InternationalQualifications()
        temp_InternationalQualifications.applicant = temp_Personal

        temp_InternationalQualifications.int_qualification_complete = request.POST[
            'int_qualification_complete']
        temp_InternationalQualifications.int_qualification_month = request.POST[
            'int_qualification_month']
        temp_InternationalQualifications.int_qualification_authority = request.POST[
            'int_qualification_authority']

        temp_InternationalQualifications.save()

        # Previous or Current Tertiary Education

        temp_TertiaryEducationStudies = TertiaryEducationStudies()
        temp_TertiaryEducationStudies.applicant = temp_Personal

        temp_TertiaryEducationStudies.current_study_programme = request.POST[
            'current_study_programme']
        temp_TertiaryEducationStudies.current_institution = request.POST['current_institution']
        temp_TertiaryEducationStudies.current_student_number = request.POST[
            'current_student_number']
        temp_TertiaryEducationStudies.current_int_qualification_complete = request.POST[
            'current_int_qualification_complete']
        temp_TertiaryEducationStudies.current_start_date = request.POST["current_start_date"]
        temp_TertiaryEducationStudies.current_end_date = request.POST["current_end_date"]
        temp_TertiaryEducationStudies.current_graduation_date = request.POST[
            "current_graduation_date"]
        temp_TertiaryEducationStudies.current_int_qualification_complete = request.POST[
            'current_int_qualification_complete']

        temp_TertiaryEducationStudies.current_study_programme2 = request.POST[
            'current_study_programme2']
        temp_TertiaryEducationStudies.current_institution2 = request.POST['current_institution2']
        temp_TertiaryEducationStudies.current_student_number2 = request.POST[
            'current_student_number2']
        temp_TertiaryEducationStudies.current_int_qualification_complete2 = request.POST[
            'current_int_qualification_complete']
        temp_TertiaryEducationStudies.current_start_date2 = request.POST["current_start_date2"]
        temp_TertiaryEducationStudies.current_end_date2 = request.POST["current_end_date2"]
        temp_TertiaryEducationStudies.current_graduation_date2 = request.POST[
            "current_graduation_date2"]
        temp_TertiaryEducationStudies.current_int_qualification_complete2 = request.POST[
            'current_int_qualification_complete2']

        temp_TertiaryEducationStudies.save()

    return render(request, 'index.html')
