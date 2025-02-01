import phonenumbers
import colorama
from colorama import Fore
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("github.com/sgtfettsack")

print(Fore.LIGHTRED_EX + rf"""
                                        

              
              ____  _   ____  ______
             / __ \/ | / / / /_  __/
            / /_/ /  |/ / /   / /   
           / ____/ /|  / /___/ /    
          /_/   /_/ |_/_____/_/     
                          
   

        
      {Fore.YELLOW}> {Fore.LIGHTYELLOW_EX}made by sgtfettsack {Fore.YELLOW}<
                  
                                                
""")





def phoneNumberLocationTracker():
    target_nmber = input(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] Enter Phone Number + country code: ")


    from phonenumbers import geocoder
    ch_number = phonenumbers.parse(target_nmber, "en")
    from phonenumbers import carrier
    service_number = phonenumbers.parse(target_nmber, "en")
    from phonenumbers import timezone
    gb_number = phonenumbers.parse(target_nmber, "en")

    print()
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] COUNTRY             :    {Fore.LIGHTMAGENTA_EX}", geocoder.description_for_number(ch_number, "en"))
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] INTERNET-PROVIDER   :    {Fore.LIGHTMAGENTA_EX}", carrier.name_for_number(service_number, "en"))
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] TIMEZONE            :    {Fore.LIGHTMAGENTA_EX}", timezone.time_zones_for_number(gb_number))
    print()
    time.sleep(3)
    phoneNumberLocationTracker()


if __name__ == "__main__":
    phoneNumberLocationTracker()
    
