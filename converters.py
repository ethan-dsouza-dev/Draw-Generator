import re
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

#converts a time in a string formatted as ##:## to a 4 digit int ####
def time_str_to_int(time_str):
    time_pattern = re.compile('\d\d')
    matches = re.findall(time_pattern, time_str)
    time_int = ''
    for match in matches:
        time_int += match
        
    return int(time_int)

# function that converts a dictionary (with keys representing tee times and values showing team member names as a list)
#   to a pdf
def dict_to_pdf(draw_dict):
    document = []
    SimpleDocTemplate('draw.pdf', pagesize=letter,
                      rightmargin=12, leftmargin=12,
                      bottommargin=12, topmargin=12).build(addTeams(document, draw_dict)) 
    
    
#adds teams to the pdf
def addTeams(doc, draw_dict):
    
    for key in draw_dict.keys():
        time = key
        team = draw_dict[key]
        
        #Inserting time and first name from team
        doc.append(Paragraph(time + ":" + "&nbsp;"*2 + team[0], 
                            ParagraphStyle(name='Time',
                                            fontFamily='Helvetica',
                                            fontSize=15,
                                            alignment=TA_LEFT)))
        doc.append(Spacer(1, 5))
        
        #Inserting rest of the names
        for i in range(1, len(team)):
            doc.append(Paragraph("&nbsp;"*12 + team[i], ParagraphStyle(name='Names',
                                                    fontFamily='Helvetica',
                                                    fontSize=15,
                                                    alignment=TA_LEFT)))
            doc.append(Spacer(1, 5))
            
        doc.append(Paragraph('-------------------------------------------------------------------------------------------',
                            ParagraphStyle(name='Separator',
                                            fontFamily='Helvetica',
                                            fontSize=15,)))
        doc.append(Spacer(1,10))
    return doc