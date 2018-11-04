from funcdrawer import *
from colorselector import*
def main():
    #初始化
    
    outstr=""
    alltb=[]
    e=[]
    f=[]  
    subnum=0
    tmpli=[]
    peakstr="Peaks:\n"

    #接收输入
    tbnum=int(input("Please input the amount of tubes."))
    tmp=float(input("Please input the percentage of the substance extracted into the second phase.End with -1"))
    while tmp!=-1:
        e.append(tmp)
        f.append(1-tmp)
        subnum+=1
        tmp=float(input("Please input the percentage of the substance extracted into the second phase.End with -1"))
    #初始化浓度
    for i in range(0,tbnum):
        alltb.append([list(subnum*"0"),list(subnum*"0")])
    for j in range(0,subnum):
        alltb[0][0][j]=100*f[j]
        alltb[0][1][j]=100*e[j]

    #对逐个组分进行从右向左逐次逆流萃取
    for m in range(0,subnum):
        for i in range(1,tbnum):
            for j in range(i,0,-1):
                alltb[j][0][m]=(float(alltb[j-1][0][m])+float(alltb[j][1][m]))*f[m]
                alltb[j][1][m]=(float(alltb[j-1][0][m])+float(alltb[j][1][m]))*e[m]
            alltb[0][0][m]=float(alltb[0][1][m]*f[m])
            alltb[0][1][m]=float(alltb[0][1][m]*e[m])

    #寻找峰值
    for i in range(0,subnum):
        for j in range(0,tbnum):
            tmpli.append(alltb[j][1][i])
        peak=max(tmpli)
        peakstr+="<"+str(i)+"> "+str(tmpli.index(peak))+"\t"+str(peak)+"\n"
        tmpli=[]
    #输出
    for k in range(0,tbnum):
        outstr+=str(k)+"\t"
        for i in range(0,subnum):
            outstr+=str(alltb[k][1][i])+"\t"
        outstr+="\n"
    print(outstr)
    print(peakstr)
    #作图
    w=root()
    for i in range(0,subnum):
        draw(w,"alltb[int(x)][1]["+str(i)+"]",0,tbnum-2,1,rancolor(),alltb)
main()
