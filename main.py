# 1
def dinamik_salom():
    from datetime import datetime
    soat = datetime.now().hour

    if 6 <= soat < 12:
        print("Xayrli tong!")
    elif 12 <= soat < 18:
        print("Xayrli kun!")
    else:
        print("Xayrli kech!")
