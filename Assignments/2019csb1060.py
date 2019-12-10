#utility functions
def date_lies_between(date, startdate, enddate):
      #basically, finds number of says since 0-0-0 for all 3 dates and compares them
      #start date val
      startval = 0
      isleap = False
      for y in range(0, startdate[2]):
            if((y%4 == 0 and y%100 != 0) or (y%400 == 0)):
                  startval = startval + 366
                  isleap = True
            else:
                  startval = startval + 365
      
      if((startdate[2]%4 == 0 and startdate[2]%100 != 0) or (startdate[2]%400 == 0)):
                  isleap = True
      
      for i in range(1, startdate[1]):
            if(i in [1, 3, 5, 7, 8, 10, 12]):
                  startval = startval + 31
            elif(i in [4, 6, 9, 11]):
                  startval = startval + 30
            elif(isleap):
                  startval = startval + 29
            else:
                  startval = startval + 28
      
      startval = startval + startdate[0]
      
      #end date val
      endval = 0
      isleap = False
      for y in range(0, enddate[2]):
            if((y%4 == 0 and y%100 != 0) or (y%400 == 0)):
                  endval = endval + 366
                  isleap = True
            else:
                  endval = endval + 365
      
      if((enddate[2]%4 == 0 and enddate[2]%100 != 0) or (enddate[2]%400 == 0)):
                  isleap = True
      
      for i in range(1, enddate[1]):
            if(i in [1, 3, 5, 7, 8, 10, 12]):
                  endval = endval + 31
            elif(i in [4, 6, 9, 11]):
                  endval = endval + 30
            elif(isleap):
                  endval = endval + 29
            else:
                  endval = endval + 28
      
      endval = endval + enddate[0]
      
      #current date val
      curval = 0
      isleap = False
      for y in range(0, date[2]):
            if((y%4 == 0 and y%100 != 0) or (y%400 == 0)):
                  curval = curval + 366
                  isleap = True
            else:
                  curval = curval + 365
      
      if((date[2]%4 == 0 and date[2]%100 != 0) or (date[2]%400 == 0)):
                  isleap = True
      
      for i in range(1, date[1]):
            if(i in [1, 3, 5, 7, 8, 10, 12]):
                  curval = curval + 31
            elif(i in [4, 6, 9, 11]):
                  curval = curval + 30
            elif(isleap):
                  curval = curval + 29
            else:
                  curval = curval + 28
      
      curval = curval + date[0]
      
      if(startval <= curval <= endval):
            return True
      else:
            return False

#to read xml

f = open("Britomart_Redeems_Faire_Amoret.xml", "r")
data = f.read()
f.close()

#list of tags, not including <ref> since it appears as &lt;ref&gt;
tags = []
tagstart = data.find('<')
while (tagstart != -1):
      tagend = data.find('>', tagstart)
      tags.append((data[tagstart + 1: tagend], tagstart))
      tagstart = data.find('<', tagstart + 1)

#removing tags before <page>
while(tags[0][0] != 'page'):
      tags.pop(0)

#print ans to q1
last_revision_index = -1
#iterating through tags in reverse and finding the first <revision> we come across
for i in range(len(tags)-1, -1, -1):
      if(tags[i][0] == "revision"):
            last_revision_index = i
            break

#finding first <text> after the previously found <revision>
corresponding_text_index = -1
for i in range(last_revision_index, len(tags)):
      if(tags[i][0].startswith("text")):
            corresponding_text_index = i
            break
#offset prevents printing "<text>" at the begginging of <text> tag contents
offset = data.find('>', tags[corresponding_text_index][1]) - tags[corresponding_text_index][1] + 1
#print(data[tags[corresponding_text_index][1] + offset: tags[corresponding_text_index + 1][1]])


#print ans to q2
#assuming dates in dd-mm-yyyy format
startdate = [int(x) for x in input().split('-')]
enddate = [int(x) for x in input().split('-')]

#finding index of all <timestamp> within given range
valid_timestamp_indexes = []
for i in range(len(tags)):
      if(tags[i][0] == "timestamp"):
            date = [int(x) for x in data[tags[i][1]+11 : tags[i][1] + 21].split('-')]
            date.reverse()
            
            if(date_lies_between(date, startdate, enddate)):
                  valid_timestamp_indexes.append(i)

#printing <text> tag after every valid <timestamp>
for ind in valid_timestamp_indexes:
      text_tag_index = -1
      for i in range(ind, len(tags)):
            if(tags[i][0].startswith("text")):
                  text_tag_index = i
                  break
      
      offset = data.find('>', tags[text_tag_index][1]) - tags[text_tag_index][1] + 1
      #print(data[tags[corresponding_text_index][1] + offset: tags[corresponding_text_index + 1][1]])


#print ans to q3
#searching separately for <ref> since it appears as &lt;ref&gt; and not "<ref>"
ref_start = data.find("&lt;ref")
while(ref_start != -1):
      ref_end = data.find("&lt;/ref&gt;", ref_start)
      ref_print_start = data.find("&gt;", ref_start)
      print("<",data[ref_start+4 : ref_print_start],">", data[ref_print_start + 4 : ref_end], "</ref>", sep = "")
      ref_start = data.find("&lt;ref", ref_start+1)