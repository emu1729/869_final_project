from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

# dimensions of our images.
img_width, img_height = 150, 150

nb_train_samples = 8000
nb_validation_samples = 2000
epochs = 10
batch_size = 1

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.load_weights('first_try.h5')

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

test_datagen = ImageDataGenerator(rescale=1. / 255)

data_dir = 'training_data/colorization.eecs.berkeley.edu/imgs/validation/'

data_generator = test_datagen.flow_from_directory(
    data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size, shuffle = False)

results = model.predict_generator(
    data_generator, steps = 4000, max_queue_size=10, workers=1, use_multiprocessing=False, verbose=0)

results_cr = results[:2000]
results_gt = results[2000:]

print(sum(i > 0.5 for i in results_cr))
print(sum(i > 0.5 for i in results_gt))

filenames_cr = data_generator.filenames[:2000]
filenames_gt = data_generator.filenames[2000:]

def findDict(results, filenames):
	d = {}
	for i in range(len(filenames)):
		d[filenames[i]] = results[i][0]
	return d

cr_dict = findDict(results_cr, filenames_cr)
gt_dict = findDict(results_gt, filenames_gt)

all_dict = findDict(results, data_generator.filenames)

sorted_all_dict = sorted(all_dict.iteritems(), key=lambda (k,v): (v,k))
sorted_cr_dict = sorted(cr_dict.iteritems(), key=lambda (k,v): (v,k))
sorted_gt_dict = sorted(gt_dict.iteritems(), key=lambda (k,v): (v,k))

print(sorted_cr_dict[1990:])
print(sorted_gt_dict[:10])

def findIntDict(name_dict):
	d = {}
	for k, v in name_dict.items():
		new_k = int(k[3:8])
		d[new_k] = v
	return d

cr_int = sorted(findIntDict(cr_dict).iteritems())
gt_int = sorted(findIntDict(gt_dict).iteritems())

count = 0
for i in range(len(cr_int)):
	if cr_int[i][1] > gt_int[i][1]:
		count = count + 1
		print(cr_int[i][0])

print(count)

data_dir = 'training_data/colorization.eecs.berkeley.edu/imgs/training/'

data_generator_1 = test_datagen.flow_from_directory(
    data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size, shuffle = False)

results_1 = model.predict_generator(
    data_generator_1, steps = 16000, max_queue_size=10, workers=1, use_multiprocessing=False, verbose=0)

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

all_dict_1 = findDict(results_1, data_generator_1.filenames)
z = merge_two_dicts(all_dict, all_dict_1)
sorted_all_dict_z = sorted(z.iteritems(), key=lambda (k,v): (v,k))
print(sorted_all_dict_z[18000:])




