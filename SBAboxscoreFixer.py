import os

directory = r'C:\Users\amhad\Documents\SBA\Boxes'
for filename in os.listdir(directory):
    if filename.endswith(".htm"):
        with open(os.path.join(directory, filename), 'r') as file:
            filedata = file.read()
            
            # Replace the target string
            filedata = filedata.replace('../images/VOODOO.jpg', 'https://i.imgur.com/eFwOrOk.png') 
            filedata = filedata.replace('../images/barons.jpg', 'https://i.postimg.cc/RZpKCSwg/Artboard-1-barons-1.png') 
            filedata = filedata.replace('../images/empire.jpg', 'https://i.postimg.cc/rm8j5sC9/Artboard-1-empire1.png') 
            filedata = filedata.replace('../images/lightning.jpg', 'https://i.postimg.cc/k4rnKbtR/Artboard-1-lightning-1.png')   
            filedata = filedata.replace('../images/badgers.jpg', 'https://i.postimg.cc/hPTnz2Dg/Artboard-1-hhb-1.png ')   
            filedata = filedata.replace('../images/titans.jpg', 'https://i.postimg.cc/CKDMbLLd/Artboard-1-titans-1.png')   
            filedata = filedata.replace('../images/cockerels.jpg', 'https://i.postimg.cc/V65Trh6s/Artboard-1-cockerels1.png')   
            filedata = filedata.replace('../images/herd.jpg', 'https://i.postimg.cc/k4g6ZX8w/Artboard-1-herd-1.png')   
            filedata = filedata.replace('../images/jackals.jpg', 'https://i.postimg.cc/xdPhvZ27/Artboard-1-jackals.png')   
            filedata = filedata.replace('../images/thoroughbreds.jpg', 'https://i.postimg.cc/5tWnNnXT/Artboard-1-thoroughbreds1.png')   
            filedata = filedata.replace('../images/lions.jpg', 'https://i.postimg.cc/xCnhcD0b/Artboard-1-lions-1.png')   
            filedata = filedata.replace('../images/bombers.jpg', 'https://i.postimg.cc/NfXrQdDm/Artboard-1-njb.png')   
            filedata = filedata.replace('../images/hounds.jpg', 'https://i.postimg.cc/3w8z7NQv/Artboard-1-hounds1.png')   
            filedata = filedata.replace('../images/odyssey.jpg', 'https://i.postimg.cc/8CSjRvPs/Artboard-1-odyssey.png')   
            filedata = filedata.replace('../images/hydra.jpg', 'https://i.postimg.cc/W1B3Zdrq/Artboard-1-hydra3-1.png')   
            filedata = filedata.replace('../images/asylum.jpg', 'https://i.postimg.cc/Kz1Lj8zj/Artboard-1-asylum1-1.png')   
            filedata = filedata.replace('../images/whiteout.jpg', 'https://i.postimg.cc/tJ8MRQ31/Artboard-1-whiteout.png')          
            filedata = filedata.replace('../images/crusaders.jpg', 'https://i.postimg.cc/W4n4L7Wm/Artboard-1-crusaders1-1.png')      
            filedata = filedata.replace('../images/resistance.jpg', 'https://i.postimg.cc/sXLbD57L/Artboard-1-resistance4-1.png')      
            filedata = filedata.replace('../images/hyenas.jpg', 'https://i.postimg.cc/mgM2mjN2/Artboard-1-hyenas-1.png')      
            filedata = filedata.replace('../images/triceratops.jpg', '') 
            filedata = filedata.replace('../images/owls.jpg', '') 
            if filedata.find("src=../images/") != -1:
                print(os.path.join(directory, filename))
                #way to find any outliers that we haven't replaced

            # Write the file out again
            with open(os.path.join(directory, filename), 'w') as file:
                file.write(filedata)
    else:
        continue