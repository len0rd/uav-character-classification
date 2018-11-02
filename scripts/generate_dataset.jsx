// In order to see this in File > Scripts menu, place in Photoshops Presets/Scripts folder

var dim = 40 // dimension of sides for the square image

// set script units to pixels:
preferences.rulerUnits = Units.PIXELS


// create 30x30 document
var baseDoc = app.documents.add(dim, dim)

var textLayer = baseDoc.artLayers.add()
textLayer.kind = LayerKind.TEXT


var text = textLayer.textItem
text.contents = "W"
text.size = 24