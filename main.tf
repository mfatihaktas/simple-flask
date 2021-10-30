terraform {
  required_version = ">= 0.13"
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

resource "docker_container" "my_img_sampler" {
  image = "img-sampler"
  name  = "my-img-sampler"
  restart = "always"
  volumes {
    container_path  = "/home/app"
    host_path = "/Users/mehmet/Desktop/code-challenge-ml-infra"
    read_only = false
  }
  ports {
    internal = 5000
    external = 8080
  }
}