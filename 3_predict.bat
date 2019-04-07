rmdir /s /q "tensorflow/src/1notrain"
rmdir /s /q "tensorflow/src/2lrain"
rmdir /s /q "tensorflow/src/3mrain"
rmdir /s /q "tensorflow/src/4hrain"
rmdir /s /q "tensorflow/src/5vhrain"
mkdir "tensorflow/src/1notrain"
mkdir "tensorflow/src/2lrain"
mkdir "tensorflow/src/3mrain"
mkdir "tensorflow/src/4hrain"
mkdir "tensorflow/src/5vhrain"
xcopy /s "satconcat" "tensorflow\src\1notrain"
cd tensorflow/src
python build_image_datav1.py
cd ../..
del "testtfrecord\validation*"
copy "tensorflow\src\validation*" "testtfrecord"
python  C:/Users/OFF-PC/Desktop/cnnsat/tf_tensor/models/research/slim/classify_image.py --num_classes 6 --infile C:/Users/OFF-PC/Desktop/cnnsat/testtfrecord/validation-00000-of-00001 --model_name inception_v3 --checkpoint_path C:/Users/OFF-PC/Desktop/cnnsat/models/tmr/inception_v3/model.ckpt-40000 --outfile C:/Users/OFF-PC/Desktop/cnnsat/out1.txt --tfrecord
python  C:/Users/OFF-PC/Desktop/cnnsat/tf_tensor/models/research/slim/classify_image.py --num_classes 6 --infile C:/Users/OFF-PC/Desktop/cnnsat/testtfrecord/validation-00000-of-00001 --model_name inception_v3 --checkpoint_path C:/Users/OFF-PC/Desktop/cnnsat/models/2day/inception_v3/model.ckpt-45000 --outfile C:/Users/OFF-PC/Desktop/cnnsat/out2.txt --tfrecord
python  C:/Users/OFF-PC/Desktop/cnnsat/tf_tensor/models/research/slim/classify_image.py --num_classes 6 --infile C:/Users/OFF-PC/Desktop/cnnsat/testtfrecord/validation-00000-of-00001 --model_name inception_v3 --checkpoint_path C:/Users/OFF-PC/Desktop/cnnsat/models/3day/inception_v3/model.ckpt-34000 --outfile C:/Users/OFF-PC/Desktop/cnnsat/out3.txt --tfrecord
python cnnsat.py > prediction.txt