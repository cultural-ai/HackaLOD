"""
https://coderslegacy.com/python/pyqt6-qlineedit/
"""

import json
import operator
import pathlib
import sys
from collections import defaultdict
from functools import reduce

import pandas as pd
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QComboBox, QWidget


class Window(QtWidgets.QWidget):
    def __init__(
        self, concepts, concept2context, capture_fp, pair2symbols, df_symbol2artwork
    ):

        super().__init__()

        # assign indices to self
        self.concepts = concepts
        self.concept2context = concept2context
        self.pair2symbols = pair2symbols
        self.df_symbol2artwork = df_symbol2artwork

        # init state the dialogue is to be set to
        with open(capture_fp, "r") as f:
            state = json.load(f)
        self.concept: str = state["concept"]
        self.context: str = state["context"]

        # build
        layout = QtWidgets.QVBoxLayout(self)

        # box 1 - concept
        self.b1 = QtWidgets.QLineEdit(self.concept)
        layout.addWidget(self.b1)
        
        # completer for box b1
        self.completer1 = QtWidgets.QCompleter(self.concepts, self.b1)
        self.completer1.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completer1.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self.completer1.setWidget(self.b1)
        self.completer1.activated.connect(self.handleCompletion1)
        self.b1.textChanged.connect(self.handleTextChanged1)
        
        self.b1.returnPressed.connect(self.captureb1)
        self._completing = False

        # combo box - context 1
        self.c1 = QComboBox(self)
        self.c1.addItems(self.concept2context[concept])
        layout.addWidget(self.c1)
        self.c1.currentTextChanged.connect(self.capturec1)

    def unity(self):
        """produce json of sampled artworks."""

        # get list of symbols which correspond to concept-context selection
        concept_context = (self.concept, self.context)
        symbols_of_interest = self.pair2symbols[concept_context]
        print(concept_context, symbols_of_interest)

        # filter artworks which math 
        slice = self.df_symbol2artwork.loc[
            self.df_symbol2artwork.loc[:, "symbol"].isin(symbols_of_interest),
            ["painting_title", "painting_image_link", "symbol"],
        ]
        print(slice)



    def captureb1(self):
        """On b1 change, update state json, and produce new unity json."""

        # ------
        # amend self.concept
        # ------
        self.concept = self.b1.text()

        # ------
        # write change to json
        # ------
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

        # ------
        # amend context boxes
        # ------
        self.c1.clear()
        self.c1.addItems(self.concept2context[self.concept])
        
        # ------
        # update unity json
        # ------
        # self.unity()

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

        self.context = self.c1.currentText()
        
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

        # ------
        # update unity json
        # ------
        self.unity()


if __name__ == "__main__":

    # load a dataframe of all symbol-concept-context triples
    df_symbols_contexts_concepts: pd.DataFrame = pd.read_csv(
        "./data/hyperreal_with_concept_labels.csv", encoding="latin1"
    )

    # build an index of concept: contexts
    concept2context = defaultdict(list)
    for i, row in df_symbols_contexts_concepts.iterrows():

        concept = row["label"]
        contexts = row["contexts"]

        if " @ " in contexts:
            for context in contexts.split(" @ "):
                if context not in concept2context[concept]:
                    concept2context[concept].append(context)
        else:
            if contexts not in concept2context[concept]:
                concept2context[concept].append(contexts)
    # build an index of (concept, context): symbols
    pair2symbols = defaultdict(list)
    for i, row in df_symbols_contexts_concepts.iterrows():

        concept = row["label"]
        contexts = row["contexts"]
        symbol = row["symbol"]

        if " @ " in contexts:
            for context in contexts.split(" @ "):
                pair2symbols[(concept, context)].append(symbol)
        else:
            if contexts not in concept2context[concept]:
                pair2symbols[(concept, contexts)].append(symbol)
    
    # build concepts list
    concepts: list[str] = sorted(list(concept2context.keys()))
    
    # ------
    # load a dataframe of artwork properties related to symbols
    # ------
    df_symbol2artwork: pd.DataFrame = pd.read_csv("./data/big_final_data.csv")

    # ------
    # build a default user-selected context and concept state
    # ------
    capture_fp: pathlib.Path = pathlib.Path("capture.json")
    if capture_fp.exists() == False:
        state = {"concept": "courage", "context": "grecoRoman"}
        with open(capture_fp, "w") as f:
            json.dump(state, f)
    else:
        pass

    # ------
    # build the pyqt app
    # ------
    app = QtWidgets.QApplication(["Test"])
    window = Window(
        concepts, concept2context, capture_fp, pair2symbols, df_symbol2artwork
    )
    window.setGeometry(600, 100, 300, 50)
    window.show()
    sys.exit(app.exec())
