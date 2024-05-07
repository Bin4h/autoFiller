import docx
import os
import students

class Social_formate:
    def __init__(self, stud):
        self.stud = stud
        self.Dictionary = {
            "N": self.stud.getCourse(),
            "CCC": self.stud.getGroup(),
            "ФАМИЛИЯ": self.stud.getSecond(),
            "ИМЯ": self.stud.getFirst(),
            "ОТЧЕСТВО": self.stud.getMiddle(),
            "BB-BB-BBB": self.stud.getCertName(),
            "DD.MM.YYYY1": self.stud.getCertDate(),
            "DD.MM.YYYY": self.stud.getCurDate()
        }
        self.path = r"C:\Users\megas\PycharmProjects\autoFiller\forms\cert\Zayavlenie_na_poluchenie_sotsialnoy_stipendii.docx"
        self.save_path = r"C:\Users\megas\PycharmProjects\autoFiller\Saved_files\saved.docx"

    def changeDocx(self):

        doc = docx.Document(self.path)
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = docx.shared.Pt(14)

        for i in self.Dictionary:
            for p in doc.paragraphs:
                if p.text.find(i) >= 0:
                    p.text = p.text.replace(i, self.Dictionary[i])
        doc.save(os.path.basename(self.save_path))