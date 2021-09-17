import math

abc = 0
while abc == 0:
    d = input("1 : السرعة الدورانية \n2 : الزخم والشغل والطاقة \n")
    if d == "1":
        rav = ["π", "d", "t", "v", "vi", "vf", "Δv", "a", "r", "θ°", "θrad", "ω", "ωi", "ωf", "Δω", "α", "f",
               "T", "F", "m", "ac", "Fc", "τ"]
        msu = ["", "m", "s", "m/s", "m/s", "m/s", "m/s", "m/s²", "m", "°", "rad", "rad/s", "rad/s", "rad/s", "rad/s",
               "rad/s²", "1/s", "s", "N", "kg", "m/s²", "N", "N.m"]
        var = [math.pi, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        a1 = len(var)
        a = 0
        b = 0
        c = 0
        h = 0

        while h < a1 :
            print ( h , " : " , rav[h] , "   " , h+1 , " : " , rav[h+1] , "   " , h+2 , " : " , rav[h+2])
            h += 3

        print("اكتب ارقام المعطيات اللي عندك :\n")
        while a < a1:
            plo = input(": ")
            if plo != "" :
                print(rav[plo], " = ")
                var[plo] = input()
            elif plo == "" :
                a = a1
            a += 1

        print("\n\n")

    # هذا بعدين لما احط قوانين الزخم والاشياء ذي
    elif d == "2":
        rav = []
        msu = []
        var = []
        a1 = len(var)
        a = 0
        b = 0
        c = 0
        print("اكتب \" . \" للتراجع للخلف\n")
        print(rav, "\n")
        while a != a1:
            rav1 = rav[a]

            if var[a] == "" or var[a] == ".":
                print(rav1, "=")
                var[a] = input()
            elif var[a] != "":
                print(rav1, " = ", var[a])

            if var[a] == ".":
                a = a - 2

            a += 1

        print("\n\n")
    # الين هنا يعني.......................
    else:
        print("يا بابا  يا ١ يا ٢ و ون اور تو (اذا ما فهمت يعني)")


    # ....................................................

    # c = a * b
    def qw(qwb, qwa, qwd):
        if var[qwd] != "" and var[qwa] != "" and var[qwb] == "":
            var[qwb] = float(var[qwd]) * float(var[qwa])
        elif var[qwb] != "" and var[qwd] != "" and var[qwa] == "":
            var[qwa] = float(var[qwb]) / float(var[qwd])
        elif var[qwb] != "" and var[qwa] != "" and var[qwd] == "":
            var[qwd] = float(var[qwb]) / float(var[qwa])


    # c = a + b
    def qa(qac, qaa, qab):
        if var[qac] == "" and var[qaa] != "" and var[qab] != "":
            var[qac] = float(var[qaa]) + float(var[qab])
        elif var[qac] != "" and var[qaa] == "" and var[qab] != "":
            var[qaa] = float(var[qac]) - float(var[qab])
        elif var[qac] != "" and var[qaa] != "" and var[qab] == "":
            var[qab] = float(var[qac]) - float(var[qaa])


    # d = a * ( b + c ) / 2
    def qf(qfd, qfa, qfb, qfc):
        if var[qfd] == "" and var[qfa] != "" and var[qfb] != "" and var[qfc] != "":
            var[qfd] = float(var[qfa]) * (float(var[qfb]) + float(var[qfc])) / 2
        elif var[qfd] != "" and var[qfa] == "" and var[qfb] != "" and var[qfc] != "":
            var[qfa] = 2 * float(var[qfd]) / (float(var[qfb]) + float(var[qfc]))
        elif var[qfd] != "" and var[qfa] != "" and var[qfb] == "" and var[qfc] != "":
            var[qfb] = float(var[qfd]) * 2 / float(var[qfa]) - float(var[qfc])
        elif var[qfd] != "" and var[qfa] != "" and var[qfb] != "" and var[qfc] == "":
            var[qfc] = float(var[qfd]) * 2 / float(var[qfa]) - float(var[qfb])

        # d = a / ( b * c )


    def qe(qed, qea, qeb, qec):
        if var[qed] == "" and var[qea] != "" and var[qeb] != "" and var[qec] != "":
            var[qed] = float(var[qea]) / (float(var[qeb]) * float(var[qec]))
        elif var[qed] != "" and var[qea] == "" and var[qeb] != "" and var[qec] != "":
            var[qea] = float(var[qed]) * float(var[qeb]) * float(var[qec])
        elif var[qed] != "" and var[qea] != "" and var[qeb] == "" and var[qec] != "":
            var[qeb] = float(var[qea]) / (float(var[qed]) * float(var[qec]))
        elif var[qed] != "" and var[qea] != "" and var[qeb] != "" and var[qec] == "":
            var[qec] = float(var[qea]) / (float(var[qeb]) * float(var[qed]))


    # θ° = θrad * 180 / π
    def qt(qtc, qta, qtb):
        if var[qtc] == "" and var[qta] != "" and var[qtb] != "":
            var[qtc] = float(var[qta]) * 180 / float(var[qtb])
        elif var[qtc] != "" and var[qta] == "" and var[qtb] != "":
            var[qta] = float(var[qtc]) * float(var[qtb]) / 180
        elif var[qtc] != "" and var[qta] != "" and var[qtb] == "":
            var[qtb] = float(var[qta]) * 180 / float(var[qtc])


    # c = 2 * a * b
    def qk(qkc, qka, qkb):
        if var[qkc] == "" and var[qka] != "" and var[qkb] != "":
            var[qkc] = 2 * float(var[qka]) * float(var[qkb])
        elif var[qkc] != "" and var[qka] == "" and var[qkb] != "":
            var[qka] = float(var[qkc]) / float(var[qkb]) / 2
        elif var[qkc] != "" and var[qka] != "" and var[qkb] == "":
            var[qkb] = float(var[qkc]) / 2 / float(var[qka])


    # a = 1 / b
    def qp(qpa, qpb):
        if var[qpa] == "" and var[qpb] != "":
            var[qpa] = 1 / float(var[qpb])
        elif var[qpa] != "" and var[qpb] == "":
            var[qpb] = 1 / float(var[qpa])


    # d = a * b sin( c )
    def ql(qld, qla, qlb, qlc):
        if var[qld] == "" and var[qla] != "" and var[qlb] != "" and var[qlc] != "":
            var[qld] = float(var[qla]) * float(var[qlb]) * math.sin(float(var[qlc]))
        elif var[qld] != "" and var[qla] == "" and var[qlb] != "" and var[qlc] != "":
            var[qla] = float(var[qld]) / math.sin(float(var[qlc])) / float(var[qlb])
        elif var[qld] != "" and var[qla] != "" and var[qlb] == "" and var[qlc] != "":
            var[qlb] = float(var[qld]) / math.sin(float(var[qlc])) / float(var[qla])
        elif var[qld] != "" and var[qla] != "" and var[qlb] != "" and var[qlc] == "":
            var[qlc] = math.sin(float(var[qld]) / float(var[qlb]) / float(var[qla])) ** (-1)


    # c = a**2 / b
    def qo(qoc, qoa, qob):
        if var[qoc] == "" and var[qoa] != "" and var[qob] != "":
            var[qoc] = float(var[qoa]) ** 2 / float(var[qob])
        elif var[qoc] != "" and var[qoa] == "" and var[qob] != "":
            var[qoa] = (float(var[qoc]) * float(var[qob])) ** (0.5)
        elif var[qoc] != "" and var[qoa] != "" and var[qob] == "":
            var[qob] = float(var[qoa]) ** 2 / float(var[qoc])


    # c = a**2 * b
    def qi(qic, qia, qib):
        if var[qic] == "" and var[qia] != "" and var[qib] != "":
            var[qic] = float(var[qia]) ** 2 * float(var[qib])
        elif var[qic] != "" and var[qia] == "" and var[qib] != "":
            var[qia] = (float(var[qic]) / float(var[qib])) ** (0.5)
        elif var[qic] != "" and var[qia] != "" and var[qib] == "":
            var[qib] = float(var[qic]) / float(var[qia]) ** 2


    # ....................................................
    # rav = ["π","d","t","v","vi","vf","Δv","a","r","θ°","θrad","ω","ωi","ωf","Δω","α","f","T","F","m","ac","Fc","τ"]

    while c != a1:
        qp(17, 16)
        qt(9, 10, 0)
        qa(13, 14, 12)
        qa(5, 6, 4)
        qf(10, 2, 12, 13)
        qf(1, 2, 4, 5)
        qw(10, 11, 2)
        qw(1, 3, 2)
        qw(6, 7, 2)
        qw(14, 15, 2)
        qw(1, 8, 10)
        qw(6, 8, 14)
        qw(3, 8, 11)
        qw(7, 8, 15)
        qw(18, 19, 7)
        qp(17, 16)
        qk(11, 0, 16)
        ql(22, 18, 8, 9)
        qo(20, 3, 8)
        qi(20, 11, 8)
        qw(21, 20, 19)

        c += 1

    # ....................................................

    while b != a1:
        if var[b] != "" :
            print(rav[b], " = ", var[b], " ", msu[b])
        b += 1

    print("\n\n")
    ghfj = input("اكتب 0 للاقفال و اكتب 1 للإعادة : ")
    if ghfj == "0":
        abc = 1
    elif ghfj == "1" or ghfj == "":
        print("\n\n\n")
    else:
        print("كل زق \n")
        abc = 1