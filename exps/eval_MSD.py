import glob
import math
import numpy as np

def GetMeanStandardDev(txt_path):
    txtli = glob.glob(txt_path)
    txtli.sort()
    lines_stack=[]
    for txtfile in txtli :
        with open(txtfile, 'r') as f:
            lines = f.readlines()
            lines_stack.append(lines)
            
    li_68=[]
    for i in range(len(lines_stack[0])): #68
        li_nine=[]
        for j in range(len(lines_stack)-1): #file cnt

            x1 = int(float(lines_stack[j][i].split(',')[0]))
            y1 = int(float(lines_stack[j][i].split(',')[1]))
            x2 = int(float(lines_stack[j+1][i].split(',')[0]))
            y2 = int(float(lines_stack[j+1][i].split(',')[1]))
            d = math.sqrt(pow(abs(x1-x2),2) + pow(abs(y1-y2),2))

            li_nine.append(d)

        li_68.append(li_nine)

    #print('file cnt = ',len(li_nine)+1)
    #print('point cnt = ',len(li_68))
    
    msd = []
    for idx,i in enumerate(li_68):
        #i = [x for x in i if x<50] # except for drift points 
        msd.append(np.std(i))

    mean_sd = sum(msd)/len(msd)
    
    return mean_sd
    
if __name__=='__main__':
    path1='./result/test1_postproc_avg/*.txt'
    msd1 = GetMeanStandardDev(path1)
    print(path1)
    print('Mean standard dev. =',msd1)
    
    path1='./result/test2_postproc_avg/*.txt'
    msd1 = GetMeanStandardDev(path1)
    print(path1)
    print('Mean standard dev. =',msd1)
    
    path1='./result/test3_postproc_avg/*.txt'
    msd1 = GetMeanStandardDev(path1)
    print(path1)
    print('Mean standard dev. =',msd1)
    
    

    
    
    