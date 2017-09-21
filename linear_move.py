#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

#Simply moves forwards or backwards depending on input
#Alex Hirst, 9/12/17

def linear_move():
    #Start New Node
    rospy.init_node('nao_mover', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel',Twist, queue_size = 10)
    vel_msg = Twist()

    #Receive user inputs
    print("Let's move Nao!")
    speed = input("Input your speed: ")
    distance = input("Input your distance: ")
    isForward = input("Forward?: ")#True or False

    #Check if forwards or backwards
    if (isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():

        #Set Current time for distance calculation
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):
            #Publish velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time for distance Calculation
            t1 = rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance = speed*(t1-t0)
            rate.sleep()

        #Stop robot after loop
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)



if __name__ == '__main__':
    try:
        #testing our function
        linear_move()
    except rospy.ROSInterruptException:
        pass
