#python
# -*- coding:utf-8 -*-
import xmind
import os

w = xmind.load("Hackindex.xmind") # load an existing file or create a new workbook if nothing is found

s1=w.getPrimarySheet() # get the first sheet
roottopic = s1.getRootTopic()
topics=roottopic.getSubTopics() # get the root topic of this sheet
#print topics

def vaild_dir_name(dirstr):
    li = [u"：",':','/','?','*',u'“','<','>','|']#
    for item in li:
        #print item
        if item in dirstr:
            return False
    return True

def getnext(topicnode,basedir=os.getcwd()):
    os.chdir(basedir)
    topics = topicnode.getSubTopics()
    if topics:
        for topic in topics:
            content = topic.getTitle()
            #print content
            if vaild_dir_name(content):
                #print "creating dir "+content
                print os.getcwd()
                if(os.path.exists(content)):
                    print "The dir has exists,change to"
                else:
                    os.mkdir(content)
                os.chdir(os.path.join(os.getcwd(),content))
                print os.getcwd()
                getnext(topic,os.getcwd()) #这里有没有第二个参数的差别是巨大的！
                #如果没有第二个参数，虽然默认也是os.getcwd(),但获取的值是py所在目录，并不是切换过后的目录！why?
                os.chdir("..")
                #print os.getcwd()
            elif content.startswith("http://") or content.startswith("https://"):
                projectname=content.split('/')[-1].replace('.git','')
                if (os.path.exists(projectname)):
                    print "{0} already exist, updating".format(projectname)
                    os.chdir(projectname)
                    os.system("git pull")
                else:
                    print "cloning {0}".format(projectname)
                    os.system("git clone {0}".format(content))
            else:
                print "error"

if __name__=="__main__":
    basedir = raw_input("the path which scripts save to:")
    if basedir=="":
        print "No path specied,save to current"
        basedir = os.getcwd()
    elif(os.chdir(basedir)):
        print "Save scripts to "+basedir
    else:
        print "Error path"
        exit(0)
    getnext(roottopic,basedir)