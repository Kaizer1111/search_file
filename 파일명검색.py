import re, os, sys

def search_os(dirname,all,include):
    if all == 0 :
        global result_os
        try:
            filenames = os.listdir(dirname)
            for filename in filenames:
                if os.path.isdir(filename) :
                    continue
                if include == 1 :
                    full_filename = os.path.join(dirname, filename)
                else :
                    full_filename = os.path.join(filename)
                #ext = os.path.splitext(full_filename)[-1]
                #os.path.basename(filename)
                # print(full_filename, end=",")
                result_os.append(full_filename)
        except PermissionError:
            pass
        print("\n파일명이 저장되었습니다.\n")
        #print(result_os)
    if all == 1 :
        try:
            for (path, dir, files) in os.walk(dirname):
                for filename in files:
                    if os.path.isdir(filename):
                        continue
                    #ext = os.path.splitext(filename)[-1]
                    #if ext == '.py':
                    if include == 1 :
                        result_os.append(path + filename)
                    else :
                        result_os.append(filename)
                    #print("%s/%s" % (path, filename))
                    #result_os.append(filename)
        except PermissionError:
            pass

def searchfile() :
    global result, result_os, jong, hello, file
    H2 = []
    H = input("확장자를 입력해주세요(여러개 입력 가능) : ")
    if ',' in H :
        tempH = H.split(',')
        for i in range(len(tempH)):
            H2.append(tempH[i].strip())
    elif ' ' in H :
        H2 = H.split()

    if hello == 0 :
        file = input("파일명을 입력해주세요(파일과 파일 사이를 쉼표 또는 스페이스(공백)으로 분리해주세요) : ")
        if ',' in file :
            rfile = file.split(',')
            rrfile = []
            for i in range(len(rfile)):
                 rrfile.append(rfile[i].strip())
            rfile = rrfile
        else :
            rfile = file.split()
    else :
        rfile = result_os

    if H2:
        H3 = ""
        for i in H2 :
            if i != H2[-1] :
                H3 += i + "$|"
            else :
                H3 += i + "$"
        sam = Tjong[:8] + H3 + ").*$"
    else :
        sam = Tjong[:8] + H + "$" + ").*$"

    for i in range(len(rfile)):
        p = re.compile(sam, re.DOTALL)
        m = p.search(rfile[i])
        if m != None:
            result.append(m.group())
    print("\n" + "*"*100)
    print("\n검색한 파일 : ", rfile)
    print("\n매치된 파일 : ", result)
    print("\n" + "*"*100 + "\n")

Tjong = ".*[.](?=bat$|exe$).*$"
Fjong = ".*[.](?!bat$|exe$).*$"

while True:
    hello = 0
    all = 0
    result_os = []
    search = ""
    result = []
    choose = input(" " * 18 + "<확장명 분류 프로그램>\n" + "="*60 + "\n1. 디렉터리에서 파일 검색후 검색한 파일을 확장명으로 분류하기\n2. 직접 파일명 입력 후 확장명으로 분리하기\n3. 프로그램 종료\n" + ("="*60) + "\n입력 : ")
    if choose == "1":
        D = input("\n검색할 디렉터리를 입력해주세요 : ")
        if not os.path.isdir(D) :
            print("\n존재하지 않는 디렉터리(경로)입니다\n")
            continue
        choose_2 = input("\n" + "="*50 + "\n1. 현재 디렉터리만 검색\n2. 하위 디렉터리까지 모두 검색 (주의 : 시간이 오래 걸릴 수 있음)\n" + "="*50 + "\n입력 : ")
        while True:
            if choose_2 == "1":
                all = 0
                break
            elif choose_2 == "2":
                all = 1
                break
            else:
                print("\n1에서 2사이의 숫자만 입력 할 수 있습니다...\n")
        choose_3 = input("\n" + "="*60 + "\n1. 경로(디렉터리)까지 포함\n2. 파일명만 포함\n(아무거나 선택해도 크게 상관은 없음)\n" + "="*60 + "\n입력 : ")
        while True:
            if choose_3 == "1" :
                include = 1
                break
            elif choose_3 == "2" :
                include = 0
                break
            else:
                print("\n1에서 2사이의 숫자만 입력할 수 있습니다...\n")
        search_os(D,all,include)
        hello = 1 # 파일명을 직접 입력 해야되는지 확인하는 변수
        searchfile()
    elif choose == "2":
        hello = 0
        searchfile()
    elif choose == "3":
        sys.exit()
    else:
        print(choose)
        print("\n1에서 3사이의 숫자만 입력할 수 있습니다...\n")