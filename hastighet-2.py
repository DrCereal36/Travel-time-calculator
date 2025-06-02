import time

sträcka = input("How long are you going to drive? (km) ")
hast = input("HOw fast do you drive? (Km/H) ")

sträcka = float(sträcka)
hast = float(hast)

tid = sträcka / hast

if tid < 1:
    tidM = tid * 60
    print(f"It will take {tidM:.2f} Min")
else:
    timmar = int(tid)
    minuter = (tid - timmar) * 60
    print(f"It will take {timmar} h {minuter:.0f} Min")


#FG36
