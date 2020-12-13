import os

directory = r'C:\Users\user\Documents\SBA\s50_sim_12'
for filename in os.listdir(directory):
    if filename.endswith(".htm"):
        with open(os.path.join(directory, filename), 'r') as file:
            filedata = file.read()
            
            # Replace the target string
            filedata = filedata.replace('../images/inferno.jpg', 'https://i.postimg.cc/9FkpxMLB/Artboard-2infernobird.png')
            filedata = filedata.replace('../images/vipers.jpg', 'https://i.postimg.cc/rm4QKhWq/Artboard_1-vipers.png')
            filedata = filedata.replace('../images/vipers.jpg', 'https://i.postimg.cc/rm4QKhWq/Artboard_1-vipers.png')
            filedata = filedata.replace('../images/boston.jpg', 'https://s20.postimg.cc/wp6u87kd9/Untitled-4.png')
            filedata = filedata.replace('../images/bullets.jpg', 'https://s20.postimg.cc/vbcileuml/Artboard_1-large.png')
            filedata = filedata.replace('../images/charlotte.jpg', 'https://i.postimg.cc/pr9d6tkC/Artboard-1-aviators.png')
            filedata = filedata.replace('../images/nightmare.jpg', 'https://i.postimg.cc/Wz7ymyCc/Artboard-1-nightmare.png')
            filedata = filedata.replace('../images/colorado.jpg', 'https://s20.postimg.cc/i5zp6tedp/Artboard_1-sba_1.png')
            filedata = filedata.replace('../images/ravens.jpg', 'https://s20.postimg.cc/5plmes3jx/SBA-_Ravens-_Logo-_Large.png')
            filedata = filedata.replace('../images/jokers.jpg', 'https://i.postimg.cc/J0BzSGQG/Artboard-1-joker-big.png')
            filedata = filedata.replace('../images/rush.jpg', 'https://i.postimg.cc/YSkLgfz8/Artboard-1-rushlarge.png')
            filedata = filedata.replace('../images/knights.jpg', 'https://s20.postimg.cc/uvslpadhp/Artboard_6-large.png')
            #filedata = filedata.replace('../images/ocelots.jpg', 'https://i.imgur.com/6nvTyuP.png')
            filedata = filedata.replace('../images/ocelots.jpg', 'https://i.postimg.cc/qv46Pxt8/ocelots.png') #sorry nano
            filedata = filedata.replace('../images/vice.jpg', 'https://i.postimg.cc/CMJq0mc5/Artboard-1-copy-vise.png')
            filedata = filedata.replace('../images/maulers.jpg', 'https://s20.postimg.cc/h2wzue22l/SBA-_Maulers-_Logo-_Large.png')
            filedata = filedata.replace('../images/monarchs.jpg', 'https://i.postimg.cc/Z5SvgyJS/Artboard-1-monarchs.png')
            filedata = filedata.replace('../images/prowlers.jpg', 'https://i.imgur.com/oZUmyjQ.png')
            filedata = filedata.replace('../images/rail.jpg', 'https://i.postimg.cc/ZR4PbzQb/Artboard-1-rail.png')
            filedata = filedata.replace('../images/abcdpage.jpg', 'https://i.postimg.cc/J0FBgbt2/SBA-_Rampage-_Logo.png')
            filedata = filedata.replace('../images/rampage.jpg', 'https://i.postimg.cc/J0FBgbt2/SBA-_Rampage-_Logo.png')
            filedata = filedata.replace('../images/ironmen.jpg', 'https://i.postimg.cc/RCsDGnJp/Artboard-1-ironmen2.png')
            filedata = filedata.replace('../images/corsairs.jpg', 'https://i.postimg.cc/L8qPN7QD/Artboard-1-1080.png')
            filedata = filedata.replace('../images/stlouis.jpg', 'https://sba.today/forums/uploads/monthly_2020_02/Battalion.png.c2cedf75a1e4e085bce7c60025f71bbb.png')
            filedata = filedata.replace('../images/tbirds.jpg', 'https://s20.postimg.cc/m85lljail/SBA-_Thunderbirds-_Logo-_Alternate-_Large.png')
            filedata = filedata.replace('../images/vancouver.jpg', 'https://i.postimg.cc/7ZSnWFWq/Artboard-1-wolverines.png')
            filedata = filedata.replace('../images/wild.jpg', 'https://i.postimg.cc/gcsCyYVm/wild.png')         
            
            if filedata.find("src=../images/") != -1:
                print(os.path.join(directory, filename))
                #way to find any outliers that we haven't replaced

            # Write the file out again
            with open(os.path.join(directory, filename), 'w') as file:
                file.write(filedata)
    else:
        continue