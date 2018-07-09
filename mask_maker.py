import utils

utils.help_option(
'''
mask_maker 
  make answer data from 'job_records' 
  and then save them into 'answer_dir'
  
synopsis
  python mask_maker.py job_records answer_dir

example
  python mask_maker.py ./job_records.bin ./answers
'''
)

import manual_selector, textMaskMakerUI 
import sys, cv2

def main(job_records_path):
    now_idx, jobs, selected = manual_selector.load(job_records_path)
    for imgpath, imgname in selected:
        print(imgname)
        textMaskMakerUI.main(imgpath,imgname)
        #img = cv2.imread(imgpath)
        #cv2.imshow('img',img); cv2.waitKey(0)                
  
if __name__ == '__main__':
    main(sys.argv[1])