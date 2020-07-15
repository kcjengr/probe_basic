from qtpyvcp.widgets.qtdesigner import _DesignerPlugin
import os

class PluginFactory():

    @staticmethod
    def import_class(cl):
        d = cl.rfind(".")
        classname = cl[d+1:len(cl)]
        m = __import__(cl[0:d], globals(), locals(), [classname])
        return getattr(m, classname)

    @staticmethod
    def pluginClass(self):
        return self.Widget_Type

    @staticmethod
    def loadPlugin(classpath,pluginname):
        plugin = type(pluginname, (_DesignerPlugin,), { 
            # data members  
            "Widget_Type":PluginFactory.import_class(classpath),
            
            # member functions 
            "pluginClass":PluginFactory.pluginClass
        })
        return plugin

    @staticmethod
    def LoadWidgetsFromPath(widget_folder,scope):
        folders = [d for d in os.listdir(widget_folder) if os.path.isdir(os.path.join(widget_folder, d))]
        print "widgets found: " + str(folders)
        for folder in folders:
            namespace = folder+"."+folder+"."+folder
            classname = folder+"_Plugin"
            scope[classname] = PluginFactory.loadPlugin(namespace,classname)

PluginFactory.LoadWidgetsFromPath(os.path.dirname(os.path.realpath(__file__)),globals())




    
