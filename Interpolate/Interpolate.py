from vanilla import *

af = AllFonts()
f = CurrentFont()


def createFontList():
	fontList = []
	for f in af:
		if f.info.familyName and f.info.styleName:
			if f.info.styleName == "Regular":
				fontList.append(f.info.familyName)
			else:
				fontList.append(f.info.familyName + " " + f.info.styleName)
		else:
			return
	return fontList
		
class InterpolateWindow(object):
	
	def __init__(self):
		self.fontSourceName = fontList[0]
		self.fontTargetName = fontList[0]
		self.fontSourceIndex = 0
		self.fontTargetIndex = 0
		self.interpolateXValue = 0
		self.interpolateYValue = 0
		self.scaleXValue = 100
		self.scaleYValue = 100
		self.sourceLayerList = af[self.fontSourceIndex].layerOrder
		self.targetLayerList = af[self.fontTargetIndex].layerOrder
		self.sourceLayerName = self.sourceLayerList[0]
		self.targetLayerName = self.targetLayerList[0]
		self.useSourceLayer = False
		self.useTargetLayer = False
		
		self.w = FloatingWindow((400, 500), "Interpolate")
		self.w.textBoxSource = TextBox((10, 10, 190, 20), "Master Font 1:")
		self.w.popUpButtonSource = PopUpButton((10, 30, 190, 20), fontList, callback=self.popUpButtonSourceCallback, sizeStyle = "regular")
		
		self.w.textBoxSourceLayer = TextBox((210, 10, -10, 20), "Layer:")
		self.w.popUpButtonSourceLayer = PopUpButton((210, 30, -10, 20), self.sourceLayerList, callback=self.popUpButtonSourceLayerCallback, sizeStyle = "regular")
		self.w.textBoxSourceLayer.show(self.useSourceLayer)
		self.w.popUpButtonSourceLayer.show(self.useSourceLayer)
		self.w.foregroundSourceCheckBox = CheckBox((10, 50, -10, 20), "Use Layer",
                           callback=self.foregroundSourceCheckBoxCallback, value=self.useSourceLayer)

		self.w.textBoxTarget = TextBox((10, 70, 190, 20), "Master Font 2:")
		self.w.popUpButtonTarget = PopUpButton((10, 90, 190, 20), fontList, callback=self.popUpButtonTargetCallback, sizeStyle = "regular")
		
		self.w.textBoxTargetLayer = TextBox((210, 70, -10, 20), "Layer:")
		self.w.popUpButtonTargetLayer = PopUpButton((210, 90, -10, 20), self.targetLayerList, callback=self.popUpButtonTargetLayerCallback, sizeStyle = "regular")
		self.w.textBoxTargetLayer.show(self.useTargetLayer)
		self.w.popUpButtonTargetLayer.show(self.useTargetLayer)
		self.w.foregroundTargetCheckBox = CheckBox((10, 110, -10, 20), "Use Layer",
                           callback=self.foregroundTargetCheckBoxCallback, value=self.useTargetLayer)
		
		self.w.interpolateXTextBox = TextBox((10, 150, -10, 20), "Interpolate X:")
		self.w.interpolateXEditText = EditText((100, 150, 60, 20),
							callback=self.interpolateXEditTextCallback)
		self.w.interpolateXSlider = Slider((10, 180, -10, 23),
							tickMarkCount=10,
							value = 0,
							maxValue = 2000,
							minValue = -1000,
							callback=self.interpolateXSliderCallback)
							
		self.w.interpolateYTextBox = TextBox((10, 210, -10, 20), "Interpolate Y:")
		self.w.interpolateYEditText = EditText((100, 210, 60, 20),
							callback=self.interpolateYEditTextCallback)
		self.w.interpolateYSlider = Slider((10, 240, -10, 23),
							tickMarkCount=10,
							value = 0,
							maxValue = 2000,
							minValue = -1000,
							callback=self.interpolateYSliderCallback)
							
		self.w.scaleXTextBox = TextBox((10, 290, -10, 20), "Scale X (%):")
		self.w.scaleXEditText = EditText((100, 290, 60, 20),
							callback=self.scaleXEditTextCallback)
		self.w.scaleXSlider = Slider((10, 320, -10, 23),
							tickMarkCount=10,
							value = 100,
							maxValue = 200,
							minValue = 1,
							callback=self.scaleXSliderCallback)
		
		self.w.scaleYTextBox = TextBox((10, 360, -10, 20), "Scale Y (%):")
		self.w.scaleYEditText = EditText((100, 360, 60, 20),
							callback=self.scaleYEditTextCallback)
		self.w.scaleYSlider = Slider((10, 390, -10, 23),
							tickMarkCount=10,
							value = 100,
							maxValue = 200,
							minValue = 1,
							callback=self.scaleYSliderCallback)
							
		self.w.bar = ProgressBar((10, 430, -10, 16), sizeStyle='small')
			
		self.fontSourceList = self.w.popUpButtonSource.getItems()
		self.fontTargetList = self.w.popUpButtonTarget.getItems()
		
		self.w.buttonOK = Button((10, -30, 90, -10), "Apply",
							callback=self.buttonOKCallback)
		self.w.buttonCancel = Button((110, -30, -10, -10), "Close",
							callback=self.buttonCancelCallback)
		
		self.w.interpolateXEditText.set(self.interpolateXValue)
		self.w.interpolateYEditText.set(self.interpolateYValue)
		self.w.scaleXEditText.set(self.scaleXValue)
		self.w.scaleYEditText.set(self.scaleYValue)
		self.w.center()
		self.w.open()
		self.newFont = RFont()
		
	def foregroundSourceCheckBoxCallback(self, sender):
		self.w.popUpButtonSourceLayer.show(sender.get())
		self.w.textBoxSourceLayer.show(sender.get())
		self.useSourceLayer = sender.get()
		
	def foregroundTargetCheckBoxCallback(self, sender):
		self.w.popUpButtonTargetLayer.show(sender.get())
		self.w.textBoxTargetLayer.show(sender.get())
		self.useTargetLayer = sender.get()
		
	def interpolateXSliderCallback(self, sender):
		#print "slider edit!", sender.get()
		self.interpolateXValue = int(sender.get())
		self.w.interpolateXEditText.set(self.interpolateXValue)
	
	def interpolateYSliderCallback(self, sender):
		#print "slider edit!", sender.get()
		self.interpolateYValue = int(sender.get())
		self.w.interpolateYEditText.set(self.interpolateYValue)
	
	def scaleXSliderCallback(self, sender):
		#print "slider edit!", sender.get()
		self.scaleXValue = int(sender.get())
		self.w.scaleXEditText.set(self.scaleXValue)
	
	def scaleYSliderCallback(self, sender):
		#print "slider edit!", sender.get()
		self.scaleYValue = int(sender.get())
		self.w.scaleYEditText.set(self.scaleYValue)
		
	def interpol(self, gS, gT, valueX, valueY):
		gI = gS.copy()
		for i in range(len(gS)):
			for j in range(len(gS[i].points)):
				sourcePoint = self.allSourcePoints[i][j]
				targetPoint = self.allTargetPoints[i][j]
				gI[i].points[j].x = (sourcePoint[0] + ((targetPoint[0] - sourcePoint[0]) * valueX/1000)) * self.scaleXValue/100
				gI[i].points[j].y = (sourcePoint[1] + ((targetPoint[1] - sourcePoint[1]) * valueY/1000)) * self.scaleYValue/100
				gI.width = (gS.width + ((gT.width - gS.width) * valueX/1000)) * self.scaleXValue/100
		return gI
    
	def buttonOKCallback(self, sender):
		 #print "Ok"
		if len(self.newFont) != 0:
			barIncrement = 100/len(self.newFont)
		else:
			barIncrement = 100
		for g in self.newFont:
			if g:
				self.newFont.removeGlyph(g.name)
				self.w.bar.increment(barIncrement)
		self.w.bar.set(0)
		sourceFont = af[self.fontSourceIndex]
		targetFont = af[self.fontTargetIndex]
		
		#print "Master 1:", sourceFont
		#print "|--layer:", self.sourceLayerName
		#print "Master 2:", targetFont
		#print "|--layer:", self.targetLayerName
		 
		 #get the first glyph's name
		#firstGlyphName = targetFont.keys()[0]
		 #parse the target font's glyphs
		barIncrement = 100/len(targetFont)
		for gT in targetFont:
		 	#parse the source font's glyphs
			for gS in sourceFont:
		 		#if their names match, I want the targetLayer to be a copy of the sourceLayer
				if gT.name == gS.name:
					
					self.w.bar.increment(barIncrement)
					#Collect Master1 points
					self.allSourcePoints = []
					self.allSourcePointsLength = []
					if self.useSourceLayer:
						sourceLayer = gS.getLayer(self.sourceLayerName)
					else:
						sourceLayer = gS
				
					for i in range(len(sourceLayer)):
						self.allSourcePoints.append([])
						for j in range(len(sourceLayer[i].points)):
							
							self.allSourcePoints[i].append((sourceLayer[i].points[j].x, sourceLayer[i].points[j].y))
							self.allSourcePointsLength.append(j)
							
					#print allSourcePoints
							
					#Collect Master2 points
					self.allTargetPoints = []
					self.allTargetPointsLength = []
					if self.useTargetLayer:
						targetLayer = gT.getLayer(self.targetLayerName)
					else:
						targetLayer = gT
					
					for i in range(len(targetLayer)):
						self.allTargetPoints.append([])
						for j in range(len(targetLayer[i].points)):
							
							self.allTargetPoints[i].append((targetLayer[i].points[j].x, targetLayer[i].points[j].y))
							self.allTargetPointsLength.append(j)
					
					#print allTargetPoints
					if self.allSourcePointsLength != self.allTargetPointsLength:
						print 'Warning: Glyph ' + gS.name + ' not matching'
						#print self.allSourcePointsLength
						#print self.allTargetPointsLength
					else:
						gI = self.interpol(gS, gT, self.interpolateXValue, self.interpolateYValue)		
						self.newFont.newGlyph(gI.name)
						self.newFont[gI.name] = gI
						self.newFont[gI.name].update()
		self.newFont.update()
		self.w.bar.set(0)

		#self.w.close()
		 
	def buttonCancelCallback(self, sender):
		 #print "Cancel"
		 self.w.close()
		
	def popUpButtonSourceCallback(self, sender):		
		self.fontSourceIndex = sender.get()
		self.fontSourceName = self.fontSourceList[sender.get()]
		self.w.popUpButtonSourceLayer.setItems(af[self.fontSourceIndex].layerOrder)
		self.sourceLayerList = af[self.fontSourceIndex].layerOrder
		self.sourceLayerName = self.sourceLayerList[0]
		
		
	def popUpButtonTargetCallback(self, sender):		
		self.fontTargetIndex = sender.get()
		self.fontTargetName = self.fontTargetList[sender.get()]
		self.w.popUpButtonTargetLayer.setItems(af[self.fontTargetIndex].layerOrder)
		self.targetLayerList = af[self.fontTargetIndex].layerOrder
		self.targetLayerName = self.targetLayerList[0]

		
	def popUpButtonSourceLayerCallback(self, sender):
		self.sourceLayerIndex = sender.get()
		self.sourceLayerName = self.sourceLayerList[self.sourceLayerIndex]
		
	def popUpButtonTargetLayerCallback(self, sender):
		self.targetLayerIndex = sender.get()
		self.targetLayerName = self.targetLayerList[self.targetLayerIndex]
	
	def isInteger(self, string):
		try:
			return int(string)
		except ValueError:
			return 0
	
	def interpolateXEditTextCallback(self, sender):
		try:
			newValue = int(sender.get())
		except ValueError:
			if sender.get() == '-':
				newValue = 0
			else:
				newValue = 0
				sender.set(0)
		self.w.interpolateXSlider.set(newValue)
		self.interpolateXValue = newValue
		
	def interpolateYEditTextCallback(self, sender):
		try:
			newValue = int(sender.get())
		except ValueError:
			if sender.get() == '-':
				newValue = 0
			else:
				newValue = 0
				sender.set(0)
		self.w.interpolateYSlider.set(newValue)
		self.interpolateYValue = newValue
		
	def scaleXEditTextCallback(self, sender):
		try:
			newValue = int(sender.get())
		except ValueError:
			if sender.get() == '-':
				newValue = 0
			else:
				newValue = 0
				sender.set(0)
		self.w.scaleXSlider.set(newValue)
		self.scaleXValue = newValue
		
	def scaleYEditTextCallback(self, sender):
		try:
			newValue = int(sender.get())
		except ValueError:
			if sender.get() == '-':
				newValue = 0
			else:
				newValue = 0
				sender.set(0)
		self.w.scaleYSlider.set(newValue)
		self.scaleYValue = newValue


fontList = createFontList()
if fontList:
	InterpolateWindow()
else:
	print 'All open fonts must have familyName and styleName'