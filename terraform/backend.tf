terraform {
  backend "remote" {
    organization = "omegazyadav"

    workspaces {
      name = "main"
    }
  }
}
