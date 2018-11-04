from tkinter import *
import math
def nx(x,l):
    return x*(400/l)+400

def ny(x,funstr,l,alltb=[]):
    funli=list(funstr)
    c=len(funli)
    for i in range(0,c):
        if funli[i]=="x":
            funli[i]=str(x)
    newstr="".join(funli)
    y=eval(newstr)   
    return 400-y/20*400

def main():
    fun=input("Please input the function.\nf(x)=")
    a=float(input("Please input the start point of the image."))
    b=float(input("Please input the end point of the image."))
    draw(fun,a,b)
def root():
    cava=Tk()
    cava.title("The image of the fuction")
    cava.geometry("810x810+400+0")
    w=Canvas(cava,width=800,height=800)
    w.pack()
    w.create_line(0,400,800,400,fill="blue")
    w.create_line(400,0,400,800,fill="blue")
    return w
def draw(w,fun,a,b,k=0.01,color="red",li=[]):
    t=a
    sc=b-a
    while t<=b:
        w.create_line(nx(t,sc),ny(t,fun,sc,li),nx(t+k,sc),ny(t+k,fun,sc,li),fill=color,width=2)
        t=t+k


