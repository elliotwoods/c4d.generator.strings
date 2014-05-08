import c4d
import os
import random

from c4d import Vector, plugins, bitmaps, gui

lineCount = 500

VAR_Count = 1001
VAR_RandomSeed = 1002
VAR_Scale = 1003

def randomCubePoint():
	x = random.uniform(-1.0, 1.0)
	y = random.uniform(-1.0, 1.0)

	face = random.randint(0, 5)

	if face == 0:
		return Vector(x, y, -1.0)
	elif face == 1:
		return Vector(x, y, +1.0)
	elif face == 2:
		return Vector(x, -1.0, y)
	elif face == 3:
		return Vector(x, +1.0, y)
	elif face == 4:
		return Vector(-1.0, x, y)
	elif face == 5:
		return Vector(+1.0, x, y)

def scalarMul(v1, v2):
	return Vector(v1.x * v2.x, v1.y * v2.y, v1.z * v2.z)

class GenerateStringsSpline(plugins.ObjectData):
	"""GenerateStringsSpline"""

	def Init(self, node):
		data = node.GetDataInstance()
		data.SetLong(VAR_Count, 200)
		data.SetLong(VAR_RandomSeed, 0)
		data.SetVector(VAR_Scale, Vector(1,1,1))
		return True

	def GetVirtualObjects(self, op, hierarchyhelp):
		spline = c4d.SplineObject(lineCount * 2, c4d.SPLINETYPE_LINEAR)

		data = op.GetDataInstance()
		random.seed(data.GetLong(VAR_RandomSeed))
		count = data.GetLong(VAR_Count)
		size = data.GetVector(VAR_Scale)

		for i in range(0, count):
			spline.SetPoint(i * 2, scalarMul(randomCubePoint(), size))
			spline.SetPoint(i * 2 + 1, scalarMul(randomCubePoint(), size))

		return spline

if __name__ == "__main__":
	bmp = bitmaps.BaseBitmap()
	dir, file = os.path.split(__file__)
	bitmapFilename = os.path.join(dir, "res", "kc_letter.png")

	result = bmp.InitWith(bitmapFilename)
	if not result:
		print "Error loading bitmap icon"
	
	result = plugins.RegisterObjectPlugin(id=1032112, str="Generate Strings Spline", info=c4d.OBJECT_GENERATOR, g=GenerateStringsSpline, description="GenerateStringsSpline", icon=bmp)
	
	gitCommitFilename = os.path.join(dir, "res", "git_commit.txt")
	gitCommitFile = open(gitCommitFilename, 'r')

	print "Generate Strings plugin initialised build: ", gitCommitFile.read()