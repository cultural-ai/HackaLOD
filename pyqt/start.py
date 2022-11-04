"""
https://coderslegacy.com/python/pyqt6-qlineedit/
"""

from collections import defaultdict
import json
import operator
import pathlib
import sys
from functools import reduce

import pandas as pd
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QComboBox, QWidget

capture_fp: pathlib.Path = pathlib.Path("capture.json")


class Window(QtWidgets.QWidget):
    def __init__(self, concepts, contexts):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)

        # box 1
        self.b1 = QtWidgets.QLineEdit()
        layout.addWidget(self.b1)

        # completer for box q
        self.completer1 = QtWidgets.QCompleter(concepts, self.b1)
        self.completer1.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completer1.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self.completer1.setWidget(self.b1)
        self.completer1.activated.connect(self.handleCompletion1)
        self.b1.textChanged.connect(self.handleTextChanged1)
        self.b1.returnPressed.connect(self.captureb1)
        self._completing = False

        # combo box - context 1
        self.c1 = QComboBox(self)
        self.c1.addItems(contexts)
        layout.addWidget(self.c1)
        self.c1.currentTextChanged.connect(self.capturec1)

    def captureb1(self):

        d = {}
        # if existing ... load
        if capture_fp.exists():

            with open(capture_fp, "r") as f:
                d = json.load(f)

        # no existing ...
        else:
            d = {"concept": None, "context": None}

        # overwrite concept and then re-save
        d["concept"] = self.b1.text()
        with open(capture_fp, "w") as f:
            json.dump({"concept": self.b1.text()}, f)

    def handleTextChanged1(self, text):
        if not self._completing:
            found = False
            prefix = text.rpartition(",")[-1]
            if len(prefix) > 1:
                self.completer1.setCompletionPrefix(prefix)
                if self.completer1.currentRow() >= 0:
                    found = True
            if found:
                self.completer1.complete()
            else:
                self.completer1.popup().hide()

    def handleCompletion1(self, text):
        if not self._completing:
            self._completing = True
            prefix = self.completer1.completionPrefix()
            self.b1.setText(self.b1.text()[: -len(prefix)] + text)
            self._completing = False

    def capturec1(self):

        # if existing ... load
        if capture_fp.exists():

            with open(capture_fp, "r") as f:
                d = json.load(f)

        # no existing ...
        else:
            d = {"concept": None, "context": None}

        # overwrite concept and then re-save
        d["context"] = self.c1.currentText()
        with open(capture_fp, "w") as f:
            json.dump(d, f)


if __name__ == "__main__":

    # load a dataframe of all symbol-concept-context triples
    df_symbols_contexts_concepts = pd.read_csv(
        "./data/hyperreal2.csv", encoding="latin1"
    )

    # build a list of available contexts
    contexts: list[str] = reduce(
        operator.concat,
        sorted(
            set(
                [
                    x.split(" @ ")
                    for x in set(df_symbols_contexts_concepts.loc[:, "contexts"])
                ]
            )
        ),
    )

    # load a dataframe of artwork properties related to symbols
    df_symbol2artword = pd.read_csv("./data/big_final_data.csv")

    # build an index of concept: contexts
    concept2context = defaultdict(list)
    for row in df_symbols_contexts_concepts.iterrows():
        concept2context[]
    
    
      
    

    # concept2context = {for }

    # load the
    concepts = ["feminism", "masculinity"]
    contexts = ["feudel japan", "italian rennaissance"]

    app = QtWidgets.QApplication(["Test"])
    window = Window(concepts, contexts)
    window.setGeometry(600, 100, 300, 50)
    window.show()
    sys.exit(app.exec())
