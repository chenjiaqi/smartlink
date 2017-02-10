#coding:utf-8
def constructSendStr(str): #添加长度和crc校验
    length = len(str)
    str = chr(length + 2) + str
    crc = 0;
    for var in str:
        crc = crc + ord(var)
        crc = crc & 0xff
    str = str + chr(crc)
    return str
    


def jrdcodechar(index,data,rest): #单个字符编码
    a = data
    index = index*4
    rest[0] = (index+0)<<2|((a>>0)&0x03);
    rest[1] = (index+1)<<2|((a>>2)&0x03);
    rest[2] = (index+2)<<2|((a>>4)&0x03);
    rest[3] = (index+3)<<2|((a>>6)&0x03);


def encodestr(str): #字符串编码
    s=[]
    
    for i in range(0,len(str)):
        rest = [0,0,0,0]
#        encodedata(i+1,ord(str[i]),rest)
        jrdcodechar(i+1,ord(str[i]),rest);

#        print(rest)
        s = s + rest
#        print(bin(ord(str[i])))
#        for var in rest:
#            print(bin(var))
        
    return s




def decode(data): #解码
    flag_table = [0 for x in range(0,256)]
    data_table = [0 for x in range(0,256)]
    datalength = 0
    for var in data:
        index = (var >> 2)
        flag_table[index] = 1
        data_table[index] = var & 0x03

        if(flag_table[4:8] == [1,1,1,1]):
            datalength = (data_table[4]) | (data_table[5] << 2) | (data_table[6] << 4) | (data_table[7] << 6)
            print("length is %s" % datalength)
        

        if( datalength > 0 ):
            is_recv_successed = True
            for vartmp in range(4,(datalength + 1) * 4 + 1 ):
                if flag_table[vartmp] == 0:
                    is_recv_successed= False
                    break
            if is_recv_successed:
                print("success!") 
                print(data_table)
                
                recv_data = ""
                print(datalength)
                for i in range(1,datalength+1):
                    c = 0
                    for j in range(0,4):
                        c = c | data_table[i*4+j] << (j*2)
                    recv_data = recv_data + chr(c)
                print(recv_data)

                return recv_data


def smartlink_frame(ssid,passwd,sn): #传输帧
    len_ssid = len(ssid)
    len_passwd = len(passwd)
    len_sn = len(sn)
    frame = chr(len_ssid) + chr(len_passwd) + ssid + passwd + sn
    return constructSendStr(frame) #返回组合帧
