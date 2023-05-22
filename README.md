<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Crop Recommendation System using GIS</h3>

  <p align="center">
    A Streamlit app written in Python using Folium/GeoPandas to help farmers decide what crop to plant based on government recommendations. 
  </p>
    <a href="https://github.com/dnezan/streamlit-geoapp-crop-suggestion">
    <img src="./data/home2.png" alt="Logo">
  </a>

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The aim is to create a simple app to suggest a crop for a farmer to grow based on the state they live in, and also display relevant weather information. I have also showcased various GIS techniques using an open source software called QGIS as well as preprocessing and deploying a Streamlit Python app on the cloud. This app is built using various open source libraries including Pandas/GeoPandas, Folium, shapely, and Streamlit, and sources data from the [Seednet initiative](https://seednet.gov.in/) by the Indian government as well as open weather data using PyOWM to access the [OpenWeatherMap API](https://openweathermap.org/api).

Here's how it works:
* The user uploads a GeoTIFF file containing vector information about their farm plot.
* The app uses latitude and longitude information to check which state the farm plot is located in by referencing a SHP file of Indian states.
* After referring official SeedNet documentation published by the Indian government, the app displays the name of the crop the farmer should plant as well as the type/hybrid name. The app also pulls local weather information via API and displays it to the user.

This app is intended as proof of concept and can thus be easily extended by using various additional metrics such as satellite imagery containing NDVI data, etc.

<!-- GETTING STARTED -->
## Getting Started

Make sure to clone the repo to run the project locally or deploy it on Streamlit Cloud/Heroku.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Using pip
  ```
pip install streamlit folium shapely geopandas pandas pyowm
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
