import string

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def findLadders(self, start, end, myDict):
        myDict-={start, end}

        tracingPairs=[]
        tracingList=dict()
        results=[]

        front=[start]
        back=[end]

        distance=2
        while front:
            new=[]
            for word in front:
                for i in range(len(word)):
                    for a in string.ascii_lowercase:
                        pWord=word[:i]+a+word[i+1:]
                        if pWord in back:
                            tracingPairs.append([word, pWord])
                        if pWord in myDict:
                            myDict.remove(pWord)
                            new.append(pWord)
                        # must do it here. for those pWord with multiple derivative sources.
                        if pWord in new:
                            if pWord in tracingList:
                                tracingList[pWord].append(word)
                            else:
                                tracingList[pWord]=[word]

            if tracingPairs:
                break

            if len(new)>len(back):
                front, back=back, new
            else:
                front=new
            distance+=1

        for p in tracingPairs:

            paths0=[[p[0]]]
            while paths0[0][-1] in tracingList:
                #I think this may have caused things to slow down since each time it will rebuild all path lists
                paths0=[path+[w] for path in paths0 for w in tracingList[path[-1]]] 

            paths1=[[p[1]]]
            while paths1[0][-1] in tracingList:
                paths1=[path+[w] for path in paths1 for w in tracingList[path[-1]]]

            
            results.extend([p1[::-1]+p2 for p1 in paths0 for p2 in paths1] if paths0[0][-1]==start else [p2[::-1]+p1 for p1 in paths0 for p2 in paths1])

        return results





















    '''
    old
    '''



    def neighbor (self, word1, word2):
        if word1==word2:
            return False

        if len(word1)==len(word2):
            mis=0
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    if mis==1:
                        return False
                    else:
                        mis+=1

            return True
        return False

    def tracing (self, traceLists, end):
        paths=[]
        if len(traceLists)==1:
            for start in traceLists[0][end]:
                paths.append([start,end])
            return paths

        for prev in traceLists[len(traceLists)-1][end]:
            for path in self.tracing (traceLists[:len(traceLists)-1], prev):
                paths.append(path+[end])

        return paths



    def findLaddersOld(self, start, end, myDict):
        myDict=set(myDict)
        myDict=myDict-{start}
        myDict=myDict-{end}


        front=[start]
        new=[]

        distance=2

        traceLists=[]

        found=False



        while front and myDict and not found:
            # print front, dict
            traceLists.append(dict())
            traceLen=len(traceLists)

            # print front

            toRemove=[]
            for word in front:
                if self.neighbor(word,end):
                    traceLists[traceLen-1][end]=[word] if end not in traceLists[traceLen-1] \
                    else traceLists[traceLen-1][end]+[word]
                    found=True
                    # print traceLists

                    # print traceLists[len(traceLists)-1]["acne"]
                    # print front
                    distance-=1
                    # break

                
                if not found:
                    for i in range(len(word)):
                        for a in string.ascii_lowercase:
                            if word[i]!=a:
                                pWord=word[:i]+a+word[i+1:]
                                # if end==pWord:
                                #     return distance
                                if pWord in myDict:
                                    toRemove.append(pWord)
                                    if pWord not in traceLists[traceLen-1]:
                                        new.append(pWord)
                                    traceLists[traceLen-1][pWord]=[word] if pWord not in traceLists[traceLen-1] else traceLists[traceLen-1][pWord]+[word]

            for word in toRemove:
                if word in myDict:
                    myDict.remove(word)
            front=new
            new=[]
            distance+=1



        
        

        if not found:
            traceLists.append(dict())
            traceLen=len(traceLists)
            for word in front:

                if self.neighbor(word,end):

                    traceLists[traceLen-1][end]=[word] if end not in traceLists[traceLen-1] else traceLists[traceLen-1][end]+[word]
                    found=True
                    # print front


        if found:
            # print found
            paths=self.tracing(traceLists,end)
        else:
            paths=[]








        return paths

if __name__=="__main__":
    solution=Solution()
    # print solution.findLadders("hit","cog",["hot","dot","dog","lot","log"])
    # print solution.findLadders("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"])
    # print solution.findLadders("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"])

    # print solution.findLadders("red", "tax", {"ted","tex","red","tax","tad","den","rex","pee"})
    # print solution.findLaddersOld("red", "tax", {"ted","tex","red","tax","tad","den","rex","pee"})
    print solution.findLadders("magic","pearl", {"flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"})
    print solution.findLaddersOld("magic","pearl",{"flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"})




        