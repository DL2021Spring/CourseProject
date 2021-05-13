




from bs4 import BeautifulSoup
import re, requests
import csv

class GradesourceSession:
    
    cookies = None
    s = requests.session()
    savedAccount = {}
    savedPIDAccount = {}
    savedName = {}
    savedNamePID = {}
    def __init__(self, username, password, courseid):
        
        s = self.s
        
        print("Logging in....")
        postData = {'User' : username, 'Password' : password}
        loginPOST = s.post('https://www.gradesource.com/validate.asp', data = postData)
        if loginPOST.status_code != 200:
            print("Login failed... Exiting")
            exit()
        
        self.cookies = loginPOST.cookies
        print("Selecting course %s" % courseid)
        
        selectcourseGET = s.get('https://www.gradesource.com/selectcourse.asp?id=%s' % courseid, cookies = self.cookies) 
        
        self.cookies = selectcourseGET.cookies
        self.s = s
        
        self.email()

    
    def updateEmailScore(self, field, CSV, overwrite):
        
        s = self.s
        print("Converting CSV into a list...")
        
        reader = csv.reader(open(CSV, 'rU'), delimiter=',')
        try:
            scoreDict = dict(reader)
        except Exception, e:
            print("oops, your file is malformed, please fix it (check for extra lines)")
        print(overwrite)
        if (float(overwrite) == 0):
            for k,v in scoreDict.items():
                if (v == "0"):
                    scoreDict[k] = ""
        print(scoreDict)
        print("CSV Converted")
        self.s = s
        self.updateScores(field, scoreDict)
    
    def updatePIDScore(self, field, CSV, overwrite):
         
        s = self.s
        print("Converting CSV into a list...")
        
        reader = csv.reader(open(CSV, 'rU'), delimiter=',')
        try:
            scoreDict = dict(reader)
        except Exception, e:
            print("oops, your file is malformed, please fix it (check for extra lines)")
        print(scoreDict)
        if (float(overwrite) == 0):
            for k,v in scoreDict.items():
                if (v == "0"):
                    scoreDict[k] = ""
        updateScore = {}
        savedPIDAccount = self.savedPIDAccount
        
        for key in savedPIDAccount.keys():
            try:
                updateScore[key] = scoreDict[savedPIDAccount[key]]
            except Exception, e:
                print(savedPIDAccount[key]+ "was unable to be joined and therefore skipped")
                continue
        print(updateScore)
        print("CSV Converted to email")
        self.s = s
        self.updateScores(field, updateScore)

    def updateScores(self, field, scoreDict):
        s = self.s
        print("Updating scores...")
        
        html = s.get('https://www.gradesource.com/editscores1.asp?id=%s' % field, cookies = self.cookies).content
        
        returnOutput = {}
        totalCount = re.compile('<td nowrap colspan=3 class=BT>&nbsp;&nbsp;Maximum Points: &nbsp;&nbsp;<font color="#336699"><b>(.*)</b></font></td>')
        maximumScore = totalCount.search(html).group(1).strip()
        for k,v in scoreDict.items():
            
            if (v == ""): 
                value = -1
            else:
                value = float(v)
            maxScore = float(maximumScore) 
            if(value > maxScore):
                
                print(k + " has a score of " + v + " which is larger than the maximum score of " + maximumScore)
                returnOutput[k] = v
                   
        
        nomnomsoup = BeautifulSoup(html)
        updatePOSTDict = {}
        updateIDDict = {}

        for x in nomnomsoup.form('input', id = re.compile("^student")):
            
            studentNumber = re.compile('input id="(.*)" name=')
            studentString = studentNumber.search(str(x))
            studStr = studentString.group(1).strip()
            
            
            gradesourceNumber = re.compile('type="hidden" value="(.*)"')
            x =  x.findNext("input")
            gradesourceString = gradesourceNumber.search(str(x))
            gradStr = gradesourceString.group(1).strip()

            updatePOSTDict[studStr] = gradStr
            
            idNumber = re.compile('input name="id(.*)" type="hidden"')
            idString = idNumber.search(str(x))
            idString = "id"+str(idString.group(1).strip())

            updateIDDict[idString] = gradStr

            

        
        joinedDictA = {}
        saveAccount = self.savedAccount
        
        for key in saveAccount.keys():
            try:
                joinedDictA[key] = scoreDict[saveAccount[key]]
            except Exception, e:
                print(saveAccount[key] + " was found in Gradesource but not in the CSV.")
                continue

        joinedDictB = {}
        
        for key in updatePOSTDict.keys():
            try:
                joinedDictB[key] = joinedDictA[updatePOSTDict[key]]
            except Exception, e:
                print(updatePOSTDict[key] + " was unable to be joined and therefore skipped")
                continue
        
        
        joinedDictB.update(updateIDDict)
        joinedDictB['assessmentId'] = field
        joinedDictB['verifyAccepted'] = 'N'
        joinedDictB['studentCount'] = str(len(saveAccount))
        
        ret = s.post('https://www.gradesource.com/updatescores1.asp', data = joinedDictB, cookies = self.cookies)
        print "Scores Updated"
        for k,v in returnOutput.items():
            print("WARNING: " + k + " HAS A SCORE OF " + v + " WHICH IS LARGER THAN MAX. SCORE INPUTTED. PLEASE CHECK SITE TO CONFIRM")
    
        
    
    def email(self):
        
        s = self.s
        print("Generating list of students")
        
        html = s.get("https://www.gradesource.com/student.asp", cookies = self.cookies).content
        
        
        nomnomsoup = BeautifulSoup(html)
        tbody = nomnomsoup('td', text=re.compile("Secret*"))[0].parent.parent.parent.parent
        
        emailDict = {}
        emailPIDDict = {}
        nameDict = {}
        namePIDDict = {}
        for tr in tbody('tr'):
            try:
                
                studentNum = tr.contents[9].find('a')['href']
                studentNum = studentNum.replace("editstudent.asp?id=", "")
                
                studentNum = studentNum.encode('ascii')
                
                studentEmail = tr.contents[7].text.strip()
                studentEmail = studentEmail.encode('ascii')
                
                studentPID = tr.contents[3].text.strip()
                studentPID = studentPID.encode('ascii')
                
                studentName = tr.contents[1].text.strip()
                studentName = studentName.encode('ascii')
                if (str(studentEmail) != "Edit") :
                    
                    emailDict[str(studentNum)] = str(studentEmail)
                    
                    emailPIDDict[str(studentEmail)] = str(studentPID)
                    
                    nameDict[str(studentName)] = str(studentEmail)
                    
                    namePIDDict[str(studentName)] = str(studentPID)
            except Exception, e:
                
                continue
        
        self.savedAccount = emailDict
        print emailDict
        print "Students List Generated"
        
        self.savedName = nameDict
        
        self.savedNamePID = namePIDDict
        self.savedPIDAccount = emailPIDDict
        
        self.s = s


    
    def downloadEmail(self):
        print("Creating CSV")
        writer = csv.writer(open('Roster.csv', 'wb'))
        for key, value in self.savedName.items():
            writer.writerow([key,value])
        print(self.savedName)
        print("CSV Created")

    def downloadiClicker(self):
        print("Creating CSV")
        writer = csv.writer(open('iClickerRoster.csv', 'wb'), escapechar=' ', quoting=csv.QUOTE_NONE)
        for key, value in self.savedNamePID.items():
            writer.writerow([key,value])
        print("CSV Created")

