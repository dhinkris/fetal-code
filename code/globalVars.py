# Global Values
# This isn't great style, but we are being a bit hacky here.
width = 96
height = 96
n_channels = 1
n_classes = 2
cappedIterations = 1001
batchStepsBetweenSummaries = 100

stepsBeforeStoppingCriteria = 2000

imageBatchDims = (-1, width, height, n_channels)
labelBatchDims = (-1, width, height)