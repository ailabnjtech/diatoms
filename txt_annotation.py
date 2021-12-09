import os
from os import getcwd

#---------------------------------------------#
#   训练前一定要注意修改classes
#   种类顺序需要和model_data下的txt一样
#---------------------------------------------#
classes = ['Acanthoceras', 'Achnanthes', 'Achnanthidium', 'Actinella', 'Actinocyclus', 'Actinoptychus senarius', 'Adlafia', 'Amphicampa', 'Amphipleura', 'Amphora', 'Aneumastus', 'Anomoeoneis', 'Asterionella', 'Aulacoseira', 'Bacillaria', 'Biddulphia reticulata', 'Biremis', 'Boreozonacola', 'Brachysira', 'Brebissonia', 'Caloneis', 'Campylodiscus', 'Campyloneis grevillei', 'Capartogramma', 'Cavinula', 'Chaetoceros', 'Chamaepinnularia', 'Cocconeis', 'Coscinodiscus', 'Cosmioneis', 'Craticula', 'Ctenophora', 'Cyclostephanos', 'Cyclotella', 'Cymatopleura', 'Cymbella', 'Cymbellonitzschia', 'Cymbopleura', 'Decussata', 'Delicata', 'Denticula', 'Diadesmis', 'Diatoma', 'Diatomella', 'Didymosphenia', 'Diploneis', 'Diprora', 'Discostella', 'Distrionella', 'Ellerbeckia', 'Encyonema', 'Encyonopsis', 'Entomoneis', 'Envekadea', 'Eolimna', 'Epithemia', 'Eucocconeis', 'Eunotia', 'Eupodiscus', 'Fallacia', 'Fragilaria', 'Fragilariforma', 'Frickea', 'Frustulia', 'Geissleria', 'Genkalia', 'Gliwiczia', 'Gomphoneis', 'Gomphonella', 'Gomphonema', 'Gomphosinica', 'Gomphosphenia', 'Grunowia', 'Gyrosigma', 'Halamphora', 'Hannaea', 'Hippodonta', 'Humidophila', 'Hydrosera', 'Hygropetra', 'Iconella', 'Karayevia', 'Kobayasiella', 'Krasskella', 'Kurtkrammeria', 'Lacustriella', 'Lemnicola', 'Licmophora cf. ehrenbergii', 'Lindavia', 'Luticola', 'Martyana schulzii', 'Mastogloia', 'Mayamaea', 'Melosira', 'Meridion', 'Microcostatus', 'Minidiscus vodyanitskiyi', 'Muelleria', 'Navicula', 'Navicymbula', 'Neidiomorpha', 'Neidiopsis', 'Neidium', 'Ninastrelnikovia', 'Nitzschia', 'Nupela', 'Odontidium', 'Orthoseira', 'Oxyneis', 'Parlibellus', 'Peronia', 'Phaeodactylum', 'Pinnularia', 'Placoneis', 'Plagiotropis', 'Planothidium', 'Platessa', 'Playaensis', 'Pleurosigma', 'Pleurosira', 'Prestauroneis', 'Proschkinia', 'Psammothidium', 'Pseudofallacia', 'Pseudostaurosira', 'Punctastriata', 'Reimeria', 'Rexlowea', 'Rhoicosphenia', 'Rhopalodia musculus', 'Rossithidium', 'Scoliopleura', 'Sellaphora', 'Seminavis strigosa', 'Semiorbis', 'Simonsenia', 'Skabitschewskia', 'Skeletonema', 'Spicaticribra', 'Stauroforma', 'Stauroneis', 'Staurophora', 'Staurosira', 'Staurosirella', 'Stephanodiscus', 'Stephanopyxis turris', 'Surirella', 'Synedra', 'Tabellaria', 'Tabularia', 'Terpsinoe', 'Tetracyclus', 'Thalassiosira', 'Tryblionella', 'Ulnaria', 'Urosolenia']
sets = ["train", "test"]

wd = getcwd()
for se in sets:
    list_file = open('cls_' + se + '.txt', 'w')

    datasets_path = "datasets/" + se
    types_name = os.listdir(datasets_path)
    for type_name in types_name:
        if type_name not in classes:
            continue
        cls_id = classes.index(type_name)
        
        photos_path = os.path.join(datasets_path, type_name)
        photos_name = os.listdir(photos_path)
        for photo_name in photos_name:
            _, postfix = os.path.splitext(photo_name)
            if postfix not in ['.jpg', '.png', '.jpeg']:
                continue
            list_file.write(str(cls_id) + ";" + '%s/%s'%(wd, os.path.join(photos_path, photo_name)))
            list_file.write('\n')
    list_file.close()

