// In order to see this in File > Scripts menu, place in Photoshop's Presets/Scripts folder

var dim = 40 // dimension of sides for the square image

// set script units to pixels:
preferences.rulerUnits = Units.PIXELS
var baseDoc = app.documents.add(dim, dim) // create new document

// setup the text layer
var textLayer = baseDoc.artLayers.add()
textLayer.kind = LayerKind.TEXT
baseDoc.layers[1]
var text = textLayer.textItem
text.size = 36

text.contents = "A"


var bounds = textLayer.bounds
// bound[0], bound[1] is the top left corner
// -bounds resets image to top left corner
// -bounds[0] + dim/2 places left edge in center
// (bounds[2] - bounds[0]) / 2 figures out the center of the content in the layer (ie: the letter)
//      and subtracts that so the center of the layer content is in the center of the document
var xTranslate = (-bounds[0] + (dim / 2)) - ((bounds[2] - bounds[0]) / 2)
var yTranslate = (-bounds[1] + (dim / 2)) - ((bounds[3] - bounds[1]) / 2)
textLayer.translate(xTranslate, yTranslate)