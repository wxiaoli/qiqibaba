import cv2
import numpy as np
 
def combine_lp_res(I_img,tex):
    nh,nw = 300,200
    target = np.ones((nh,nw),dtype=np.uint8)*255
    img_tex = cv2.cvtColor(target, cv2.COLOR_GRAY2BGR)  
    h,w = I_img.shape[:2]
    img_tex[10:10+h,10:10+w,:] = I_img
    cv2.putText(img_tex,tex, (20,240), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2, cv2.LINE_AA)
    return img_tex
  
if __name__ == '__main__':
    I_img = cv2.imread('C:/p2021_1_11_20_000030_lp0.jpg')
    combine_img = combine_lp_res(I_img,'hello world.')
    cv2.imshow("img_new_white", combine_img)
    cv2.waitKey() 