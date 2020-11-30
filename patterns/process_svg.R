library(rsvg)

files <- list.files("svg/")

for(file in files){
  # Load a small version
  arr <- rsvg::rsvg(paste0("svg/", file))
  height <- dim(arr)[1]
  width <- dim(arr)[2]

  # Load desired size
  if(width > height){
    arr <- rsvg::rsvg(paste0("svg/", file), width = 1280)
  } else{
    arr <- rsvg::rsvg(paste0("svg/", file), height = 1280)
  }

  # Add bands to make it square
  diff <- abs(dim(arr)[1] - dim(arr)[2])
  size_1 <- trunc(diff / 2)
  size_2 <- ifelse(diff / 2 > size_1, size_1 + 1, size_1)

  if(width > height){
    band1 <- array(0, dim=c(size_1, 1280, 4))
    band2 <- array(0, dim=c(size_2, 1280, 4))
    arr <- DescTools::Abind(band1, arr, band2, along=1)
  } else{
    band1 <- array(0, dim=c(1280, size_1, 4))
    band2 <- array(0, dim=c(1280, size_2, 4))
    arr <- DescTools::Abind(band1, arr, band2, along=2)
  }

  # Recolor
  arr[, , 1:3] <- ifelse(arr[, , 1:3] < 0.5, 0, 1)
  # plot(density(as.matrix(arr[, , 1:3])))

  # render it into a bitmap array
  png::writePNG(arr, paste0("png/", gsub(".svg", ".png", file)))
}

