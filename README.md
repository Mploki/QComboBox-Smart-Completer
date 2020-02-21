# QComboBox-Smart-Completer
PyQt5 QComboBox and QCompleter custom implementation to have a smart autocompleter which sort results (by StartsWith then Contains model) and handles Tab Key autocompletion and Tab Key select completion

There are 2 reimplementations of classics PyQt5 classes :

  -	CustomAutoCompleter is an QCompleter which matches "containing prefix" models and sort them by StartsWith first and Contains (but not StartsWith) then, all in source ItemModel entries Order

  - ExtendedCombo is a QComboBox which handles Tab key and find in the linked completer model list the better match (or the selected one)

Those 2 classes are independant, you can link any other completer with the "ExtendedCombo" class or you can use the "CustomAutoCompleter" alone.

There is a example of use in the test.py file