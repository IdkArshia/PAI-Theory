class Image:
    def __init__(self,pixelData):
        self.pixelData=pixelData

    def getCopy(self):
        return [row[:] for row in self.pixelData]

    def applyTransformation(self,transformationFunc):
        self.pixelData=transformationFunc(self.pixelData)


def flipHorizontal(pixelData):
    return [row[::-1] for row in pixelData]

def adjustBrightness(pixelData,brightnessValue):
    return [[pixel+brightnessValue for pixel in row] for row in pixelData]

def rotateNinetyDegrees(pixelData):
    rows=len(pixelData)
    cols=len(pixelData[0])
    return [[pixelData[rows-1-r][c] for r in range(rows)] for c in range(cols)]


class AugmentationPipeline:
    def __init__(self):
        self.steps=[]

    def addStep(self,transformFunc):
        self.steps.append(transformFunc)

    def processImage(self,originalImage):
        results=[]
        for func in self.steps:
            imgCopy=Image(originalImage.getCopy())
            imgCopy.applyTransformation(func)
            results.append(imgCopy.pixelData)
        return results

originalPixels=[[10,20,30],[40,50,60]]
img=Image(originalPixels)

pipe=AugmentationPipeline()
pipe.addStep(flipHorizontal)
pipe.addStep(lambda data:adjustBrightness(data,10))
pipe.addStep(rotateNinetyDegrees)

augmented=pipe.processImage(img)

for a in augmented:
    print(a)
