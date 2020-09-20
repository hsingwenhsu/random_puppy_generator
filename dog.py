import sys
sys.path.append('usr/local/')
import cv2
import numpy as np
from random import randrange

comp_path = 'components/'
output_path = 'doggie/'

def paste_mouth(dog, mouth): #paste the mouth
    mouth = cv2.bitwise_not(mouth)
    mouth = cv2.resize(mouth, (int(mouth.shape[1]//4.5), int(mouth.shape[0]//4.5)), cv2.INTER_AREA)
    kernel = np.ones((3, 3))
    mouth = cv2.dilate(mouth, kernel, iterations=1)
    mouth = cv2.bitwise_not(mouth)
    m_start_x = 110
    m_start_y = 140
    m_end_x = m_start_x+mouth.shape[1]
    m_end_y = m_start_y+mouth.shape[0]
    patch = dog[m_start_y:m_end_y, m_start_x:m_end_x]
    patch[mouth==0] = mouth[mouth==0]
    dog[m_start_y:m_end_y, m_start_x:m_end_x] = patch
    return dog
def color(dog, color_list, color_idx):
    print(color_list[color_idx])
    b = color_list[color_idx][0]
    g = color_list[color_idx][1]
    r = color_list[color_idx][2]
    if(color_idx==0):
        dog[np.where((dog==[255,255,255]).all(axis=2))] = [b, g, r]
    else:
        b_pre = color_list[color_idx-1][0]
        g_pre = color_list[color_idx-1][1]
        r_pre = color_list[color_idx-1][2]
        dog[np.where((dog==[b_pre,g_pre,r_pre]).all(axis=2))] = [b, g, r]
    return dog
def draw_eye(dog, eyetype): #type: 0~4
    print(eyetype)
    if eyetype==0:
        x_offset = 10
        cv2.circle(dog, (133-x_offset, 133), 30, (255, 255, 255), -1)
        cv2.circle(dog, (212-x_offset, 133), 30, (255, 255, 255), -1)
        cv2.circle(dog, (133-x_offset, 133), 30, (0, 0, 0), 3)
        cv2.circle(dog, (212-x_offset, 133), 30, (0, 0, 0), 3)
        cv2.circle(dog, (133-x_offset, 133), 10, (0, 0, 0), -1)
        cv2.circle(dog, (212-x_offset, 133), 10, (0, 0, 0), -1)
    if eyetype==1:
        x_offset = 10
        cv2.circle(dog, (133-x_offset, 133), 30, (255, 255, 255), -1)
        cv2.circle(dog, (212-x_offset, 133), 30, (255, 255, 255), -1)
        cv2.circle(dog, (133-x_offset, 133), 30, (0, 0, 0), 3)
        cv2.circle(dog, (212-x_offset, 133), 30, (0, 0, 0), 3)

        cv2.circle(dog, (133-20, 133), 10, (0, 0, 0), -1)
        cv2.circle(dog, (212+5, 133), 10, (0, 0, 0), -1)
    if eyetype==2:
        x_offset = 10
        cv2.circle(dog, (133-x_offset, 133), 30, (255, 255, 255), -1)
        cv2.circle(dog, (212-x_offset, 133), 30, (255, 255, 255), -1)
        cv2.circle(dog, (133-x_offset, 133), 30, (0, 0, 0), 3)
        cv2.circle(dog, (212-x_offset, 133), 30, (0, 0, 0), 3)

        cv2.circle(dog, (133-x_offset, 133), 25, (0, 0, 0), -1)
        cv2.circle(dog, (212-x_offset, 133), 25, (0, 0, 0), -1)

        cv2.circle(dog, (133-x_offset, 133-5), 5, (255, 255, 255), -1)
        cv2.circle(dog, (212-x_offset, 133-5), 5, (255, 255, 255), -1)
    if eyetype==3:
        print('line 69', eyetype)
        x_offset = 10
        cv2.circle(dog, (133-x_offset, 133), 28, (255, 255, 255), -1)
        cv2.circle(dog, (212-x_offset, 133), 28, (255, 255, 255), -1)
        cv2.circle(dog, (133-x_offset, 133), 25, (0, 0, 0), 5)
        cv2.circle(dog, (212-x_offset, 133), 25, (0, 0, 0), 5)
    if eyetype==4:
        
        
        x_offset = 10
        cv2.circle(dog, (133-x_offset, 133), 20, (0, 0, 0), -1)
        cv2.circle(dog, (212-x_offset, 133), 20, (0, 0, 0), -1)
        #cv2.circle(dog, (133-x_offset, 133), 25, (0, 0, 0), 5)
        #cv2.circle(dog, (212-x_offset, 133), 25, (0, 0, 0), 5)
    return dog
def get_puppy(dog_list, mouth, color_list):
    which_puppy = randrange(4)
    which_color = randrange(3)
    which_eye = randrange(4)
    dog_list[which_puppy] = paste_mouth(dog_list[which_puppy], mouth)
    colored = color(dog_list[which_puppy], color_list, which_color)
    your_puppy = draw_eye(dog_list[which_puppy], which_eye)
    cv2.imshow('Your puppy!', your_puppy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def gen_all_puppies(dog_list, mouth, color_list):
    for i in range(dog_num):
        dog_list[i] = paste_mouth(dog_list[i], mouth)
    
    for i in range(dog_num): #4
        for j in range(3):#3
            colored = color(dog_list[i], color_list, j)
            
            for k in range(5):#4
                print(i, j, k)
                todraweye = colored[:, :].copy()
                todraweye = draw_eye(todraweye, k)
                name = str(i)+'_'+str(j)+'_'+str(k)+'.png'
                cv2.imwrite('doggie/'+name, todraweye)

#prepare dogs
dog_list = []
img = cv2.imread(comp_path+'dog1.png')
dog_list.append(img)
img = cv2.imread(comp_path+'dog2.png')
dog_list.append(img)
img = cv2.imread(comp_path+'dog3.png')
dog_list.append(img)
img = cv2.imread(comp_path+'dog4.png')
dog_list.append(img)
dog_num = len(dog_list)
#color list
color_list = []
c1 = [255, 255, 255] #white dog
c2 = [205, 250, 255] #lemonchiffon 
c3 = [0, 215, 255] #gold

color_list.append(c1)
color_list.append(c2)
color_list.append(c3)

print(color_list[0])
print(color_list[1])
print(color_list[2])

mouth = cv2.imread(comp_path+'mouth.png')# mouth

if __name__=='__main__':
    get_puppy(dog_list, mouth, color_list)
    #gen_all_puppy(dog_list, mouth, color_list)


