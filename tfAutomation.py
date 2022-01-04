from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# write register name and location of file
print("Write File Name(File name including the Location of File)")
name = input() #'3 0.625mm bone alg.nrrd'
regName = name.split('\\')[-1]
# create a new 'Nrrd Reader'
covoidCTnrrd = NrrdReader(registrationName=regName, FileName=name)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
covoidCTnrrdDisplay = Show(covoidCTnrrd, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
covoidCTnrrdDisplay.Representation = 'Outline'
covoidCTnrrdDisplay.ColorArrayName = ['POINTS', '']
covoidCTnrrdDisplay.SelectTCoordArray = 'None'
covoidCTnrrdDisplay.SelectNormalArray = 'None'
covoidCTnrrdDisplay.SelectTangentArray = 'None'
covoidCTnrrdDisplay.OSPRayScaleArray = 'ImageScalars'
covoidCTnrrdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
covoidCTnrrdDisplay.SelectOrientationVectors = 'None'
covoidCTnrrdDisplay.ScaleFactor = 35.92968749999999
covoidCTnrrdDisplay.SelectScaleArray = 'ImageScalars'
covoidCTnrrdDisplay.GlyphType = 'Arrow'
covoidCTnrrdDisplay.GlyphTableIndexArray = 'ImageScalars'
covoidCTnrrdDisplay.GaussianRadius = 1.7964843749999997
covoidCTnrrdDisplay.SetScaleArray = ['POINTS', 'ImageScalars']
covoidCTnrrdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
covoidCTnrrdDisplay.OpacityArray = ['POINTS', 'ImageScalars']
covoidCTnrrdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
covoidCTnrrdDisplay.DataAxesGrid = 'GridAxesRepresentation'
covoidCTnrrdDisplay.PolarAxes = 'PolarAxesRepresentation'
covoidCTnrrdDisplay.ScalarOpacityUnitDistance = 1.1747109343482527
covoidCTnrrdDisplay.OpacityArrayName = ['POINTS', 'ImageScalars']
covoidCTnrrdDisplay.IsosurfaceValues = [-376.0]
covoidCTnrrdDisplay.SliceFunction = 'Plane'
covoidCTnrrdDisplay.Slice = 254

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
covoidCTnrrdDisplay.ScaleTransferFunction.Points = [-3024.0, 0.0, 0.5, 0.0, 2272.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
covoidCTnrrdDisplay.OpacityTransferFunction.Points = [-3024.0, 0.0, 0.5, 0.0, 2272.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
covoidCTnrrdDisplay.SliceFunction.Origin = [-12.551562500000017, -0.3515625, -190.49750000000003]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(covoidCTnrrdDisplay, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
covoidCTnrrdDisplay.RescaleTransferFunctionToDataRange(True, True)

# change representation type
covoidCTnrrdDisplay.SetRepresentationType('Volume')


# get opacity transfer function/opacity map for 'ImageScalars'
imageScalarsPWF = GetOpacityTransferFunction('ImageScalars')
imageScalarsPWF.Points = [-3024.0, 0.0, 0.5, 0.0, -580.2742919921875, 0.0, 0.5, 0.0, -330.606, 0.18125, 0.5, 0.0, -247.383, 0.0, 0.5, 0.0, 2272.0, 0.0, 0.5, 0.0]

# get color transfer function/color map for 'ImageScalars'
imageScalarsLUT = GetColorTransferFunction('ImageScalars')
imageScalarsLUT.ApplyPreset('Rainbow Desaturated', True)
imageScalarsLUT.RGBPoints = [-3024.0, 0.278431372549, 0.278431372549, 0.858823529412, -2266.6719999999996, 0.0, 0.0, 0.360784313725, -1924.830078125, 0.0, 0.4549019607843137, 0.6509803921568628, -1514.6400000000003, 0.0, 1.0, 1.0, -587.8400000000001, 0.0, 0.588235, 0.172549, -451.65700000000015, 0.0, 0.501961, 0.0, -383.5659999999998, 1.0, 1.0, 0.0, -315.47400000000016, 1.0, 0.380392, 0.10196078431372549, 1514.67, 0.419607843137, 0.0, 0.0, 2272.0, 0.878431372549, 0.301960784314, 0.301960784314]
# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(975, 794)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-59.07443409743513, -1156.6283105610426, -144.3572803384063]
renderView1.CameraFocalPoint = [-12.55155944824218, -0.3515624999999893, -190.49749851226795]
renderView1.CameraViewUp = [0.06635749951344566, 0.03711871945432829, 0.997105251678274]
renderView1.CameraParallelScale = 299.74656093981326

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).