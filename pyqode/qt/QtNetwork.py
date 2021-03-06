import os
from pyqode.qt import QT_API
from pyqode.qt import PYQT5_API
from pyqode.qt import PYQT4_API
from pyqode.qt import PYSIDE_API

try:
    if os.environ[QT_API] == PYQT5_API:
        from PyQt5.QtNetwork import *
    elif os.environ[QT_API] == PYQT4_API:
        from PyQt4.QtNetwork import *
    elif os.environ[QT_API] == PYSIDE_API:
        from PySide.QtNetwork import *
except ImportError:
    assert os.environ.get('SPHINX', None) == '1'

    class QTcpSocket:
        pass
