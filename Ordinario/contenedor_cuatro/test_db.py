from models import *
from base_alchemy import *

anime = AnimeBySearch(1213, 'lalala', '24', 'seinen', '6.9', 'www.lalala.com', '9', 'asdsdfasf asdfsadf fghd trhgr hgnhgdn gfdh', '2007', 'Yoply')

#Base.metadata.create_all(engine)


#session.add(anime)
#session.commit()
anim = session.query(AnimeBySearch).all()
for cosa in anim:
    print(cosa.title + "asd"+ cosa.synopsis, cosa.image_url)
    print()
session.close()