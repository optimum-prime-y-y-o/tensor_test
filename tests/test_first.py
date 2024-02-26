from pages.sbis_main_page import SbisMainPage

def test_first(browser):
    
    main_page = SbisMainPage(browser)
    contacts_page = main_page.go_to_contact_page()
    
    tensor_main_page = contacts_page.click_banner()
    tensor_main_page.valid_url()
    tensor_main_page.have_strength_in_people_block()

    tensor_about_page = tensor_main_page.go_to_about()

    tensor_about_page.valid_url()
    tensor_about_page.work_photos_same_height_and_width()




    