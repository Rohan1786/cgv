from vpython import *

scene = canvas(width = 500, height=500, background = color.white)

def cuboid(pos,length,width,height,color):
    cuboid = box(pos = vector(*pos), length=length, width=width, height= height, color= color)
    return cuboid

def drcylinder(pos,radius,height,color):
    cyl = cylinder(pos= vector(*pos), radius= radius, height= height, color= color)
    return cyl

def translate(obj,tx,ty,tz):
    obj.pos += vector(tx,ty,tz)

def rotate(obj, angle, axis):
    obj.rotate(angle=angle,axis=vector(*axis))

def scale(obj,sx,sy,sz):
    obj.size = vector(obj.size.x*sx, obj.size.y*sy, obj.size.z*sz)

cuboid = cuboid((-2,0,0),2,2,2,color.red)

translate(cuboid, 4, 0, 0)

rotate(cuboid, angle=45, axis=(0,1,0))

scale(cuboid, 1.5, 1.5, 1.5)

cylinder = drcylinder((2,2,0), 1, 10, color.blue)

translate(cylinder, 0, -2, 0)

rotate(cylinder, angle=30, axis=(1, 0, 0))

scale(cylinder, 1.5, 1.5, 1.5)

while True:
    rate(30)