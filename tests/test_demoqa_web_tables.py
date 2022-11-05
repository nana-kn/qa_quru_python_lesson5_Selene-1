from selene.support.shared import browser
from selene import have, be


def test_web_tables(open_page_webtables):
    #add new row
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('Ekaterina')
    browser.element('#lastName').type('Knyazeva')
    browser.element('#userEmail').type('Kate_Kn@mail.ru')
    browser.element('#age').type('23')
    browser.element('#salary').type('65000')
    browser.element('#department').type('Test')
    browser.element('#submit').click()
    check_fourth_lines = browser.element('.rt-tbody .rt-tr-group:nth-of-type(4)')
    check_fourth_lines.all('.rt-td').should(have.texts(
        'Ekaterina',
        'Knyazeva',
        '23',
        'Kate_Kn@mail.ru',
        '65000',
        'Test',
        ''
    ))

    # edit second row
    check_second_lines = browser.element('.rt-tbody .rt-tr-group:nth-of-type(2)')
    check_second_lines.element('#edit-record-2').click()

    age = browser.element('#age')
    age.clear()
    age.type('46')
    salary = browser.element('#salary')
    salary.clear()
    salary.type('135000')
    browser.element('#submit').click()

    check_second_lines.all('.rt-td').should(have.texts(
        'Alden',
        'Cantrell',
        '46',
        'alden@example.com',
        '135000',
        'Compliance',
        ''
    ))

    # delete third row
    browser.element('#delete-record-3').click()
    check_count_lines = browser.all('.rt-tbody .rt-tr-group .-padRow')
    check_count_lines.should(have.size(7))












