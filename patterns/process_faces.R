library(magick)

imgs <- list.files("faces/faces_database/")
for(file in imgs){
  magick::image_read(paste0("faces/faces_database/", file)) %>%
    magick::image_resize("1280") %>%  # Height
    magick::image_quantize(colorspace = 'gray') %>%
    magick::image_equalize() %>%
    magick::image_write(paste0("faces/", gsub(".jpg", ".png", file)))
}

