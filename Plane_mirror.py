##### Run the script for the first time without changing anything #####



#### Change distances #####
d0=15
d1=30
d2=20



##### Rotate the right mirror.
##### If anlge>0, then clockwise
##### If angle<0, then counter-clockwise
angle_degrees=0




##### Change the speed of animation. The greater, the faster.
speed=200






############################# No changes #######################################################



main_scene=canvas(title='display_1', center=vector(0,0,0), width=1200, height=900)

### scale all distances ##
d0=d0/10
d1=d1/10
d2=d2/10

length=1
width=0.2
height=0.2
angle_laser=atan(d1/d2)


### Check the rotation of the mirror. If the rotation is too great
a0=atan(d1/d0)
angle=pi*angle_degrees/180

if angle>=pi/2:
    raise ValueError("Rotation angle is too great. Please choose the smaller angle")

########## LASER ############################
laser_position=vector(-(d2+length/2),0,0)
laser=box(pos=laser_position, size=vector(length,width,height), axis=vector(1,0,0))
red_ball=sphere(pos=laser_position+vector(laser.length/2,0,0), radius=0.1, color=color.red )
laser.rotate(angle=angle_laser, axis=vector(0,0,1), origin=red_ball.pos)




######### Extra lines ########################
d1_line=arrow(pos=red_ball.pos, axis=vector(0,d1,0), shaftwidth=0.01, color=vector(0.5,0.3,0.1))
d1_line_label=label( pos=vector(d1_line.pos.x+0.2,d1_line.pos.y+(d1_line.length/2),0), text="d1", height=25)

d2_line_1=arrow(pos=red_ball.pos, axis=vector(d2,0,0), shaftwidth=0.01, color=vector(0.8, 0.3, 0.1))
d2_line_label=label(pos=vector(d2_line_1.pos.x+d2_line_1.length/2,d2_line_1.pos.y-0.2,0), text="d2", height=25)
######### Screen in the origin ##############
screen_left=box(pos=vector(-0.01/2,0,0), size=vector(0.01, d0+1, 1), color=color.yellow)
screen_right=box(pos=vector(0.01/2,0,0), size=vector(0.01,d0,1), color=color.red)
d3_line_part1=arrow(pos=vector(0,0,screen_left.width*0.6), axis=vector(0,screen_right.height/2,0), shaftwidth=0.03, color=color.green)
d3_line_part2=arrow(pos=vector(0,0,screen_left.width*0.6), axis=vector(0,-screen_right.height/2,0), shaftwidth=0.03, color=color.green)
d0_line_label=label(pos=vector(d3_line_part1.pos.x-0.3,0,screen_right.width/2+0.2), text="d0", height=25)



######### Upper mirror ######################
upper_mirror=box(pos=vector(0,d1+0.1,0), size=vector(1,0.2,0.6), color=color.green)

######## RIght mirror ########################
right_mirror=box(pos=vector(upper_mirror.pos.x+d2+0.1,0,0),
                 size=vector(0.2,1,0.6), color=color.yellow,
                 opacity=0.4)
d2_line_2=arrow(pos=vector(0,0,0), axis=vector(d2,0,0), shaftwidth=0.01, color=vector(0.4, 0.3, 0.1))
d2_line_label=label(pos=vector(d2_line_2.pos.x+d2_line_2.length/3, d2_line_2.pos.y-0.2,0), text="d2", height=25)


####### test  label ##########################
test=sphere(radius=0.02, color=color.red,
            pos=vector(upper_mirror.pos.x+d2,0,0))


#### Rotate right mirror and normal line accordingly
angle=pi*angle_degrees/180
rmp=right_mirror.pos
right_mirror.rotate(origin=test.pos,
                    axis=vector(0,0,1),
                    angle=2*pi-angle)





#### RIght mirror normal line #######
normal=arrow(pos=test.pos,
             axis=vector(-0.3*d2,0,0),
             shaftwidth=0.03, color=color.yellow, opacity=0.4)

normal.rotate(origin=normal.pos, axis=vector(0,0,1), angle=2*pi-angle)



##### labels for angles #####
#a0_label=label(pos=red_ball.pos,text="2"^2^, xoffset=20,yoffset=30)

############## Function to simulate the motion of the laser ray ################
def laser_ray(red_ball,upper_mirror,right_mirror):
    ray=sphere(pos=red_ball.pos, radius=(red_ball.radius)/10, color=color.red, make_trail=True)


    ## Reach the upper mirror
    initial_position=ray.pos
    final_position_1=vector(upper_mirror.pos.x,upper_mirror.pos.y-(upper_mirror.height/2),0)

    teta=atan((final_position_1.y-initial_position.y)/(final_position_1.x-initial_position.x))
    v_magnutide=1
    vx=v_magnutide*cos(teta)
    vy=v_magnutide*sin(teta)
    v_vector=vector(vx,vy,0)
    ray.velocity=v_vector

    stop=False
    dt=0.01
    while stop==False:
        rate(speed)
        if ray.pos.x>=final_position_1.x or ray.pos.y>=final_position_1.y:
            stop=True
            break
        else:
            ray.pos=ray.pos+ray.velocity*dt

    ### Reach the right mirror ###
    initial_position=final_position_1
    final_position_2=test.pos
    v_vector=vector(vx,-vy,0)
    ray.velocity=v_vector
    stop=False
    dt=0.01
    while stop==False:
        rate(speed)
        if ray.pos.x>=final_position_2.x or ray.pos.y<=final_position_2.y:
            stop=True
            break
        else:
            ray.pos=ray.pos+ray.velocity*dt


    #### Reflection process ########
    a0=atan(d1/d2)
    a1=angle


    if a1<a0:
        teta=(2*a1)-a0
        print(degrees(teta))
        vx=v_magnutide*cos(teta)
        vy=v_magnutide*sin(teta)
        v_vector=vector(-vx,vy,0)
        ray.velocity=v_vector
        stop=False
        while stop==False:
            rate(speed)
            if ray.pos.x<=screen_right.pos.x:
                stop=True
                break
            else:
                ray.pos=ray.pos+ray.velocity*dt

    elif a1>a0:
        teta=2*a1-a0-pi/2
        vx=v_magnutide*sin(teta)
        vy=v_magnutide*cos(teta)
        v_vector=vector(vx,vy,0)
        ray.velocity=v_vector
        stop=False
        print(vx, vy)
        while stop==False:
            rate(speed)
            if ray.pos.y>=upper_mirror.pos.y:
                stop=True
                break
            else:
                ray.pos=ray.pos+ray.velocity*dt


    ### Check the position of the ray
    ### If the position is within the red screen, then: success
    A=screen_left.pos.y+(screen_left.height)/2
    B=upper_mirror.pos.y-(upper_mirror.height)/2
    if abs(ray.pos.y)<= abs(screen_right.pos.y+(screen_right.height)/2):

        #### finding a good position for the label ####

        message=label(pos=vector(0,(B+A)/2,0), text="YES")
    else:
        message=label(pos=vector(0,(B+A)/2,0), text="NO")

laser_ray(red_ball,upper_mirror,right_mirror)
