"""
Exception Handling  →           try:
                                    {kodu çalıştırmak için bu bloktayım}
                                except:
                                    {exception var ise bu bloktayım}
                                else:
                                    {exception yok ise bu bloktayım}
                                finally:
                                    {mutlaka bu bloktayım}
"""
def mValid():
    try:
        from selenium import webdriver
        # import netmiko
    except ModuleNotFoundError:
        return 0
    else:
        return 1

result = mValid()
if result==0:
    print("Modül Host PC'de Kurulu Değil")
else:
    print("Modül Host PC'de Kurulu")

