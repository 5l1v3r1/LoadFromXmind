#-*- coding: utf-8 -*-
import xmind
import os
from xmind.core import workbook,saver
from xmind.core.topic import TopicElement

w = xmind.load("Hackindex.xmind") # load an existing file or create a new workbook if nothing is found

s1=w.getPrimarySheet() # get the first sheet
roottopic = s1.getRootTopic()
topics=roottopic.getSubTopics() # get the root topic of this sheet
#print topics

def getnext(roottopic):
    topics = roottopic.getSubTopics()
    if topics:
        for topic in topics:
            if topic is dir:
                print topic.getTitle()
                getnext(topic)
            elif topic.startwith("http://") or topic.startwith("https://"):
                os.system("git clone {0}".format(topic))
            else:
                print "error"

if __name__=="__main__":
    getnext(roottopic)