from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class StatusBar(ABC):
    system: str

    @abstractmethod
    def create(self):
        pass

@dataclass
class MainMenu(ABC):
    system: str

    @abstractmethod
    def create(self):
        pass


@dataclass
class WindowsStatusBar(StatusBar):
    system: str = None

    def __post__init(self):
        self.system = 'Windows'

    def create(self) -> None:
        print(f'status bar {self.system}')

'''Windows class'''
@dataclass
class WindowsMainMenu(MainMenu):
    system: str = None

    def __post__init(self):
        self.system = 'Windows'

    def create(self) -> None:
        print(f'mainMenu {self.system}')


'''Linux class'''
@dataclass
class LinuxStatusBar(StatusBar):
    system: str = None

    def __post__init(self):
        self.system = 'Linux'

    def create(self) -> None:
        print(f'status bar {self.system}')


@dataclass
class LinuxMainMenu(MainMenu):
    system: str = None

    def __post__init(self):
        self.system = 'Linux'

    def create(self) -> None:
        print(f'mainMenu {self.system}')


'''Абстрактная фабрика'''
@dataclass
class GuiAbstractFactory(ABC):

    @abstractmethod
    def getStatusBar(self) -> StatusBar:
        pass

    @abstractmethod
    def getMainMenu(self) -> MainMenu:
        pass


'''Фабрики'''
@dataclass
class WindowsGUIFactory(GuiAbstractFactory):

    def getStatusBar(self) -> StatusBar:
        return WindowsStatusBar()

    def getMainMenu(self) -> MainMenu:
        return WindowsMainMenu()


@dataclass
class LinuxGUIFactory(GuiAbstractFactory):

    def getStatusBar(self) -> StatusBar:
        return LinuxStatusBar()

    def getMainMenu(self) -> MainMenu:
        return LinuxMainMenu()


@dataclass
class Application:
    gui_factory: GuiAbstractFactory

    def create_gui(self):
        status_bar = self.gui_factory.getStatusBar()
        main_menu = self.gui_factory.getMainMenu()
        status_bar.create()
        main_menu.create()


def create_factory(system_name: str) -> GuiAbstractFactory:
    factory_dict = {
        'Windows': WindowsGUIFactory(),
        'Linux': LinuxGUIFactory()
    }

    return factory_dict[system_name]


if __name__ == '__main__':
    system_name = 'Linux'
    ui = create_factory(system_name)
    app = Application(ui)
    app.create_gui()
