import SimpleITK as sitk

inputImagePath = "\\\\Mac\\Home\\Documents\\Python\\VSD\\Assignments\\Project\\Covid CT Data\\"
outputImagePath = "\\\\Mac\\Home\\Documents\\Python\\VSD\\Assignments\\Project\\Covid CT nrrd\\"
inputImageFileName = "volume-covid19-A-0002.nii.gz"
outputImageFileName = "volume-covid19-A-0002.nrrd"

reader = sitk.ImageFileReader()
reader.SetImageIO("NiftiImageIO")
pNum = "0"
while True:
    pNum = input("Patient #: (0 to Quit) ")
    if int(pNum) == 0:
        break
    else:
        inputImageFileName = "volume-covid19-A-" + pNum + ".nii.gz"
        outputImageFileName = "volume-covid19-A-" + pNum + ".nrrd"

        reader.SetFileName(inputImagePath + inputImageFileName)
        image = reader.Execute()

        writer = sitk.ImageFileWriter()
        writer.SetFileName(outputImagePath + outputImageFileName)
        writer.Execute(image)
        print('done')
print ("All done...")
