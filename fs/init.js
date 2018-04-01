// 電子レンジハック用ESP32開発ボード(๑´ڡ`๑)
// ESP32 Dev Board for hacking my STUPID microwave

// Load Mongoose OS API
load('api_gpio.js');
load('api_mqtt.js');
load('api_sys.js');
load('api_timer.js');

let wattageButton = 19;
let sec10Button = 18;
let minButton = 5;
let min10Button = 17;
let startButton = 16;
let stopButton = 4;
let topic = 'microwave';
let obj;

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
let i;
let sec10;
let min;
let min10;

// Receive commands from Alexa via AWS IoT MQTT broker and control microwave
MQTT.sub(topic, function(conn, topic, msg) {
  print('Topic: ', topic, 'message:', msg);
  obj = JSON.parse(msg);
  sec10 = obj.sec/10;
  min = obj.min;
  min10 = 0;
  
  // Power
  if(obj.power === 500){
    GPIO.write(wattageButton, 1);
    Sys.usleep(200000); //200msc
    GPIO.write(wattageButton, 0);
    Sys.usleep(200000); //200msc
  }else if(obj.power === 200){
    GPIO.write(wattageButton, 1);
    Sys.usleep(200000); //200msc
    GPIO.write(wattageButton, 0);
    Sys.usleep(200000); //200msc
    GPIO.write(wattageButton, 1);
      Sys.usleep(200000); //200msc
    GPIO.write(wattageButton, 0);
    Sys.usleep(200000); //200msc
  }
    //10-second button push
    for (i = 0; i < sec10; i++) {
      GPIO.write(sec10Button, 1);
      Sys.usleep(200000); 
      GPIO.write(sec10Button, 0);
      Sys.usleep(200000); 
    }  
    
    // Minute button push
    for (i = 0; i < min; i++) {
      GPIO.write(minButton, 1);
      Sys.usleep(200000); 
      GPIO.write(minButton, 0);
      Sys.usleep(200000); 
    }  

    // 10-minute button push
    for (i = 0; i < min; i++) {
      GPIO.write(min10Button, 1);
      Sys.usleep(200000); 
      GPIO.write(min10Button, 0);
      Sys.usleep(200000); 
    }  

    // Start button push
    if(sec10 !== 0 || min !== 0){
      GPIO.write(startButton, 1);
      Sys.usleep(200000); 
      GPIO.write(startButton, 0);
      Sys.usleep(200000); 
    }


}, null);

