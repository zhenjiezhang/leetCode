'''
71. Simplify Path
Total Accepted: 43703 Total Submissions: 207323 Difficulty: Medium

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

click to show corner cases.
Corner Cases:

    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
'''
    # #better code in OJ

# class Solution:
# # @param path, a string
# # @return a string
# def simplifyPath(self, path):
#     result = []
#     pathList = path.split('/')
#     for content in pathList:
#         if content:
#             if content == '..':
#                 try:
#                     result.pop()
#                 except:
#                     result = []
#             elif content != '.':
#                 result.append(content)
#     return '/'+'/'.join(result)



class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        pathList=path.split('/')
        pathStack=[]
        for name in pathList:
            if not name:
                continue
            if name not in ['.','..']:
                pathStack.append(name)
            else:
                if name=='.':
                    continue
                else:
                    if pathStack:
                        pathStack.pop()

        return '/'+'/'.join(pathStack)







    def simplifyPathOld(self, path):
    	newPath=''
    	level=False
        for i in xrange(len(path)):
        	if path[i]=='/':
        		if level==True:
        			continue
        		else:
        			newPath+=path[i]
        			level=True
	        else:
	        	newPath+=path[i]
	        	level=False

        path=newPath

        i=0
        newPath=''
        while i < len(path):
        	if path[i]=='.' and path[i-1]=='/' and ((i<len(path)-1 and path[i+1]=='/') or i==len(path)-1):
        		if i>0 and path[i-1]=='/':
        			i+=2
        			continue
        	if path[i]=='.' and path[i-1]=='/' and (i< len(path)-2 and path[i+1]=='.' and path[i+2]=='/' or (i==len(path)-2 and path[i+1]=='.')):
        		if len(newPath)<2:
        			i+=3
        			continue
        		else:
        			i+=3
        			newPath=newPath[:-1]
        			while newPath[-1]!='/':
        				newPath=newPath[:-1]
        			continue
        	else:
        	    newPath+=path[i]
        	i+=1
       	# if newPath[-1]=='.':
       	# 	newPath=newPath[:-1]
        return newPath if (newPath[-1]!='/' or len(newPath)==1) else newPath[:-1]


if __name__=="__main__":
	solution=Solution()
	print solution.simplifyPath("/a/./b/../../c/")
	print solution.simplifyPath("/user/../../")
	print solution.simplifyPath("/.")
	print solution.simplifyPath("/..")





