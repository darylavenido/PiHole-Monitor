#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           userinit.sh
#  Send pushover notification when motionEyeOS boots.
#  Use with pushover_boot.py
#
# Author : Matt Hawkins
# Date   : 12/06/2020
#
# https://www.raspberrypi-spy.co.uk/tag/motioneyeos/
#
#--------------------------------------
user="replace_me_with_your_user_key"
token="replace_me_with_your_api_token"
port="40000"

sleep 15

ip=$(curl -s https://api.ipify.org)
ip="$ip:$port"

python /data/pushover_boot.py $ip $user $token > /var/log/pushover &
