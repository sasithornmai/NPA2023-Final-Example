                
test = [{"name":"Chelsea","local_names":{"vi":"Chelsea, Luân Đôn","nl":"Chelsea","fa":"چلسی","eu":"Chelsea","fr":"Chelsea","da":"Chelsea","ur":"چیلسی، لندن","ar":"تشيلسي","pl":"Chelsea","et":"Chelsea","es":"Chelsea","sk":"Chelsea","el":"Τσέλσι","ga":"Chelsea","ko":"첼시","he":"צ'לסי","ja":"チェルシー","af":"Chelsea, Londen","ru":"Челси","zh":"車路士","en":"Chelsea","sh":"Chelsea, London","hu":"Chelsea","sv":"Chelsea, London","de":"Chelsea","tr":"Chelsea, Londra","id":"Chelsea, London","uk":"Челсі","no":"Chelsea","it":"Chelsea","hi":"चेल्सी, लंदन","az":"Çelsi","pt":"Chelsea"},"lat":51.4875167,"lon":-0.1687007,"country":"GB","state":"England"}]
                
              
print(test[0]["lat"])


test2 ={
    "coord":
        {"lon":-0.1687,
         "lat":51.4875},
        "weather":
            [
                {
                    "id":802,
                    "main":"Clouds",
                    "description":"scattered clouds",
                    "icon":"03d"
                    }
                ],
            "base":"stations",
            "main":
                {
                    "temp":290.28,
                    "feels_like":289.62,"temp_min":288.81,"temp_max":291.18,"pressure":1017,"humidity":60},"visibility":10000,"wind":{"speed":2.57,"deg":250},"clouds":{"all":40},"dt":1710951987,"sys":{"type":2,"id":2091269,"country":"GB","sunrise":1710914558,"sunset":1710958406},"timezone":0,"id":2653265,"name":"Chelsea","cod":200}

print(test2["weather"][0]["description"])
print(test2["main"]["temp"])

q = "London"
limit = 1
appid = "eb84a3bb03a361e8c9ae42914ec98ac3"