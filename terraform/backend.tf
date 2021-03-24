terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "omegazyadav"

    workspaces {
      prefix = "main"
    }
  }
}

