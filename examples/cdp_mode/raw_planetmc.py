from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "www.planetminecraft.com/account/sign_in/"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.cdp.gui_click_element("#turnstile-widget")
    sb.sleep(2)
