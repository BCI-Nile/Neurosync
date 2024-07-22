## Neurosync
![image](https://github.com/BCI-Nile/Neurosync/blob/3eca9142e0e26492b058d7fba56f1d615877358e/logo.png)

Neurosync is Brain-Computer Interface (BCI), have become a viable means of bridging the gap between human cognitive capacities and machine interfaces, 

Decode speech patterns from our brain activities and interpret the neural signals to enable communication or interaction between the brain and computer

It helps severely paralyzed individuals or individuals with disabilities to be able to communicate with the outside world, as well as to overcome physical limitations

---

## Problem Statement
This project focuses on developing and implementing a Brain-Computer Interface (BCI) system that addresses their  challenges, with a specific emphasis on 
- covert speech communication, 
- emotion recognition, 
- and robotic control.

### Aim
A BCI system prototype that decodes brain EEG signals in order to interpret imagined speech, robotic control, and emotions.

### Objectives
- To design a BCI system that can interpret EEG signals for covert speech, emotion recognition and robotic control.
- To develop a prototype and test system to ensure accuracy and reliability
- To implement modification based on the testing result to improve performance

---
### Video Demonstration

Click thumbnail below 👇 to play video 

[![Video Title](https://img.youtube.com/vi/vKvDjvW-Kd0/0.jpg)](https://www.youtube.com/watch?v=vKvDjvW-Kd0)

---
### How to run
- Clone the repository
- Install the required libraries from `requirements.txt`
- Run the `main.py` file
- To get the uri for the raspberry pi, run the command below

```console
hostname -I
```

- Then copy the url and paste it in the `main.py` and `send_dummy_data.py` file 

```python
uri = "ws://copied_url:8765"
```

### How to test headset connection
- To test if the cortex headset is connected and working, run the `test_headset.py` file

### How to test raspberry pi connection
- To the connection between the raspberry pi and the computer using dummy data, run the `send_dummy_data.py` file

---
### Results
XGBoost result
![image](https://github.com/BCI-Nile/BCI-Project/assets/171136286/ef2fd52e-50e0-4f59-bfad-8620fbde0f01)







