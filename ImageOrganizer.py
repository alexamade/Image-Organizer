# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:26:27 2020

@author: Somil
"""

import PIL.Image
import os
import shutil
import datetime



class ImageOrganizer:
    def __init__(self,dirname=''):
        self.images = os.listdir(dirname)
        self.dirname = dirname
        
    # def preprocess_exif(self,data):
    #     data = data.strip()
    #     data = data.strip('\x00')
        
    #     return data
    def preprocess_exif(self, exif_data):
        return exif_data.strip().replace('\x00', '')

    # function called rename_files_with_datetime. Purpose to rename the files with the timestamp of the image in the format YYYYMMDD_HHMMSS.
    # also needs to handle multiple directories and subdirectories and rename the files in each level. 
    def rename_files_with_datetime(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
                
            if exif and 306 in exif:
                ts = self.preprocess_exif(exif[306])
                date = ts.split(' ')[0]
                time = ts.split(' ')[1]
                new_name = date.replace(':','') + '_' + time.replace(':','') + '.jpg'
                
                os.rename(os.path.join(self.dirname,fname),os.path.join(self.dirname,new_name))
                print("Image {} renamed to {} successfully\n".format(fname,new_name))
            else:
                print(f"No EXIF timestamp found for {fname}")
    
    
    def sort_by_device(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
            
            manuf = self.preprocess_exif(exif[271])
            device = self.preprocess_exif(exif[272])
            merged = manuf + ' ' + device
            
            if not os.path.isdir(merged):
                os.mkdir(merged)
        
            shutil.move(os.path.join(self.dirname,fname),os.path.join(merged,fname))
            print("Image {} moved from {} to {} successfully\n".format(fname,os.path.join(self.dirname,fname),os.path.join(merged,fname)))
            
            
    def sort_by_year(self, parent_folder):
        # Ensure the parent folder exists
        if not os.path.isdir(parent_folder):
            os.mkdir(parent_folder)

        # Ensure the no_datetime folder exists
        no_datetime_folder = os.path.join(parent_folder, 'no_datetime')
        if not os.path.isdir(no_datetime_folder):
            os.mkdir(no_datetime_folder)

        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname, fname)) as img:
                exif = img._getexif()

            if exif and 306 in exif:
                ts = self.preprocess_exif(exif[306])
                date = ts.split(' ')[0]
                year = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%Y')
                year_folder = os.path.join(parent_folder, year)

                if not os.path.isdir(year_folder):
                    os.mkdir(year_folder)

                shutil.copy(os.path.join(self.dirname, fname), os.path.join(year_folder, fname))
                print(f"Image {fname} moved from {os.path.join(self.dirname, fname)} to {os.path.join(year_folder, fname)} successfully\n")
            else:
                print(f"No EXIF timestamp found for {fname}, moving to no_datetime folder")
                shutil.copy(os.path.join(self.dirname, fname), os.path.join(no_datetime_folder, fname))
                print(f"Image {fname} moved from {os.path.join(self.dirname, fname)} to {os.path.join(no_datetime_folder, fname)} successfully\n")
            

    def sort_by_yr_month(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
            if exif and 306 in exif:
                if exif and 306 in exif:
                    ts = self.preprocess_exif(exif[306])
                else:
                    print(f"No EXIF timestamp found for {fname}")
                    continue
            else:
                print(f"No EXIF timestamp found for {fname}")
                continue
            
            ts = self.preprocess_exif(exif[306])
            date = ts.split(' ')[0]
            year = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%Y')
            month = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%b')
                     
            if not os.path.isdir(year):
                os.mkdir(year)
            
            if not os.path.isdir(os.path.join(year,month)):
                os.mkdir(os.path.join(year,month))
        
            shutil.copy(os.path.join(self.dirname,fname),os.path.join(year,month,fname))
            print("Image {} moved from {} to {} successfully\n".format(fname,os.path.join(self.dirname,fname),os.path.join(year,month,fname)))
            
        
    def sort_by_device_yr_month(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
            
            ts = self.preprocess_exif(exif[306])
            date = ts.split(' ')[0]
            manuf = self.preprocess_exif(exif[271])
            device = self.preprocess_exif(exif[272])
            merged = manuf + ' ' + device
            year = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%Y')
            month = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%b')
            
            if not os.path.isdir(merged):
                os.mkdir(merged)
                
            if not os.path.isdir(os.path.join(merged,year)):
                os.mkdir(os.path.join(merged,year))
            
            if not os.path.isdir(os.path.join(merged,year,month)):
                os.mkdir(os.path.join(merged,year,month))
        
            shutil.copy(os.path.join(self.dirname,fname),os.path.join(merged,year,month,fname))
            print("Image {} moved from {} to {} successfully\n".format(fname,os.path.join(self.dirname,fname),os.path.join(merged,year,month,fname)))
        
