# seeed_relay_board
Home assistant integration for [Seeed's 4-Channel SPDT Relay Raspberry Pi Hat](https://www.seeedstudio.com/Raspberry-Pi-Relay-Board-v1-0.html)
![relay board V1](https://media-cdn.seeedstudio.com/media/catalog/product/cache/9d0ce51a71ce6a79dfa2a98d65a0f0bd/h/t/httpsstatics3.seeedstudio.comimagesproduct103030029201.jpg)

It uses [relay_lib_seeed.py](https://github.com/johnwargo/seeed-studio-relay-board/blob/main/relay_lib_seeed.py) written by @johnwargo

Using this integration should be simple as cloning this repo in you custom_integration folder and adding following lines to your configuration.yaml:

```yaml
switch:
  - platform: seeed_relay_board
    ports:
      1: relay 1
      2: relay 2
      3: relay 3
      4: relay 4
```

By default this integration uses i2c adress 21, this can be changed at [line 19 of relay_lib_seed.py](https://github.com/toams/seeed_relay_board/blob/c592a2a731e9d8ddfe4bbae4d5fec38ebfeaeeb0/relay_lib_seeed.py#L19)

This integration is only tested on the [first version](https://www.seeedstudio.com/Raspberry-Pi-Relay-Board-v1-0.html) of the relay board (released in 2015) but the [newer version](https://www.seeedstudio.com/Raspberry-Pi-Relay-Board-v1-0.html) (released in 2021) should also work.
