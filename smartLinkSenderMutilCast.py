# -*- coding:utf-8 -*-
import socket
import time
import random
import SmartLink
import struct
HOST = "224.1.1.1"
PORT = 5000
BUFFSIZE = 1024
ADDR = (HOST,PORT)

socketClient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)



socketClient.bind(('192.168.0.3',5000))

def sender():    
    #s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)    
    #socketClient.bind((SENDERIP,SENDERPORT))    

    # Set Time-to-live (optional)    
    #ttl_bin = struct.pack('@i', MYTTL)    
    #s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl_bin)    
    #status = s.setsockopt(IPPROTO_IP,IP_ADD_MEMBERSHIP,inet_aton(MYGROUP) + inet_aton(SENDERIP))
    #加入到组播组    
    while True:
        socketClient.sendto("data".encode(),("224.1.1.1",2000))
        time.sleep(0.1);
        print ("send data ok !")
#sender()


frame = SmartLink.smartlink_frame("aabcd","efgh","ijklmnopqrst")
print(frame)
print(len(frame))

def multicast_encode(str):
    length = len(str)
    dest = [] 
    index = 0;

    if length % 2:
        str = str + chr(0)


    for index in range(0,length,2):
        dest = dest + [index / 2 + 1,ord(str[index]), ord(str[index + 1])]
    return dest

dest = multicast_encode(frame)
print (dest)

def mutilcast_decode(dest):
    result = [0] * 64
    result_str = ''
    for var in range(0,len(dest),3):

        index = dest[var]
        data1 = dest[var + 1]
        data2 = dest[var + 2]
        result[(index-1) * 2 ] = data1;
        result[(index-1) * 2 + 1] = data2;

    print(result)
    length = result[0]   
    print(length)
    for i in range(0,length):
       result_str = result_str + chr(dest[i])
    return result_str

decode_data = mutilcast_decode(dest)
print(decode_data)
print(len(decode_data))






count = 0
while count > 0:
    
    for i in range(0,len(dest),3):
        host = socket.inet_ntoa(struct.pack('I',socket.htonl((224 <<24)+ (dest[i] << 16 ) + (dest[i+1] << 8) + (dest[i+2]))))
        socketClient.sendto("data".encode(),(host,2000))
    count = count -1
    time.sleep(0.1)

print ("over")
