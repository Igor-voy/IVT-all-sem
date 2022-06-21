import datetime


def print_results(*args, action, result):
    '''
    >>> print_results(1,2,3,action = '+', result = '6')
    #################
    # 1 # 2 # 3 # + #
    #################
    #        6      #
    #################
    >>> print_results(1,2,4,action = '*', result = '8')
    #################
    # 1 # 2 # 4 # * #
    #################
    #        8      #
    #################
    '''
    st = len(str(args)) + len(args) + 5
    print(st * "#")
    print("# ", end="")
    for i in args:
        print(i, end=" # ")
    print(action + " #")
    print(st * "#")
    st1 = st - len(str(result))
    print("#" + str(result).rjust(len(str(result)) + st1 // 2)
          + str().ljust((st1 - 1) // 2 - 1) + "#")
    print(st * "#")


def write_log(*args, action=None, result=None,
              file='calc-history.log.txt'):
    f = open(file, mode='a', errors='ignore')
    f.write(f"{datetime.datetime.now()} : {action}: {args} = {result} \n")
    f.close()