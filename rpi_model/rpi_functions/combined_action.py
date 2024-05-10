#combined madness!!
#Rpi Interface
import cv2
import time
from picamera2 import Picamera2
import onnxruntime as ort
import numpy as np
import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pwmPin1=18
pwmPin2=12
GPIO.setup(pwmPin1,GPIO.OUT)
GPIO.setup(pwmPin2,GPIO.OUT)
pwm1=GPIO.PWM(pwmPin1,50)
pwm2=GPIO.PWM(pwmPin2,50)
pwm1.start()
pwm2.start()
SIZE=128


categories=['apoderus_javanicus', 'aulacaspis_tubercularis', 'ceroplastes_rubens', 'cisaberoptus_kenyae', 'dappula_tertia', 
'dialeuropora_decempuncta', 'erosomyia_sp', 'icerya_seychellarum', 'ischnaspis_longirostris', 'mictis_longicornis', 
'neomelicharia_sparsa', 'normal', 'orthaga_euadrusalis', 'procontarinia_matteiana', 'procontarinia_rubus', 'valanga_nigricornis']
picam2= Picamera2()
#picam2.preview_configuration.main.size(1280,720)
#In case of the above command picam tuple is not callable
picam2.preview_configuration.main.format="RGB888"
#picam2.preview_configuration.align()
#picam2.configure("preview")
picam2.start()
fps=0
pos=(130,160)

try:
    while True:
        im=picam2.capture_array()
        cv2.imshow("camera",im)
        for i in range(1,11):
            pwm1.changeDutyCycle(i)
            
    
            #print im([0,0]) gives data on single pixel
    
            # Change shapes and types to match model
            #input1 = np.zeros([1, 128, 128,3], np.float32)

            # path="C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\screen\\images\\black\\8d8e558b-39f7-4bdb-b72b-2dcc23ad39d1.png"
            # img=cv2.imread(path)
            im=picam2.capture_array()
            cv2.imshow("camera",im)
            img = np.float32(im)
            img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            im=cv2.resize(img_rgb,(SIZE,SIZE))
            data=[]
            data.append(im)

            data_arr=np.array(data)
            data_arr=data_arr/255


            # Start from ORT 1.10, ORT requires explicitly setting the providers parameter if you want to use execution providers
            # other than the default CPU provider (as opposed to the previous behavior of providers getting set/registered by default
            # based on the build flags) when instantiating InferenceSession.
            # Following code assumes NVIDIA GPU is available, you can specify other execution providers or don't include providers parameter
            # to use default CPU provider.
            sess = ort.InferenceSession("model1.onnx")#, providers=["CUDAExecutionProvider"])
            model_inputs = sess.get_inputs()

            for input in model_inputs:
                print(f"Input Name: {input.name}, Shape: {input.shape}")

            # Set first argument of sess.run to None to use all model outputs in default order
            # Input/output names are printed by the CLI and can be set with --rename-inputs and --rename-outputs
            # If using the python API, names are determined from function arg names or TensorSpec names.
            results_ort = sess.run(None, {"x": data_arr})
            print(results_ort)
            print(categories[np.argmax(results_ort)])

            if cv2.waitKey(1)==ord("q"):
                picam2.close()
                break

            time.sleep(0.1)
            # for j in range(1,7):
            #     pwm2.changeDutyCycle(j)
            #     time.sleep(0.1)
            # pwm2.changeDutyCycle(1)
            pwm1.changeDutyCycle(i+0.5)
            im=picam2.capture_array()
            cv2.imshow("camera",im)
            img = np.float32(im)
            img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            im=cv2.resize(img_rgb,(SIZE,SIZE))
            data=[]
            data.append(im)

            data_arr=np.array(data)
            data_arr=data_arr/255


            # Start from ORT 1.10, ORT requires explicitly setting the providers parameter if you want to use execution providers
            # other than the default CPU provider (as opposed to the previous behavior of providers getting set/registered by default
            # based on the build flags) when instantiating InferenceSession.
            # Following code assumes NVIDIA GPU is available, you can specify other execution providers or don't include providers parameter
            # to use default CPU provider.
            sess = ort.InferenceSession("model1.onnx")#, providers=["CUDAExecutionProvider"])
            model_inputs = sess.get_inputs()

            for input in model_inputs:
                print(f"Input Name: {input.name}, Shape: {input.shape}")

            # Set first argument of sess.run to None to use all model outputs in default order
            # Input/output names are printed by the CLI and can be set with --rename-inputs and --rename-outputs
            # If using the python API, names are determined from function arg names or TensorSpec names.
            results_ort = sess.run(None, {"x": data_arr})
            print(results_ort)
            print(categories[np.argmax(results_ort)])

            if cv2.waitKey(1)==ord("q"):
                picam2.close()
                break

            time.sleep(0.1)
        for i in range(10,1,-1):
            pwm1.changeDutyCycle(i+0.5)
            im=picam2.capture_array()
            cv2.imshow("camera",im)
            img = np.float32(im)
            img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            im=cv2.resize(img_rgb,(SIZE,SIZE))
            data=[]
            data.append(im)

            data_arr=np.array(data)
            data_arr=data_arr/255


            # Start from ORT 1.10, ORT requires explicitly setting the providers parameter if you want to use execution providers
            # other than the default CPU provider (as opposed to the previous behavior of providers getting set/registered by default
            # based on the build flags) when instantiating InferenceSession.
            # Following code assumes NVIDIA GPU is available, you can specify other execution providers or don't include providers parameter
            # to use default CPU provider.
            sess = ort.InferenceSession("model1.onnx")#, providers=["CUDAExecutionProvider"])
            model_inputs = sess.get_inputs()

            for input in model_inputs:
                print(f"Input Name: {input.name}, Shape: {input.shape}")

            # Set first argument of sess.run to None to use all model outputs in default order
            # Input/output names are printed by the CLI and can be set with --rename-inputs and --rename-outputs
            # If using the python API, names are determined from function arg names or TensorSpec names.
            results_ort = sess.run(None, {"x": data_arr})
            print(results_ort)
            print(categories[np.argmax(results_ort)])

            if cv2.waitKey(1)==ord("q"):
                picam2.close()
                break

            time.sleep(0.1)
            # for j in range(1,7):
            #     pwm2.changeDutyCycle(j)
            #     time.sleep(0.1)
            # pwm2.changeDutyCycle(1)
            pwm1.changeDutyCycle(i)
            im=picam2.capture_array()
            cv2.imshow("camera",im)
            img = np.float32(im)
            img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            im=cv2.resize(img_rgb,(SIZE,SIZE))
            data=[]
            data.append(im)

            data_arr=np.array(data)
            data_arr=data_arr/255


            # Start from ORT 1.10, ORT requires explicitly setting the providers parameter if you want to use execution providers
            # other than the default CPU provider (as opposed to the previous behavior of providers getting set/registered by default
            # based on the build flags) when instantiating InferenceSession.
            # Following code assumes NVIDIA GPU is available, you can specify other execution providers or don't include providers parameter
            # to use default CPU provider.
            sess = ort.InferenceSession("model1.onnx")#, providers=["CUDAExecutionProvider"])
            model_inputs = sess.get_inputs()

            for input in model_inputs:
                print(f"Input Name: {input.name}, Shape: {input.shape}")

            # Set first argument of sess.run to None to use all model outputs in default order
            # Input/output names are printed by the CLI and can be set with --rename-inputs and --rename-outputs
            # If using the python API, names are determined from function arg names or TensorSpec names.
            results_ort = sess.run(None, {"x": data_arr})
            print(results_ort)
            print(categories[np.argmax(results_ort)])

            if cv2.waitKey(1)==ord("q"):
                picam2.close()
                break

            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    cv2.destroyAllWindows()











