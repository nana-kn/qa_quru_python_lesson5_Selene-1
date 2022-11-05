import os
from selene.support.shared import browser
from selene import have, be


def test_student_registration_form(open_page_form):

    browser.element('#firstName').type('Ekaterina')
    browser.element('#lastName').type('Knyazeva')
    browser.element('#userEmail').type('Kate_Kn@mail.ru')
    gender_is_female = browser.element('[for = "gender-radio-2"]')
    gender_is_female.click()
    browser.element('#userNumber').type('89214977764')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    month_of_date_of_birth = browser.element('[value="4"]')
    month_of_date_of_birth.click()
    browser.element('.react-datepicker__year-select').click()
    year_of_date_of_birth = browser.element('[value="1999"]')
    year_of_date_of_birth.click()
    browser.element('.react-datepicker__day--014').click()
    browser.element('#subjectsInput').type('Ma').press_enter()
    hobby_is_music = browser.element('[for = "hobbies-checkbox-3"]')
    hobby_is_music.click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../attachments/image.JPG'))
    browser.element('#currentAddress').type('St. Petersburg, Moskovskaya st., house No. 196')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('Har').press_enter()
    browser.element('#react-select-4-input').type('Pan').press_enter()
    browser.element('#submit').press_enter()

    browser.elements('.modal-body tr').should(have.texts(
        'Label Values',
        'Student Name Ekaterina Knyazeva',
        'Student Email Kate_Kn@mail.ru',
        'Gender Female',
        'Mobile 8921497776',
        'Date of Birth 14 May,1999',
        'Subjects Maths',
        'Hobbies Music',
        'Picture image.JPG',
        'Address St. Petersburg, Moskovskaya st., house No. 196',
        'State and City Haryana Panipat'
        ))




