
import datetime
import struct

class noaagts:
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
            self.body = m[22:-12].decode("utf-8")
            self.pid = m[22:30].decode("utf-8")
            self.jd = m[31:34].decode("utf-8")
            self.msgtime = m[34:40].decode("utf-8")
            site = self.header[7:11]
            self.msgbody = m[41:-12]#.decode("utf-8") # if NOAA
            self.dams = m[-11:].decode("utf-8") # NOAA sat signal data

def testjig():

    testmsg = b'SXHI50 KWAL 100303\r\r\n\x1eEDD067F2 041030336b2B@OTmpJ 37+0NN 120W'

    M = gts(testmsg)

    if M is not None:

        print(M.header)
        print(M.body)
        print(M.pid)
        print(M.jd)
        print(M.msgtime)
        print(M.msgbody)
        print(M.dams)

# == MAIN ==
if __name__ == '__main__':
    testjig()


