![](./.github/banner.png)

<p align="center">
  A Python script to parse Fortinet products serial numbers, and detect the associated model and revision.
  <br>
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/p0dalirius/ParseFortinetSerialNumber">
  <a href="https://twitter.com/intent/follow?screen_name=podalirius_" title="Follow"><img src="https://img.shields.io/twitter/follow/podalirius_?label=Podalirius&style=social"></a>
  <a href="https://www.youtube.com/c/Podalirius_?sub_confirmation=1" title="Subscribe"><img alt="YouTube Channel Subscribers" src="https://img.shields.io/youtube/channel/subscribers/UCF_x5O7CSfr82AfNVTKOv_A?style=social"></a>
  <br>
</p>


![](./.github/exemple.png)

## Example

```
$ ./ParseFortinetSerialNumber.py FG100EPA12345678
[+] Detected FortiGate 100E (FG100E-PA12345678)
```

## Source of information

There is two main sources of information:

### The docs

In Fortinet products datasheets (available in [./docs/](./docs/)), we can see what the device looks like and its technical characteristics. 

![](./.github/docs.png)

### Ebay

Another great source of information is [ebay.com](https://www.ebay.com/). This is very useful to find serial number photos and know the serial number pattern for the given model: 

![](./.github/ebay.png)

You can find many of the photos extracted from ebay in [./photos/](./photos/).

## Contributing

Feel free to open a pull requests if you want to add other serial numbers, documentations or screenshots we don't have yet.
