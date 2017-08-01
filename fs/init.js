// Load Mongoose OS API
load('api_gpio.js');
load('api_mqtt.js');
load('api_sys.js');
load('api_timer.js');

// Map physical buttons with GPIOs
let wattageButton = 19;
let sec10Button = 18;
let minButton = 5;
let min10Button = 17;
let startButton = 16;
let stopButton = 4;

// MQTT
let topic = 'microwave';
let obj;
let i;
let sec10; //for 10-sec button
let min;
let min10; //for 10-min button

// Duration of button depression, 
let waitTime = 200000; //200 msec

// Initialize GPIOs
GPIO.set_mode(wattageButton, GPIO.MODE_OUTPUT);
GPIO.set_mode(sec10Button, GPIO.MODE_OUTPUT);
GPIO.set_mode(minButton, GPIO.MODE_OUTPUT);
GPIO.set_mode(min10Button, GPIO.MODE_OUTPUT);
GPIO.set_mode(startButton, GPIO.MODE_OUTPUT);
GPIO.set_mode(stopButton, GPIO.MODE_OUTPUT);
GPIO.write(wattageButton, 0);
GPIO.write(sec10Button, 0);
GPIO.write(minButton, 0);
GPIO.write(min10Button, 0);
GPIO.write(startButton, 0);
GPIO.write(stopButton, 0);

// Receive commands from Alexa via MQTT and control microwave
MQTT.sub(topic, function(conn, topic, msg) {
  print('Topic: ', topic, 'message:', msg);
  obj = JSON.parse(msg);
  sec10 = obj.sec10;
  min = obj.min;
  min10 = obj.min10;

  // Power
  if(obj.power === 500){
    GPIO.write(wattageButton, 1);
    Sys.usleep(waitTime);
    GPIO.write(wattageButton, 0);
    Sys.usleep(waitTime);
  }else if(obj.power === 200){
    GPIO.write(wattageButton, 1);
    Sys.usleep(waitTime);
    GPIO.write(wattageButton, 0);
    Sys.usleep(waitTime);
    GPIO.write(wattageButton, 1);
      Sys.usleep(waitTime);
    GPIO.write(wattageButton, 0);
    Sys.usleep(waitTime);
  }
    //10-second button push
    for (i = 0; i < sec10; i++) {
      GPIO.write(sec10Button, 1);
      Sys.usleep(waitTime);
      GPIO.write(sec10Button, 0);
      Sys.usleep(waitTime);
    }

    // Minute button push
    for (i = 0; i < min; i++) {
      GPIO.write(minButton, 1);
      Sys.usleep(waitTime);
      GPIO.write(minButton, 0);
      Sys.usleep(waitTime);
    }

    // 10-minute button push
    for (i = 0; i < min; i++) {
      GPIO.write(min10Button, 1);
      Sys.usleep(waitTime);
      GPIO.write(min10Button, 0);
      Sys.usleep(waitTime);
    }

    // Start button push
    if(sec10 !== 0 || min !== 0){
      GPIO.write(startButton, 1);
      Sys.usleep(waitTime);
      GPIO.write(startButton, 0);
      Sys.usleep(waitTime);
    }
}, null);
