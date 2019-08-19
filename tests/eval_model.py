from keras.models import model_from_json
# paths to model.son and model.h5
model_dir = "C:\\Users\\Florian\\frag.extract.a\\extraction_model\\result_full_data\\model.json"
weights_dir = "C:\\Users\\Florian\\frag.extract.a\\extraction_model\\result_full_data\\model.h5"
# this is a quick way to load the model
json_file = open(model_dir, 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights(weights_dir)
# load test data
f = open("test_data.txt", 'r')
lines = f.readlines()
print(lines)