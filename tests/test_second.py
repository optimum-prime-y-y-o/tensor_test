from pages.sbis_main_page import SbisMainPage

def test_second(browser):
    
    main_page = SbisMainPage(browser)
    contacts_page = main_page.go_to_contact_page()
    
    contacts_page.check_default_region()
    contacts_page.check_partners()
    contacts_page.change_region()

    contacts_page.check_new_region_url()
    contacts_page.check_new_region_partners()
    contacts_page.check_new_region_name()
    contacts_page.check_new_region_title()