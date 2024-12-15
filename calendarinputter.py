import fileinput
import sys
import os

intro = input("Would you like to add or remove a date?" + '\n')

here = os.path.dirname(os.path.abspath(__file__))
calendarfile = os.path.join(here, 'calendar.html')

def changecalendar():
    if intro == "add":
        inputdate = input("What date do you want to place an event? (mmddyy)" + '\n')
        alreadyclass = input("Is there already a class on this date? (y/n)" + '\n')
        classtype = input("Please input the class type and time." + '\n')
        paypaldropdown = input("Please input the PayPal form option." + '\n')
        classtypeid = classtype.replace(" ", "")
        classtypeid = classtypeid.replace("-", "")
        classtypeid = classtypeid.replace(":", "")
        for line in fileinput.FileInput(calendarfile, inplace=True):
            if alreadyclass == "n":
                if inputdate + 'd' in line:
                    line = line.rstrip()
                    line = line.rstrip("</div></td>")
                    line = line + '<br><a class="callink" href="#dateselection" id="' + classtype + inputdate + '">' + classtype + '</a></div></td>' + '\n'
                sys.stdout.write(line)
            if alreadyclass == "y":
                if inputdate + 'd' in line:
                    line = line.rstrip()
                    line = line.rstrip("</div></td>")
                    line = line + '><br><a class="callink" href="#dateselection" id="' + classtype + inputdate + '">' + classtype + '</a></div></td>' + '\n'
                sys.stdout.write(line)
        for line in fileinput.FileInput(calendarfile, inplace=True):
            if 'pymarker' in line:
                line = '        <option value="' + paypaldropdown + '">' + paypaldropdown + '</option>' + '<!--' + inputdate + 'r-->' + '\n' + '<!--pymarker-->' + '\n'
            sys.stdout.write(line)
        for line in fileinput.FileInput(calendarfile, inplace=True):
            if 'idmarker' in line:
                line = '    var ' + classtypeid + inputdate + ' = document.getElementById("' + classtype + inputdate + '");' + '//' + inputdate + 'r' + '\n' + '//idmarker' + '\n'
            sys.stdout.write(line)
        for line in fileinput.FileInput(calendarfile, inplace=True):
            if 'dropdownmarker' in line:
                line = '    ' + classtypeid + inputdate + '.addEventListener("click", dateChange);' + '//' + inputdate + 'r' + '\n' + '  ' + classtypeid + inputdate + '.dropdowndate = "' + paypaldropdown + '";' + '//' + inputdate + 'r' + '\n' + '//dropdownmarker' + '\n'
            sys.stdout.write(line)
    if intro == "remove":
        inputdate = input("What date would you like to clear? (mmddyy)" + '\n')
        inputday = input("Which day of the month is it? (e.g. January 27th would be 27)" + '\n')
        for line in fileinput.FileInput(calendarfile, inplace=True):
            if inputdate + 'd' in line:
                line = '                <td><div class="daybody"><!--' + inputdate + 'd-->' + inputday + '</div></td>' + '\n'
            sys.stdout.write(line)
        for line in fileinput.FileInput(calendarfile, inplace=True):
            if inputdate + 'r' in line:
                line = ''
            sys.stdout.write(line)
    again = input("Add another? (y/n)")
    if again == 'y':
        changecalendar()


changecalendar()