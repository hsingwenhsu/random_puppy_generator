# random_puppy_generator
This is a python project that generates puppies of different looks!
## Usage
```
$ python3 dog.py
```
## Code explained
1. Pasting the mouth of the puppy onto an empty puppy body.
```python
for i in range(dog_num):
    dog_list[i] = paste_mouth(dog_list[i], mouth)
```
2. function `paste_mouth` explained
- I drew an image of the mouth on a piece of paper and then post processed it so that it looks right on the puppy's face.
- Post processing:
    ```python
    mouth = cv2.bitwise_not(mouth)
    mouth = cv2.resize(mouth, (int(mouth.shape[1]//4.5), int(mouth.shape[0]//4.5)), cv2.INTER_AREA)
    kernel = np.ones((3, 3))
    mouth = cv2.dilate(mouth, kernel, iterations=1)
    mouth = cv2.bitwise_not(mouth)
    ```
3. Different eyes are drawn according to the generated randomly generated number

## Demo
- Result of the program:
![alt text](demo.png = 400x)
