#!/bin/python
#Bibliotecas

import os


#######################################################################################################################
print(""" \033[33m
___________$$$$
_____________$$$$
______________$$$$
________________$$$
_________________$$$
__________________$$$
__________________$$$$
___________________$$$$
$__________________$$$$
$$__________________$$$$
$$$$$________________$$$$
_$$$$$$______$$______$$$$$$
___$$$$_____$$_$$$__$$$$$$$
____$$$$___$$_____$$$$$$$$$
____$$$$___$________$$$_$$____$$$$$$$
____$$$$__$$$_________$___$$$$$$$$$$$$$$$$
_____$$$__$$$________$$_$$$$$__________$$$
_______$$$$$$_______$$$_$$$
_________$$$$$__$$$___$$$$$$$
____________$$$$$$____$$$$$_$$$$
________$$$$$$$$$$$$$$$$$$___$$$$
______$$$$_____$$$$$$$$$$$$____$$$$
_____$$$$______$$$$$$$___$$_____$$$$
_____$$$_______$$$__$$___$_______$$$$
____$$$________$$$________________$$$$
___$$$$________$$$$________________$$$
__$$$$__________$$$_________________$$$
__$$$____________$$$$________________$$
_$$$______________$$$$_______________$$
$$$________________$$$_______________$$
____________________$$$
______________________$$
________________________$
\033[m
""")
print("\033[31mBem-Vindo ao Salazar\033[m")
pg = str(input("\033[30 Deseja continuar ? S/N => "))
if pg =="S":
    os.system("sudo apt-get updade")
    os.system(""" sudo sh -c "echo 'deb https://http.kali.org/kali kali-rolling main non-free contrib' > /etc/apt/sources.list.d/kali.list """)
    os.system("sudo apt-get update")
else:
    exit()

print("""\033[36m
    ####################################################################################################################
    ## 01) Information Gathering        | 06) Forensics Tools           | 11) Reverse Engineering                     ##
    ## 02) Vulnerability Analysis       = 07) Stress Testing            = 12) Hardware Hacking                        ##
    ## 03) Wireless Attacks             | 08) Sniffing & Spoofing       |                                             ##
    ## 04) Web Applications             = 09) Password Attacks          =                                             ## 
    ## 05) Exploitation Tools           | 10) Maintaining Access        |                                             ##
    ####################################################################################################################
    """)

opcao = str(input("\033[31mESCOLHA A OPÇÃO ==> "))

if opcao == "1":
    os.system(
        "sudo apt-get install ace-voip     amap     apt2     arp-scan     automater     bing-ip2hosts     braa     casefile     cdpsnarf     cisco-torch     copy-router-config     dmitry     dnmap     dnsenum     dnsmap     dnsrecon     dnstracer     dnswalk     dotdotpwn     enum4linux     enumiax     eyewitness     faraday     fierce     firewalk     fragroute     fragrouter     ghost phisher     golismero     goofile     hping3     ident-user-enum     inspy     intrace     ismtp     lbd     maltego teeth     masscan     metagoofil     miranda     nbtscan-unixwiz     nikto     nmap     ntop     osrframework     p0f     parsero     recon-ng     set     smbmap     smtp-user-enum     snmp-check     sparta     sslcaudit     sslsplit     sslstrip     sslyze     sublist3r     thc-ipv6     theharvester     tlssled     twofi     unicornscan     urlcrazy     wireshark     wol-e     xplico")
elif opcao == "2":
    os.system(
        "sudo apt-get istall     bbqsql     bed     cisco-auditing-tool     cisco-global-exploiter     cisco-ocs     cisco-torch     copy-router-config     doona     dotdotpwn     hexorbase     jsql injection     lynis     nmap     ohrwurm     openvas     oscanner     powerfuzzer     sfuzz     sidguesser     siparmyknife     sqlmap     sqlninja     sqlsus     thc-ipv6     tnscmd10g     unix-privesc-check     yersinia")
elif opcao == "3":
    os.system(
        "sudo apt-get install        airbase-ng     aircrack-ng     airdecap-ng and airdecloak-ng     aireplay-ng     airgraph-ng     airmon-ng     airodump-ng     airodump-ng-oui-update     airolib-ng     airserv-ng     airtun-ng     asleap     besside-ng     bluelog     bluemaho     bluepot     blueranger     bluesnarfer     bully     cowpatty     crackle     eapmd5pass     easside-ng     fern wifi cracker     freeradius-wpe     ghost phisher     giskismet     gqrx     gr-scan     hostapd-wpe     ivstools     kalibrate-rtl     killerbee     kismet     makeivs-ng     mdk3     mfcuk     mfoc     mfterm     multimon-ng     packetforge-ng     pixiewps     pyrit     reaver     redfang     rtlsdr scanner     spooftooph     tkiptun-ng     wesside-ng     wifi honey     wifiphisher     wifitap     wifite     wpaclean")
elif opcao == "4":
    os.system(
        "sudo apt-get install apache-users     arachni     bbqsql     blindelephant     burp suite     cutycapt     davtest     deblaze     dirb     dirbuster     fimap     funkload     gobuster     grabber     hurl     jboss-autopwn     joomscan     jsql injection     maltego teeth     nikto     padbuster     paros     parsero     plecost     powerfuzzer     proxystrike     recon-ng     skipfish     sqlmap     sqlninja     sqlsus     ua-tester     uniscan     w3af     webscarab     webshag     webslayer     websploit     wfuzz     whatweb     wpscan     xsser     zaproxy")
elif opcao == "5":
    os.system(
        " sudo apt-get install    armitage     backdoor factory     beef     cisco-auditing-tool     cisco-global-exploiter     cisco-ocs     cisco-torch     commix     crackle     exploitdb     jboss-autopwn     linux exploit suggester     maltego teeth     metasploit framework     msfpc     routersploit     set     shellnoob     sqlmap     thc-ipv6     yersinia")
elif opcao == "6":
    os.system(
        "sudo apt-get install      binwalk     bulk-extractor     capstone     chntpw     cuckoo     dc3dd     ddrescue     dff     distorm3     dumpzilla     extundelete     foremost     galleta     guymager     iphone backup analyzer     p0f     pdf-parser     pdfid     pdgmail     peepdf     regripper     volatility     xplico ")
elif opcao == "7":
    os.system(
        "sudo apt-get install      dhcpig     funkload     iaxflood     inundator     inviteflood     ipv6-toolkit     mdk3     reaver     rtpflood     slowhttptest     t50     termineter     thc-ipv6     thc-ssl-dos ")
elif opcao == "8":
    os.system(
        "sudo apt-get install     bettercap     burp suite     dnschef     fiked     hamster-sidejack     hexinject     iaxflood     inviteflood     ismtp     isr-evilgrade     mitmproxy     ohrwurm     protos-sip     rebind     responder     rtpbreak     rtpinsertsound     rtpmixsound     sctpscan     siparmyknife     sipp     sipvicious     sniffjoke     sslsplit     sslstrip     thc-ipv6     voiphopper     webscarab     wifi honey     wireshark     xspy     yersinia     zaproxy")
elif opcao == "9":
    os.system(
        "sudo apt-get install brutespray     burp suite     cewl     chntpw     cisco-auditing-tool     cmospwd     creddump     crowbar     crunch     findmyhash     gpp-decrypt     hash-identifier     hashcat     hexorbase     thc-hydra     john the ripper     johnny     keimpx     maltego teeth     maskprocessor     multiforcer     ncrack     oclgausscrack     ophcrack     pack     patator     phrasendrescher     polenum     rainbowcrack     rcracki-mt     rsmangler     seclists     sqldict     statsprocessor     thc-pptp-bruter     truecrack     webscarab     wordlists     zaproxy  maintaining access         cryptcat     cymothoa     dbd     dns2tcp     httptunnel     intersect     nishang     polenum     powersploit     pwnat     ridenum     sbd     shellter     u3-pwn     webshells     weevely     winexe  hardware hacking         android-sdk     apktool     arduino     dex2jar     sakis3g     smali  reverse engineering         apktool     dex2jar     distorm3     edb-debugger     jad     javasnoop     jd-gui     ollydbg     smali     valgrind     yara  reporting tools         casefile     cherrytree     cutycapt     dos2unix     dradis     magictree     metagoofil     nipper-ng     pipal     rdpy  ")
elif opcao == "10":
    os.system(
        "sudo apt-get installl      cryptcat     cymothoa     dbd     dns2tcp     httptunnel     intersect     nishang     polenum     powersploit     pwnat     ridenum     sbd     shellter     u3-pwn     webshells     weevely     winexe")
elif opcao == "11":
    os.system(
        "sudo apt-get install     apktool     dex2jar     distorm3     edb-debugger     jad     javasnoop     jd-gui     ollydbg     smali     valgrind     yara")
elif opcao == "12":
    os.system("sudo apt-get install     android-sdk     apktool     Arduino     dex2jar     Sakis3G     smali")
else:
    print("\033[02:31:40m Esta opção não existe \033[m")
    exit()