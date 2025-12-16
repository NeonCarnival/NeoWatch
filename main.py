from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass
from path_config import VIOLA_LOG_PATH

class NeoWatchDashboard(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20)
        self.title_label = Label(text="NEOWATCH DASHBOARD", font_size='24sp', bold=True)
        self.status_label = Label(text=f"Log-Quelle: {VIOLA_LOG_PATH}", font_size='14sp')
        self.info_label = Label(text="Viola Service: Initialisiere...", font_size='18sp')
        
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.info_label)
        
        # Startet den Hintergrunddienst
        self.start_viola_service()
        return self.layout

    def start_viola_service(self):
        try:
            service = autoclass('org.fusion.neowatch.ServiceViolaservice')
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            service.start(mActivity, "")
            self.info_label.text = "Viola Service: AKTIV"
        except Exception as e:
            self.info_label.text = f"Service-Fehler: {str(e)}"

if __name__ == "__main__":
    NeoWatchDashboard().run()
