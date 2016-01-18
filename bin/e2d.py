#!/usr/bin/python 
from datetime import datetime,time
import sys

help_msg='Usage: epoch2datetime.py [epoch milliseconds from_1970|epoch seconds from 1970]' + '\n'\
        +'Version: 0.0.1'

DATE_FORMAT='%Y-%m-%d %H:%M:%S'
EPOCH_MS_LEN=13
EPOCH_SEC_LEN=10
MS_SEP = '.'

def epochms2datetime(epoch_ms):
    decimal_part = epoch_ms % 1000
    dt = datetime.fromtimestamp(epoch_ms/1000)
    str_dt = dt.strftime(DATE_FORMAT) + MS_SEP + str(decimal_part)
    return str_dt
def epochs2datetime(epoch_s):
    dt = datetime.fromtimestamp(epoch_s)
    str_dt = dt.strftime(DATE_FORMAT)
    return str_dt


if __name__ =='__main__':
    if len(sys.argv) != 2:
        print help_msg
        sys.exit()
    str_epoch = sys.argv[1]
    int_epoch=int(str_epoch)
    epoch_len = len(str_epoch) 
    if epoch_len == EPOCH_SEC_LEN:
        print epochs2datetime(int_epoch)
    elif epoch_len == EPOCH_MS_LEN:
        print epochms2datetime(int_epoch)
    else:
        print "lenth not correct!"
        print help_msg

