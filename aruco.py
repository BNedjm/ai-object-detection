import cv2 as cv


ARUCO_DICT = {
	"DICT_4X4_50": cv.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv.aruco.DICT_APRILTAG_36h11
}

aruco_type = "DICT_5X5_100"

aruco_dict = cv.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])

aruco_params = cv.aruco.DetectorParameters()

detector = cv.aruco.ArucoDetector(aruco_dict, aruco_params)

vid = cv.VideoCapture(0)

vid.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
vid.set(cv.CAP_PROP_FRAME_HEIGHT, 720)


while vid.isOpened():
    
	ret, img = vid.read()

	h, w, _ = img.shape

	width = 1000
	height = int(width*(h/w))
	img = cv.resize(img, (width, height), interpolation=cv.INTER_CUBIC)
 
	# corners, ids, rejected = detector.detectMarkers(img, arucoDict, parameters=arucoParams)
    # corners, ids, rejected = detector.detectMarkers(img, arucoDict)
	markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(img)


	# detected_markers = aruco_display(markerCorners, markerIds, rejectedCandidates, img)

	cv.aruco.drawDetectedMarkers(img, markerCorners, markerIds)

	cv.imshow("Image", img)

	key = cv.waitKey(1) & 0xFF
	if key == ord("q"):
	    break

cv.destroyAllWindows()
vid.release()