# alexa-microwave

## Overview

This is the Mongoose OS app that controls a microwave via MQTT. 

For the microwave, you can hack one with photo relays or regular relays.
Basically what you need to do is to simulate the depression of button pushes.

Make sure you unplug your microwave before disassembly.

<b>STEP1</b>  Take the top cover and the front control panel off.
<p align="center">
  <img src="https://lh3.googleusercontent.com/BE_hNF1LdfZXLSORKBjyZ4sX-Q5cCuA5vYJMa3Ms7J1G19Rg67aRfXmXxem6URVo_q4dkNlWM5QxhxTx7_L3Z9Obl54fKXVdrk2YlRYrqKAWM6ukwxL7cO-SPoY3cDAIUV1ALT7Fj-BdOXPRUQHme6pCLuvKzMKGA7A6kZgBG9b77heRr-zXv7KsHjZy0ejyLCN7L5FXhfS89kzDdWL1u_PExzuEjH6GUvIcLMoDAOrkXnl1ALmCTBcDXXo51OFAmZlx4kEUX4vcnWOtgyi8uJXudMmGqD0SbWgEbjNm3olR_4H_ZVgBuamUzCSAKcwUY2kWJgeDljBeqfZdQ_GEEsWXKs54H14aiExc4HZXOeIB5GNJLd7O-ga-z0XPwGmvWNFJFUcNAgcXhYnff102ztobmHi8Dn4ASL8PeG64j_LPrcYl6zj7gCInAhRNe97w_kDbYhVSxHBsemNcwX18bT2qADVJRk5SIjx5kMXa9dyUVaRIJMeErjd5R4K2VGxrnJMCblThsSLYljV8hAtrnGbExMe2BErSSpujWO7sIUaFGaSTqskhf8Di7PZQ74ADobW62FuyeipnapCXOkg_fM5XAbnrd5G8xQPFi17VP4WWq52Na3bATtaP=w2204-h1652-no" width="50%">
</p>

<p align="center">
  <img src="https://lh3.googleusercontent.com/mriSR35jLShd8fLAe8ANZAWlbBPVW5MOnJ9BMCKUuRRQNaBwPvZpt0hgEeorBvg9QAQZIplv3gR73iG7lZhrnzmA1FAy2BwJSfehjFmjS_oSuJNrekRj9b9jl4D5QCp4Md0lJfQbdDWMklZLUENwhqb623FrVbup89WyTleXPIga9wITCiva8GkKhZsRmE2JX0w78sEMnDP6tyvyZYGy536Cd_QR4vxQL0toWpN7CgEGFcujzJsdHvbzvk2WIrE3uImkQU83FlozmAXnI4I2YcTmoQWnKY8dx36RKF1povppRXFI0UZSK_jtDtYqHOjjpbcv2MnxYB1hcJlBojidnM_viBNIBJ4CtW5OY-3wJLe0CVlV3X00E3f7LZMeMocEjgJBqv3SH-D9DiH__su20zdDGjwfkw7qlDjhtp16H7E3zApPem0EkTpSBCb64uCdtq1SpL3OvoktUN4VGhbPNVAg-eOrZQydyR9ujRFpu5t2UJCspuGA3hlHHQAG_Y3SmIT05kI-20IonUVKldoyAp89JjNisFm0MDOyow21_rrfUPTiWCMT5IS9Z1OjShBM3WRfPdmjImqYS16zaNwS0qKoUM6PCKX2m3cQDNPh-0k2JkhfcukVlktB=w2204-h1652-no" width="50%">
</p>



<b>STEP2</b> Find ribbon cables that connect buttons and the control panel board.

<p align="center">
  <img src="https://lh3.googleusercontent.com/-KhV_hQBzJ6ozUtW5YJnMMw94_BmtnS5E0gCOQHeYMsrLpV--dsHmkUVeIBtyEaAMmLrdqvX1XkFZaEBC_1oWlazhUpH9Vuh8Mq4HwzFtaQM5aE_yliPoqiJlZcIg0Lce_O7VYJHqJFVz55HHmQ5-dF_q2-kEGuZJQvQI8sf9Qe1unrQskd2UXYYKOaihWhM4QMEFRCZNEdem6-WjFXlL1ENhWL1D1GMTr0xHwc0Ak_jxm-SYb0HOIjGMjLurikp__8Bc_va_BRr1-D7PRVwoUX3sWIIEn3UlapBOFP-bWk4fTyCwlXjhVpXd9jfMEYlZOc5S0QmrYhOppTiquPly_fxYxu6iFsBLGd9kxr4v0SBHkPsjDZVI4hia4DkXyN53LvG4TVxTBg6MfD6RFf74TuBcuUfZ61KLXnupbS50vneRyz6LbXhGhMaZdWRFzhWFS7gNh9d75zyNbGLSmYXhdOcZRey9gUYMt1w3sZK4WM_y0uTSlZmgWuKH4wCCYrB4XLHy6bwMils_gZmkws1PTq8og9q0zZ9PAnGLNNSfdjUOOpL4tPthE2AGo2Y0asslZNUDiBkmVUWib8nKRbhhUOjGCT-4Gkon5txf6cDSPLpNt8hcxv-hF4Q=w2204-h1652-no" width="50%">
</p>

<b>STEP3</b> Solder jumber cables to the board so that you have another set of "ribbon cables".

<p align="center">
  <img src="https://lh3.googleusercontent.com/4cRpeme5jobsFXDH6cBqykkKQJn0k03jZ9RW07PbXteYdOOpsA_1o0ydgZ2V14Pnwsk_SZJcUV1T8u84jjSxqMO9-f6Llwd_e7nGNnD3Z-FZJ2meBC1g6aIjW8_orN5Xamm9HWffkTxi69U8LKoZJlGN7U-HqLn31dmi6Ra6qm4uBOY9LCGq40mlkvMTG7QG69bItSlwUJ13Yo5XtJjmlxwiMnvT5I3OpKYNNqowlfLIoecKetvCkZZ2WUd5jrj4jZjt04MJ7rn_Ww2vdohalmYhLsco0HhyqtlMzsuI9FVVtqfUE38pnOk_72U-57Ng2Hzd0ePpbLmOysMTXjXL6RErV2R1Zr-H1dT1eHUmmc7FRg3zRKuRQIE-o6oQYiA7HaGUU0ZO8ov0rbZFuXoDqbUirccqyIRpFih3_LL703uSnXU0iPLykimGwRqjD6emvZTIt6fsp2lf_odEFVinGVFwRv8WbnpJQbg9OK8X7BpLimxphxuGalHEWf0SS-WxCgE5MG987QGKYQ1yQC0RicDc860Qsp__b8SIMG2cyrJR2tEbt0u0cn09J3xp1ANlUnvX-hhXDZff7Xod3a8tluqwxRMnp0AZZtKnvpFe99CHgW5DpV5cKsHZ=w2204-h1652-no" width="50%">
</p>

<b>STEP4</b> Short every combination of the jumber cables and find which combination does min button push, 10 sec button push, start button push, etc.

<p align="center">
  <img src="https://lh3.googleusercontent.com/ugORoaUIAZ7M_erG5CdNhrwu3u-MKIcUBnh9A0cG1pnO3iTZHJ0fTr8CaFwh8iDry3G7-eyJIOeOlSIBS0WVEe9beQ9NLv1r8WZNM7upl115ssgGLc5Vx70s0dKJ5IxoHrwD3uYsR9TE4aZzLhp1anX-qz4iJprB-719J2OtVLpwcKfQEqhkWjjPQf_zDHc4pWMLiSYTedrmsffqGmrcoNMSsEYlYu0lHRj0wlm_plu-RnVIk-Kq6VqKsbA8p3UzEmTMtOGA-xoGbh8uAh3X1tJlPr65svGCq2fljUK-VL6anTB0enHz72gmOyN6j5GGBx6Sf2hRVNDzZNb9Q8KqWSP9Z9DkDY7G4XNl3v2Q-5xD6g0l3TO4Y3sGB1JnY31pEuE2eyxOC2EIqQYN5nlLgDu1hDLIysjivNNgv057UtoS36vRIRREfVDQYDQet3kt1LvgirhDQ7aen5ak2issgKoAPBmFciBMFt1NShHr-WaPrkVJ-RwSXenkMKrgWXzlt50--yKzWaP2vz3jlaJdj3uyTWRDZtppyMXEEexbFGBSz6n2QLbKHYoqu1YjCEPtwRjyTagF00Mj66YQ2a-Slul3ZmLkkuPFdQ70bk1b2SiBiufQluD43nmb=w2204-h1652-no" width="50%">
</p>

<b>STEP5</b> Connect jumber cables and ESP32 via photo relays.

<p align="center">
  <img src="https://lh3.googleusercontent.com/BuBSRjUM845-wHAII7dv8vCTvwjE0z39D_MgRFZIv36Pl7yOiglLm5A-bVN0VrsVidXi9FTIiRqgIUl6d6estWSArZl0HN87mkgPbd1yOfV4nWqu4G0QMDr2IoRSnivdF_HxKIx-BySrkMFVQPZo_hN-OO6jImI90xMFFJn-NBJj26xj-5OYOmiYob_waEk5y67rm1by9gDUlcbSmJclYA_HrI5fQDGGyGlJAOB0iSWwXbaSGTFc4NaQCapGWAwP9sw2HB7OwZuqWl2Qk4ni99y9fgoIHd8NlRWrSsdDoOMQ3iLyqxn9Wv0-IH2Gu0Tt1Bs_rFAmnZQHBxIInFFiu5-gvPxtSm4HN7uEph9EjOzZaI_NsJkK8XnpSnmV1ZLwYNKzrFXDxUdWWSaX_ORD6hgs8b-3ly0h38cc5Ta_ebz3TNekQqki0rne5Sl5IqQKvmkQRfCoTfMu_UzdExaYrd2onzNZVY647LRA1QtoM8QQ-i_hTLlOuqh-2zeYtLpedLZRYyXDGZnALJ03hsvxsIcgsp46Yf6AeEpE1TSSW0l6g6A-LZ9hXALROc9-xNNn8lnovvjFKfXA_23niiL7RIZKT2jAH4cpED-uw-uWYPeK2oSOaVSbf339=w2204-h1652-no" width="50%">
</p>

<b>STEP6</b> Build an Alexa skill which sends control commands via MQTT.

e.g. topic: microwave, {"power": 500, "min": 3}


## How to install this app

- Install and start [mos tool](https://mongoose-os.com/software.html)
- Switch to the Project page, find and import this app, build and flash it:

<p align="center">
  <img src="https://mongoose-os.com/images/app1.gif" width="75%">
</p>
