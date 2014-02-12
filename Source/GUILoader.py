#-*- coding: utf-8 -*-
__author__ = 'Fábio'
import sys, pygtk, gtk, gtk.glade

class HelloWorldGTK:
    def __init__(self):
        #Set the Glade file
        self.gladeFile = './GUI/HDA3.8.glade'
        self.wTree = gtk.glade.XML(self.gladeFile)

        #Get the Main Window and connect the 'destroy' event
        self.window = self.wTree.get_widget("MainFrame")

        if (self.window):
            self.window.connect("destroy", gtk.main_quit)

class  QueryRelevanceEvaluationApp:
    def __init__(self):
        filename = "foo.glade"
        builder = gtk.Builder()
        builder.add_from_file('./GUI/HDA3.8.glade')
        builder.connect_signals(self)
        builder.get_object('TrackerMainWindow').show_all()
        settings = gtk.settings_get_default()
        settings.props.gtk_button_images = True

if __name__ == "__main__":
    app = QueryRelevanceEvaluationApp()
    gtk.main()