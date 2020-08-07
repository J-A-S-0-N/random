from time import sleep
ban = 10

sw1 = True
sw2 = True
swf = True

if sw1 == True:
    print("this is your first WARNING DO NOT SWEAR")  
    if sw2 == True:
        print("you are ban for " + str(ban) +" seccond")
        print("next is ban for life")
        sleep(ban)
        if swf == True:
            print("you are ban for life")
            quit()
