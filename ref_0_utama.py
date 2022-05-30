from time import sleep
def sen1(data):
    try:
        ganti_c(2)
        result=baca_s(1,data)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
    finally:
        return result
def sen2(data):
    try:
        ganti_c(4)
        result=baca_s(2,data)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
    finally:
        return result
def sen3(data):
    try:
        ganti_c(5)
        result=baca_s(3,data)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
    finally:
        return result
def sen4(data):
    try:
        ganti_c(7)
        result=baca_s(4,data)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
    finally:
        return result
