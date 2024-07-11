import crc

if __name__ == '__main__':
    print('main program start')
    fd_data = [0,0,0,0,236,0,0,0,6,54,0,0,0,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#e2eは除く data9(6)->shift要求なし 縦ID49
    CRC = crc.e2e_calc(fd_data[2:],30,0x00,0x5a)
    e2e_hex = format(int(CRC), '04X')
    print("e2e == ",(e2e_hex))

    fd_data[1] = int(e2e_hex[0:2],16)
    fd_data[0] = int(e2e_hex[2:4],16)
    print(fd_data)
