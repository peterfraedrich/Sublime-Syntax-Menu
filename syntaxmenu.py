import sublime, sublime_plugin, os

class OpenSyntaxMenuCommand(sublime_plugin.WindowCommand, sublime.View):

    def run(self):
        # get list of syntaxes for quick panel
        syntaxes = os.listdir(sublime.cache_path())
        # create quick panel with syntaxes
        self.window.show_quick_panel(syntaxes, self.onDone, 0)
        pass

    def onDone(self, index):
        view = self.window.active_view()
        if index == -1:
            # do nothing if no syntax selected
            return
        else:
            # get syntax list again, because this is dumb
            syn = os.listdir(sublime.cache_path())
            sname = syn[index]
            try:
                view.settings().set('syntax','Packages/' + sname + '/' + sname + '.sublime-syntax')
                return
            except:
                pass
            try:
                view.settings().set('syntax','Packages/' + sname + '/' + sname + '.tmLanguage')
                return
            except:
                pass
