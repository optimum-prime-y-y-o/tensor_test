from pages.sbis_main_page import SbisMainPage

def test_third(browser):
    
    main_page = SbisMainPage(browser)
    download_page = main_page.go_to_download_page()
    download_page.go_to_plugin()
    download_page.download_plugin()

    download_page.plugin_downloaded()
    download_page.correct_plugin_size()