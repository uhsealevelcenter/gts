
import datetime
import struct

noaa = ['KWAL']

class gts:
    def __init__(self,data = None):
        self.load(data)

    def load(self,data):
        self.entire_msg = data
        self.unpack()

    def unpack(self):
        if self.entire_msg:
            m = self.entire_msg

            self.txlen = len(self.entire_msg)
            self.header = m[0:18].decode("utf-8")
            self.wmotype = m[0:6].decode("utf-8")
            self.ncepctr = m[7:11].decode("utf-8")
            self.domhrmin = m[12:18].decode("utf-8")
#            self.body = m[22:-12].decode("utf-8")
            if self.ncepctr in noaa: #if noaa
                self.fmt = 'noaa'
                self.pid = m[22:30].decode("utf-8")
                self.jd = m[31:34].decode("utf-8")
                self.msgtime = m[34:40].decode("utf-8")
                self.msgbody = m[41:-12]#.decode("utf-8") # if NOAA
                self.dams = m[-11:].decode("utf-8") # NOAA sat signal data
            else:
                self.fmt = 'other'
                self.pid = None
                self.jd = None
                self.msgtime = None
                self.msgbody = m[22:]#.decode("utf-8")
                self.dams = None

def testjig():

    testmsg = b'SXHI50 KWAL 100303\r\r\n\x1eEDD067F2 041030336b2B@OTmpJ 37+0NN 120W'

#    testmsg = b'SWPH41 RJTD 152356\r\r\n\x1e:PRS 1 #1 2331 2334 2336 2340 2345 2350 2353 2357 2361 2365 2368 2373\r\n:RAD 1 #1 7933 7941 7945 7948 7952 7955 7953 7956 7963 7970 79*5 7978\r\n:ENC 5 #6 1653 1676 1699 1724 :SW1 56 #60 0 :SW2 26 #60 60 :BAT 5 #6\r\n13.0 :NAME 06505F20='
    M = gts(testmsg)

    if M is not None:

        print(M.txlen)
        print(M.header)
        print(M.wmotype)
        print(M.ncepctr)
        print(M.domhrmin)
        print(M.pid)
        print(M.jd)
        print(M.msgtime)
        print(M.msgbody)
        print(M.dams)

# == MAIN ==
if __name__ == '__main__':
    testjig()


