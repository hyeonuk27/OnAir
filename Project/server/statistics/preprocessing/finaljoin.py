import os
import glob
import pandas as pd

os.chdir("./")
extension = 'csv' #csv로 파일 확장자 지정 
all_filenames = [i for i in glob.glob('res_*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ]) #지정한 파일 경로에 있는 모든 파일 불러오기
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig') 