#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request

def bubbleSort(keys, values):
    isSorted = False
    while isSorted == False:
        swapMade = 0
        for i in range(len(values) - 1):
            #sort through the lists item by item
            if values[i] < values[i + 1]:
                swapMade = 1
                temp = values[i]
                values[i] = values[i+1]
                values[i+1] = temp
                keysTemp = keys[i]
                keys[i] = keys[i+1]
                keys[i+1] = keysTemp

        if swapMade == 0:
            swapMade = 9000
            #print(keys, values)
            isSorted = True
    return([keys, values])



def get_text():
    """This retrieves text from Project Gutenburg
    """
    url = "http://pastebin.com/raw/kktJRg84"
    head = 103
    foot = 7
    body = ''
    with request.urlopen(url) as url_fh:
        body = url_fh.read().decode('UTF-8')
    body = body.split('\n', head)[-1]
    body = body.rsplit('\n', foot)[0]

    return body


def main():
    """This is what runs when you call `python word_count.py`.
    """
    text = get_text()
    #text = "one two two three three three four four four four five five five five five six six six six six six seven seven seven seven seven seven seven eight eight eight eight eight eight eight eight nine nine nine nine nine nine nine nine nine ten ten ten ten ten ten ten ten ten ten eleven eleven eleven eleven eleven eleven eleven eleven eleven eleven eleven twelve twelve twelve twelve twelve twelve twelve twelve twelve twelve twelve twelve thirteen thirteen thirteen thirteen thirteen thirteen thirteen thirteen thirteen thirteen thirteen thirteen thirteen fourteen fourteen fourteen fourteen fourteen fourteen fourteen fourteen fourteen fourteen fourteen fourteen fourteen fourteen fifteen fifteen fifteen fifteen fifteen fifteen fifteen fifteen fifteen fifteen fifteen fifteen fifteen fifteen fifteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen sixteen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen seventeen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen eighteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen nineteen twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty twenty"
    for i in text:
            if not i.isalpha():
                if i != " ":
                    if i != "\n":
                        if i !="'":
                            text = text.replace(i, " ")
    text = text.lower()
    text = text.split()

    shakespeare = {}
    for i in text:
        if i in shakespeare:
            shakespeare[i] += 1

        else:
            shakespeare[i] = 1

    keyList = []
    valueList = []
    for akey in shakespeare:
        keyList.append(akey)
        valueList.append(shakespeare[akey])
    sortedLists = bubbleSort(keyList, valueList)
    #for i in range(len(sortedLists[0])):
    for i in range(100):
        print(i+100, sortedLists[0][i+100], sortedLists[1][i+100])
    #print((sortedLists))





    #print(keyList)
    #print(valueList)


# leave this code as it is
if __name__ == "__main__":
    main()
