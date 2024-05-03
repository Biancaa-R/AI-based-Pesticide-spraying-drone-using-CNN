import csv
f=open(r"C:\Users\Biancaa. R\rpi_disease\pest_classification\training_set.csv",'r')
reader=csv.reader(f)
value=reader
categories=[]
# for i in reader:
#     #print(i)
#     if i[1] not in categories and i[1]!='label':
#         categories.append(i[1])
# print(categories)

'''
['apoderus_javanicus', 'aulacaspis_tubercularis', 'ceroplastes_rubens', 'cisaberoptus_kenyae', 'dappula_tertia', 
'dialeuropora_decempuncta', 'erosomyia_sp', 'icerya_seychellarum', 'ischnaspis_longirostris', 'mictis_longicornis', 
'neomelicharia_sparsa', 'normal', 'orthaga_euadrusalis', 'procontarinia_matteiana', 'procontarinia_rubus', 'valanga_nigricornis']'''

import os
folder_dir="C:\\Users\\Biancaa. R\\rpi_disease\\pest_classification\\training_dataset"
folder_name="C:\\Users\\Biancaa. R\\rpi_disease\\pest_classification\\images"
for file in os.listdir(folder_dir):

    # for i in reader:
    #     if i[0]==file:
    #         category=i[1]
            
    #         if(file.endswith("jpg")):
    #             filename=file.removesuffix('.jpg')
    #             os.rename(folder_dir+"\\"+file,folder_name+"\\"+category+"\\"+filename+".jpg")
        
    #         if(file.endswith("png")):
    #             filename=file.removesuffix('.png')
    #             os.rename(folder_dir+"\\"+file,folder_name+"\\"+category+"\\"+filename+".png")

    for i in value:
        if i[0]==str(file):
            category=i[1]

            if(file.endswith("jpg")):
                filename=file.removesuffix('.jpg')
                os.rename(folder_dir+"\\"+file,folder_name+"\\"+category+"\\"+filename+".jpg")
        
            if(file.endswith("png")):
                filename=file.removesuffix('.png')
                os.rename(folder_dir+"\\"+file,folder_name+"\\"+category+"\\"+filename+".png")
print("done")

