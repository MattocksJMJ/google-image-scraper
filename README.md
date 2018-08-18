# google-image-scraper
With a user inputted url the script will download the first 20 images from the page.

## Usage
- Clone it 
- Create a folder next to the scrape.py file named "images"
- Go to google images, search for something and copy the link
- Run the scrape.py file and when prompted paste the link

The scraper should now download 20 images and save them in the images folder

## Issues
The scraper only gets the image that is displayed, so it is quite small. In order to correct this I need to be able to access the source of the image. 

This could be done by getting the id of the image and adding it to the end of the url but beautiful soup doesn't get id's of files so I need to find another solution.
