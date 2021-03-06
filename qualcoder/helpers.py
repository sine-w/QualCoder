from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from information import DialogInformation
from PyQt5 import QtCore, QtGui, QtWidgets


def msecs_to_mins_and_secs(msecs):
    """ Convert milliseconds to minutes and seconds.
    msecs is an integer. Minutes and seconds output is a string."""

    secs = int(msecs / 1000)
    mins = int(secs / 60)
    remainder_secs = str(secs - mins * 60)
    if len(remainder_secs) == 1:
        remainder_secs = "0" + remainder_secs
    return str(mins) + "." + remainder_secs


class Message(QtWidgets.QMessageBox):
    """ This is called a lot , but is styled to font size """
    def __init__(self, app, title, text, icon=None):
        QtWidgets.QMessageBox.__init__(self)
        
        self.setStyleSheet("* {font-size:" + str(app.settings['fontsize']) + "pt} ")
        self.setWindowTitle(title)
        self.setText(text)
        if icon == "warning":
            self.setIcon(QtWidgets.QMessageBox.Warning)
        if icon == "Information":
            self.setIcon(QtWidgets.QMessageBox.Information)
        if icon == "critical":
            self.setIcon(QtWidgets.QMessageBox.Critical)


#TODO check if this is used anywhere
# Delete otherwise
'''class CodedMediaMixin_OLD:
    def coded_media(self, data):
        """ Display all coded media for this code.
        Coded media comes from ALL files and ALL coders.
        This is called from code_text
        """

        ui = DialogInformation("Coded text : " + data['name'], "<br />")
        cur = self.app.conn.cursor()
        CODENAME = 0
        COLOR = 1
        SOURCE_NAME = 2
        POS0 = 3
        POS1 = 4
        SELTEXT = 5
        OWNER = 6
        sql = "select code_name.name, color, source.name, pos0, pos1, seltext, code_text.owner from "
        sql += "code_text "
        sql += " join code_name on code_name.cid = code_text.cid join source on fid = source.id "
        sql += " where code_name.cid =" + str(data['cid']) + " "
        sql += " order by source.name, pos0, code_text.owner "
        cur.execute(sql)
        results = cur.fetchall()
        # Text
        for row in results:
            # added str() to color to catch any RQDA color import errors, should not occur now
            title = '<span style=\"background-color:' + str(row[COLOR]) + '\">'
            title += " File: <em>" + row[SOURCE_NAME] + "</em></span>"
            title += ", Coder: <em>" + row[OWNER] + "</em> "
            title += ", " + str(row[POS0]) + " - " + str(row[POS1])
            ui.ui.textEdit.insertHtml(title)
            ui.ui.textEdit.append(row[SELTEXT] + "\n\n")

        # Images
        sql = "select code_name.name, color, source.name, x1, y1, width, height,"
        sql += "code_image.owner, source.mediapath, source.id, code_image.memo "
        sql += " from code_image join code_name "
        sql += "on code_name.cid = code_image.cid join source on code_image.id = source.id "
        sql += "where code_name.cid =" + str(data['cid']) + " "
        sql += " order by source.name, code_image.owner "
        cur.execute(sql)
        results = cur.fetchall()
        for counter, row in enumerate(results):
            ui.ui.textEdit.insertHtml('<span style=\"background-color:' + row[COLOR] + '\">File: ' + row[8] + '</span>')
            ui.ui.textEdit.insertHtml('<br />Coder: ' + row[7])
            img = {'mediapath': row[8], 'x1': row[3], 'y1': row[4], 'width': row[5], 'height': row[6]}
            #self.put_image_into_textedit(img, counter, ui.ui.textEdit)  # cannot do this
            dimensions = "x: " + str(int(img['x1'])) + ", y: " + str(int(img['y1'])) + ", width: "
            dimensions += str(int(img['width'])) + ", height: " + str(int(img['height']))
            ui.ui.textEdit.append(dimensions)
            ui.ui.textEdit.append("Memo: " + row[10] + "\n\n")

        # Media
        sql = "select code_name.name, color, source.name, pos0, pos1, code_av.memo, "
        sql += "code_av.owner, source.mediapath, source.id from code_av join code_name "
        sql += "on code_name.cid = code_av.cid join source on code_av.id = source.id "
        sql += "where code_name.cid = " + str(data['cid']) + " "
        sql += " order by source.name, code_av.owner "
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            ui.ui.textEdit.insertHtml('<span style=\"background-color:' + row[COLOR] + '\">File: ' + row[7] + '</span>')
            start = msecs_to_mins_and_secs(row[3])
            end = msecs_to_mins_and_secs(row[4])
            ui.ui.textEdit.insertHtml('<br />[' + start + ' - ' + end + '] Coder: ' + row[6])
            ui.ui.textEdit.append("Memo: " + row[5] + "\n\n")
        ui.exec_()'''
