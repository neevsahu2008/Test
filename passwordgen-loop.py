result=['test']
mainlist=['0', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'q', 'a', 'w', 's', 'z', 'x', 'c', 'd', 'e', 'r', 'f', 'v', 'b', 'g', 't', 'y', 'u', 'h', 'j', 'm', 'n', 'k', 'i', 'o','l','p']
for x1 in mainlist:
    result.clear()
    result.append(x1)
    for x2 in mainlist:
        del result[1:]
        result.append(x2)
        for x3 in mainlist:
            del result[2:]
            result.append(x3)
            for x4 in mainlist:
                del result[3:]
                result.append(x4)
                for x5 in mainlist:
                    del result[4:]
                    result.append(x5)
                    for x6 in mainlist:
                        del result[5:]
                        result.append(x6)
                        for x7 in mainlist:
                            del result[6:]
                            result.append(x7)
                            for x8 in mainlist:
                                del result[7:]
                                result.append(x8)
                                for b in result:
                                    string=''
                                    string+=b
                                    print(string,end='')
                                print('\n')
        
        
        
