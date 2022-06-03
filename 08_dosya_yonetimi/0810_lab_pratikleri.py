def authMethod(arg):
    if str(arg).find("chap") !=-1:
        return "chap"
    elif str(arg).find("pap") !=-1:
        return "pap"
    else:
        return "no auth"

with open("running_config.txt") as f:
    result = f.read()
    liste = [i for i in result.split("!") if i.startswith("\ninterface dialer 1\n")]
    # print(liste[0].strip("\n").replace("\t", ""))
    dialer1 = liste[0].strip("\n").replace("\t", "")
    # region DRY
    # bunun yerine DRY yapmaya karar verdim
    '''x = dialer1.find("chap")
    if x != -1:
        print("aut. method chap")
    else:
        print("aut. method pap")'''
    # endregion
    print(f"aut. method {authMethod(dialer1)}")
