# [temt6000 modular service](https://app.viam.com/module/coderscafe/temt6000)

This module implements the [rdk sensor API](https://github.com/rdk/sensor-api) in a `coderscafe:sensor:temt6000 model`.
With this model, you can read the Light Intensity and Illuminance from TEMT6000 sensor.

## Requirements

Please make sure that [I2C communication is enabled](https://docs.viam.com/operate/reference/prepare/rpi-setup/#enable-communication-protocols) on the device to which the sensor is connected. If you're unsure about the connection get more details from [here](https://codelabs.viam.com/guide/pomodoro-bot/index.html?index=..%2F..index#5).

## Build and Run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the [`coderscafe:sensor:temt6000` module](https://app.viam.com/module/coderscafe/temt6000).

## Configure your sensor

> [!NOTE]  
> Before configuring your sensor, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

* Navigate to the **Config** tab of your robot’s page in [the Viam app](https://app.viam.com/).
* Click on the **Components** subtab and click the `sensor` subtab.
* Select the `coderscafe:sensor:temt6000` model. 
* Enter a name for your sensor and click **Create**.
* On the new component panel, copy and paste the following attribute template into your sensor’s **Attributes** box:

```json
{
  "channel": channel-on-ADC-to-which-S-pin-is-connected
}
```
* Save and wait for the component to finish setup

> [!NOTE]  
> For more information, see [Configure a Robot](https://docs.viam.com/manage/configuration/).

### Attributes

The following attributes are available for `coderscafe:sensor:temt6000` sensor:

| Name | Type | Inclusion | Description |
| ---- | ---- | --------- | ----------- |
| `channel` | integer | **Required** |  Channel on ADS1115 ADC to which the S pin of TEMT6000 is connected |

### Example Configuration

```json
{
  "channel":0
}
```
