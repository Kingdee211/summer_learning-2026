from models import RegistrationData
from web_scrapper import end_product

details = end_product("gai.ssd")
try:
    details = RegistrationData(**details)
    print(details.expires_on)

    ans = details.expires_on - details.registered_on
    print(ans)
except Exception as ex:
    print(f"❌❌ Failed: See error below:\n{str(ex).splitlines()[0]}")

data = 2031 - 2000

print(data * 365)