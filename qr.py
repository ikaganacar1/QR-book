from PIL import Image
import qrcode
from random import choice
from string import ascii_letters, digits
from pb import publitio_api
from os import listdir,rename
import json
import hashlib

def qr_generator(name,data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qr_codes/{name}.png")
    #sleep(0.3)
    image = Image.open(f'qr_codes/{name}.png')

    resized = image.resize((58, 41))
    resized.save(f'qr_codes/{name}.png')

def create_name():
    name = "qr_"
    for _ in range(11):
        name += str(choice(ascii_letters + digits)) 
    
    return name

def create_list_of_files(path):
    a = list()
    for files in listdir(path):
        a.append(str(files))
    
    a.sort()
    return a

def upload_file_to_publit(file_name):
    pt = publitio_api('r2xGdVpnmXkcs14tgpoX','rpJd0TxhrQ7P7zDQDzPQSX3k2RPm93k8')
    pt.upload_file(f"images/{file_name}","temp","temp")

    url = pt.get_url(-1)
    return str(url)

def get_photos_from_publit_make_qr():
    pt = publitio_api('r2xGdVpnmXkcs14tgpoX','rpJd0TxhrQ7P7zDQDzPQSX3k2RPm93k8')
    lst = pt.get_list(1,1000)#there is 1466 skipped first get 1000 which is mac limit

    url_list = []
    for i in lst['files']:
        url = (i['url_preview'])
        url_list.append(url)
    
    lst = pt.get_list(1001,1000)#get the rest 
    for i in lst['files']:
        url = (i['url_preview'])
        url_list.append(url)

    for i in url_list:
        qr_generator(create_name(),str(i))
     
def images_to_qr():   
    for files in create_list_of_files("images"):
        url = upload_file_to_publit(str(files))
        qr_generator(create_name(),url)

def blank_qr():
    for i in range(20):
        qr_generator(create_name(),str(i))

def data_from_json_to_qr():
    json_file = open('result.json')
    data= json.load(json_file)

    for i in data:
        qr_data = f"{i}_{data[i]}"
        qr_generator(i,qr_data)

def sha256_to_qr():
    a=0
    
    for i in "abimbanaiskenceediyor@gmail.com":
        a+=1

        sha256 = hashlib.sha256()
        sha256.update(bytes(i,'utf8'))
        string_hash = sha256.hexdigest()
        
        txt = f"{a}_{string_hash}"
        print(txt)
        #qr_generator(create_name(),txt)

def yt_links_to_qr():
    
    txt_file = open('ytlinks.txt')
    count= 0

    while True:
        line = txt_file.readline()
        if not line:
            break
        if line.startswith("y") or line.startswith(" y"):
            #print(line)
            qr_generator(create_name(),str(line))
    
    txt_file.close()

def theuselessweb_to_qr():
    urls =  ["https://longdogechallenge.com/",

		"https://checkboxrace.com/",

		"https://onesquareminesweeper.com/",

		"http://heeeeeeeey.com/",

		"http://corndog.io/",

		"https://binarypiano.com/",

		"https://mondrianandme.com/",

		"https://puginarug.com",

		"http://floatingqrcode.com/",

		"https://checkboxolympics.com/",

		"https://alwaysjudgeabookbyitscover.com",

		"https://thatsthefinger.com/",

		"https://cant-not-tweet-this.com/",

		"https://cursoreffects.com",

		"http://eelslap.com/",

		"http://www.staggeringbeauty.com/",

		"http://burymewithmymoney.com/",

		"https://smashthewalls.com/",

		"https://jacksonpollock.org/",

		"http://endless.horse/",

		"http://drawing.garden/",

		"https://www.trypap.com/",

		"http://www.republiquedesmangues.fr/",

		"http://www.movenowthinklater.com/",

		"http://www.rrrgggbbb.com/",

		"http://www.koalastothemax.com/",

		"http://www.everydayim.com/",

		"http://randomcolour.com/",

		"http://cat-bounce.com/",

		"http://chrismckenzie.com/",

		"https://thezen.zone/",

		"http://ninjaflex.com/",

		"http://ihasabucket.com/",

		"http://corndogoncorndog.com/",

		"http://www.hackertyper.com/",

		"https://pointerpointer.com",

		"http://imaninja.com/",

		"http://www.partridgegetslucky.com/",

		"http://www.ismycomputeron.com/",

		"http://www.nullingthevoid.com/",

		"http://www.muchbetterthanthis.com/",

		"http://www.yesnoif.com/",

		"http://lacquerlacquer.com",

		"http://potatoortomato.com/",

		"http://iamawesome.com/",

		"https://strobe.cool/",

		"http://thisisnotajumpscare.com/",

		"http://doughnutkitten.com/",

		"http://crouton.net/",

		"http://corgiorgy.com/",

		"http://www.wutdafuk.com/",

		"http://unicodesnowmanforyou.com/",

		"http://chillestmonkey.com/",

		"http://scroll-o-meter.club/",

		"http://www.crossdivisions.com/",

		"http://tencents.info/",

		"https://boringboringboring.com/",

		"http://www.patience-is-a-virtue.org/",

		"http://pixelsfighting.com/",

		"http://isitwhite.com/",

		"https://existentialcrisis.com/",

		"http://onemillionlols.com/",

		"http://www.omfgdogs.com/",

		"http://oct82.com/",

		"http://chihuahuaspin.com/",

		"http://www.blankwindows.com/",

		"http://tunnelsnakes.com/",

		"http://www.trashloop.com/",

		"http://www.ascii-middle-finger.com/",

		"http://spaceis.cool/",

		"http://www.doublepressure.com/",

		"http://www.donothingfor2minutes.com/",

		"http://buildshruggie.com/",

		"http://buzzybuzz.biz/",

		"http://yeahlemons.com/",

		"http://wowenwilsonquiz.com",

		"https://thepigeon.org/",

		"http://notdayoftheweek.com/",

		"http://www.amialright.com/",

		"http://nooooooooooooooo.com/",

		"https://greatbignothing.com/",

		"https://zoomquilt.org/",

		"https://dadlaughbutton.com/",

		"https://remoji.com/",

		"http://papertoilet.com/",

		"https://loopedforinfinity.com/",

		"https://www.bouncingdvdlogo.com/",

		"https://findtheinvisiblecow.com/"]

    for url in urls:
        qr_generator(create_name(),url)

def lorempicsum_to_qr():
    json_file = open("randompic.json") 
    data = json.load(json_file)

    for i in data:
        #print(i["download_url"])
        qr_generator(create_name(),i["download_url"])

def random_wiki_to_qr():
    url = "https://tr.wikipedia.org/wiki/Special:Random" # one url but goes diffirent page everytime

    for i in range(300):
        qr_generator(create_name(),url)

def random_meme_to_qr():
    url = "https://img.randme.me" # this is one url but goes diffirent page everytime

    for i in range(500):
        qr_generator(create_name(),url)

def spotify_urls_to_qr():
    f = open('spotify.json')
    data = json.load(f)
    for i in data:
        #print(i["url"])
        qr_generator(create_name(),i["url"])

def videos_to_qr():
    urls= ["https://media.publit.io/file/20240311-121321.html",
           'https://media.publit.io/file/20240311-145530.html',
           "https://media.publit.io/file/VID-20240312-WA0005.html",
           "https://media.publit.io/file/VID-20240312-WA0000.html",
           "https://media.publit.io/file/VID-20240312-WA0001.html",
           "https://media.publit.io/file/VID-20240311-WA0041.html",
           "https://media.publit.io/file/VID-20240311-WA0006.html",
           "https://media.publit.io/file/VID-20240311-WA0042.html",
           "https://media.publit.io/file/VID-20240311-WA0026.html",
           "https://media.publit.io/file/VID-20240311-WA0025.html",
           "https://media.publit.io/file/VID-20240311-WA0000.html",
           "https://media.publit.io/file/VID-20240310-WA0040.html",
           "https://media.publit.io/file/VID-20240310-WA0037.html",
           "https://media.publit.io/file/VID-20240310-WA0036.html",
           "https://media.publit.io/file/VID-20240310-WA0035.html",
           "https://media.publit.io/file/VID-20240310-WA0033.html",
           "https://media.publit.io/file/VID-20240310-WA0031.html",
           "https://media.publit.io/file/VID-20240310-WA0026.html",
           "https://media.publit.io/file/VID-20240310-WA0024.html",
           "https://media.publit.io/file/VID-20240310-WA0023.html",
           "https://media.publit.io/file/VID-20240310-WA0021.html",
           "https://media.publit.io/file/VID-20240310-WA0013.html",
           "https://media.publit.io/file/VID-20240310-WA0012.html",
           "https://media.publit.io/file/20240311-111831.html"

           ]
    
    for i in urls:
        name = i[29:]
        try:
            name , _ = name.split(".")
        except:
            pass
        qr_generator(name,i)

def rename_qrs():
    lst = create_list_of_files(r"Final\130__")
    for i in lst:
        rename(f"Final/130__/{i}",f"{create_name()}.png")


if __name__ == '__main__':
    #images_to_qr()
    #blank_qr()
    #data_from_json_to_qr()
    sha256_to_qr()
    #yt_links_to_qr()
    #theuselessweb_to_qr()
    #lorempicsum_to_qr()
    #random_wiki_to_qr()
    #random_meme_to_qr()
    #spotify_urls_to_qr()
    #get_photos_from_publit_make_qr()
    #videos_to_qr()
    #rename_qrs()
    #qr_generator("ilkqr","https://media.publit.io/file/K-sa-bir-a-klama-ekleyin-2.png")
    #qr_generator("1025438697","http://ikaganacar.com/1025438697")
    pass



