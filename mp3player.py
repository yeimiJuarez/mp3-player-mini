from PyQt5 import  QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import sys, os
from pygame import mixer
import pygame

home = os.getenv("HOME")


class mainInitial(QtWidgets.QMainWindow):
  def __init__(self):
      super(mainInitial, self).__init__()

      uic.loadUi("reproductor.ui", self)
      
      self.buttonPlay = self.findChild(QtWidgets.QPushButton, 'btnPlay') # Find the button
      self.buttonPlay.clicked.connect(self.play_song)
      self.buttonOpen = self.findChild(QtWidgets.QPushButton, 'btnOpen') # Find the button
      self.buttonOpen.clicked.connect(self.open_folder)

      self.show()

  def open_folder(self):
      options = QFileDialog.Options()
      options |= QFileDialog.DontUseNativeDialog
      fileName, _ = QFileDialog.getOpenFileName(self,"Buscar archivos mp3", "","All Files (*.mp3);;Mp3 Files (*.mp3)", options=options)
      if fileName:
          #print(fileName)
          self.lista = self.findChild(QtWidgets.QListWidget, 'listWidget')
          self.lista.addItem(fileName)



  def play_song(self):
      self.lista = self.findChild(QtWidgets.QListWidget, 'listWidget')
      items=[]
      pygame.init()

      for i in range(self.lista.count()):
          items.append(self.lista.item(i).text())
          print (self.lista.item(i).text())
          pygame.mixer.music.load(self.lista.item(i).text())
          pygame.mixer.music.play()
      print (items)
      
 

if __name__ == '__main__':   
    app = QtWidgets.QApplication(sys.argv)
    myapp = mainInitial()
    sys.exit(app.exec_())