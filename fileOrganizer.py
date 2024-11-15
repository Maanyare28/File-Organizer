import os
import shutil

#path of where we want to search, AKA our directory that we will be working with
path_directory = r'C:\Users\Ahass\OneDrive\Desktop' #desktop the one we want
images_path_directory = r'C:\Users\Ahass\OneDrive\Desktop\Images' #puts the images
pdf_path_directory = r'C:\Users\Ahass\OneDrive\Desktop\PDFs' #puts the pdfs in specific place
pp_path_directory = r'C:\Users\Ahass\OneDrive\Desktop\Presentations' #puts the power points in a specific place
txt_path_directory = r'C:\Users\Ahass\OneDrive\Desktop\Text Files' #puts the text folders in a specific place
mp3_path_directory = r'C:\Users\Ahass\OneDrive\Desktop\Audios' #puts audio files to Audios folder

# Where we search for extension type
txtExtension = '.txt'
jpgExtension = '.JPG'
docxExtension ='.docx'
pngExtension = '.png'
pptxExtension = '.pptx'
pdfExtension = '.pdf'
mp3Extension = '.mp3'

#For loop to search through the directory
for file in os.listdir(path_directory):
    file_path = os.path.join(path_directory, file) #joins the path_directory(dir where the data is) with the file(the one we are searching for)

    if os.path.splitext(file)[1] == txtExtension:
        shutil.move(file_path, txt_path_directory)
        print("Text moved successfully")

    elif os.path.splitext(file)[1] == jpgExtension:
        shutil.move(file_path, images_path_directory)
        print("JPS moved successfully")

    elif os.path.splitext(file)[1] == docxExtension:
        shutil.move(file_path, txt_path_directory)
        print("Documents moved successfully")

    elif os.path.splitext(file)[1] == pngExtension:
        shutil.move(file_path, images_path_directory)
        print("PNGS moved successfully")

    elif os.path.splitext(file)[1] == pptxExtension:
        shutil.move(file_path, pp_path_directory)
        print("PowerPoints moved successfully")

    elif os.path.splitext(file)[1] == pdfExtension:
        shutil.move(file_path, pdf_path_directory)
        print("PDFS moved successfully")

    elif os.path.splitext(file)[1] == mp3Extension:
        shutil.move(file_path, mp3_path_directory)
        print("Audio moved successfully")

