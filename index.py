import os
from flask import Flask, render_template, request, session, sessions, redirect, url_for
from saveClassInfo import updateClassInfo, selectClassInfo
from werkzeug.utils import secure_filename
from StdDetails import addStd, removeStd, getStd
from SubjectDetails import addSubject, removeSubject, getSubject, mapSubjectPrice, getMapSubjectPrice
from base64 import b64encode
from StudentRegistrationForm import getStudentRegistrationFullSubject, getStudentProfileImg, getLogoImg, registerNewStudent, getSubjectList, getSelStdList, StudentRegistration_Fess_Subject
from StudentProfile import getStudentProfile, getStudentProfileByName

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.secret_key = 'wkk'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def Starup():
    return render_template('MainScreen.html')


@app.route('/MainScreen.html', methods=['POST', 'GET'])
def MainPageHtml():
    return render_template('MainScreen.html')


@app.route('/mainpage', methods=['POST', 'GET'])
def MainPage():
    if request.method == 'POST':
        return render_template('MainScreen.html')


@app.route('/Settings.html', methods=['POST', 'GET'])
def SettingHTML():
    return render_template('Settings.html')


@app.route('/ClassInfo.html', methods=['POST', 'GET'])
def ClassInfohtml():
    if request.method == 'POST':
        ClassName = request.form.get('ClassName')
        ClassEmail = request.form.get('ClassEmail')
        ClassAddress = request.form.get('ClassAddress')
        ClassContact = request.form.get('ClassContact')
        ClassLogo = request.form.get('ClassLogo')
        ClassInfoData = [ClassName, ClassEmail,
                         ClassAddress, ClassContact, ClassLogo]
        updateClassInfo(ClassInfoData)
        Classinfo = selectClassInfo()
        ClassData = list(Classinfo)
        Classname = str(ClassData[0][0])
        Address1 = str(ClassData[0][1])
        Email = str(ClassData[0][2])
        ContactInfo = str(ClassData[0][3])
        Logo = str(ClassData[0][4])
        LastUpdatedDate = str(ClassData[0][5])

        return render_template('ClassInfo.html', LogoHtml=Logo, ContactInfoHtml=ContactInfo, ClassnameHtml=Classname, Address1html=Address1, EmailHtml=Email, LastUpdatedDate=LastUpdatedDate)
    if request.method == 'GET':
        Classinfo = selectClassInfo()
        ClassData = list(Classinfo)
        Classname = str(ClassData[0][0])
        Address1 = str(ClassData[0][1])
        Email = str(ClassData[0][2])
        ContactInfo = str(ClassData[0][3])
        Logo = ClassData[0][4]
        Logoimage = b64encode(Logo).decode("utf-8")
        LastUpdatedDate = str(ClassData[0][5])
        return render_template('ClassInfo.html', LogoHtml=Logoimage, ContactInfoHtml=ContactInfo, ClassnameHtml=Classname, Address1html=Address1, EmailHtml=Email, LastUpdatedDate=LastUpdatedDate)


@app.route('/addclassinfo', methods=['POST', 'GET'])
def ClassInfo():
    if request.method == 'POST':
        ClassName = request.form.get('ClassName')
        ClassEmail = request.form.get('ClassEmail')
        ClassAddress = request.form.get('ClassAddress')
        ClassContact = request.form.get('ClassContact')
        ClassLogo = request.form.get('ClassLogo')
        TempLogo = request.files["file"]
        TempLogoBinary = TempLogo.read()
        ClassInfoData = [ClassName, ClassEmail,
                         ClassAddress, ClassContact, ClassLogo, TempLogoBinary]
        updateClassInfo(ClassInfoData)
        Classinfo = selectClassInfo()
        ClassData = list(Classinfo)
        Classname = str(ClassData[0][0])
        Address1 = str(ClassData[0][1])
        Email = str(ClassData[0][2])
        ContactInfo = str(ClassData[0][3])
        Logo = ClassData[0][4]
        Logoimage = b64encode(Logo).decode("utf-8")
        LastUpdatedDate = str(ClassData[0][5])
        return render_template('ClassInfo.html', LogoHtml=Logoimage, ContactInfoHtml=ContactInfo, ClassnameHtml=Classname, Address1html=Address1, EmailHtml=Email, LastUpdatedDate=LastUpdatedDate)
    if request.method == 'GET':
        Classinfo = selectClassInfo()
        ClassData = list(Classinfo)
        Classname = str(ClassData[0][0])
        Address1 = str(ClassData[0][1])
        Email = str(ClassData[0][2])
        ContactInfo = str(ClassData[0][3])
        Logo = str(ClassData[0][4])
        LastUpdatedDate = str(ClassData[0][5])
        return render_template('ClassInfo.html', LogoHtml=Logo, ContactInfoHtml=ContactInfo, ClassnameHtml=Classname, Address1html=Address1, EmailHtml=Email, LastUpdatedDate=LastUpdatedDate)


@app.route('/AddClass.html', methods=['POST', 'GET'])
def AddClassHtml():
    stdDetails = getStd()
    return render_template('AddClass.html', stdlist=stdDetails)


@app.route('/stdinfo', methods=['POST', 'GET'])
def AddStdClass():
    if request.method == 'POST':
        clicked = request.form.get('submitButton')
        if clicked == 'AddStdInfo':
            StdName = request.form.get('StdName')
            addStd(StdName)
            stdDetails = getStd()
            return render_template('AddClass.html', stdlist=stdDetails)
        if clicked == 'RemoveStdInfo':
            StdID = request.form.get('Std_detailsName')

            removeStd(StdID)
            stdDetails = getStd()
            return render_template('AddClass.html', stdlist=stdDetails)

    if request.method == 'GET':
        stdDetails = getStd()
        return render_template('AddClass.html', stdlist=stdDetails)


@app.route('/Subjects.html', methods=['POST', 'GET'])
def AddSubjectHtml():
    stdDetails = getStd()
    subjectDetails = getSubject()
    SubjectPriceMapping = getMapSubjectPrice()
    return render_template('Subjects.html', Subjectlist=subjectDetails, stdlist=stdDetails, result=SubjectPriceMapping)


@app.route('/subjectsinfo', methods=['POST', 'GET'])
def AddSubject():
    if request.method == 'POST':
        clicked = request.form.get('submitButton')
        if clicked == 'AddSubjectName':
            StdName = request.form.get('SubjectName')
            addSubject(StdName)
            stdDetails = getStd()
            subjectDetails = getSubject()
            SubjectPriceMapping = getMapSubjectPrice()
            return render_template('Subjects.html', Subjectlist=subjectDetails, stdlist=stdDetails, result=SubjectPriceMapping)
        if clicked == 'RemoveSubjectName':
            SubjectID = request.form.get('Subject_detailsName')
            removeStd(SubjectID)
            stdDetails = getStd()
            subjectDetails = getSubject()
            SubjectPriceMapping = getMapSubjectPrice()
            return render_template('Subjects.html', Subjectlist=subjectDetails, stdlist=stdDetails, result=SubjectPriceMapping)
        if clicked == 'MapSubjectName':
            Std_detailsNameID = request.form.get('Std_detailsNameID')
            Subject_detailsNameID = request.form.get('Subject_detailsNameID')
            SubjectPrice = request.form.get('SubjectPrice')
            MappingSubjectPriceData = [
                Std_detailsNameID, Subject_detailsNameID, SubjectPrice]
            mapSubjectPrice(MappingSubjectPriceData)
            stdDetails = getStd()
            subjectDetails = getSubject()
            SubjectPriceMapping = getMapSubjectPrice()
            return render_template('Subjects.html', Subjectlist=subjectDetails, stdlist=stdDetails, result=SubjectPriceMapping)

    if request.method == 'GET':
        stdDetails = getStd()
        subjectDetails = getSubject()
        SubjectPriceMapping = getMapSubjectPrice()
        return render_template('Subjects.html', Subjectlist=subjectDetails, stdlist=stdDetails, result=SubjectPriceMapping)


@app.route('/StudentRegistration.html', methods=['POST', 'GET'])
def StudentRegistrationHtml():
    if request.method == 'GET':
        logoimg = getLogoImg()
        Classinfo = selectClassInfo()
        ClassData = list(Classinfo)
        Classname = str(ClassData[0][0])
        Address1 = str(ClassData[0][1])
        Email = str(ClassData[0][2])
        ContactInfo = str(ClassData[0][3])
        stdDetails = getStd()
        return render_template('StudentRegistration.html', stdlist=stdDetails, logoimage=logoimg, ClassnameHtml=Classname, Address1Html=Address1, EmailHtml=Email, ContactInfoHtml=ContactInfo)


@app.route('/RegisterStudent', methods=['POST', 'GET'])
def StudentRegistration():
    if request.method == 'POST':
        StudentFName = request.form.get('StudentFName')
        StudentMName = request.form.get('StudentMName')
        StudentLName = request.form.get('StudentLName')
        StudentAddress = request.form.get('StudentAddress')
        StudentEmail = request.form.get('StudentEmail')
        StudentContactInfo = request.form.get('StudentContactInfo')
        Student_Dob = request.form.get('Student_Dob')
        Student_gender = request.form.get('Student_gender')
        Student_AadhaarNo = request.form.get('Student_AadhaarNo')
        Student_Reference = request.form.get('Student_Reference')
        Student_FatherName = request.form.get('Student_FatherName')
        Student_FatherContactNo = request.form.get('Student_FatherContactNo')
        Student_MotherName = request.form.get('Student_MotherName')
        Student_MotherContactNo = request.form.get('Student_MotherContactNo')
        Student_ProfilePic = request.files["file"]
        Student_ProfilePicBinary = Student_ProfilePic.read()
        Student_TotalFees = request.form.get('total')
        Student_Discount = request.form.get('discount')
        Student_FinalTotal = request.form.get('finaltotal')
        Std_detailsName = request.form.get('Std_detailsName')
        Student_Subject_detailsName = request.form.getlist(
            'Subject_detailsName')
        StudentData = [StudentFName, StudentMName, StudentLName, StudentAddress, StudentEmail, StudentContactInfo, Student_Dob, Student_gender,
                       Student_AadhaarNo, Student_Reference, Student_FatherName, Student_FatherContactNo, Student_MotherName, Student_MotherContactNo, Student_ProfilePicBinary]
        StudentRollNo = registerNewStudent(StudentData)
        Student_SubjectOpted = [
            StudentRollNo, Student_TotalFees, Student_Discount, Student_FinalTotal, Std_detailsName, Student_Subject_detailsName]
        StudentRegistration_Fess_Subject(Student_SubjectOpted)
        StudentRollNoList = [StudentRollNo]
        studentimageDB = getStudentProfileImg(StudentRollNo)
        fullsubjectlist = getStudentRegistrationFullSubject(StudentRollNoList)

        logoimg = getLogoImg()
        Classinfo = selectClassInfo()
        ClassData = list(Classinfo)
        Classname = str(ClassData[0][0])
        Address1 = str(ClassData[0][1])
        Email = str(ClassData[0][2])
        ContactInfo = str(ClassData[0][3])

        return render_template('StudentRegistrationPrint.html', fullsubjectlistHTML=fullsubjectlist, StudentRollNoHTML=StudentRollNo, studentimage=studentimageDB, Student_FinalTotalHTML=Student_FinalTotal, Student_TotalFeesHTML=Student_TotalFees, Student_DiscountHTML=Student_Discount, Student_MotherContactNoHtml=Student_MotherContactNo, Student_MotherNameHtml=Student_MotherName, Student_FatherContactNoHtml=Student_FatherContactNo, Student_FatherNameHtml=Student_FatherName, Student_ReferenceHtml=Student_Reference, Student_AadhaarNoHtml=Student_AadhaarNo, Student_genderHtml=Student_gender, Student_DobHtml=Student_Dob, StudentContactInfoHtml=StudentContactInfo, StudentEmailHtml=StudentEmail, StudentAddressHtml=StudentAddress, StudentLNameHtml=StudentLName, StudentMNameHtml=StudentMName, StudentFNameHtml=StudentFName, logoimage=logoimg, ClassnameHtml=Classname, Address1Html=Address1, EmailHtml=Email, ContactInfoHtml=ContactInfo)


@app.route('/RegisterStudentPrint', methods=['POST', 'GET'])
def StudentRegistrationfinalPrint():
    return render_template('MainScreen.html')


@app.route('/StudentRegistrationStdSubject', methods=['GET', 'POST'])
def StudentRegistrationStdSubject():
    if request.method == 'POST':
        logoimg = getLogoImg()
        Classinfo = selectClassInfo()
        ClassData = list(Classinfo)
        Classname = str(ClassData[0][0])
        Address1 = str(ClassData[0][1])
        Email = str(ClassData[0][2])
        ContactInfo = str(ClassData[0][3])
        StudentFName = request.form.get('StudentFName')
        StudentMName = request.form.get('StudentMName')
        StudentLName = request.form.get('StudentLName')
        StudentAddress = request.form.get('StudentAddress')
        StudentEmail = request.form.get('StudentEmail')
        StudentContactInfo = request.form.get('StudentContactInfo')
        Student_Dob = request.form.get('Student_Dob')
        Student_gender = request.form.get('Student_gender')
        Student_AadhaarNo = request.form.get('Student_AadhaarNo')
        Student_Reference = request.form.get('Student_Reference')
        Student_FatherName = request.form.get('Student_FatherName')
        Student_FatherContactNo = request.form.get('Student_FatherContactNo')
        Student_MotherName = request.form.get('Student_MotherName')
        Student_MotherContactNo = request.form.get('Student_MotherContactNo')
        Std_detailsName = request.form.get('Std_detailsName')
        stdDetails = getStd()
        Subject_detailsName = getSubjectList(Std_detailsName)
        SelStd_detailsName = getSelStdList(Std_detailsName)
        return render_template('StudentRegistrationNext.html', selstdlist=SelStd_detailsName, subjectlist=Subject_detailsName, Student_MotherContactNoHtml=Student_MotherContactNo, Student_MotherNameHtml=Student_MotherName, Student_FatherContactNoHtml=Student_FatherContactNo, Student_FatherNameHtml=Student_FatherName, Student_ReferenceHtml=Student_Reference, Student_AadhaarNoHtml=Student_AadhaarNo, Student_genderHtml=Student_gender, Student_DobHtml=Student_Dob, StudentContactInfoHtml=StudentContactInfo, StudentEmailHtml=StudentEmail, StudentAddressHtml=StudentAddress, StudentLNameHtml=StudentLName, StudentMNameHtml=StudentMName, StudentFNameHtml=StudentFName, stdlist=stdDetails, logoimage=logoimg, ClassnameHtml=Classname, Address1Html=Address1, EmailHtml=Email, ContactInfoHtml=ContactInfo)


@app.route('/StudentProfile.html', methods=['GET', 'POST'])
def StudentProfileHtml():
    return render_template('StudentProfile.html')


@app.route('/SearchStudent', methods=['GET', 'POST'])
def StudentProfile():
    if request.method == 'POST':
        SearchBy = request.form.get('SearchBy')
        if SearchBy == 'StudentName':
            StudentRollNo = request.form.get('StudentRollNo')
            StudentProfileData = getStudentProfileByName(StudentRollNo)
            if StudentProfileData == '' or StudentProfileData == None:
                StudentFName = ''
                StudentMName = ''
                StudentLName = ''
                StudentAddress = ''
                StudentEmail = ''
                StudentContactInfo = ''
                errormessage = 'No Student Record found'
                return render_template('StudentProfile.html', errormessagehtml=errormessage, StudentFNameHtml=StudentFName, StudentMNameHtml=StudentMName, StudentLNameHtml=StudentLName, StudentContactInfoHtml=StudentContactInfo, StudentAddressHtml=StudentAddress, StudentEmailHtml=StudentEmail)
            StudentFName = ''
            StudentMName = ''
            StudentLName = ''
            StudentAddress = ''
            StudentEmail = ''
            StudentContactInfo = ''
            errormessage = ''
            return render_template('StudentProfile.html', StudentProfileDatahtml=StudentProfileData, errormessagehtml=errormessage, StudentFNameHtml=StudentFName, StudentMNameHtml=StudentMName, StudentLNameHtml=StudentLName, StudentContactInfoHtml=StudentContactInfo, StudentAddressHtml=StudentAddress, StudentEmailHtml=StudentEmail)

        if SearchBy == 'RollNumber':
            try:
                StudentRollNo = int(request.form.get('StudentRollNo'))

            except ValueError:
                StudentFName = ''
                StudentMName = ''
                StudentLName = ''
                StudentAddress = ''
                StudentEmail = ''
                StudentContactInfo = ''
                errormessage = 'Enter a Valid Roll Number'
                return render_template('StudentProfile.html', errormessagehtml=errormessage, StudentFNameHtml=StudentFName, StudentMNameHtml=StudentMName, StudentLNameHtml=StudentLName, StudentContactInfoHtml=StudentContactInfo, StudentAddressHtml=StudentAddress, StudentEmailHtml=StudentEmail)

            studentimageDB = getStudentProfileImg(StudentRollNo)
            StudentProfileData = getStudentProfile(StudentRollNo)
            if StudentProfileData == '':
                StudentFName = ''
                StudentMName = ''
                StudentLName = ''
                StudentAddress = ''
                StudentEmail = ''
                StudentContactInfo = ''
                errormessage = 'No Student Record found'
                return render_template('StudentProfile.html', errormessagehtml=errormessage, studentimage=studentimageDB, StudentFNameHtml=StudentFName, StudentMNameHtml=StudentMName, StudentLNameHtml=StudentLName, StudentContactInfoHtml=StudentContactInfo, StudentAddressHtml=StudentAddress, StudentEmailHtml=StudentEmail)
            errormessage = ''
            StudentFName = StudentProfileData[0][0]
            StudentMName = StudentProfileData[0][1]
            StudentLName = StudentProfileData[0][2]
            StudentAddress = StudentProfileData[0][3]
            StudentEmail = StudentProfileData[0][4]
            StudentContactInfo = StudentProfileData[0][5]

            return render_template('StudentProfile.html', errormessagehtml=errormessage, studentimage=studentimageDB, StudentFNameHtml=StudentFName, StudentMNameHtml=StudentMName, StudentLNameHtml=StudentLName, StudentContactInfoHtml=StudentContactInfo, StudentAddressHtml=StudentAddress, StudentEmailHtml=StudentEmail)


if __name__ == '__main__':
    app.run(debug=True)
