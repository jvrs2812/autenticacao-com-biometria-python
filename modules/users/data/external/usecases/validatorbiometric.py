import os
import cv2


class ValidatorBiometric:

    @staticmethod
    def validator(pathInitial, pathUser):
        score = 0
        kp1, kp2, mp = None, None, None

        target_image = cv2.imread(
            "./biometrias/"+os.path.basename(pathInitial))

        source_image1 = cv2.imread(
            "./biometrias/"+os.path.basename(pathUser))

        sift = cv2.SIFT_create()
        kp1, des1 = sift.detectAndCompute(source_image1, None)
        kp2, des2 = sift.detectAndCompute(target_image, None)
        matches = cv2.FlannBasedMatcher(
            dict(algorithm=1, trees=10), dict()).knnMatch(des1, des2, k=2)

        mp = []
        for p, q in matches:
            if p.distance < 0.1 * q.distance:
                mp.append(p)
                keypoints = 0
                if len(kp1) <= len(kp2):
                    keypoints = len(kp1)
                else:
                    keypoints = len(kp2)

                if len(mp) / keypoints * 100 > score:
                    score = len(mp) / keypoints * 100
                    result = cv2.drawMatches(
                        source_image1, kp1, target_image, kp2, mp, None)
                    result = cv2.resize(result, None, fx=1, fy=1)
                    return True
                else:
                    return False
