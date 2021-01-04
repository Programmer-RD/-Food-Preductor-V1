# The start of the program
import random
import time
import pickle
import math
import smtplib
import smtpd
from email.mime.multipart import MIMEMultipart
from math import remainder
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

user__name = "Ranuga"
password_p = "go2ranuga@gmail.com" or "go2indika@gmail.com" or "go2dinusha@gmail.com"

def send_mail(to_email):
    msg = MIMEMultipart()
    msg['From'] = "go2ranuga@gmail.com"
    msg['To'] = to_email
    msg['subject'] = " Hi ! "
    msg['Body'] = "Hi ...."
    msg.attach(MIMEText("Hi... This is from the foodP program...", 'plain'))
    msg.attach(MIMEText("Did you enter your email and logged into our program ? ", 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login("go2ranuga@gmail.com", "ranuga2008")
        server.sendmail("go2ranuga@gmail.com", to_email, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(" Something went wrong...." + str(e))
        return False
send_mail(password_p)
user_name: str = input(" > Enter the User Name... \n > ")
password: str or int = input(" > Enter the Password_Email... \n > ")
while password_p != password or password != password_p or user__name != user_name or user_name != user__name:
    user_name: str = input(" > Enter the User name... \n > ")
    password: str or int = input(" > Enter the Password_Email... \n > ")
print(" < | > Welcome < | > ")
first_name: str = input(" > What is your first Name ? \n > ")
second_name: str = input(f" > {first_name} what is your second Name ? \n > ")
Age: str = input(f" > {first_name} how old are you ? \n > ")
if Age < str(18):
    print(" > You are too young...")
    print(" > | Bye Bye | < ")
    quit()
elif Age > str(18):
    pass
else:
    print(" > An error occurred please try again later")
full_name = first_name + second_name


def add():
    what_is_the_measuring_unit: str = input(" > What is the measuring Unit ? (Kg or g or Pounds) \n > ")
    time.sleep(2.5)
    name: str = input(" > Enter the Name of the food.... \n > ")
    how_much = int(input(" > Enter how much do you use it per day ? \n > "))
    ho_much = int(input(" > How Much did you buy in total ? \n > "))
    how_many_das = int(
        input(
            f" > {first_name} How many days are you thinking of using the {ho_much} {what_is_the_measuring_unit} ? \n > "))
    m = how_much / ho_much
    x = how_many_das / ho_much
    v = remainder(how_much, ho_much)
    z = remainder(how_many_das, ho_much)
    per_week_the_Amount = how_much * 7
    per_month_the_Amount = per_week_the_Amount * 4
    per_year_the_Amount = per_month_the_Amount * 12
    ap = open("per_days.txt", "a")
    ap.write(f" \n > Per Day : {how_much} ")
    ap.close()
    time.sleep(2.5)
    rafaa = open("per_weeks.txt", "a")
    rafaa.write(f" \n > Per week : {per_week_the_Amount}{what_is_the_measuring_unit} ")
    rafaa.close()
    time.sleep(2.5)
    rafaatedud = open("per_months.txt", "a")
    rafaatedud.write(f" \n > Per Month : {per_month_the_Amount} {what_is_the_measuring_unit}")
    rafaatedud.close()
    time.sleep(2.5)
    fygedgsjth = open("per_years.txt", "a")
    fygedgsjth.write(f" \n > Per year : {per_year_the_Amount} {what_is_the_measuring_unit} ")
    fygedgsjth.close()
    time.sleep(2.5)
    print(f" \n > With amount that you eat per day it will take {m} days for you to finish {ho_much}")
    time.sleep(2.5)
    print(f" \n > The remainder of {ho_much}{what_is_the_measuring_unit} is {v}")
    time.sleep(2.5)
    print(
        f" \n > if you want to use {ho_much} for {how_many_das} you should eat {x}{what_is_the_measuring_unit} per day")
    time.sleep(2.5)
    print(f" \n > the remainder of the above is {z} \n")
    time.sleep(2.5)
    forhow = input(f" > For how many day did you buy the above {name} ? (Day or Week or month or year) \n > ")

    if forhow == "Week" or "week":
        how_many_days = m * 4 * 12
        how_mont = m * 4
        how_d = m / 7
        kk = open("Per__how_much.txt", "a")
        kk.write(f" \n > Per Day : {how_d}{what_is_the_measuring_unit}")
        kk.write(f" \n > Per Month : {how_mont}{what_is_the_measuring_unit}")
        kk.write(f" \n > Per Year : {how_many_days}{what_is_the_measuring_unit}")
        kk.close()

        addd = open("per_days.txt", "a")
        addd.write(f" \n > Per Day : {how_d}{what_is_the_measuring_unit}")
        addd.close()

        print(f" > Per Year : {how_many_days}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(f" > Per Month : {how_mont}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(f" > Per Day : {how_d}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(
            "> An average person should eat : 18.82408 kilo gram | 18824.08 gram | 41.499992603 Pounds {What_is_it} "
            "per Day")
        ap = open("per_days.txt", "a")
        ap.write(f" \n > Per Day : {how_d}{what_is_the_measuring_unit}")
        ap.close()
        time.sleep(2.5)
        rafaatedud = open("per_months.txt", "a")
        rafaatedud.write(f" \n > Per Month : {how_mont}{what_is_the_measuring_unit}")
        rafaatedud.close()
        time.sleep(2.5)
        fygedgsjth = open("per_years.txt", "a")
        fygedgsjth.write(f" \n > Per year : {how_many_days}{what_is_the_measuring_unit}")
        fygedgsjth.close()
        time.sleep(2.5)
    elif forhow == "Day" or "day":
        ff = 7 * m
        fg = 4 * ff
        fh = 12 * fg
        fs = open("Per__how_much.txt", "a")
        fs.write(f" \n > Per Week : {ff}{what_is_the_measuring_unit}")
        fs.write(f" \n > Per Month : {fg}{what_is_the_measuring_unit}")
        fs.write(f" \n > Per Year : {fh}{what_is_the_measuring_unit}")
        fs.close()
        print(f" \n > Per Year : {fh}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(f" \n > Per Month : {fg}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(f" \n > Per Week : {ff}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(" \n > An average person should eat : | 75450 g | 75.45 kg | 166.33878 pounds | per month")

        rafaa = open("per_weeks.txt", "a")
        rafaa.write(f" \n > Per week : {ff}{what_is_the_measuring_unit}")
        rafaa.close()
        time.sleep(2.5)
        rafaatedud = open("per_months.txt", "a")
        rafaatedud.write(f" \n > Per Month : {fg}{what_is_the_measuring_unit}")
        rafaatedud.close()
        time.sleep(2.5)
        fygedgsjth = open("per_years.txt", "a")
        fygedgsjth.write(f" \n > Per year : {fh}{what_is_the_measuring_unit}")
        fygedgsjth.close()
        time.sleep(2.5)
    elif forhow == "Month" or "month":
        dfg = m / 4
        hi = dfg / 7
        how_many_day = m * 12
        z = open("Per__how_much.txt", "a")
        z.write(f" \n > Per Day : {dfg}{what_is_the_measuring_unit}")
        z.write(f" \n > Per Week : {hi}{what_is_the_measuring_unit}")
        z.write(f" \n > Per Year : {how_many_day}{what_is_the_measuring_unit}")
        z.close()
        time.sleep(2.5)
        print(" > An average person should eat : | 75450 g | 75.45 kg | 166.33878 pounds | per month")
        print(f" > Per Year : {how_many_day}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(f" > Per Week : {hi}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(f" > Per Day : {dfg}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        app = open("per_days.txt", "a")
        app.write(f" \n > Per Day : {dfg}{what_is_the_measuring_unit}")
        app.close()
        time.sleep(2.5)
        tedlfdud = open("per_weeks.txt", "a")
        tedlfdud.write(f" \n > Per week : {hi}{what_is_the_measuring_unit}")
        tedlfdud.close()
        time.sleep(2.5)
        fygeidfeif = open("per_years.txt", "a")
        fygeidfeif.write(f" \n > Per year : {how_many_day}{what_is_the_measuring_unit}")
        fygeidfeif.close()
        time.sleep(2.5)
    elif forhow == "year" or "Year" or "YEAR":
        ggg = m / 12 #month
        hhi = ggg / 2 #week
        ho_many_daytt = hhi / 7# day
        pp = open("Per__how_much.txt", "a")
        pp.write(f" \n > Per Day : {ho_many_daytt}{what_is_the_measuring_unit}")
        pp.write(f" \n > Per Week : {hhi}{what_is_the_measuring_unit}")
        pp.write(f" \n > Per Month : {ho_many_daytt}{what_is_the_measuring_unit}")
        pp.close()
        time.sleep(2.5)
        print(" > An average person should eat : | 75450 g | 75.45 kg | 166.33878 pounds | per month")
        print(f" > Per Month : {ho_many_daytt}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(f" > Per Week : {hhi}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        print(f" > Per Day : {ggg}{what_is_the_measuring_unit}")
        time.sleep(2.5)
        app = open("per_days.txt", "a")
        app.write(f" \n > Per Day : {ggg}{what_is_the_measuring_unit}")
        app.close()
        time.sleep(2.5)
        tedlfdud = open("per_weeks.txt", "a")
        tedlfdud.write(f" \n > Per week : {hhi}{what_is_the_measuring_unit}")
        tedlfdud.close()
        time.sleep(2.5)
        fygeidfeif = open("per_months.txt", "a")
        fygeidfeif.write(f" \n > Per Month : {ho_many_daytt}{what_is_the_measuring_unit}")
        fygeidfeif.close()
        time.sleep(2.5)
    else:
        print(" > An error occurred")
        print(" > Please try again later")

    if how_much < 18.232 or 40.19467964 or 18232:
        print(" > I think you should Eat a little bit more")

    elif how_much > 75.458870685916664911 or 75458.870685916670482 or 166.35833333333332007:
        pass

    else:
        print(" > An error occurred")
        print(" > Try again later")
    want_to_qut: str = input(" > Do you want to quit or go to the main menu ? ")
    if want_to_qut == "Quit" or "quit":
        quit()
    elif want_to_qut == "mAIN MENU" or "main menu" or "main" or "Main" or "Main Menu" or "Main menu":
        main_menu()


def pr():
    one_or_more = input(" > Do you only Want to enter one product or many ? \n > ")
    if one_or_more == "Many" or "many":
        times = int(input(" > How many iteams do you ant to add ? \n > "))
        for i in range(0, times):
            name_of_the_product = input(" > What is the Name of the product ? \n > ")
            how_much_are_ther: int = input(f" > How many packs are there of {name_of_the_product} ")
            ii = input(" > What is the mass weight unit ? (Kg) or (g) or (Pounds)\n > ")
            o = input(" > For what can you enter the price ? (Per day or per week or Per month).. \n > ")
            money_type = input("What is the money Type ? ($ or Rs) \n > ")

            if o == "per day" or "Per Day" or "per Day" or "Per day":
                pric = int(input(f" > Enter the price per one {ii} of {name_of_the_product} per day..\n > "))
                per_week_one = pric * 7
                per_month_one = per_week_one * 4
                per_yyear_one = per_month_one * 12

                per_week = pric * 7 * how_much_are_ther
                per_month = per_week_one * 4 * how_much_are_ther
                per_yyear = per_month_one * 12 * how_much_are_ther
                #make more stuff fgbedfh

                r = open("Per__week.txt", "a")
                r.write(f" \n > Per Week : {money_type}{per_week_one} ")
                r.write(f" \n > Per Month : {money_type}{per_month_one}")
                r.write(f" \n > Per Year : {money_type}{per_yyear_one} ")
                r.close()
                time.sleep(2.5)
                ad = open("per_day.txt", "a")
                ad.write(f" \n > Per Day : {pric} ")
                ad.close()
                time.sleep(2.5)
                raf = open("per_week.txt", "a")
                raf.write(f" \n > Per week : {per_week_one} ")
                raf.close()
                time.sleep(2.5)
                rafaatedeeeee = open("per_month.txt", "a")
                rafaatedeeeee.write(f" \n > Per Month : {per_month_one} ")
                rafaatedeeeee.close()
                time.sleep(2.5)
                fygedgs = open("per_year.txt", "a")
                fygedgs.write(f" \n > Per year : {per_yyear_one} ")
                fygedgs.close()
                time.sleep(2.5)
                print(f" > Per Week : {money_type}{per_week_one}")
                time.sleep(2.5)
                print(f" > Per Month : {money_type}{per_month_one}")
                time.sleep(2.5)
                print(f" > Per year : {money_type}{per_yyear_one}")
                time.sleep(2.5)
                print(
                    f" > Per Week for {name_of_the_product} with the quantity of {how_much_are_ther} : {money_type}{per_week}")
                time.sleep(2.5)
                print(
                    f" > Per Month for {name_of_the_product} with the quantity of {how_much_are_ther} : {money_type}{per_month}")
                time.sleep(2.5)
                print(
                    f" > Per year for {name_of_the_product} witht eh quantity of {how_much_are_ther} : {money_type}{per_yyear}")
                time.sleep(2.5)
            elif o == "Month" or "month":
                name_of_the_products = name_of_the_product
                price = int(input(f" > Enter the price per one {ii} of {name_of_the_products} per Month..\n > "))
                per_week = price / 4
                per_____da = per_week / 7
                per_year = price * 12


                Ra = open("Per__wee.txt", "a")
                Ra.write(f" \n > Per Day : {per_____da} ")
                Ra.write(f" \n > Per Week : {per_week}")
                Ra.write(f" \n > Per Year : {per_year} ")
                Ra.close()
                time.sleep(2.5)
                adf = open("per_days.txt", "a")
                adf.write(f" \n > Per Day : {per_____da} ")
                adf.close()
                time.sleep(2.5)
                rafa = open("per_week.txt", "a")
                rafa.write(f" \n > Per week : {per_week} ")
                rafa.close()
                time.sleep(2.5)
                rafaated = open("per_month.txt", "a")
                rafaated.write(f" \n > Per Month : {price} ")
                rafaated.close()
                time.sleep(2.5)
                fygedgsj = open("per_year.txt", "a")
                fygedgsj.write(f" \n > Per year : {per_year} ")
                fygedgsj.close()
                time.sleep(2.5)
                print(f" > Per Day  : {money_type}{per_____da}")
                time.sleep(2.5)
                print(f" > Per Week : {money_type}{per_week}")
                time.sleep(2.5)
                print(f" > Per year : {money_type}{per_year}")

            elif o == "Per week" or "Week" or "week" "per week":
                per__wee = int(input(f" > Enter the price of {name_of_the_product} per week... \n > "))
                per__da = per__wee / 7
                per__monh = per__wee * 4
                per__yea = per__monh * 12
                ran = open("Per__week.txt", "a")
                ran.write(f" \n > Per Day : {money_type}{per__da} ")
                ran.write(f" \n > Per Month : {money_type}{per__monh}")
                ran.write(f" \n > Per Year : {money_type}{per__yea} ")
                ran.close()
                time.sleep(2.5)
                a = open("per_days.txt", "a")
                a.write(f" \n > Per Day : {per__da} ")
                a.close()
                time.sleep(2.5)
                rafaa = open("per_week.txt", "a")
                rafaa.write(f" \n > Per week : {per__wee} ")
                rafaa.close()
                time.sleep(2.5)
                rafaatedu = open("per_month.txt", "a")
                rafaatedu.write(f" \n > Per Month : {per__monh} ")
                rafaatedu.close()
                time.sleep(2.5)
                fygedgsjt = open("per_year.txt", "a")
                fygedgsjt.write(f" \n > Per year : {per__yea} ")
                fygedgsjt.close()
                time.sleep(2.5)
                print(f" > Per Day : {money_type}{per__da}")
                time.sleep(2.5)
                print(f" > Per Month : {money_type}{per__monh}")
                time.sleep(2.5)
                print(f" > Per year : {money_type}{per__yea}")

            else:
                print(" > An error occured")
                print(" > Please try again later")

    elif one_or_more == "One" or "1" or "one":
        X = input(" > What is the mass weight unit ? (Kg) or (g) or (Pounds)\n > ")
        P = input(" > For what can you enter the price ? (Per day or Per Week or Per month).. \n > ")
        money_type = input(" > What is the money type ? ($ OR Rs) \n > ")
        Name_of_the_product = input(" > What is the name of the product ? \n > ")
        if P == "per day" or "Per Day" or "per Day" or "Per day" or "Day" or "day":
            price = int(input(f" > Enter the price per one {X} of {Name_of_the_product} per day..\n > "))
            per____week = price * 7
            per____month = per____week * 4
            per____year = per____month * 12
            ranu = open("Per__Day.txt", "a")
            ranu.write(f" \n > Per Week : {money_type}{per____week} ")
            ranu.write(f" \n > Per Month : {money_type}{per____month}")
            ranu.write(f" \n > Per Year : {money_type}{per____year} ")
            ranu.close()
            time.sleep(2.5)
            au = open("per_days.txt", "a")
            au.write(f" \n > Per Day : {price} ")
            au.close()
            time.sleep(2.5)
            rafaa = open("per_week.txt", "a")
            rafaa.write(f" \n > Per week : {per____week} ")
            rafaa.close()
            time.sleep(2.5)
            rafaatedud = open("per_month.txt", "a")
            rafaatedud.write(f" \n > Per Month : {per____month} ")
            rafaatedud.close()
            time.sleep(2.5)
            fygedgsjth = open("per_year.txt", "a")
            fygedgsjth.write(f" \n > Per year : {per____year} ")
            fygedgsjth.close()
            time.sleep(2.5)
            print(f" > Per Week : {money_type}{per____week}")
            time.sleep(2.5)
            print(f" > Per month : {money_type}{per____month}")
            time.sleep(2.5)
            print(f" > Per Year : {money_type}{per____year}")

        elif P == "Month" or "month" or "Per month" or "per month":
            price = int(input(f" > Enter the price per one {X} of {Name_of_the_product} per Month..\n > "))
            per___week = price / 4
            per___day = per___week / 7
            per___year = price * 12
            ranug = open("Per__Month.txt", "a")
            ranug.write(f" \n > Per Day : {money_type}{per___day} ")
            ranug.write(f" \n > Per Week : {money_type}{per___week}")
            ranug.write(f" \n > Per Year : {money_type}{per___year} ")
            ranug.close()
            time.sleep(2.5)
            aua = open("per_days.txt", "a")
            aua.write(f" \n > Per Day : {money_type}{per___day} ")
            aua.close()
            time.sleep(2.5)
            rafaat = open("per_week.txt", "a")
            rafaat.write(f" \n > Per week : {money_type}{per___week} ")
            rafaat.close()
            time.sleep(2.5)
            rafaatedudu = open("per_month.txt", "a")
            rafaatedudu.write(f" \n > Per Month : {money_type}{price} ")
            rafaatedudu.close()
            time.sleep(2.5)
            fygedgsjthd = open("per_year.txt", "a")
            fygedgsjthd.write(f" \n > Per year : {money_type}{per___year} ")
            fygedgsjthd.close()
            time.sleep(2.5)
            print(f" > Per Day : {money_type}{per___day}")
            time.sleep(2.5)
            print(f" > Per Week : {money_type}{per___week}")
            time.sleep(2.5)
            print(f" > Per Year : {money_type}{per___year}")

        elif P == "Per week" or "Week" or "week" "per week":
            per__week = int(input(f" > Enter the price of {Name_of_the_product} per week... \n > "))
            per__day = per__week / 7
            per__month = per__week * 4
            per__year = per__month * 12
            anuga = open("Per__Wek.txt", "a")
            anuga.write(f" \n > Per Day : {money_type}{per__day} ")
            anuga.write(f" \n > Per Month : {money_type}{per__month}")
            anuga.write(f" \n > Per Year : {money_type}{per__year} ")
            anuga.close()
            time.sleep(2.5)
            auga = open("per_day.txt", "a")
            auga.write(f" \n > Per Day : {money_type}{per__day} ")
            auga.close()
            time.sleep(2.5)
            rafaaty = open("per_week.txt", "a")
            rafaaty.write(f" \n > Per Week : {money_type}{per__week} ")
            rafaaty.close()
            time.sleep(2.5)
            rafaatedudue = open("per_month.txt", "a")
            rafaatedudue.write(f" \n > Per Month : {money_type}{per__month} ")
            rafaatedudue.close()
            time.sleep(2.5)
            fygedgsjthdt = open("per_year.txt", "a")
            fygedgsjthdt.write(f" \n > Per year : {money_type}{per__year} ")
            fygedgsjthdt.close()
            time.sleep(2.5)
            print(f" > Per Day : {money_type}{per__day}")
            time.sleep(2.5)
            print(f" > Per Week : {money_type}{per__month}")
            time.sleep(2.5)
            print(f" > Per Year : {money_type}{per__year}")
            time.sleep(2.5)
        else:
            print(" > An error occurred")
            print(" > Please try again later")

        want_to_quit: str = input(" > Do you want to quit ? ")
        if want_to_quit == True or "Yes" or "yes" or "Yep" or "yep":
            quit()

        elif want_to_quit == False or "No" or "no" or "Nope" or "nope":
            pass

        do_you_want_go_back_to_the_main_menu: str = input(" > Do you want to go back to the main menu ? \n > ")
        if do_you_want_go_back_to_the_main_menu == True or "Yes" or "yes" "Yep" or "yep":
            main_menu()

        elif do_you_want_go_back_to_the_main_menu == False or "No" or "no" or "Nope" or "nope":
            quit()

        else:
            print(" > I don't understand that...")


def view():
    global attachment, filename
    how_manytime = int(input(" > How many documents do you want View ? \n > "))
    for i in range(0, how_manytime):
        print(" > Funtions : ")
        print(f"""
        PR = Predicted prices
        AD= Predicted amount of kg or g or Pounds
        """)
        choice: str = input(" > Enter what is your option... \n > ")
        if choice == "PR" or "pr" or "Pr" or "pR":
            print("""
        
	        A = Per Day
	    
	        B = Per Week
	        
	        C = Per Month
	    
	        D = Per Year
	    
	        """)
            what_is_you_choice = input(" > Enter option... \n > ")
            djbd = int or str(input("> We can send you a email , Do you want to get the information by your email ? "
                                    "\n > "))
            if djbd == "Yes" or "yes" or "yep" or "Yep" or True:
                f = int or str(input(" > Please enter you email...  \n > "))
                email_user = 'go2ranuga@gmail.com'
                email_password = 'ranuga2008'
                email_send = f

                subject = 'Thank you for Using our program '
                body = 'Here is the information that was calculated....'

                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = email_send
                msg['Subject'] = subject

                msg.attach(MIMEText(body, 'plain'))

                if what_is_you_choice == "a" or "A":
                    attachment = open("per_day.txt.txt", 'rb')
                elif what_is_you_choice == "b" or "B":
                    attachment = open("per_week.txt.txt", 'rb')
                elif what_is_you_choice == "C" or "c":
                    attachment = open("per_months.txt", 'rb')
                elif what_is_you_choice == "D" or "d":
                    attachment = open("per_year.txt", 'rb')
                else:
                    print(" > Invalid Choice")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= " + filename)
                print(" > Message Sending...")
                msg.attach(part)
                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_user, email_password)
                server.sendmail(email_user, email_send, text)
                print(" > Message sent....")
                server.quit()
            if what_is_you_choice == "A" or "a":
                pp = open("per_day.txt", "r")
                pp.read()
                pp.close()

            elif what_is_you_choice == "B" or "b":
                zz = open("per_week", "r")
                zz.read()
                zz.close()

            elif what_is_you_choice == "c" or "C":
                oo = open("per_month", "r")
                oo.read()
                oo.close()

            elif what_is_you_choice == "D" or "d":
                ee = open("per_year", "r")
                ee.read()
                ee.close()

            else:
                print(" > Invalid Choice")
                random.choice(view(), main_menu(), quit())
            want_to_quit: str = input(" > Do you want to quit or go to the main menu ? ")
            if want_to_quit == "Quit" or "quit":
                quit()
            elif want_to_quit == "mAIN MENU" or "main menu" or "main" or "Main" or "Main Menu" or "Main menu":
                main_menu()
        elif choice == "AD" or "ad" or "Ad" or "aD":
            print("""
        
               	a = Per Day
               	
               	b = Per Week
               	
                c = Per Month
                
           	    d = Per Year
           	    
             	    """)
            what_is_the_choice: str = input(" > Enter your choice... \n > ")
            djbd = int or str(input("> We can send you a email , Do you want to get the information by your email ? "
                                    "\n > "))
            if djbd == "Yes" or "yes" or "yep" or "Yep" or True:
                f = int or str(input(" > Please enter you email...  \n > "))
                email_user = 'go2ranuga@gmail.com'
                email_password = 'ranuga2008'
                email_send = f

                subject = 'Thank you for Using our program '
                body = 'Here is the information that was calculated....'

                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = email_send
                msg['Subject'] = subject

                msg.attach(MIMEText(body, 'plain'))

                if what_is_the_choice == "a" or "A":
                    filename = 'per_days.txt'  # Where i ended
                    attachment = open("per_days.txt.txt", 'rb')
                elif what_is_the_choice == "b" or "B":
                    filename = 'per_weeeks.txt.txt'
                    attachment = open("per_weeeks.txt.txt", 'rb')
                elif what_is_the_choice == "C" or "c" :
                    attachment = open("per_months.txt", 'rb')
                elif what_is_the_choice == "D" or "d" :
                    attachment = open("per_years.txt", 'rb')
                else:
                    print(" > Invalid Choice")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= " + filename)
                print(" > Message Sending...")
                msg.attach(part)
                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_user, email_password)
                server.sendmail(email_user, email_send, text)
                print(" > Message sent....")
                server.quit()
            if what_is_the_choice == "per day" or "Per day" or "Per Day" or "per Day":
                zzz = open("per_days.txt", "r")
                zzz.read()
                zzz.close()

            elif what_is_the_choice == "Per week" or "per week" or "Per Week" or "per Week":
                pppp = open("per_weeeks.txt", "r")
                pppp.read()
                pppp.close()

            elif what_is_the_choice == "Per Month" or "per Month" or "Per month":
                ooooo = open("per_months.txt", "r")
                ooooo.read()
                ooooo.close()

            elif what_is_the_choice == "Per year" or "per year" or "Per Year" or "per year":
                iiiii = open("per_years.txt", "r")
                iiiii.read()
                iiiii.close()
        want_to_Quit: str = input(" > Do you want to quit or go to the main menu ? ")
        if want_to_Quit == "Quit" or "quit":
            quit()
        elif want_to_Quit == "mAIN MENU" or "main menu" or "main" or "Main" or "Main Menu" or "Main menu":
            main_menu()


def main_menu():
    print(" > Function : ")
    print(" > | - MAIN MENU - | < ")
    print("""
    
	 > Add = : = To calculator for Month or Day or Year
	 
	 > Pri = : = To calculate prices
	 
	 > Vie = : = To View the stored data(To use the Vie option you should first use this programm 5 times)
	 
	 > qui = : = To quit the programm
	 
	""")
    enter_choice = input(" > Enter your choice... \n > ")
    if enter_choice == "Add" or enter_choice == "add":
        add()

    elif enter_choice == "Pri" or enter_choice == "pri":
        pr()

    elif enter_choice == "Vie" or "vie":
        view()

    elif enter_choice == "quit" or "Quit" or "Qui" or "qui":
        print(" > Bye | Bye < ")
        quit()

    elif enter_choice != "quit" or "Vie" or "Pri" or "Add":
        print(f" > There is No function as {enter_choice}")
        want_to_quit = input(" > Do yu want to quit ? ")

        if want_to_quit == "Yes" or "yes" or True or "Yep" "yep":
            quit()

        elif want_to_quit == "No" or "no" or "Nope" or "nope":
            main_menu()

        else:
            print(" > An error occurred")
            main_menu()
    else:
        print(F" > {enter_choice} is Not available")
        random.choices(main_menu(), quit())


main_menu()
Email = int or str(input(" Can you enter your email ? "))
if Email == "Yes" or "yes" or "Yep" or "yep" or True:
    email = int or str(input(" > Please enter your email address.."))


    def send_mail(from_email, Password, to_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        msg.attach(MIMEText(subject, 'plain'))
        try:
            print(" . Email Sending....")
            print(" > Please Wait.....")
            server = smtplib.SMTP_SSL('smtp.gmail.com')
            server.ehlo()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.sendmail(from_email, to_email, msg.as_string())
            server.close()
            print(" > Email Sended.....")
            print(" > Thank you.....")
            return True
        except Exception as e:
            print(" Something went wrong...." + str(e))
            return False
    send_mail("go2ranuga@gmail.com", "ranuga2008", email, "Thank you for using our program",
              "See you later | Bye | Bye | ")
elif Email == "No" or "Nope" or "nope" or "no" or False:
    pass
print(" | > Bye < Bye > < | ")
print(f" > Have a Nice Day {first_name}{second_name} < ")
print(" > Thank you for using our program < ")
print(f" > Thank you Bye See you later {first_name} < ")
D = open("Emails.txt", "w")
D.write(f"{first_name} : {email}")
D.close()
quit()
'''
Comments:Vibhatha
Done
'''
# The end of the program