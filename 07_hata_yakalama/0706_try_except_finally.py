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

a = 10
def mValid():
    try:
        # from selenium import webdriver
        import netmiko
    except ModuleNotFoundError:
        return 0
    else:
        return 1
    finally:
        print("merak ediyorum return mü kazanacak finally mi")

result = mValid()
if result==0:
    print("Modül Host PC'de Kurulu Değil")
else:
    print("Modül Host PC'de Kurulu")

"""
finally nerelerde kullanırız:
Database İŞlemlerinde Connection Kapat
Dosya Açık İse Kapat
derken
"""