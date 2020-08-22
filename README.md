# Visual Dataset Builder

<details open>
<summary> <b>Brief Review<b></summary>

[<img src="https://img.shields.io/badge/-Python-FFD43B?style=for-the-badge&logo=python&logoColor=white&labelColor=4B8BBE" />]()
[<img src="https://img.shields.io/badge/-OpenCV-001010?style=for-the-badge&logo=python&logoColor=white&labelColor=0000AB" />]()

<p align = "center">

A handy python script for building custom image datasets. 

You just configure the xml file for the requested parameters and run the application.  This is very useful application for building images dataset directly from your computer and can also change directly the resolution and colorspace of the output images.

This application works on videos and usb camera input, you could change from manual mode to automatic mode and start building your dataset.

<p align = "center">
  <img src = "https://github.com/issaiass/VisualDatasetBuilder/blob/master/imgs/xmlfile.PNG?raw=true">
</p>


</details>

<details open>
<summary> <b>Installation<b></summary>

For installing the application there are only two prerequisites that are:
[<img src="https://img.shields.io/badge/-OpenCV-001010?style=for-the-badge&logo=python&logoColor=white&labelColor=0000AB" />]()
[<img src="https://img.shields.io/badge/-Numpy-306998?style=for-the-badge&logo=python&logoColor=FFE873&labelColor=4B8BBE" />]()

Having installed python do the following commands `workon <your_virtual_env>` if you have a virtualenvironment installed, if not, continue to install the requirements by `pip install -r requirements.txt` and that's it!.

</details>


<details open>
<summary> <b>Usage<b></summary>

##### Manual Mode

- Open the XML File and configure:
  - Configure 0 for `frequency`.
  - Specify the dataset folder in `dsfolder`.
  - Leave in blank or 0 for the camera, but you culd also  specify the path of the video file in `videopath`.
  - Specify the size of the image in the `width` and `height` paramenters.
  - Leave in blank or specify the `colorspace`.

  - NOTE:  Mandatory paramenters are `frequency`, `dsfolder` and `width`, `height`
  - execute the application `python dataset_builder.py --xml config.xml`
  - Click on the present window and for capture a frame press SPACEBAR.

##### Automatic Mode

- Open the XML File and configure:
  - Configure a number greather than 0 (i.e. could be 0.9) for `frequency`.
  - Specify the dataset folder in `dsfolder`.
  - Leave in blank or 0 for the camera, but you culd also  specify the path of the video file in `videopath`.
  - Specify the size of the image in the `width` and `height` paramenters.
  - Leave in blank or specify the `colorspace`.
  - NOTE:  Mandatory paramenters are `frequency`, `dsfolder` and `width`, `height`
  - execute the application `python dataset_builder.py --xml config.xml`
  - See the window and check the instructions if you are in automatic mode.  If you are in automatic mode, the application will construct the captures and close when the video.

##### Inserting in your application

In resume, if you want to use it in your own application, as a visual dataset constructor, you have to call/import the file and specify the parameters, please refer to `dataset_builder.py` for a better understanding.

~~~
from VisualDS.Builder import VisualDSBuilder
.
.
.
visds = VisualDSBuilderf(<FREOQUENCY>, <OUTPUT_IMAGES_FOLDER>, <PATH_OF_THE_VIDEO__0_FOR_CAMERA>, <(WIDTH,HEIGHT)>, <COLOR_SPACE>)
visds.run()
~~~

</details>

<details open>
<summary> <b>Results<b></summary>

You could see the results on this youtube video.  

<p align="center">

<img src= "https://img.youtube.com/vi/JcSQ-o2mbb0/0.jpg" >

</p>

The video only shows how to use the application, not the explanation of the camera calibration.

Below more images of the application:

<p align = "center">
  <img src = "https://github.com/issaiass/VisualDatasetBuilder/blob/master/imgs/outputfolder.PNG?raw=true">
  <img src = "https://github.com/issaiass/VisualDatasetBuilder/blob/master/imgs/automode.PNG?raw=true">
  <img src = "https://github.com/issaiass/VisualDatasetBuilder/blob/master/imgs/autodataset.PNG?raw=true">
</p>


</details>

<details open>
<summary> <b>Issues<b></summary>

Currently are no issues present.

</details>

<details open>
<summary> <b>Contributiong<b></summary>

Your contributions are always welcome! Please feel free to fork and modify the content but remember to finally do a pull request.

</details>

<details open>
<summary> :iphone: <b>Having Problems?<b></summary>

<p align = "center">

[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/riawa)
[<img src="https://img.shields.io/badge/telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](https://t.me/issaiass)
[<img src="https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white">](https://www.instagram.com/daqsyspty/)
[<img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />](https://twitter.com/daqsyspty) 
[<img src ="https://img.shields.io/badge/facebook-%233b5998.svg?&style=for-the-badge&logo=facebook&logoColor=white%22">](https://www.facebook.com/daqsyspty)
[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/riawe)
[<img src="https://img.shields.io/badge/tiktok-%23000000.svg?&style=for-the-badge&logo=tiktok&logoColor=white" />](https://www.linkedin.com/in/riawe)
[<img src="https://img.shields.io/badge/whatsapp-%23075e54.svg?&style=for-the-badge&logo=whatsapp&logoColor=white" />](https://wa.me/50766168542?text=Hello%20Rangel)
[<img src="https://img.shields.io/badge/hotmail-%23ffbb00.svg?&style=for-the-badge&logo=hotmail&logoColor=white" />](mailto:issaiass@hotmail.com)
[<img src="https://img.shields.io/badge/gmail-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" />](mailto:riawalles@gmail.com)

</p>

</details>

<details open>
<summary> <b>License<b></summary>
<p align = "center">
<img src= "https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg" />
</p>
</details>
