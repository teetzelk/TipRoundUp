from anvil import *
import math

class Form1(Form1Template):

  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def calculate_click (self, **event_args):
    actualCheck = float(self.checkTotal.text)
    
    initialTip = float(self.initialTip.text)
    
    tipValue = actualCheck * (initialTip / 100)
    
    withTipTotal = actualCheck + tipValue
    
    tipTotalCeil = math.ceil(withTipTotal)
    
    tipDelta = tipTotalCeil - withTipTotal
    
    newTip = tipValue + tipDelta
    newTotal = newTip + actualCheck
    
    self.finalCheckTotal.text = "${:,.2f}".format(actualCheck)
    self.finalTip.text = "${:,.2f}".format(newTip)
    self.finalTotal.text = "${:,.2f}".format(newTotal)
    pass

